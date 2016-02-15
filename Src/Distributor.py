"""
-------------------------------------------------------
This file contains and defines the Distributor class.
-------------------------------------------------------
Author:  Tom LaMantia
Email:   tom@lamantia.mail.utoronto.ca
Version: February 7th 2016
-------------------------------------------------------
"""

class Distributor:
    
    def __init__(self, initialStock, outgoingOrdersQueue, incomingDeliveriesQueue):
        """
        -------------------------------------------------------
        Constructor for the Distributor class.
        -------------------------------------------------------
        Preconditions: 
            
        Postconditions:
            Initializes the Distributor object in its initial state.
        -------------------------------------------------------
        """
        self.currentStock = initialStock
        self.numberOfCasesOnOrderByWholesaler = 0
        self.outgoingOrdersQueue = outgoingOrdersQueue
        self.incomingDeliveriesQueue = incomingDeliveriesQueue
        self.costsIncurred = 0
        return
    
    def PlaceOrderToFactory(self):
        
        return
    
    def ReceiveOrderFromFactory(self):
        
        return
    
    def DeliverBeer(self):
        
        return
    
    def CalcCostsForTurn(self):
        
        return
    
    def TakeTurn(self):
        
        return