import { createFileRoute } from '@tanstack/react-router';
import { Center } from '@mantine/core';
import { LoginForm } from '#/features/auth/login-form';

export const Route = createFileRoute('/login')({
  component: Login,
});

function Login() {
  return (
    <Center mih="100vh">
      <LoginForm />
    </Center>
  );
}
