import js from '@eslint/js';
import typescript from '@typescript-eslint/eslint-plugin';
import tsParser from '@typescript-eslint/parser';
import react from 'eslint-plugin-react';
import reactHooks from 'eslint-plugin-react-hooks';
import jsxA11y from 'eslint-plugin-jsx-a11y';
import importPlugin from 'eslint-plugin-import';

export default [
  js.configs.recommended,
  {
    files: ['**/*.{js,jsx,ts,tsx}'],
    plugins: {
      '@typescript-eslint': typescript,
      'react': react,
      'react-hooks': reactHooks,
      'jsx-a11y': jsxA11y,
      'import': importPlugin,
    },
    languageOptions: {
      parser: tsParser,
      parserOptions: {
        ecmaVersion: 'latest',
        sourceType: 'module',
        ecmaFeatures: {
          jsx: true,
        },
      },
      globals: {
        // Browser globals
        document: 'readonly',
        window: 'readonly',
        console: 'readonly',
        // Node.js globals
        process: 'readonly',
        Buffer: 'readonly',
        // Web API globals
        Request: 'readonly',
        Response: 'readonly',
        Headers: 'readonly',
        fetch: 'readonly',
      },
    },
    settings: {
      react: {
        version: 'detect',
      },
      'import/resolver': {
        typescript: {},
      },
    },
    rules: {
      ...typescript.configs.recommended.rules,
      ...react.configs.recommended.rules,
      ...reactHooks.configs.recommended.rules,
      ...jsxA11y.configs.recommended.rules,
      
      // Disable some rules that might be too strict for this project
      'react/react-in-jsx-scope': 'off', // React 17+ doesn't need this
      '@typescript-eslint/no-unused-vars': ['warn', { argsIgnorePattern: '^_' }],
    },
  },
  {
    ignores: [
      'node_modules/**',
      '.cache/**',
      'build/**',
      'public/build/**',
      'coverage/**',
      '.DS_Store',
    ],
  },
];