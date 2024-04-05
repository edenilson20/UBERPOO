from car import car
from Account import Account
from uberx import uberx
from user import user

if_name_=="_main_";
print ("inicializando las info de los carros")
print("cAR")
car = car ("ams256", Account("kevin gonzalez", "asd122344",
kevingonza210@gmail.com "2134"))
print(vars(car))
print (vars (car,driver))

print("uberx")
uberx = uberx ("klo2233", Account("kevin gon ", "sghj1223"
"kevineden@gemail.com", "234" ), "toyota", "corolla")
print (vars (uberx))
print(vars (uberx.driver))

pr("uber")
user= user("kevin kkk", "SDFG125F", "kevingonzalez210@gmail.com",
"7556")
print(vars(user))