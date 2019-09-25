# @Author: subalakshmi
# @Date:   2019-09-25T17:30:12+05:30
# @Last modified by:   subalakshmi
# @Last modified time: 2019-09-25T17:34:39+05:30

import random
#Account of money possesed by one
account=0
for i in range(30):
    # Accepting for seven days
    # bet = int(input("Your bet from 1 to 10: "))
    bet = random.randint(1,10)
    lucky_draw=random.randint(1,10)
    #print("My bet: "+str(bet),end='\n')
    #print("Lucky draw: "+str(lucky_draw),end='\n')

    # User wons - he spent 100 initially , 900 was the profit
    if bet==lucky_draw:
        account=account+900-100
    else:
        account=account-100

print("Amount in your account after one month: "+ str(account),end='\n')
