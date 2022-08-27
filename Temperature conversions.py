import time
from tkinter import *

#CONVERSION TABLE
while True:
    temp = int(input("What is the current temperature in fahrenheit?\n"))

    Temptype = input("Would you like this converted to celcius or kelvin?\n")
    if Temptype == "kelvin": 
        print(f"Temperature in kelvin is: {round((((temp - 32)*5)/9)+273.15)}\n")
        time.sleep(3)
    elif Temptype == "celcius":
        print(f"Temperature in celcius is: {round((temp - 32)*.5556)}\n")
        time.sleep(3)