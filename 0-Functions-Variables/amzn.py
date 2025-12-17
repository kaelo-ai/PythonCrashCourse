welcomeMessage = "Welcome to Thirdspace!!!!!"
print(welcomeMessage)
print("Add add a new company to listings... - amzn.py:3")

# input function / captures an input and assignes it to a variable
companyName = input("Company Name: ")
ceo = input("CEO: ")
marketCap = input("Market Cap: ")
openingPrice = input ("Opening Price: ")
closingPrice = input ("Closing Price: ")
priceMovement = (float(closingPrice)- float(openingPrice))
peRatio = int(input("PE Ratio: "))
#create function 


def companyInfo(name, ceo, marketCap, exchange="NASDAQ"):
    print("________________________________________ - amzn.py:16")
    print("Company Name: - amzn.py:17", name)
    print("Exchange: - amzn.py:18", exchange)
    print("Ceo: - amzn.py:19", ceo)
    #print("PE Ratio: ", peRatio)
    pe = int(input("PE Ratio: "))
    if pe <50:
            print("strong,buy - amzn.py:25")
    if pe >50:
            print("strong sell - amzn.py:27")
    elif pe ==50:
            print("neutral - amzn.py:29")
    print("_________________________________________ - amzn.py:30")

def tradeActivity(opening,closing, priceMovement):
    print("Opening Price: - amzn.py:33", openingPrice)
    print("Closing Price: - amzn.py:34", closingPrice)
    priceMovement = (float(closingPrice)- float(openingPrice))
    if priceMovement >0:
        print("Price went down by", priceMovement)
    if priceMovement <0:
        print("Price went up by", priceMovement)
    elif priceMovement ==0:
        print("No price movement")
# Function Call Company Info
companyInfo(companyName, ceo, marketCap,)
# Function Call Trade Activity
tradeActivity(openingPrice, closingPrice, priceMovement,)

print ("Success! - amzn.py:38")