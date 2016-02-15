"""
-------------------------------------------------------
This file contains and defines the Factory class.
-------------------------------------------------------
Author:  Tom LaMantia
Email:   tom@lamantia.mail.utoronto.ca
Version: February 7th 2016
-------------------------------------------------------
"""

from SupplyChainActor import SupplyChainActor
from SupplyChainQueue import SupplyChainQueue

class Factory(SupplyChainActor):
    
    def __init__(self, IncomingOrdersFromDistributorQueue, OutgoingDeliveriesToDistributorQueue):
        
        self.numberOfCasesOnOrderByDistributor = 0
        self.IncomingOrdersFromDistributorQueue = IncomingOrdersFromDistributorQueue
        self.OutgoingDeliveriesToDistributorQueue = OutgoingDeliveriesToDistributorQueue
        self.BeerProductionDelayQueue = SupplyChainQueue()
        return
    
    def ReceiveOrderFromDistributor(self):
        
        return
    
    
    def ProduceBeer(self):
        
        return
     
    def TakeTurn(self, weekNum):
        
        return