"""
-------------------------------------------------------
This file contains program settings and configurations.
-------------------------------------------------------
Author:  Tom LaMantia
Email:   tom@lamantia.mail.utoronto.ca
Version: February 14th 2016
-------------------------------------------------------
"""

"""
-------------------------------------------------------
Program constants are defined here. 
-------------------------------------------------------
"""
STORAGE_COST_PER_UNIT = 0.5
BACKORDER_PENALTY_COST_PER_UNIT = 1

#We can play the full game since no actor is programmed to dump stock near end of game
WEEKS_TO_PLAY = 36

QUEUE_DELAY_WEEKS = 2

INITIAL_STOCK = 12

INITIAL_COST = 0

INITIAL_CURRENT_ORDERS = 0

CUSTOMER_INITIAL_ORDERS = 4
CUSTOMER_SUBSEQUENT_ORDERS = 8

TARGET_STOCK = 12