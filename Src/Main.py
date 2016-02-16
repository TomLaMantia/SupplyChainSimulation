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

from Settings import *
from Customer import Customer
from SupplyChainQueue import SupplyChainQueue
from Retailer import Retailer
from Wholesaler import Wholesaler
from Distributor import Distributor
from Factory import Factory

"""
-------------------------------------------------------
Given two SupplyChainActors B <--> A, where
A is higher in the supply chain, let "top queue" denote A's
outgoingOrderQueue/B's incomingOrderQueue. Let "bottom queue"
denote B's outgoingDeliveryQueue/A's incoming delivery queue. 
-------------------------------------------------------
"""
wholesalerRetailerTopQueue = SupplyChainQueue()
wholesalerRetailerBottomQueue = SupplyChainQueue()

distributorWholesalerTopQueue = SupplyChainQueue()
distributorWholesalerBottomQueue = SupplyChainQueue()

factoryDistributorTopQueue = SupplyChainQueue()
factoryDistributorBottomQueue = SupplyChainQueue()

"""
-------------------------------------------------------
Each queue should have at least 2 orders of size CUSTOMER_INITIAL_ORDER 
-------------------------------------------------------
"""
for i in range(0,2):
    wholesalerRetailerTopQueue.PushEnvelope(CUSTOMER_INITIAL_ORDERS)
    wholesalerRetailerBottomQueue.PushEnvelope(CUSTOMER_INITIAL_ORDERS)
    distributorWholesalerTopQueue.PushEnvelope(CUSTOMER_INITIAL_ORDERS)
    distributorWholesalerBottomQueue.PushEnvelope(CUSTOMER_INITIAL_ORDERS)
    factoryDistributorTopQueue.PushEnvelope(CUSTOMER_INITIAL_ORDERS)
    factoryDistributorBottomQueue.PushEnvelope(CUSTOMER_INITIAL_ORDERS)

"""
-------------------------------------------------------
Now we initialize our SupplyChainObjects. Passing the correct
queues is essential.
-------------------------------------------------------
"""

theCustomer = Customer()
myRetailer = Retailer(None, wholesalerRetailerTopQueue, wholesalerRetailerBottomQueue, None, theCustomer)

myWholesaler = Wholesaler(wholesalerRetailerTopQueue, distributorWholesalerTopQueue,
                          distributorWholesalerBottomQueue, wholesalerRetailerBottomQueue)

myDistributor = Distributor(distributorWholesalerTopQueue, factoryDistributorTopQueue,
                            factoryDistributorBottomQueue, distributorWholesalerBottomQueue)

myFactory = Factory(factoryDistributorTopQueue, None, None, factoryDistributorBottomQueue)

"""
-------------------------------------------------------
Main game-play!
-------------------------------------------------------
"""

for thisWeek in range(0, WEEKS_TO_PLAY):
    
    print("--- Week {0} ---".format(thisWeek))
    myRetailer.TakeTurn(thisWeek)
    myWholesaler.TakeTurn(thisWeek)
    myDistributor.TakeTurn(thisWeek)
    myFactory.TakeTurn(thisWeek)

print(theCustomer.GetBeerReceived())



