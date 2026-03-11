import { Card, CardContent, CardHeader, CardTitle } from '#/shared/ui/card';
import { Input } from '#/shared/ui/input';
import { Button } from '#/shared/ui/button';

export function LoginForm() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Вход в систему</CardTitle>
      </CardHeader>
      <CardContent className="flex flex-col gap-4 min-w-[300px]">
        <Input type="email" placeholder="Логин" />
        <Input type="password" placeholder="Пароль" />
        <Button type="submit">Войти</Button>
      </CardContent>
    </Card>
  );
}
