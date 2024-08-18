import math
def lcm(num1, num2):
    return (num1 * num2) // math.gcd(num1, num2)

def is_leap(year):
    if year % 400 == 0: return True
    if year % 100 == 0: return False
    return year % 4 == 0 

def calculate(year, month, day, add_day):
    year_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while True:
        if is_leap(year):
            year_list[2] = 29
        else:
            year_list[2] = 28
            
        while month <= 12:
            if day + add_day <= year_list[month]:
                day += add_day
                return (year, month, day)
            else:
                add_day -= year_list[month]
                month += 1        
        else:
            month = 1
            year += 1

number = int(input())
num_list = list(map(int, input().split()))
year, month, day = list(map(int, input().split("/")))

for i in range(number):
    num_list[0] = lcm(num_list[i], num_list[0])
add_day = num_list[0]

year, month, day = calculate(year, month, day, add_day)
print(f"{year}/{month:02d}/{day:02d}")
