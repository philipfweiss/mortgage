
from lib.utils import (
    calculate_interest_payment,
    find_interest_giving_total,
    calc_monthly_payment,
)

##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################


# How much money is left on your mortgage? 
OUTSTANDING_AMOUNT = 600000

#How many years on your mortgage?
YEARS = 30

# What is your interest rate?
# 0.06 = 6.00% interest
INTEREST_RATE = 0.06

# Once your terms are set, you can pay extra money up front.
# What difference does that make for you? 
EXTRA_PAYDOWN = 50000

##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################

print("\n****")
print(f"Outstanding Loan Amount: {OUTSTANDING_AMOUNT}")
print(f"Years on loan: {YEARS}")
print(f"Interest Rate: {round(100*INTEREST_RATE, 2)}%")
print(f"Extra Paydown: ${EXTRA_PAYDOWN}")

print("****\n")

monthly = round(calc_monthly_payment(OUTSTANDING_AMOUNT, INTEREST_RATE, YEARS), 2)
interest_0, outstanding_0, t_0 = calculate_interest_payment(
    extra_paydown=0,
    years=YEARS,
    current_outstanding=OUTSTANDING_AMOUNT,
    interest_rate=INTEREST_RATE,
    monthly_payment=monthly,
)

interest_1, outstanding_1, t_1 = calculate_interest_payment(
    extra_paydown=EXTRA_PAYDOWN,
    years=YEARS,
    current_outstanding=OUTSTANDING_AMOUNT,
    interest_rate=INTEREST_RATE,
    monthly_payment=monthly,
)
savings = round(interest_0 - interest_1, 2)

print("====")
print(f"Monthly payment is ${monthly}")

print(f"With $0 paydown, you would pay ${round(interest_0, 2)} "
    f"interest over {round(t_0, 2)} years."
)

if EXTRA_PAYDOWN > 0:
    print(f"With ${EXTRA_PAYDOWN} paydown, you would pay ${round(interest_1, 2)} "
        f"interest over {round(t_1, 2)} years."
    )

    # print(
    #     f"The savings of ${savings} is equivalent to a "
    #     f"{find_interest_giving_total(EXTRA_PAYDOWN, EXTRA_PAYDOWN + savings, YEARS)}% "
    #     f"APY on the initial ${EXTRA_PAYDOWN} invested over {YEARS} years. "
    # )
print("====\n")

