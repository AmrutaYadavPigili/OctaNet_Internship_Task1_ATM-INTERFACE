#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time


# In[2]:


print("Please Insert Your CARD")
time.sleep(5)
password=1234
pin=int(input("Enter your ATM Pin"))
balance = 10000
if pin==password:
    while True:
        print(""""
        1 == balance
        2 == withdraw balance
        3 == deposit balance
        4 == exit
        """)
        try:
            option=int(input("Please enter your choice:"))
        except:
            print("Please enter valid option")
        if option==1:
            print(f"Your Current Balance is {balance}")
        if option==2:
            withdraw_amount=int(input("Please enter withdraw_amount: "))
            balance=balance-withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"Your Updated Balance is {balance}")
        if option==3:
            deposit_amount=int(input("Please enter deposit_amount"))
            balance=balance+deposit_amount
            print(f"{deposit_amount}is credited to your account")
            print(f"Your Updated Balance is {balance}")
        if option==4:
            break
        
else:
    print("Wrong Pin, Please try again")
    


# In[ ]:




