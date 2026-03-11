export function validateLogin(login: string) {
  return login.length > 0 && login.length <= 100;
}

export function validatePassword(password: string) {
  return password.length > 0;
}
