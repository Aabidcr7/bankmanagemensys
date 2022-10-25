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
