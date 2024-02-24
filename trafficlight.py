# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 19:29:08 2024

@author: funky
"""

#This program will simulate a traffic light.
import time

class TrafficLight:
    def __init__(self):
        self.color = "Green"
        self.car = False
        
    def greenlight(self):
        self.color = "Green"
        print("The traffic light is currently " + self.color + ". Please proceed.")
    
    def yellowlight(self):
        self.color = "Yellow"
        print("The traffic light is currently flashing " + self.color + ". Slow down.")
    
    def redlight(self):
        self.color = "Red"
        print("The traffic light is currently flashing " + self.color + "! Please stop!")
    
    def checklight(self):
        print("The light is currently " + self.color +".")
    
    def checkcar(self):
        if self.car == False:
            print("There is no car at the traffic light.")
        else:
            print("There is a car at the traffic light.")
    
    def caratlight(self):
        self.car = True
    
    def startlight(self):
        state = True
        while state == True:
            self.greenlight()
            time.sleep(1)
            self.yellowlight()
            time.sleep(1)
            self.redlight()
            Q1 = input("Do you want to continue? ").lower()
            if Q1 == "no":
                break
            elif Q1 == "caratlight":
                self.caratlight()
                Q2 = input("Would you like to check to see if there is a car at the light? ").lower()
                if Q2 == "yes":
                    self.checkcar()
                    Q3 = input("Do you want to resume? ").lower()
                    if Q3 == "no":
                        break
            elif Q1 == "checkcar":
                self.checkcar()
                Q4 = input("Would you like to simulate a car at the light? ").lower()
                if Q4 == "no":
                    Q5 = input("Would you like to resume? ").lower()
                    if Q5 == "no":
                        break
                elif Q4 == "yes":
                    self.caratlight()
                    Q6 = input("Would you like to check to see if there is a car at the light? ").lower()
                    if Q6 == "no":
                        Q7 = input("Would you like to resume? ").lower()
                        if Q7 == "no":
                            break
                    else:
                        self.checkcar()
                        Q8 = input("Would you like to resume? ").lower()
                        if Q8 == "no":
                            break
            elif Q1 == "yellowlight":
                self.yellowlight()
                Q9 = input("Would you like to resume? ").lower()
                if Q9 == "no":
                    break
            elif Q1 == "redlight":
                self.redlight()
                Q10 = input("Would you like to resume? ").lower()
                if Q10 == "no":
                    break

traffic_light = TrafficLight()
traffic_light.startlight()
