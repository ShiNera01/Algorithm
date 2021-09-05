def solution(a, b):
    answer = ''
    total = 0
    month_day = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    for i in range(a - 1):
        total += month_day[i]
    
    total += b
    
    if total % 7 == 0:
        result = "THU"
    elif total % 7 == 1:
        result = "FRI"
    elif total % 7 == 2:
        result = "SAT"
    elif total % 7 == 3:
        result = "SUN"
    elif total % 7 == 4:
        result = "MON"
    elif total % 7 == 5:
        result = "TUE"
    elif total % 7 == 6:
        result = "WED"
    answer = result
    return answer
