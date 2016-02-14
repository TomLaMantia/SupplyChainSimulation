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

class Retailer:
    
    def __init__(self, initialStock, outGoingOrdersQueue, incomingDeliveriesQueue):
        """
        -------------------------------------------------------
        Constructor for the Retailer class.
        -------------------------------------------------------
        Preconditions: 
            initialStock - an integer representing the current stock
            outGoingOrdersQueue - a queue object for the outgoing orders to the wholesaler.
                                This queue is SHARED with the wholesaler (handled by Main)!
            incomingDeliveriesQueue - a queue object for the incoming deliveries from the wholesaler.
                                This queue is SHARED with the wholesaler (handled by Main)!
        Postconditions:
            Initializes the retailer object in its initial state.
        -------------------------------------------------------
        """
        self.customer = Customer()
        self.currentStock =  initialStock
        self.numCasesOnOrderByCustomer = 0
        self.currentBackorder = 0
        self.outGoingOrdersQueue = outGoingOrdersQueue
        self.incomingDeliveriesQueue = incomingDeliveriesQueue
        self.costsIncurred = 0
        return
    
    def ReceiveCustomerOrder(self, numberOfCases):
        """
        -------------------------------------------------------
        Receives an order from the customer
        -------------------------------------------------------
        Preconditions: 
            numberOfCases - the number of cases requested by the
                customer in a given week.
        Postconditions:
            Updates the current orders accordingly.
        -------------------------------------------------------
        """
        self.numCasesOnOrderByCustomer += numberOfCases
        return
    
    def PlaceOrderToWholesaler(self):
        """
        -------------------------------------------------------
        Places an order to the wholesaler. This needs to be determined
        by an appropriate helper function!
        -------------------------------------------------------
        Preconditions: 
            None
        Postconditions:
            Places the order to the customer. Note: the advancement
            of the queues is handled by the main program.
        -------------------------------------------------------
        """
        self.outGoingOrdersQueue.PushOrder(5)
        return
    
    def ReceiveOrderFromWholesaler(self):
        """
        -------------------------------------------------------
        Receives an order to the wholesaler.
        -------------------------------------------------------
        Preconditions: 
            None
        Postconditions:
            Updates the current stock based on the incoming
            deliveries queue.
        -------------------------------------------------------
        """
        quantityReceived = self.incomingDeliveriesQueue.TakeDelivery()
        
        if quantityReceived > 0:
            self.currentStock += quantityReceived
                
        return
    
    def DeliverBeer(self):
        """
        -------------------------------------------------------
        Calculates how much beer to deliver to the customer. The
        current stock and number of cases currently on order by the
        customer are updated from within this function.
        -------------------------------------------------------
        Preconditions: 
            None
        Postconditions:
            Returns deliveryQuantitiy - the number of cases to be delivered
            to the customer. numCasesOnOrderByCustomer, currentStock are
            updated to reflect this delivery quantity. 
        -------------------------------------------------------
        """
        deliveryQuantity = 0
        
         #If we can fill the customer's order, we must do it.
        if currentStock > 0 and self.currentStock >= self.numCasesOnOrderByCustomer:
            deliveryQuantity = self.numCasesOnOrderByCustomer
            self.currentStock -= deliveryQuantity
            self.numCasesOnOrderByCustomer -= deliveryQuantity
        #If the current stock cannot cover the order, we must fill as much as we can, and back-order the rest.
        elif self.currentStock >= 0 and self.currentStock < self.numCasesOnOrderByCustomer:
            deliveryQuantity = self.currentStock
            self.currentStock = 0
            self.numCasesOnOrderByCustomer -= deliveryQuantity

        return deliveryQuantity
    
    def TakeTurn(self):
        
        #The steps for taking a turn are as follows:
        
        #RECEIVE NEW DELIVERY FROM WHOLESALER
        ReceiveOrderFromWholesaler()
        
        #RECEIVE NEW ORDR FROM CUSTOMER
        self.numCasesOnOrderByCustomer += self.customer.CalculateOrder()
        
        #PREPARE DELIVERY
        self.customer.RecieveFromRetailer(self.DeliverBeer())
        
        #PLACE ORDER
        self.PlaceOrderToWholesaler()
        
        return
    
    