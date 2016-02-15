"""
-------------------------------------------------------
This file contains and defines the Retailer class.
-------------------------------------------------------
Author:  Tom LaMantia
Email:   tom@lamantia.mail.utoronto.ca
Version: February 7th 2016
-------------------------------------------------------
"""

from SupplyChainQueue import SupplyChainQueue
from Customer import Customer
from SupplyChainActor import SupplyChainActor

class Retailer(SupplyChainActor):
    
    def __init__(self, outgoingOrdersToWholesalerQueue, incomingDeliveriesFromWholesalerQuueue):
        """
        -------------------------------------------------------
        Constructor for the Retailer class.
        -------------------------------------------------------
        Preconditions: 
            initialStock - an integer representing the current stock
            outgoingOrdersToWholesalerQueue - a queue object for the outgoing orders to the wholesaler.
                                This queue is SHARED with the wholesaler (handled by Main)!
            incomingDeliveriesFromWholesalerQuueue - a queue object for the incoming deliveries from the wholesaler.
                                This queue is SHARED with the wholesaler (handled by Main)!
        Postconditions:
            Initializes the retailer object in its initial state.
        -------------------------------------------------------
        """
        super(Retailer, self).__init__()
        self.customer = Customer()
        self.numCasesOnOrderByCustomer = 0
        self.outgoingOrdersToWholesalerQueue = outgoingOrdersToWholesalerQueue
        self.incomingDeliveriesFromWholesalerQuueue = incomingDeliveriesFromWholesalerQuueue
        return
    
    def PlaceOrderToWholesaler(self):
        """
        -------------------------------------------------------
        Places an order to the Wholesaler. This needs to be determined
        by an appropriate helper function!
        -------------------------------------------------------
        Preconditions: 
            None
        Postconditions:
            Places the order to the Wholesaler. Note: the advancement
            of the queues is handled by the main program.
        -------------------------------------------------------
        """
        #This is a temp value of 5!!!!!!!! Will choose dynamically later!
        self.outgoingOrdersToWholesalerQueue.PushEnvelope(5)
        return
    
    def ReceiveOrderFromWholesaler(self):
        """
        -------------------------------------------------------
        Receives an order from the Wholesaler.
        -------------------------------------------------------
        Preconditions: 
            None
        Postconditions:
            Updates the current stock based on the incoming
            deliveries queue.
        -------------------------------------------------------
        """
        quantityReceived = self.incomingDeliveriesFromWholesalerQuueue.PopEnvelope()
        
        if quantityReceived > 0:
            self.currentStock += quantityReceived
                
        return
    
    def TakeTurn(self, weekNum):
        
        #The steps for taking a turn are as follows:
        
        #RECEIVE NEW DELIVERY FROM WHOLESALER
        self.ReceiveOrderFromWholesaler()    #This also advances the queue!
        
        #RECEIVE NEW ORDR FROM CUSTOMER
        self.numCasesOnOrderByCustomer += self.customer.CalculateOrder(weekNum)
        
        #PREPARE DELIVERY
        self.customer.RecieveFromRetailer(self.CalcBeerToDeliver())
        
        #PLACE ORDER
        self.PlaceOrderToWholesaler()
        
        #UPDATE COSTS
        self.costsIncurred += self.CalcCostForTurn(weekNum)
        
        return