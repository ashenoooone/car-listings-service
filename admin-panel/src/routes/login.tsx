import { createFileRoute } from '@tanstack/react-router';
import { LoginForm } from '#/features/auth/login-form';

export const Route = createFileRoute('/login')({
  component: Login,
});

function Login() {
  return (
    <main className="flex items-center justify-center h-screen">
      <LoginForm />
    </main>
  );
}
