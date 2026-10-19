# Part B: Reflection

## 1. Tests, production code, and ratio

I wrote 8 test functions in Part A. The production code has 45 non-empty lines. The ratio is 8:45, or about 1 test function for every 5.6 lines of code.

## 2. The longest red bar

The longest red bar was in A7. The test expected 228 g, but the result was 201 g. I learned that I needed to convert ounces to grams before adding them.

## 3. Fake It, triangulation, and Obvious Implementation

I used Fake It in A6 when `plus()` returned `grams(500)`. This helped me make the test pass first.

I used triangulation by testing multiplication with different numbers. This showed that the code needed to work with different inputs.

I used Obvious Implementation in `Sum.reduce()` by converting both values and adding them. I think these choices helped me learn TDD.

## 4. Remaining test list

I would test converting grams to ounces and what happens when a conversion rate is missing. I would do the missing-rate test next. I would remove tests for features that are not needed.

## 5. The `Quantity.reduce()` method

If I designed everything first, I might not have created `Quantity.reduce()`. I added it when the tests showed that I needed it. TDD helped me find the design step by step.

## 6. Writing tests before and after the code

In Part 0, I wrote tests after the code. In Part A, I wrote tests before the code and saw them fail first. This helped me understand what I needed to implement. I learned that tests can help design the code, not only check it.