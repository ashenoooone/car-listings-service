import { describe, expect, it } from 'vitest';
import { isLoginValid, isPasswordValid } from '../validators';

describe('validators', () => {
  describe('login', () => {
    describe('when login is empty', () => {
      it('should return false', () => {
        expect(isLoginValid('')).toBe(false);
      });
    });
    describe('when login is too long', () => {
      it('should return false', () => {
        expect(isLoginValid('a'.repeat(101))).toBe(false);
      });
    });
    describe('when login is valid', () => {
      it('should return true', () => {
        expect(isLoginValid('test')).toBe(true);
      });
    });
  });
  describe('password', () => {
    describe('when password is empty', () => {
      it('should return false', () => {
        expect(isPasswordValid('')).toBe(false);
      });
    });
    describe('when password is valid', () => {
      it('should return true', () => {
        expect(isPasswordValid('test')).toBe(true);
      });
    });
  });
});
