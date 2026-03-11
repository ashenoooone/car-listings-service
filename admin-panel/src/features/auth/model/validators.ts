const PASSWORD_ERRORS = {
  EMPTY: 'Пароль не может быть пустым',
  TOO_SHORT: 'Пароль должен быть не менее 8 символов',
  TOO_LONG: 'Пароль должен быть не более 100 символов',
};

const LOGIN_ERRORS = {
  EMPTY: 'Логин не может быть пустым',
  TOO_LONG: 'Логин должен быть не более 100 символов',
};

export function isLoginValid(login: string) {
  if (login.length === 0) {
    return LOGIN_ERRORS.EMPTY;
  }
  if (login.length > 100) {
    return LOGIN_ERRORS.TOO_LONG;
  }
  return null;
}

export function isPasswordValid(password: string) {
  if (password.length === 0) {
    return PASSWORD_ERRORS.EMPTY;
  }
  if (password.length < 8) {
    return PASSWORD_ERRORS.TOO_SHORT;
  }
  if (password.length > 100) {
    return PASSWORD_ERRORS.TOO_LONG;
  }
  return null;
}
