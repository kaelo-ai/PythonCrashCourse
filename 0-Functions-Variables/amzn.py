from email.mime import base


welcomeMessage = "Welcome to KLS Trading!!!!!"
print(welcomeMessage)
print("Add add a new company to listings... - amzn.py:3")

# input function / captures an input and assignes it to a variable
companyName = input("Company Name: ")
ceo = input("CEO: ")
marketCap = input("Market Cap: ")
estYear = input("Year Founded? ")
exchanges = ["NASDAQ","DOW","S&P500","FTSE","DAX","NIKKEI225"]
openingPrice = input ("Opening Price: ")
closingPrice = input ("Closing Price: ")
choiceYes = bool(True)
choiceNo = bool(False)
priceMovement = (float(closingPrice)- float(openingPrice))
peRatio = int(input("PE Ratio: "))
list (enumerate(exchanges))
selection = [(0,"NASDAQ"), (1,"DOW"), (2,"S&P500"), (3,"FTSE"), (4,"DAX"), (5,"NIKKEI225")]
#create function 


def companyInfo(name, ceo, exchanges, marketCap,selection,):
    print("________________________________________ - amzn.py:16")
    print("Company Name: - amzn.py:17", name)
    print("Ceo: - amzn.py:19", ceo)
    print("Select exhange", list(enumerate(exchanges)))
    selection = str(input("Select exchange"))
    if selection == "NASDAQ":
          print("Session opens @ 16:30")
    elif selection =="DOW":
          print("Session opens @ 16:30")
    elif selection == "S&P500" or selection == "FTSE" or selection == "DAX" or selection == "NIKKEI225":
          print("Sorry you are looking at the wrong stock, try again later")

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
companyInfo(companyName, ceo, exchanges, marketCap, selection=list,)
# Function Call Trade Activity
tradeActivity(openingPrice, closingPrice, priceMovement,)

print ("Success! - amzn.py:38")