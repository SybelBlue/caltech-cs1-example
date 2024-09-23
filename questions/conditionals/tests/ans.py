if member:
    if age < 18:
        cost = 8 * 0.7
    elif age >= 65:
        cost = 6 * 0.7
    else:
        cost = 10 * 0.7
else:
    if age < 18:
        cost = 8
    elif age >= 65:
        cost = 6
    else:
        cost = 10