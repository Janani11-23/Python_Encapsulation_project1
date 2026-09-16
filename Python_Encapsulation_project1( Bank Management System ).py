class Bank:
    BankName='🏦 SBI'
    Branch='🏢 Vadapalani'
    Ifsc='🔐 SBIN00011'

    def __init__(self,Name,Acc_no,pin,initial_balance):
        self.Name=Name
        self.__Acc_no=Acc_no
        self.__pin=pin
        self.__initial_balance=initial_balance
        self.__Last_transaction='📄 NO TRANSACTION YET DONE'

    def cust_dt(self):
        print(f'🏦 BankName:{self.BankName}')
        print(f'🏢 Branch:{self.Branch}')
        print(f'🔐 IFSC:{self.Ifsc}')
        print(f'👤 Name:{self.Name}')
        print(f'💳 Acc_no:{self.__Acc_no}')
        print(f'🔑 pin_no:{self.__pin}')
        print(f'💰 Initial_balance:₹{self.__initial_balance}')

    def __authenticate(self):
        Accno=int(input('💳 Enter Account no:'))
        Pin=int(input('🔑 Enter pin no:'))
        return Accno==self.__Acc_no and Pin==self.__pin

    def __generate_receipt(self,type,amount):
        return f'''
        🧾 -------- TRANSACTION RECEIPT -------- 🧾
        🏦 BankName:{self.BankName}
        💳 AccountNo:{self.__Acc_no}
        💰 Current_balance:₹{self.__initial_balance}
        💵 Transaction amount:₹{amount}
        🔄 Transaction Type:{type}
        '''

    def __deposit(self,amount):
        self.__initial_balance+=amount

    def __withdraw(self,amount):
        self.__initial_balance-=amount

    def show_balance(self):
        if self.__authenticate():
           print('💰 Balance: ₹',self.__initial_balance)

    def show_details(self):
        if self.__authenticate():
            print('📋 SHOW DETAILS')
            self.cust_dt()

    def Lst_transaction(self):
        if self.__authenticate():
            print("🧾 Last transaction:",self.__Last_transaction)

    def deposit_money(self):
                if self.__authenticate():
                    print("✅ Authentication successful")
                    amount=int(input('💵 Enter deposit amount: ₹'))
                    if amount>0 and amount<=self.__initial_balance:
                        self.__deposit(amount)
                        print(f'✅ Deposit successful: ₹{amount}')
                        print(f'💰 Balance: ₹{self.__initial_balance}')
                        self.__Last_transaction=self.__generate_receipt('DEPOSIT',amount)
                        print(self.__generate_receipt('DEPOSIT',amount))
                    else:
                        print('❌ Invalid amount')
                else:
                    print("❌ Authentication failed")

    def withdraw_money(self):
            if self.__authenticate():
                amount=int(input("💸 Enter withdraw amount: ₹"))
                if amount>0 and amount<=self.__initial_balance:
                    self.__withdraw(amount)
                    print(f"✅ Withdraw successful: ₹{amount}")
                    print(f"💰 Balance: ₹{self.__initial_balance}")
                    self.__Last_transaction=self.__generate_receipt('WITHDRAW',amount)
                    print(self.__generate_receipt('WITHDRAW',amount))
                else:
                        print('❌ Invalid amount')
            else:
                    print("❌ Authentication failed")
            
obj1=Bank('janani',3245,1123,3000)

while True:
    print('''
           🏦 ============================= 🏦
                  WELCOME TO SBI BANK
           🏦 ============================= 🏦

           💰 1. Deposit Money
           💸 2. Withdraw Money
           💳 3. Show Balance
           👤 4. Show Details
           🧾 5. Last Transaction
           🚪 6. Exit
           ''')

    n=int(input("👉 Enter a choice:"))

    if n==1:
        obj1.deposit_money()

    elif n==2:
        obj1.withdraw_money()

    elif n==3:
        obj1.show_balance()

    elif n==4:
        obj1.show_details()

    elif n==5:
        obj1.Lst_transaction()

    elif n==6:
        print("👋 EXIT - Thank you for banking with SBI!")
        break

    else:
        print('⚠️ Enter Valid Number')
    
