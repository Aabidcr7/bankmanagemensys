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
