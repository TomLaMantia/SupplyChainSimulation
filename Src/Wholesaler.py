"""
-------------------------------------------------------
This file contains and defines the Wholesaler class.
-------------------------------------------------------
Author:  Tom LaMantia
Email:   tom@lamantia.mail.utoronto.ca
Version: February 7th 2016
-------------------------------------------------------
"""

from SupplyChainQueue import SupplyChainQueue
from SupplyChainActor import SupplyChainActor

class Wholesaler(SupplyChainActor):
    
    def __init__(self, outgoingOrdersToDistributorQueue, incomingDeliveriesFromDistributorQueue, 
                 incomingOrdersFromRetailerQueue, outgoingDeliveriesToRetailerQueue):
        """
        -------------------------------------------------------
        Constructor for the Wholesaler class.
        -------------------------------------------------------
        Preconditions: 
            
        Postconditions:
            Initializes the retailer object in its initial state.
        -------------------------------------------------------
        """
        self.numberOfCasesOnOrderByRetailer = 0
        self.outgoingOrdersToDistributorQueue = outgoingOrdersToDistributorQueue
        self.incomingDeliveriesFromDistributorQueue = incomingDeliveriesFromDistributorQueue
        self.incomingOrdersFromRetailerQueue = incomingOrdersFromRetailerQueue
        self.outgoingDeliveriesToRetailerQueue = outgoingDeliveriesToRetailerQueue
        return
    
    def PlaceOrderToDistributor(self):
        """
        -------------------------------------------------------
        Places an order to the Distributor. This needs to be determined
        by an appropriate helper function!
        -------------------------------------------------------
        Preconditions: 
            None
        Postconditions:
            Places the order to the Distributor. Note: the advancement
            of the queues is handled by the main program.
        -------------------------------------------------------
        """
        #We will determine this later. For now, we assume 5 during development
        self.outgoingOrdersToDistributorQueue.PushEnvelope(5)
        return
    
    def ReceiveOrderFromDistributor(self):
        """
        -------------------------------------------------------
        Receives an order from the Distributor.
        -------------------------------------------------------
        Preconditions: 
            None
        Postconditions:
            Updates the current stock based on the incoming
            deliveries queue.
        -------------------------------------------------------
        """
        quantityReceived = self.incomingDeliveriesFromDistributorQueue.PopEnvelope()
        
        if quantityReceived > 0:
            self.currentStock += quantityReceived
            
        return
    
    def ReceiveOrderFromRetailer(self):
        """
        -------------------------------------------------------
        Receives an order from the Retailer.
        -------------------------------------------------------
        Preconditions: 
            None
        Postconditions:
            Updates the current order from retailer based on this
            new order from the retailer.
        -------------------------------------------------------
        """
        quantityOrdered = self.incomingOrdersFromRetailerQueue.PopEnvelope()
        
        if quantityOrdered > 0:
            self.numberOfCasesOnOrderByRetailer += quantityOrdered
        return
    
    def TakeTurn(self, weekNum):
        
        #The steps for taking a turn are as follows:
        
        #RECEIVE NEW DELIVERY FROM DISTRIBUTOR
        self.ReceiveOrderFromDistributor()    #This also advances the queue!
        
        #RECEIVE NEW ORDR FROM RETAILER
        self.ReceiveOrderFromRetailer()     #This also advances the queue!
        
        #PREPARE DELIVERY
        self.outgoingDeliveriesToRetailerQueue.PushEnvelope(self.CalcBeerToDeliver())
        
        #PLACE ORDER
        PlaceOrderToDistributor()
        
        #UPDATE COSTS
        self.costsIncurred += self.CalcCostForTurn(weekNum)
        
        return