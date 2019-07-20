from multiprocessing import Process,Queue
import sys
import csv

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
    shebao_money,tax,salary = rate(before_tax_salary)
    newdata.append(ID)
    newdata.append(int(before_tax_salary))
    newdata.append('{:.2f}'.format(shebao_money))
    newdata.append('{:.2f}'.format(tax))
    newdata.append('{:.2f}'.format(salary))
    queue2.put(newdata)

def q3(queue2,gongzifile):
    newdata=queue2.get()
    with open(gongzifile,"a+") as f2:
        writer = csv.writer(f2)
        writer.writerow(newdata)

def main():

    # 获得三个文件的绝对路径 configfile;userfile;gongzifile
    args = sys.argv[1:]
    index_c = args.index('-c')
    configfile = args[index_c+1]
    index_d = args.index('-d')
    userfile = args[index_d+1]
    index_o = args.index('-o')
    gongzifile = args[index_o+1]
 
    # 处理configfile,configz_dict是一个包含各个指标的字典
    # total是各个指标的和
    # min是税前工资下限，max是税后工资上限

    with open(configfile,'r') as f3:
        datas = f3.readlines()
        config_dict = {}
        for data in datas:
            ID,NUM = data.strip().split("=")
            config_dict[ID.strip()] = NUM.strip()
        global total
        total = 0
        for key,value in config_dict.items():
            if key=="JiShuL":
                global min
                min=float(value)
            elif key == "JiShuH":
                global max
                max=float(value)
            else:
                total += float(value)
    #global min
    #global max
    #global total
    # 打开userfile，针对每个user开进程
    with open(userfile,'r') as f4:
        users = list(csv.reader(f4))
        for user_data in users:
            Process(target=q1,args=(queue1,user_data)).start()
            Process(target=q2,args=(queue1,queue2)).start()
            Process(target=q3,args=(queue2,gongzifile)).start()

if __name__ == "__main__":
    main()
