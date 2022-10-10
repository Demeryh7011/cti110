Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("This program calculates and display travel expenses")
This program calculates and display travel expenses
>>> budget=float(input("Enter Budget: "))
Enter Budget: 1200
>>> destination=input("Enter your travel destination: ")
Enter your travel destination: Ashville
>>> gas = float(input("How much do you think you will spend on gas?"))
How much do you think you will spend on gas? 250
>>> hotel = float(input("Approximately, how much will you need for accomodation/hotel?"))
Approximately, how much will you need for accomodation/hotel? 300
>>> food = float(input("Last, how much do you need for food?"))
Last, how much do you need for food? 200
>>> print("-----------Travel Expenses----------------")
-----------Travel Expenses----------------
>>> print("Location: \t\t\t", destination)
Location: 			 Ashville
>>> print("Initial Budget: \t", f"${budget}")
Initial Budget: 	 $1200.0
>>> print("Fuel: \t\t\t\t", f"${gas}")
Fuel: 				 $250.0
>>> print("Accomodation: \t\t", f"${hotel}")
Accomodation: 		 $300.0
>>> print("Food: \t\t\t\t", f"${food}")
Food: 				 $200.0
>>> print("------------------------------------------")
------------------------------------------
>>> print("Remaining Balance: \t", f"${budget-gas-hotel-food}")
Remaining Balance: 	 $450.0
