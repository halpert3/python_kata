"""
Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), 
is part of the second quarter; and month 11 (November), is part of the fourth quarter.
"""
def quarter_of(month):
    quarter = None
    if month in range(4):
        quarter = 1
    elif month in range(4,7):
        quarter = 2
    elif month in range(7, 10):
        quarter = 3
    else:
        quarter = 4
    return quarter