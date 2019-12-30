import datetime as dt

d = {0: "oh",
     1: "one",
     2: "two",
     3: "three",
     4: "four",
     5: "five",
     6: "six",
     7: "seven",
     8: "eight",
     9: "nine",
     10: "ten",
     11: "eleven",
     12: "twelve",
     13: "thirteen",
     14: "fourteen",
     15: "fifteen",
     16: "sixteen",
     17: "seventeen",
     18: "eighteen",
     19: "nineteen",
     20: "twenty",
     30: "thirty",
     40: "forty",
     50: "fifty",
     60: "sixty"}

def display_time(t):
    Hour = d[int( t[0:2])] if t[0:2] != "00" else d[12]
    Suffix = 'a.m.' if d[int( t[7:9])] == Hour else 'p.m.'

    if  t[3] == "0":
        if  t[4] == "0":
            Minute = ""
        else:
            Minute = d[0] + " " + d[int(t[4])]
    else:
        Minute = d[int(t[3])*10] + '-' + d[int(t[4])]
    print('The time is', Hour, Minute, Suffix)

display_time(dt.datetime.now().strftime('%I %M %H'))
