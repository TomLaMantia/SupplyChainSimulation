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
    
    def __init__(self, incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue, productionDelayWeeks):
        """
        -------------------------------------------------------
        Constructor for the Factory class.
        -------------------------------------------------------
        Preconditions: incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue - 
                the supply chain queues. Note: outgoingOrdersQueue and incomingDeliveriesQueue should be NONE.
                productionDelayWeeks - an integer value indicating the nunber of weeks required to make a case of beer.
        Postconditions:
            Initializes the Factory object in its initial state
            by calling parent constructor and setting the
            retailer's customer.
        -------------------------------------------------------
        """
        super().__init__(incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue)
        self.BeerProductionDelayQueue = SupplyChainQueue(productionDelayWeeks)
        
        #We assume that the factory already has some runs in production. This is in the rules, and ensures initial stability.
        self.BeerProductionDelayQueue.PushEnvelope(CUSTOMER_INITIAL_ORDERS)
        self.BeerProductionDelayQueue.PushEnvelope(CUSTOMER_INITIAL_ORDERS)
        return
    
    def ProduceBeer(self):
        """
        -------------------------------------------------------
        Calculates the size of this week's production run.
        -------------------------------------------------------
        Preconditions: None.
        Postconditions:
            Calculates the production run using an anchor and maintain
            strategy.
        -------------------------------------------------------
        """
        #We want to cover any backorders, if they exist
        maintain = 0
        if self.currentOrders > 0:
            maintain = self.currentOrders
        
        anchor = 0
        targetInventory = TARGET_STOCK - self.currentStock
        if targetInventory > 0:
            anchor = targetInventory
        
        amountToProduce = maintain + anchor
        self.BeerProductionDelayQueue.PushEnvelope(amountToProduce)
        
        self.lastOrderQuantity = amountToProduce
        
        return
    
    def FinishProduction(self):
        
        amountProduced = self.BeerProductionDelayQueue.PopEnvelope()
        
        if amountProduced > 0:
            self.currentStock += amountProduced
        
        return
     
    def TakeTurn(self, weekNum):
        
        #The steps for taking a turn are as follows:
        
        #PREVIOUS PRODUCTION RUNS FINISH BREWING.
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