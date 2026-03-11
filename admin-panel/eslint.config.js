import antfu from '@antfu/eslint-config';
import tseslint from 'typescript-eslint';
import reactRefresh from 'eslint-plugin-react-refresh';

export default antfu(
  {
    stylistic: {
      indent: 2,
      quotes: 'single',
      jsx: true,
      semi: true,
    },
    ignores: ['dist', 'node_modules', 'public'],
    react: true,
    formatters: {
      css: 'prettier',
    },
  },
  {
    plugins: [
      tseslint.configs.recommended,
      reactRefresh.configs.vite,
    ],
    languageOptions: {
      ecmaVersion: 2020,
    },
    rules: {
      'curly': ['error', 'all'],
      'style/brace-style': ['error', 'stroustrup'],
      'ts/consistent-type-definitions': ['error', 'type'],
      'perfectionist/sort-imports': 'off',
      'perfectionist/sort-named-imports': ['off'],
    },
  },
);
