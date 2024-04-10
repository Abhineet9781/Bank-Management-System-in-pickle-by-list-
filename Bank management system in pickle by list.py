import pickle

def bankdetails():
    obj=open('BMS.dat','ab+')
    record=[]
    while True:
        acc=int(input('Enter account no.:'))
        name=input('Enter name:')
        add=input('Enter address:')
        PNo=int(input('Enter Phone no.:'))
        GID=input('Enter Govt ID:')
        AT=input('Enter Account type:')
        Amo=int(input('Enter Amount:'))
        data=[acc,name,add,PNo,GID,AT,Amo]
        record.append(data)
        ch=input('More(y/n)?')
        if ch=='n':
            break
    pickle.dump(record,obj)        
    print('Account Creaded')
    print('-'*50)    
    obj.close()

def update():
    obj=open('BMS.dat', 'rb+')
    ANo=int(input('Account no.'))
    obj.seek(0)
    try:
        while True:
            rpos=obj.tell()
            data1=pickle.load(obj)
            for i in data1:
                if i[0]==ANo:
                    print('Record found \n1. Check Balance \n2. Deposit \n3. Withdraw')
                    n=int(input('enter the choice:'))
                    if (n==1):
                        print('-'*50)
                        print('Available Balance:',i[6])
                        print('-'*50)
                        break
                    if (n==2):                    
                        a=int(input('enter the amount Deposit:'))
                        b=i[6]
                        print('Deposit Successful \nAvailable Balance:',a+b)
                        print('-'*50)
                        i[6]=a+b
                        obj.seek(rpos)
                        pickle.dump(data1,obj)
                        break
                    if (n==3):
                        a=int(input('enter the amount Withdraw:'))
                        b=i[6]
                        if i[6]<=a:
                            print('Balance not sufficient')
                            print('Try Next Time')
                        else:
                            print('Withdraw Successful \nAvailable Balance:',b-a)
                            print('-'*50)
                            i[6]=b-a                        
                            obj.seek(rpos)
                            pickle.dump(data1,obj)
                            break
                    break

    except Exception:
        print(' ')
        i=1
        while i==1:
            break
    obj.close()             

while True:
    print('-'*50)
    print((' '*10),'Bank Management System',(' '*10))
    print('-'*50)
    n=int(input('1. New Customer \n2. Exiting customer\n3. Exit \nEnter the choice:'))
    if (n==1):
        bankdetails()
    if (n==2):
        update()
    if (n==3):
        exit()
        break
    continue
