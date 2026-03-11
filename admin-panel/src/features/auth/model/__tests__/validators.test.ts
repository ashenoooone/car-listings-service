import { describe, expect, it } from 'vitest';
import { validateLogin, validatePassword } from '../validators';

describe('validators', () => {
  describe('login', () => {
    describe('when login is empty', () => {
      it('should return false', () => {
        expect(validateLogin('')).toBe(false);
      });
    });
    describe('when login is too long', () => {
      it('should return false', () => {
        expect(validateLogin('a'.repeat(101))).toBe(false);
      });
    });
    describe('when login is valid', () => {
      it('should return true', () => {
        expect(validateLogin('test')).toBe(true);
      });
    });
  });
  describe('password', () => {
    describe('when password is empty', () => {
      it('should return false', () => {
        expect(validatePassword('')).toBe(false);
      });
    });
    describe('when password is valid', () => {
      it('should return true', () => {
        expect(validatePassword('test')).toBe(true);
      });
    });
  });
});
