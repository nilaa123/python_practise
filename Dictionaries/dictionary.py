#All the keys should be unique
customer={
    "name":"jaden smith",
    "age":2,
    "is_male":True
}

print(customer["name"]) #if the key is missing you get an error
print(customer.get("birthday")) #if the key is missing you get "None"

#Incase of absence of key
print(customer.get("birthPlace","key is missing"))

#updation of key
customer["name"]="martin" 
print(customer["name"])

#addition of key
customer["birthday"]="1 jan 2001"
print(customer["birthday"])



