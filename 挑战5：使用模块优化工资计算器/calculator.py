from multiprocessing import Process,Queue
import sys
import csv
import getopt
from datetime import datetime,date
from configparser import ConfigParser

queue1 = Queue()
queue2 = Queue()

#global min
#global max
#global total

def rate(before_tax_salary):
    if before_tax_salary<min:
        num_1 = min
    elif before_tax_salary>max:
        num_1 = max
    else:
        num_1 = before_tax_salary
    shebao_money = num_1*total
    should_tax = before_tax_salary-shebao_money-5000
    if should_tax<=0:
        tax=0
    elif 0<should_tax<=3000:
        tax=should_tax*0.03
    elif 3000<should_tax<=12000:
        tax=should_tax*0.1-210
    elif 12000<should_tax<=25000:
        tax=should_tax*0.2-1410
    elif 25000<should_tax<=35000:
        tax=should_tax*0.25-2660
    elif 35000<should_tax<=55000:
        tax=should_tax*0.3-4410
    elif 55000<should_tax<=80000:
        tax=should_tax*0.35-7160
    else:
        tax=should_tax*0.45-15160
    salary = before_tax_salary-shebao_money-tax
    return shebao_money,tax,salary

def q1(queue1,user_data):
    data=[]
    ID = user_data[0]
    before_tax_salary = user_data[1]
    data.append(ID)
    data.append(before_tax_salary)
    queue1.put(data)

def q2(queue1,queue2):
    data = queue1.get()
    newdata=[]
    ID = data[0]
    before_tax_salary=float(data[1])
    cal_time = datetime.now().time()
    hours,minutes,seconds = [cal_time.hour,cal_time.minute,cal_time.second]
    shebao_money,tax,salary = rate(before_tax_salary)
    newdata.append(ID)
    newdata.append(int(before_tax_salary))
    newdata.append('{:.2f}'.format(shebao_money))
    newdata.append('{:.2f}'.format(tax))
    newdata.append('{:.2f}'.format(salary))
    newdata.append(str(datetime.now())[:-7])
    queue2.put(newdata)

def q3(queue2,gongzifile):
    newdata=queue2.get()
    with open(gongzifile,"a+") as f2:
        writer = csv.writer(f2)
        writer.writerow(newdata)

def main():

    opts,args = getopt.getopt(sys.argv[1:],'hC:c:d:o:',['help'])
    options = dict(opts)
    the_city = options['-C'].upper()
    configfile = options['-c']
    userfile = options['-d']
    gongzifile = options['-o']
    config = ConfigParser()
    config.read('test.cfg',encoding='UTF-8')
    sections = config.sections()
    if the_city in sections:
        the_config = dict(config.items(the_city))
    else:
        the_config = dict(config['DEFAULT'])
    global total
    total = 0
    for key, value in the_config.items():
        if key == "JiShuL".lower():
            global min
            min = float(value)
        elif key == "JiShuH".lower():
            global max
            max = float(value)
        else:
            total += float(value)

    with open(userfile,'r') as f4:
        users = list(csv.reader(f4))
        for user_data in users:
            Process(target=q1,args=(queue1,user_data)).start()
            Process(target=q2,args=(queue1,queue2)).start()
            Process(target=q3,args=(queue2,gongzifile)).start()

if __name__ == "__main__":
    main()
