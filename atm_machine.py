import sys
import getpass

# input small letter only
M = True
while M:
    if M == True:
        login = input(" LOG IN?")
        if (login != "yes"):
            sys.exit ("COME BACK LATER")
            M=False
            break
        else:
               print("""
                    ATM SYSTEM    
            """)
         
         # username is marygraceelias
         # pasword  is gracia123
         
        username = input("USERNAME:")
        password = getpass.getpass("PASSWORD:")
       
        if (username != "marygraceelias" and password != "gracia123"):
            print("""
                    ERROR LOG IN  
            """)
       
        elif (username != "marygraceelias" and password == "gracia123"):
              print("""
                    ERROR LOG IN
            """)
       
       
        elif (username == "marygraceelias" and password != "gracia123"):
             print("""
                  ERROR LOG IN
            """)
       
        else:
            print("""
              ******************************
              ******************************
              **                          **
              **      MARYGRACE ELIAS     **
              **      ACCOUNT             **
              ******************************
              ******************************""")
            money = 15000
           
            transaction = True
            while transaction:
                if transaction == True:
                    print("""
                 ::::::::::::::::::::::::::::::::
                 ::                            ::
                 ::   CHOOSE YOUR TRANSACTION  ::
                 ::       1) BALANCED          ::  
                 ::       2) WITHDRAW          ::
                 ::       3) DEPOSIT           ::
                 ::       4) LOG OUT           ::
                 ::                            ::
                 ::::::::::::::::::::::::::::::::
                """)
               
                    option = int(input("Enter Transaction:"))
                    if (option == 1):
                        print("Total Balance: Php ", money,".00")
                   
                    elif (option == 2):
                        out = int(input("Enter amount:"))
                        if (out > money):
                            print("YOUR OUT OF MONEY")
                        else:
                            withdraw = money - out
                            print(" Balance: Php", withdraw,".00")
               
                    elif (option == 3):
                        IN = int(input("Enter amount:"))
                        deposit = money + IN
                        print(" Balance: Php", deposit,".00")
                   
                    elif (option == 4):
                        back = input("WOULD YOU LIKE TO LOG OUT?")
                        if (back == "yes"):
                            transaction = False
                            print("""
                     >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                     >>                            >>
                     >>  You successfully log out  >>
                     >>                            >>
                     >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                     """)
                            break
                        else:
                            print("try again later")