import { Button, Card, PasswordInput, Stack, TextInput, Title } from '@mantine/core';
import { useLoginForm, useLoginFormValidation } from './model/use-login-form';

export function LoginForm() {
  const loginForm = useLoginForm();
  const loginFormValidation = useLoginFormValidation();

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
  };

  return (
    <Card shadow="sm" padding="lg" radius="md" withBorder w={300} h={400}>
      <form onSubmit={handleSubmit} style={{ height: '100%' }}>
        <Stack h="100%" justify="space-between" gap="md">
          <Stack gap="md">
            <Title order={3}>
              Вход в систему
            </Title>
            <TextInput
              label="Логин"
              placeholder="Введите логин"
              value={loginForm.login}
              onChange={e => loginForm.setLogin(e.currentTarget.value)}
              error={loginFormValidation.login}
            />
            <PasswordInput
              label="Пароль"
              placeholder="Введите пароль"
              value={loginForm.password}
              onChange={e => loginForm.setPassword(e.currentTarget.value)}
              error={loginFormValidation.password}
            />
          </Stack>
          <Button
            type="submit"
            fullWidth
            disabled={!loginFormValidation.isValid}
          >
            Войти
          </Button>
        </Stack>
      </form>
    </Card>
  );
}
