import mysql.connector

mydb=mysql.connector.connect(user='root',
passwd='root123',
host='localhost',
auth_plugin='mysql_native_password',
database='BankDB'
)

mycursor=mydb.cursor(buffered=True)
#Created Database BankDB
#mycursor.execute('create database BankDB')
def Menu(): #Function to display the menu
    print("*"*140)
    print("MAIN MENU".center(140))
    print("1. Insert Record/Records".center(140))
    print("2. Display Records as per Account Number".center(140))
    print(" a. Sorted as per Account Number".center(140))
    print(" b. Sorted as per Customer Name".center(140))
    print(" c. Sorted as per Customer Balance".center(140))
    print("3. Search Record Details as per the account number".center(140))
    print("4. Update Record".center(140))
    print("5. Delete Record".center(140))
    print("6. TransactionsDebit/Withdraw from the account".center(140))
    print(" a. Debit/Withdraw from the account".center(140))
    print(" b. Credit into the account".center(140))
    print("7. Exit".center(140))
    print("*"*140)
def MenuSort():
    print(" a. Sorted as per Account Number".center(140))
    print(" b. Sorted as per Customer Name".center(140))
    print(" c. Sorted as per Customer Balance".center(140))
    print(" d. Back".center(140))
def MenuTransaction():
    print(" a. Debit/Withdraw from the account".center(140))
    print(" b. Credit into the account".center(140))
    print(" c. Back".center(140))
def Create():
    try:
        mycursor.execute('create table bank(ACCNO varchar(10),NAME varchar(20),MOBILE varchar(10),EMAIL varchar(20),ADDRESS varchar(20),CITY varchar(10),COUNTRY varchar(20),BALANCE integer(15))')
        print("Table Created")
        Insert()
    except:
        print("Table Exist")
        Insert()
def Insert():
    while True: #Loop for accepting records
        Acc=input("Enter account no")
        Name=input("Enter Name")
        Mob=input("Enter Mobile")
        email=input("Enter Email")
        Add=input("Enter Address")
        City=input("Enter City")
        Country=input("Enter Country")
        Bal=float(input("Enter Balance"))
        Rec=[Acc,Name.upper(),Mob,email.upper(),Add.upper(),City.upper(),Country.upper(),Bal]
        Cmd="insert into BANK values(%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(Cmd,Rec)
        mydb.commit()
        ch=input("Do you want to enter more records")
        if ch=='N' or ch=='n':
            break
def DispSortAcc(): #Function to Display records as per ascending order of Account Number
    try:
        cmd="select * from BANK order by ACCNO"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        F="%15s %15s %15s %15s %15s %15s %15s %15s"
        print(F % ("ACCNO","NAME","MOBILE","EMAIL ADDRESS","COMPLETEADDRESS","CITY","COUNTRY","BALANCE"))
        print("="*125)
        for i in S:
            for j in i:
                print("%14s" % j, end=' ')
            print()
        print("="*125)
    except:
        print("Table doesn't exist")
def DispSortName(): #Function to Display records as per ascending order of Name
    try:
        cmd="select * from BANK order by NAME"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        F="%15s %15s %15s %15s %15s %15s %15s %15s"
        print(F % ("ACCNO","NAME","MOBILE","EMAIL ADDRESS","COMPLETEADDRESS","CITY","COUNTRY","BALANCE"))
        print("="*125)
        for i in S:
            for j in i:
                print("%14s" % j, end=' ')
            print()
        print("="*125)
    except:
        print("Table doesn't exist")
    
def DispSortBal(): #Function to Display records as per ascending order of Balance
    try:
        cmd="select * from BANK order by BALANCE"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        F="%15s %15s %15s %15s %15s %15s %15s %15s"
        print(F % ("ACCNO","NAME","MOBILE","EMAIL ADDRESS","COMPLETEADDRESS","CITY","COUNTRY","BALANCE"))
        print("="*125)
        for i in S:
            for j in i:
                print("%14s" % j, end=' ')
        print()
        print("="*125)
    except:
        print("Table doesn't exist")
        
def DispSearchAcc(): #Function to Search for the Record from the File with respect to the account number
    try:
        cmd="select * from BANK"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        ch=input("Enter the accountno to be searched")
        for i in S:
        if i[0]==ch:
            print("="*125)
            F="%15s %15s %15s %15s %15s %15s %15s %15s"
            print(F % ("ACCNO","NAME","MOBILE","EMAILADDRESS","COMPLETE ADDRESS","CITY","COUNTRY","BALANCE"))
            print("="*125)
            for j in i:
                print('%14s' % j,end=' ')
            print()
            break

        else:
            print("Record Not found")

    except:
        print("Table doesn't exist")

def Update(): #Function to change the details of a customer
    try:
        cmd="select * from BANK"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        A=input("Enter the accound no whose details to be changed")
        for i in S:
            i=list(i)
            if i[0]==A:
                 ch=input("Change Name(Y/N)")
                if ch=='y' or ch=='Y':
                    i[1]=input("Enter Name")
                    i[1]=i[1].upper()
                    ch=input("Change Mobile(Y/N)")
                if ch=='y' or ch=='Y':
                    i[2]=input("Enter Mobile")
                    ch=input("Change Email(Y/N)")
                if ch=='y' or ch=='Y':
                    i[3]=input("Enter email")
                    i[3]=i[3].upper()
                    ch=input("Change Address(Y/N)")
                if ch=='y' or ch=='Y':
                    i[4]=input("Enter Address")
                    i[4]=i[4].upper()
                    ch=input("Change city(Y/N)")
                if ch=='y' or ch=='Y':
                    i[5]=input("Enter City")
                    i[5]=i[5].upper()
                    ch=input("Change Country(Y/N)")
                if ch=='y' or ch=='Y':
                    i[6]=input("Enter country")
                    i[6]=i[6].upper()
                    ch=input("Change Balance(Y/N)")
                if ch=='y' or ch=='Y':
                    i[7]=float(input("Enter Balance"))
                cmd="UPDATE BANK SET NAME=%s,MOBILE=%s,EMAIL=%s,ADDRESS=%s,CITY=%s,COUNTRY=%s,BALANCE=%s WHERE ACCNO=%s"
                val=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Account Updated")
                break

            else:
                print("Record not found")

    except:
        print("No such table")
def Delete(): #Function to delete the details of a customer
    try:
        cmd="select * from BANK"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        A=input("Enter the accound no whose details to be changed")
        for i in S:
            i=list(i)
            if i[0]==A:
                cmd="delete from bank where accno=%s"
                val=(i[0],)
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Account Deleted")
                break

            else:
                print("Record not found")

    except:
        print("No such Table")

def Debit(): #Function to Withdraw the amount by assuring the min balance of Rs 5000
    try:
        cmd="select * from BANK"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        print("Please Note that the money can only be debited if min balance of Rs 5000 exists")
        acc=input("Enter the account no from which the money is to be debited")
        for i in S:
        i=list(i)
        if i[0]==acc:
            Amt=float(input("Enter the amount to be withdrawn"))
            if i[7]-Amt>=5000:
                i[7]-=Amt
                cmd="UPDATE BANK SET BALANCE=%s WHERE ACCNO=%s"
                val=(i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Amount Debited")
                break
            else:
                print("There must be min balance of Rs 5000")
                break

        else:
            print("Record Not found")

    except:
        print("Table Doesn't exist")
        
