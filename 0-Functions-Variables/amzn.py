welcomeMessage = "Welcome to Thirdspace!!!!!"
print(welcomeMessage)
print("Add add a new company to listings...")

# input function / captures an input and assignes it to a variable
companyName = input("Company Name: ")
ceo = input("CEO: ")


def companyInfo(name, ceo, exchange="NASDAQ"):
    print("_________________________________________")
    print("Company Name: ", name)
    print("Exchange:", exchange)
    print("Ceo: ", ceo)
    print("_________________________________________")


# Function Call
companyInfo(companyName, ceo)
