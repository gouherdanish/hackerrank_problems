def is_leap(year):
    leap = False
    
    # Write your logic here
    year_divisible_by_4 = year % 4 == 0
    year_divisible_by_100 = year % 100 == 0
    year_divisible_by_400 = year % 400 == 0
    if year_divisible_by_100:
        if year_divisible_by_400:
            return True
        else:
            return False
    elif year_divisible_by_4:
        leap = True
    return leap

year = int(input())
print(is_leap(year))