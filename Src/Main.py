"""
-------------------------------------------------------
The main program. The main program handles the simulation
by co-ordinating the game. This involves incrementing all of the
communication queues between the different parts of the system.

The main program also acts as the customer, receiving the
product at the end of the supply chain system.
-------------------------------------------------------
Author:  Tom LaMantia
Email:   tom@lamantia.mail.utoronto.ca
Version: February 14th 2016
-------------------------------------------------------
"""

from SupplyChainQueue import SupplyChainQueue
from Retailer import Retailer

q1 = SupplyChainQueue()
q2 = SupplyChainQueue()
q3 = SupplyChainQueue()
q4 = SupplyChainQueue()
myRetailer = Retailer(q1, q2, q3, q4)
  
# q = SupplyChainQueue(5)
# for i in range(0,5):
#     q.PushOrder(i)
#     q.PrettyPrint()
# 
# print("----")
# for i in range(0,5):
#     print(q.TakeDelivery())
#     q.PrettyPrint()
# 
# print("----")
# for i in range(5,10):
#     q.PushOrder(i)
#     q.PrettyPrint()



