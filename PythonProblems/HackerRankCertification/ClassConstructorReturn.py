#!/bin/python

import math
import os
import random
import re
import sys


class Car:
    s=0
    u=''
    res=''
    # parameterized constructor 
    def __init__(self, max_speed, speed_unit): 
        self.s = max_speed
        self.u = speed_unit 
        
        
    def __str__(self):
        return str("Car with the maximum speed of "+str(self.s)+" "+str(self.u))
    
class Boat:
    a=0
    res=''
    # parameterized constructor 
    def __init__(self, speed): 
        self.a = speed
    
    def __str__(self):
        return str("Boat with the maximum speed of "+str(self.a) + " knots")
    


if __name__ == '__main__':
    obj1 = Car(120,"km/h")
    print(obj1)
    obj2 = Boat(15)
    print(obj2)
