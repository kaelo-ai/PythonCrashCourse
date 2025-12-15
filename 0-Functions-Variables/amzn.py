welcomeMessage = "Welcome to Thirdspace!!!!!"
print(welcomeMessage)
print("Add add a new company to listings...")

# input function / captures an input and assignes it to a variable
companyName = input("Company Name: ")
ceo = input("CEO: ")
marketCap = input("Market Cap: ")
peRatio = input("PE Ratio: ")
#create function 


def companyInfo(name, ceo, marketCap, exchange="NASDAQ"):
    print("_________________________________________")
    print("Company Name: ", name)
    print("Exchange:", exchange)
    print("Ceo: ", ceo)
    print("Market Cap:", marketCap)
    print("PE Ratio: ", peRatio)
    print("_________________________________________")


# Function Call
companyInfo(companyName, ceo, marketCap,)
print ("Success!")