
# Mortgage Calculator

Super simple mortgage calculator, allowing you to play with the following variables:

```
# How much money is left on your mortgage? 
OUTSTANDING_AMOUNT = 605229

#How many years on your mortgage?
YEARS = 30

# What is your interest rate?
# 0.0515 = 5.15% interest
INTEREST_RATE = 0.0641

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
Outstanding Loan Amount: 605229
Years on loan: 30
Interest Rate: 6.41%
Extra Paydown: $0
****

====
Monthly payment is $3789.71
With $0 paydown, you would pay $759043.09 interest over 30.0 years.
====
```