"""
-------------------------------------------------------
This file contains and defines the Retailer class.
-------------------------------------------------------
Author:  Tom LaMantia
Email:   tom@lamantia.mail.utoronto.ca
Version: February 7th 2016
-------------------------------------------------------
"""

from Customer import Customer
from SupplyChainActor import SupplyChainActor
from SupplyChainQueue import SupplyChainQueue

class Retailer(SupplyChainActor):
    
    def __init__(self, incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue, theCustomer):
        """
        -------------------------------------------------------
        Constructor for the Retailer class.
        -------------------------------------------------------
        Preconditions: incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue - 
                the supply chain queues. Note: outgoingDeliveriesQueue and incomingOrdersQueue should be NONE.
                
                theCustomer - a customer object.
        Postconditions:
            Initializes the retailer object in its initial state
            by calling parent constructor and setting the
            retailer's customer.
        -------------------------------------------------------
        """
        super().__init__(incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue)
        self.customer = theCustomer

        return
    
    def ReceiveIncomingOrderFromCustomer(self, weekNum):
        self.currentOrders += self.customer.CalculateOrder(weekNum)
        return
    
    def ShipOutgoingDeliveryToCustomer(self):
        self.customer.RecieveFromRetailer(self.CalcBeerToDeliver())
        return
    
    def TakeTurn(self, weekNum):
        
        #The steps for taking a turn are as follows:
        
        #RECEIVE NEW DELIVERY FROM WHOLESALER
        self.ReceiveIncomingDelivery()    #This also advances the queue!
        
        #RECEIVE NEW ORDER FROM CUSTOMER
        self.ReceiveIncomingOrderFromCustomer(weekNum)
        
        #CALCULATE AMOUNT TO BE SHIPPED, THEN SHIP IT
        self.ShipOutgoingDeliveryToCustomer()
        
        #PLACE ORDER TO WHOLESALER
        self.PlaceOutgoingOrder()
        
        #UPDATE COSTS
        self.costsIncurred += self.CalcCostForTurn()
        
        return