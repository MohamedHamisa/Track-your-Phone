import phonenumbers
from phonenumbers import carrier  #to service provider name
number = ""
from phonenumbers import geocoder #transformation a description of a location
ch_number = phonenumders.parse(number,"CH")  #for  country name
print(geocoder.description_for_number(ch_number,"en"))
service_number = phonenumbers.parse(number,"en")
print(carrier.name_for_number(service_number,"en"))
