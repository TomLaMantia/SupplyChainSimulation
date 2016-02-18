"""
-------------------------------------------------------
This file contains and defines the Wholesaler class.
-------------------------------------------------------
Author:  Tom LaMantia
Email:   tom@lamantia.mail.utoronto.ca
Version: February 7th 2016
-------------------------------------------------------
"""

from SupplyChainActor import SupplyChainActor

class Wholesaler(SupplyChainActor):
    
    def __init__(self, incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue):
        """
        -------------------------------------------------------
        Constructor for the Wholesaler class.
        -------------------------------------------------------
        Preconditions: incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue - 
                the supply chain queues.
        Postconditions:
            Initializes the Wholesaler object in its initial state
            by calling parent constructor.
        -------------------------------------------------------
        """
        super().__init__(incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue)
        return
    
    def TakeTurn(self, weekNum):
        
        #The steps for taking a turn are as follows:
        
        #RECEIVE NEW DELIVERY FROM DISTRIBUTOR
        self.ReceiveIncomingDelivery()    #This also advances the queue!
        
        #RECEIVE NEW ORDER FROM RETAILER
        self.ReceiveIncomingOrders()     #This also advances the queue!
        
        #PREPARE DELIVERY
        if weekNum <= 4:
            self.PlaceOutgoingDelivery(4)
        else:
            self.PlaceOutgoingDelivery(self.CalcBeerToDeliver())
        
        #PLACE ORDER
        self.PlaceOutgoingOrder(weekNum)
        
        #UPDATE COSTS
        self.costsIncurred += self.CalcCostForTurn()
        
        return