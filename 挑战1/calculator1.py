#!/usr/bin/env python3
import sys

a = sys.argv[1]
try:
    salary = int(a)
    tax_salary = salary-5000
    if tax_salary<=0:
        tax = 0
    elif 0< tax_salary<=3000:
        tax = 0.03 * tax_salary
    elif 3000< tax_salary <=12000:
        tax = 0.1*tax_salary-210
    elif 12000<tax_salary<=25000:
        tax = 0.2*tax_salary-1410
    elif 25000<tax_salary<=35000:
        tax = 0.25*tax_salary-2660
    elif 35000<tax_salary<=55000:
        tax = 0.3*tax_salary-4410
    elif 55000<tax_salary<=80000:
        tax = 0.35*tax_salary-7160
    elif 80000<tax_salary:
        tax = 0.45*tax_salary-15160
    print(format(tax,".2f"))
except:
    print("Parameter Error")
