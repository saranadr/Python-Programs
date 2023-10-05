"""Bank ATM machine Project
  Design a program to do the functionalities of Bank ATM machine.

Requirements,
 - Display "Welcome Screen" with menu options
    1. Account Summary
    2. Withdraw Amount
    3. Deposit Amount
    4. Mini Statement [optional]
    5. Transfer Amount [optional]
    6. Exit
 - For any option, get the card number and pin details and
 do the authentication [first time authentication]

Level-1
-------
bank_account, (Table)
  accno -> integer
  firstname -> text
  lastname -> text
  balance -> float
  createddate -> date default now

1. Account Summary (select query)
  Get the account number: 12345
  Display account no, account name, balance.

2. Withdraw Amount (update query - reduce balance)
  Get the account number: 12345
  Get the amount: 500

3. Deposit Amount (update query - add balance)
  Get the account number: 12345
  Get the amount: 50

4. Add Account,
  Get the accno, account name, amount


Level-2
-------
Add below fields to table,
 email -> text
 username -> text
 password -> text


* Whenever there is a transaction (withdraw/deposit), send email notification to the user email address.
  MSG: The account ending with xxxx1234 has been credited/debited with Rs.500. Current balance Rs. 1200

* Transfer amount from one account to another
  5. Transfer Amount
    Get the account number from user to transfer amount from one account to another
    Enter the From account number: 12345
    Enter the To account number: 12346
    Enter the amount to transfer: 1000


Level-3
-------
Create a new table with below fields.
transactions (Table)
 accno -> foreign key refers to bank account (accno)
 amount -> integer
 type -> text  (credit / debit)
 trans_date -> timestamp (default to current system date)

* For every credit/debit into account add an entry in this table.

* Add a new option for mini statement,
  6. Mini Statement
    Get the account number from user and display last 10 transaction statements.
    Enter the account number: 12345

    Mini Statement:
    Date, Credit/debit, Amount

* Add a new option to download account statement.
  7. Download statement
  If the user selects option-5, then we need to ask for 2 sub-options as,
    1. Download Locally
    2. Send Email
  If "Download Locally", then write the account data to excel and generate the file locally.
  IF "Send Email", then write the account data to excel file and send it as an attachment in email.



Level-4
-------
Convert the above program using GUI(Tkinter) or Web page (Flask)
Add below new fields to back_account table,
 usertype -> text (Admin / Normal)
 status -> text (Active / InActive)

1. Get the username and password from user.
2. Based on profile like admin / normal user show the options.
  Admin User,
  1. Account Summary
  2. Withdraw Amount
  3. Deposit Amount
  4. Add Account
  5. Remove/Disable Account
  6. Mini Statement
  7. Transaction History
  8. Transfer Amount
  9. Exit Program

  Normal User,
  1. Account Summary
  2. Withdraw Amount
  3. Deposit Amount
  4. Mini Statement
  5. Transaction History
  6. Transfer Amount
  7. Exit Program
"""

import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="mysql123", database="ATM")

##print("Database connection established successfully")
cur = db.cursor();

while True:
    print('****** Welcome ******)\n 1. Account Summary\n 2. Withdraw Amount\n 3. Deposit Amount\n 4. Mini Statement\n 5. Transfer Amount\n 6. Exit')
    op = int(input('Choose your option [1-6]:'))
    if op == 1:
        accno = int(input('Enter the account number:'))
        query = 'select accno from bank_account'
        cur.execute(query)
        acclog = cur.fetchall()
        cur.close()
        if accno not in acclog:
            print('Account number entered is incorrect')
            pass
        query = 'select accno,firstname,lastname,balance,createddate from bank_account where accno={0}'.format(accno)
        cur.execute(query)
        data = cur.fetchone()
        cur.close()
        print(
            '***** Account Summary *****\nAccount Number : {0}\nFirstname      : {1}\nLastname       : {2}\nBalance        : {3}'.format(
                data[0], data[1], data[2], data[3]))


    elif op == 2:
        accno = int(input('Enter the account number for withdrawal: '))
        amt = float(input('Enter the amount: '))
        query = 'select balance from bank_account where accno={0}'.format(accno)
        cur.execute(query)
        balance = cur.fetchone()
        cur.close()
        if int(balance) < int(amt):
            print('Insufficient balance')
            pass
        query = 'update bank_account set balance=balance-{0} where accno={1}'.format(amt, accno)
        cur.execute(query)
        db.commit()
        print('Amount has been withdrawed successfully')
        query = 'insert into transaction(accno,amount,type,trans_date) values({0},{1},{2},{3})'.format(accno, amt,
                                                                                                       'debit', now())
        cur.execute(query)
        db.commit()

    elif op == 3:
        accno = int(input('Enter the account number for deposit: '))
        amt = float(input('Enter the amount for Deposit: '))
        query = 'update bank_account set balance=balance+{0} where accno={1}'.format(amt, accno)
        cur.execute(query)
        db.commit()
        print('Amount has been deposited successfully')
        query = 'insert into transaction(accno,amount,type,trans_date) values({0},{1},{2},{3})'.format(accno, amt,
                                                                                                       'credit', now())
        cur.execute(query)
        db.commit()

    elif op == 4:
        accno = int(input('Enter the account number: '))
        query = 'select amount,type,trans_date from transaction where accno={0}'.format(accno)
        cur.execute(query)
        print('***** Mini statement *****\nAmount Transaction Date & Time')
        for i in cur.fetchall():
            print(i)


    elif op == 5:
        accno = int(input('Enter the account number for withdrawal: '))
        amt = float(input('Enter the amount: '))
        query = 'select balance from bank_account where accno={0}'.format(accno)
        cur.execute(query)
        balance = cur.fetchone()
        cur.close()
        if int(balance) < int(amt):
            print('Insufficient balance')
            pass

        query = 'update bank_account set balance=balance-{0} where accno={1}'.format(amt, accno)
        cur.execute(query)
        db.commit()
        query = 'insert into transaction(accno,amount,type,trans_date) values({0},{1},{2},{3})'.format(accno, amt,
                                                                                                       'debit', now())
        cur.execute(query)
        db.commit()

        accno = int(input('Enter the account number for deposit: '))
        query = 'update bank_account set balance=balance+{0} where accno={1}'.format(amt, accno)
        cur.execute(query)
        db.commit()
        print('Amount has been tranferred successfully')
        query = 'insert into transaction(accno,amount,type,trans_date) values({0},{1},{2},{3})'.format(accno, amt,
                                                                                                       'credit', now())
        cur.execute(query)
        db.commit()

    elif op == 6:
        print('Exiting system')
        break
    else:
        print('Invalid option')
        pass
