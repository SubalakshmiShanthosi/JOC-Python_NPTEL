# @Author: subalakshmi
# @Date:   2019-09-25T18:32:14+05:30
# @Last modified by:   subalakshmi
# @Last modified time: 2019-09-25T18:37:54+05:30

import random
import matplotlib.pyplot as plt
#Account of money possesed by one
account=0
x=[]
y=[]

for i in range(365):
    # Accepting for seven days
    # bet = int(input("Your bet from 1 to 10: "))
    x.append(i+1)
    bet = random.randint(1,10)
    lucky_draw=random.randint(1,10)
    #print("My bet: "+str(bet),end='\n')
    #print("Lucky draw: "+str(lucky_draw),end='\n')

    # User wons - he spent 100 initially , 900 was the profit
    if bet==lucky_draw:
        account=account+900-100
    else:
        account=account-100
    y.append(account)
#print("Amount in your account after one month: "+ str(account),end='\n')
plt.plot(x,y)
plt.xlabel("Days")
plt.ylabel("Profit in a day")
plt.show(block=True)
