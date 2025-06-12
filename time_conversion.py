def timeConversion(s)-> str:
    period = s[-2:]
    hours = int(s[:2])
    rest = s[2:-2]
    if period == "AM":
        if hours == 12:
            hours = 0
        
    else:
        if hours != 12:
            hours += 12        
        
    return f"{hours:02d}{rest}"


print(timeConversion("12:05:45AM"))