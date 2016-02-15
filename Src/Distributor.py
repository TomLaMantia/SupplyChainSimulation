"""
-------------------------------------------------------
This file contains and defines the Distributor class.
-------------------------------------------------------
Author:  Tom LaMantia
Email:   tom@lamantia.mail.utoronto.ca
Version: February 7th 2016
-------------------------------------------------------
"""

from SupplyChainActor import SupplyChainActor

class Distributor(SupplyChainActor):
    
    def __init__(self, initialStock, outgoingOrdersToFactoryQueue , incomingDeliveriesFromFactoryQueue,
                 outogingOrdersToWholesalerQueue, incomingOrdersFromWholesalerQueue):
        """
        -------------------------------------------------------
        Constructor for the Distributor class.
        -------------------------------------------------------
        Preconditions: 
            
        Postconditions:
            Initializes the Distributor object in its initial state.
        -------------------------------------------------------
        """
        self.numberOfCasesOnOrderByWholesaler = 0
        self.outgoingOrdersToFactoryQueue  = outgoingOrdersToFactoryQueue 
        self.incomingDeliveriesFromFactoryQueue = incomingDeliveriesFromFactoryQueue
        self.outogingOrdersToWholesalerQueue = outogingOrdersToWholesalerQueue
        self.incomingOrdersFromWholesalerQueue = incomingOrdersFromWholesalerQueue
        return
    
    
    def TakeTurn(self, weekNum):
        
        #The steps for taking a turn are as follows:
        
        #RECEIVE NEW DELIVERY FROM FACTORY
        self.ReceiveIncomingDelivery()    #This also advances the queue!
        
        #RECEIVE NEW ORDER FROM WHOLESALER
        self.ReceiveIncomingOrders()     #This also advances the queue!
        
        #PREPARE DELIVERY
        self.PlaceOutgoingDelivery(self.CalcBeerToDeliver())
        
        #PLACE ORDER
        self.PlaceOutgoingOrder()
        
        #UPDATE COSTS
        self.costsIncurred += self.CalcCostForTurn(weekNum)
        
        return