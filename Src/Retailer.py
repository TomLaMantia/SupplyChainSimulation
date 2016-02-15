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
from Settings import *

class Retailer:
    
    def __init__(self, initialStock, outgoingOrdersQueue, incomingDeliveriesQueue):
        """
        -------------------------------------------------------
        Constructor for the Retailer class.
        -------------------------------------------------------
        Preconditions: 
            initialStock - an integer representing the current stock
            outgoingOrdersQueue - a queue object for the outgoing orders to the wholesaler.
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
        self.outgoingOrdersQueue = outgoingOrdersQueue
        self.incomingDeliveriesQueue = incomingDeliveriesQueue
        self.costsIncurred = 0
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
        #This is a temp value of 5!!!!!!!! Will choose dynamically later!
        self.outgoingOrdersQueue.PushOrder(5)
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
        if self.currentStock >= self.numCasesOnOrderByCustomer:
            deliveryQuantity = self.numCasesOnOrderByCustomer
            self.currentStock -= deliveryQuantity
            self.numCasesOnOrderByCustomer -= deliveryQuantity
        #If the current stock cannot cover the order, we must fill as much as we can, and back-order the rest.
        elif self.currentStock >= 0 and self.currentStock < self.numCasesOnOrderByCustomer:
            deliveryQuantity = self.currentStock
            self.currentStock = 0
            self.numCasesOnOrderByCustomer -= deliveryQuantity

        return deliveryQuantity
    
    def CalcCostForTurn(self):
        """
        -------------------------------------------------------
        This function calculates the total costs incurred for the
        current turn. 
        -------------------------------------------------------
        Preconditions: This program must be called LAST in the turn
            sequence to account for orders taken and deliveries.
        Postconditions:
            Returns costsThisTurn - the total cost incurred during
            this turn.
        -------------------------------------------------------
        """
        costsThisTurn = 0
        
        inventoryStorageCost = self.currentStock * STORAGE_COST_PER_UNIT
        backorderPenaltyCost = self.numCasesOnOrderByCustomer * BACKORDER_PENALTY_COST_PER_UNIT
        
        costsThisTurn = inventoryStorageCost + backorderPenaltyCost
        
        return costsThisTurn
    
    def TakeTurn(self, weekNum):
        
        #The steps for taking a turn are as follows:
        
        #RECEIVE NEW DELIVERY FROM WHOLESALER
        ReceiveOrderFromWholesaler()    #This also advances the queue!
        
        #RECEIVE NEW ORDR FROM CUSTOMER
        self.numCasesOnOrderByCustomer += self.customer.CalculateOrder(weekNum)
        
        #PREPARE DELIVERY
        self.customer.RecieveFromRetailer(self.DeliverBeer())
        
        #PLACE ORDER
        self.PlaceOrderToWholesaler()
        
        #UPDATE COSTS
        self.costsIncurred += self.CalcCostForTurn(weekNum)
        
        return