import phonenumbers
from phonenumbers import timezone, geocoder, carrier
from main import mynumber 

phoneNumber = phonenumbers.parse(mynumber)
timeZone = timezone.time_zones_for_number(phoneNumber)


#print(operator)

# Getting carrier of a phone number
Carrier = carrier.name_for_number(phoneNumber, 'en')

# Getting region information
Region = geocoder.description_for_number(phoneNumber, 'en')

possible_number = phonenumbers.is_possible_number(phoneNumber)
valid_number = phonenumbers.is_valid_number(phoneNumber)

print("Continent and City Name Is :- " ,timeZone)
print(" ")
print("Operator Name is :- " ,Carrier)
print(" ")
print("Country Name Is :- " ,Region)
print(" ")
print(possible_number, "It's a Possible Number")
print(" ")
print(valid_number, "It's a Valid Number")

