def is_leap(year):
    if year==2100:
        return False
    elif year % 4==0:
        return True
    else:
        return False


year = int(input())
print(is_leap(year))
