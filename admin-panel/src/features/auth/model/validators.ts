export function isLoginValid(login: string) {
  return login.length > 0 && login.length <= 100;
}

export function isPasswordValid(password: string) {
  return password.length > 0;
}
