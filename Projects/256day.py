# 256th day of the year
def dayOfProgrammer(year):
    #         Jan Feb Mar Apr May Jun Jul Aug Sep
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30]
    day = 256

    # 1918, feb 14 was 32nd day of the year
    if year == 1918:
        months[1] = 15
    # 1700 - 1917, LY div by 4
    # 1918+, LY divisible by 400 || divisible by 4 and not divisible by 100.
    #is it a leap year?
    if year >= 1918:
        if year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0):
            months[1] += 1
    else:
        if year % 4 == 0:
            months[1] += 1

    days = 0
    while days <= day:
        for d in months:
            days += d

    return(f'{months[-1] - abs(days - day)}.09.{year}')

print(dayOfProgrammer(1918))