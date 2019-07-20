#!/usr/bin/env python3

import sys
a_dict = {}

def calculate(alist):
    a,b = alist.split(":")
    try:
        c = int(b)
        insurance =0.165*c
        d = c-5000-insurance
        if d<=0:
            salary = c-insurance
        elif 0<d<=3000:
            salary = c-insurance-0.03*d
        elif 3000<d<=12000:
            salary = c-insurance-(0.1*d-210)
        elif 12000<d<=25000:
            salary = c-insurance-(0.2*d-1410)
        elif 25000<d<=35000:
            salary = c-insurance-(0.25*d-2660)
        elif 35000<d<=55000:
            salary = c-insurance-(0.3*d-4410)
        elif 55000<d<=80000:
            salary = c-insurance-(0.35*d-7160)
        elif 80000<d:
            salary = c-insurance-(0.45*d-15160)
        a_dict[a]=format(salary,".2f")
    except:
        print("Parameter Error")


if __name__ == "__main__":
    alists = sys.argv[1:]
    for alist in alists:
        calculate(alist)
    for key,value in a_dict.items():
        print(key+":"+value)
