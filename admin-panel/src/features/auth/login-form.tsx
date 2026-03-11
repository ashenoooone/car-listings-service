import { Card, CardContent, CardHeader, CardTitle } from '#/shared/ui/card';
import { Input } from '#/shared/ui/input';
import { Button } from '#/shared/ui/button';
import { useLoginForm, useLoginFormValidation } from './model/use-login-form';

export function LoginForm() {
  const loginForm = useLoginForm();
  const loginFormValidation = useLoginFormValidation();

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
  };

  return (
    <Card>
      <CardHeader>
        <CardTitle>Вход в систему</CardTitle>
      </CardHeader>
      <CardContent className="flex flex-col gap-4 min-w-[300px]">
        <Input
          type="email"
          placeholder="Логин"
          value={loginForm.login}
          onChange={e => loginForm.setLogin(e.target.value)}
        />
        <Input
          type="password"
          placeholder="Пароль"
          value={loginForm.password}
          onChange={e => loginForm.setPassword(e.target.value)}
        />
        <Button type="submit">Войти</Button>
      </CardContent>
    </Card>
  );
}
