def how_eligible(essay):
    total = 0
    if '"' in essay:
        total = total + 1
    if '?' in essay:
        total = total + 1
    if '!' in essay:
        total = total + 1
    if ',' in essay:
        total = total + 1
    print(total)