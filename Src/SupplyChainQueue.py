"""
-------------------------------------------------------
This file contains and defines the SupplyChainQueue class. 
The SupplyChainQueue consists of a two element list. Element
0 is the oldest order/delivery in the queue, and element 1
is the second oldest order/delivery in the queue,ect. The
queue length is limited by the queueLength parameter.
-------------------------------------------------------
Author:  Tom LaMantia
Email:   tom@lamantia.mail.utoronto.ca
Version: February 14th 2016
-------------------------------------------------------
"""

class SupplyChainQueue():
    
    def __init__(self, queueLength):
        """
        -------------------------------------------------------
        Constructor for the SupplyChainQueue class.
        -------------------------------------------------------
        Preconditions: None
        Postconditions: Initializes an empty supply chain queue.
        -------------------------------------------------------
        """
        self.queueLength = queueLength
        self.data = []
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
        
        if len(self.data) < self.queueLength:
            self.data.append(numberOfCasesToOrder)
            orderSuccessfullyPlaced = True
            
        return orderSuccessfullyPlaced
    
    def AdvanceQueue(self):
        """
        -------------------------------------------------------
        This utility function advances the queue. This mechanism
        drives the delay loop.
        -------------------------------------------------------
        Preconditions: None.
        Postconditions: The item at index [1] (second oldest) is moved
            to index [0], item at index [2] is moved to index [1], etc...
        -------------------------------------------------------
        """
        self.data.pop(0)
        return
    
    def TakeDelivery(self):
        """
        -------------------------------------------------------
        Returns the beer order in the queue.
        -------------------------------------------------------
        Preconditions: None.
        Postconditions: Returns the number of cases of beer ordered.

        This method also advances the queue!
        -------------------------------------------------------
        """
        if len(self.data) >= 1:
            quantityDelivered = self.data[0]
            self.AdvanceQueue()
        else:
            quantityDelivered = 0
        
        return quantityDelivered
    
    def PrettyPrint(self):
        """
        -------------------------------------------------------
        Pretty prints the queue.
        -------------------------------------------------------
        Preconditions: None.
        Postconditions: Queue state is printed to the Python console.
        -------------------------------------------------------
        """
        print(self.data)
        return