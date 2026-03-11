import { create, useStore } from 'zustand';
import type { LoginFormStore } from './types';
import { validateLogin, validatePassword } from './validators';

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
    login: validateLogin(login),
    password: validatePassword(password),
  };
}
