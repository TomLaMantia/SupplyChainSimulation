"""
-------------------------------------------------------
This file contains and defines the Factory class.
-------------------------------------------------------
Author:  Tom LaMantia
Email:   tom@lamantia.mail.utoronto.ca
Version: February 7th 2016
-------------------------------------------------------
"""

from Settings import *
from SupplyChainActor import SupplyChainActor
from SupplyChainQueue import SupplyChainQueue

class Factory(SupplyChainActor):
    
    def __init__(self, incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue):
        """
        -------------------------------------------------------
        Constructor for the Factory class.
        -------------------------------------------------------
        Preconditions: incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue - 
                the supply chain queues. Note: outgoingOrdersQueue and incomingDeliveriesQueue should be NONE.
        Postconditions:
            Initializes the Factory object in its initial state
            by calling parent constructor and setting the
            retailer's customer.
        -------------------------------------------------------
        """
        super().__init__(incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue)
        self.BeerProductionDelayQueue = SupplyChainQueue()
        
        #We assume that the factory already has some runs in production. This is in the rules, and ensures initial stability.
        self.BeerProductionDelayQueue.PushEnvelope(CUSTOMER_INITIAL_ORDERS)
        self.BeerProductionDelayQueue.PushEnvelope(CUSTOMER_INITIAL_ORDERS)
        return
    
    def ProduceBeer(self):
        amountOfBeerToProduce = 8
        self.BeerProductionDelayQueue.PushEnvelope(amountOfBeerToProduce)
        return
    
    def FinishProduction(self):
        
        amountProduced = self.BeerProductionDelayQueue.PopEnvelope()
        
        if amountProduced > 0:
            self.currentStock += amountProduced
        
        return
     
    def TakeTurn(self, weekNum):
        
        #The steps for taking a turn are as follows:
        
        #SOME PREVIOUS PRODUCTION RUNS FINISH BREWING.
        self.FinishProduction()
        
        #RECEIVE NEW ORDER FROM DISTRIBUTOR
        self.ReceiveIncomingOrders()     #This also advances the queue!
        
        #PREPARE DELIVERY
        self.PlaceOutgoingDelivery(self.CalcBeerToDeliver())
        
        #PRODUCE BEER
        self.ProduceBeer()
        
        #UPDATE COSTS
        self.costsIncurred += self.CalcCostForTurn()
        
        return