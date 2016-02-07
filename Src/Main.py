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
Version: February 7th 2016
-------------------------------------------------------
"""

from SupplyChainQueue import SupplyChainQueue
from Wholesaler import Wholesaler
from Retailer import Retailer
 
# q = SupplyChainQueue()
# q.PushOrder(10)
# q.AdvanceQueue()
# q.PushOrder(30)
# print(q.TakeDelivery())
# q.AdvanceQueue()
# print(q.TakeDelivery())
