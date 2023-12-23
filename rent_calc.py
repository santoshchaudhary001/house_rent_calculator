# house rent charge
# electricity bill 
# charge_spend_per_unit
# wifi + water + waster 300 + 100 + 100
# number of persons 2,3,4,5
# house rent calulator

print("*****************************************************\n")
rent = int(input("Enter your room/flate rent: "))
electricity_bill = int(input("Enter a number of unit: "))
charge_per_unit = int(input("Enter a electricity charge per unit: "))
total_bill = electricity_bill * charge_per_unit
wifi_charge = int(input("Enter your wifi charge: "))
no_of_persons = int(input("Enter a number of persons: "))
final_bill_of_rent = (rent + total_bill + wifi_charge) // no_of_persons
print("*****************************************************\n")
print("Each person pay bill: Rs", final_bill_of_rent)


