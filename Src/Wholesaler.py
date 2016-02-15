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
from Settings import *

class Wholesaler:
    
    def __init__(self, initialStock, outgoingOrdersQueue, incomingDeliveriesQueue):
        """
        -------------------------------------------------------
        Constructor for the Wholesaler class.
        -------------------------------------------------------
        Preconditions: 
            
        Postconditions:
            Initializes the retailer object in its initial state.
        -------------------------------------------------------
        """
        self.currentStock = initialStock
        self.numberOfCasesOnOrderByRetailer = 0
        self.outgoingOrdersQueue = outgoingOrdersQueue
        self.incomingDeliveriesQueue = incomingDeliveriesQueue
        self.costsIncurred = 0
        return
    
    def PlaceOrderToDistributer(self):
        
        return
    
    def ReceiveOrderFromDistributor(self):
        
        return
    
    def DeliverBeer(self):
        
        return 
    
    def CalcCostForTurn(self):
        
        return
    
    def TakeTurn(self, weekNum):
        
        return