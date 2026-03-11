import { create, useStore } from 'zustand';
import type { LoginFormStore } from './types';
import { isLoginValid, isPasswordValid } from './validators';

const loginStore = create<LoginFormStore>(set => ({
  login: '',
  password: '',
  setLogin: (login: string) => set({ login }),
  setPassword: (password: string) => set({ password }),
}));

export function useLoginForm() {
  return useStore(loginStore);
}

export function useLoginFormValidation() {
  const { login, password } = useLoginForm();

  return {
    login: isLoginValid(login),
    password: isPasswordValid(password),
    isValid: !isLoginValid(login) && !isPasswordValid(password),
  };
}
