import type { TestingLibraryMatchers } from "@testing-library/jest-dom/matchers";

// jest-dom ships its vitest augmentation against vitest 4's `Assertion<T>`, which
// no longer merges with vitest 5's `Assertion<R, T>`. Augment `Matchers`, the
// extension point vitest 5 documents for custom matchers, instead. The type
// parameters must mirror vitest's declaration exactly for the merge to apply,
// so `T` stays unused here.
declare module "vitest" {
  /* eslint-disable @typescript-eslint/no-empty-object-type, @typescript-eslint/no-unused-vars */
  interface Matchers<
    R extends void | Promise<void> = void | Promise<void>,
    T = unknown,
  > extends TestingLibraryMatchers<unknown, R> {}
  /* eslint-enable @typescript-eslint/no-empty-object-type, @typescript-eslint/no-unused-vars */
}
