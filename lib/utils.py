def calculate_interest_payment(
    extra_paydown,
    years,
    current_outstanding,
    interest_rate,
    monthly_payment,
):

    """
    We consider `years` of interest payments.

    Returns the amount paid in interest after `years`,
    and the amount outstanding.

    Args:
        extra_paydown (str|Date|None):
        years (int):
        current_outstanding (float):
        interest_rate (float):
        monthly_payment (float):
    Returns:
        interest (float):  amount paid in interest in above period
        outstanding (float): amount outstanding after above period
    """
    total_interest = 0
    current_outstanding -= extra_paydown
    for t in range(12 * years):
        interest = (current_outstanding * interest_rate) / 12
        principal_paydown = monthly_payment - interest
        current_outstanding -= principal_paydown
        if current_outstanding <= 0:
            break
        total_interest += interest
    
    return round(total_interest, 2), round(current_outstanding, 2), (t+1)/12.

def interest_on_money_calculator(base, interest, years):
    """
    How much money would you make after *years* at *interest_rate*
    on *base* calculated yearly (APR).
    Args:
        base (float): base amount for interest calc
        interest (float): interest rate
        years (int): years of interest
    Returns:
        interest (float)
    """
    accum = base
    for _ in range(years):
        extra = accum * interest
        accum += extra
    return accum - base


def find_interest_giving_total(base, total, years):
    """
    What % interest rate do you need to
    reach `total` after `years` APR interest on `base`?

    Args:
        base (float): base cash amt
        total (float): target cash amt
        years (int): years of interest
    Returns:
        interest (float)
    """
    lower, upper = 0, 1
    iters = 0
    while lower < upper and iters < 500:
        mid = (lower + upper) / 2
        calc = base + interest_on_money_calculator(base, mid, years)
        if abs(calc - total) < 5:
            return 100 * round(mid, 5)
        else:
            if calc < total:
                lower = mid
            else:
                upper = mid
        iters += 1

    return 100 * round(mid, 5)

def calc_monthly_payment(p, i, n):
    """
    Monthly payment amount for mortgage

    Args:
        p (float): bsae amount of mortgage
        i (float): interest rate
        n (int): years on loan
    Returns:
        interes
    """
    i /= 12
    n *= 12
    return p * (i*(1 + i)**n) / ((1 + i)**n - 1)

