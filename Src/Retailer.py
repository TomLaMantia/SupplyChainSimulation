"""
-------------------------------------------------------
This file contains and defines the Retailer class.
-------------------------------------------------------
Author:  Tom LaMantia
Email:   tom@lamantia.mail.utoronto.ca
Version: February 7th 2016
-------------------------------------------------------
"""
from Wholesaler import Wholesaler

class Retailer:
    
    def __init__(self, theWholesaler, initialStock):
        
        self.theWholesaler = theWholesaler
        self.currentStock =  initialStock
        return
    
    def RecieveCustomerOrder(self, numberOfCases):
        
        return
    
    def PlaceOrderToWholesaler(self, numberOfCasesToOrder):
        
        return
    
    def DeliverBeer(self):
        
        return
    
    