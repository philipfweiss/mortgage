
# Mortgage Calculator

Super simple mortgage calculator, allowing you to play with the following variables:

```
# How much money is left on your mortgage? 
OUTSTANDING_AMOUNT = 600000

#How many years on your mortgage?
YEARS = 30

# What is your interest rate?
# 0.06 = 6.00% interest
INTEREST_RATE = 0.06

# Once your terms are set, you can pay extra money up front.
# What difference does that make for you? 
EXTRA_PAYDOWN = 0
```

### How to run
1. Clone the repo.
2. `cd mortgage`.
3. Update the four variables above on mortgage.py L15 -> 26.
4. Run `python ./mortgage.py`.

### Example Output

```
****
Outstanding Loan Amount: 600000
Years on loan: 30
Interest Rate: 6.0%
Extra Paydown: $0
****

====
Monthly payment is $3597.3
With $0 paydown, you would pay $695031.17 interest over 30.0 years.
====
```

With a $50k extra paydown, you get:

```
****
Outstanding Loan Amount: 600000
Years on loan: 30
Interest Rate: 6.0%
Extra Paydown: $50000
****

====
Monthly payment is $3597.3
With $0 paydown, you would pay $695031.17 interest over 30.0 years.
With $50000 paydown, you would pay $492838.91 interest over 24.17 years.
====
```
