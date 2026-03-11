export type LoginFormState = {
  login: string;
  password: string;
};

export type LoginFormActions = {
  setLogin: (login: string) => void;
  setPassword: (password: string) => void;
};

export type LoginFormStore = LoginFormState & LoginFormActions;
