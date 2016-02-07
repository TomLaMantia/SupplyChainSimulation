"""
-------------------------------------------------------
This file contains and defines the SupplyChainQueue class. 
The SupplyChainQueue consists of a two element list. Element
0 is the oldest order/delivery in the queue, and element 1
is the newest order/delivery in the queue.
-------------------------------------------------------
Author:  Tom LaMantia
Email:   tom@lamantia.mail.utoronto.ca
Version: February 7th 2016
-------------------------------------------------------
"""

class SupplyChainQueue():
    
    def __init__(self):
        """
        -------------------------------------------------------
        Constructor for the SupplyChainQueue class.
        -------------------------------------------------------
        Preconditions: None
        Postconditions: Initializes an empty supply chain queue.
        -------------------------------------------------------
        """
        self.data = [None, None]
        return
    
    def PushOrder(self, numberOfCasesToOrder):
        """
        -------------------------------------------------------
        Places an order/delivery into the supply chain queue.
        -------------------------------------------------------
        Preconditions: numberOfCases - an integer which
            indicates the number of cases to order/send out.
        Postconditions: Returns True if the order is successfully
            placed, False otherwise. 
        -------------------------------------------------------
        """
        orderSuccessfullyPlaced = False
        
        if self.data[1] == None:
            self.data[1] = numberOfCasesToOrder
            orderSuccessfullyPlaced = True
            
        return orderSuccessfullyPlaced
    
    def TakeDelivery(self):
        """
        -------------------------------------------------------
        Returns the beer order in the queue.
        -------------------------------------------------------
        Preconditions: None.
        Postconditions: Returns the number of cases of beer ordered. 
        -------------------------------------------------------
        """
        if self.data[0] != None:
            quantityDelivered = self.data[0]
            self.data[0] = None
        else:
            quantityDelivered = 0
        
        return quantityDelivered
    
    def AdvanceQueue(self):
        """
        -------------------------------------------------------
        This utility function advances the queue. This mechanism
        drives the delay loop.
        -------------------------------------------------------
        Preconditions: None.
        Postconditions: The item at index [1] (newest) is moved
            to index [0], and becomes the oldest item.
        -------------------------------------------------------
        """
        self.data[0] = self.data[1]
        self.data[1] = None
        return