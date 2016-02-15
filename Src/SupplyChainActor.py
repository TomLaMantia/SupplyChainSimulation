"""
-------------------------------------------------------
This file contains and defines the SupplyChainActor class.
-------------------------------------------------------
Author:  Tom LaMantia
Email:   tom@lamantia.mail.utoronto.ca
Version: February 7th 2016
-------------------------------------------------------
"""

from Settings import *

class SupplyChainActor:
    
    def __init__(self):
        self.currentStock = INITIAL_STOCK
        self.costsIncurred = INITIAL_COST
        return
    
    def CalcBeerToDeliver(self):
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