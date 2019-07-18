#!/usr/bin/env pytho3

import sys
import csv
import json

def shebao_calculate(num,total,min,max):
    num = float(num)
    if num<min:
        num_1 = min
    elif num>max:
        num_1 = max
    else:
        num_1 = num
    shebao_money = num_1 * total
    should_tax = num-shebao_money-5000
    if should_tax<=0:
        tax = 0
    elif 0<should_tax<=3000:
        tax = should_tax*0.03
    elif 3000<should_tax<=12000:
        tax = should_tax*0.1-210
    elif 12000<should_tax<=25000:
        tax = should_tax*0.2-1410
    elif 25000<should_tax<=35000:
        tax = should_tax*0.25-2660
    elif 35000<should_tax<=55000:
        tax = should_tax*0.3-4410
    elif 55000<should_tax<=80000:
        tax = should_tax*0.35-7160
    else:
        tax = should_tax*0.45-15160
    gongzi = num-shebao_money-tax
    return shebao_money,tax,gongzi

def calculate(user,total,min,max):
    user_info = []
    id = user[0]
    num = user[1]
    a, b, c = shebao_calculate(num,total,min,max)
    user_info.append(int(id))
    user_info.append(int(num))
    user_info.append('{:.2f}'.format(float(a)))
    user_info.append('{:.2f}'.format(float(b)))
    user_info.append('{:.2f}'.format(float(c)))
    return user_info


if __name__ == "__main__":
    # ??????
    args = sys.argv[1:]
    index_c = args.index('-c')
    configfile = args[index_c + 1]
    index_d = args.index('-d')
    userfile = args[index_d + 1]
    index_o = args.index('-o')
    gongzifile = args[index_o + 1]

    # ??????
    with open(configfile, 'r') as f2:
        datas = f2.readlines()
        config_dict = {}
        for data in datas:
            ID, NUM = data.strip().split("=")
            config_dict[ID.strip()] = NUM.strip()
        total = 0
        for key, value in config_dict.items():
            if key == "JiShuL":
                min = float(value)
            elif key == "JiShuH":
                max = float(value)
            else:
                total += float(value)

    # ????????
    with open(userfile, 'r') as f1:
        users = list(csv.reader(f1))
        users_info = []
        for user in users:
            user_info = calculate(user,total,min,max)
            users_info.append(user_info)

    with open(gongzifile,'w') as f3:
        csv.writer(f3).writerows(users_info)

