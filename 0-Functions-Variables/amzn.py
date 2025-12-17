from email.mime import base


welcomeMessage = "Welcome to KLS Trading!!!!!"
print(welcomeMessage)
print("Add add a new company to listings...")

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
    print("________________________________________")
    print("Company Name:", name)
    print("Ceo:", ceo)
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
            print("strong,buy")
    if pe >50:
            print("strong sell")
    elif pe ==50:
            print("neutral")
    print("_________________________________________")

def tradeActivity(opening,closing, priceMovement):
    print("Opening Price:", openingPrice)
    print("Closing Price:", closingPrice)
    priceMovement = (float(closingPrice)- float(openingPrice))
    if priceMovement >0:
        print("Price went down by", priceMovement)
    if priceMovement <0:
        print("Price went up by", priceMovement)
    elif priceMovement ==0:
        print("No price movement")

def startAgain(choiceYes, choiceNo, input, navigate):
    print("Would you like to start again?", choiceYes, "or", choiceNo)
    if input == (bool(choiceYes)): 
           navigate = companyInfo(companyName, ceo, exchanges, marketCap, selection=list,)
    elif input == choiceNo:
            print("Thank you for testing KLS Trading")
# Function Call Company Info
companyInfo(companyName, ceo, exchanges, marketCap, selection=list,)
# Function Call Trade Activity
tradeActivity(openingPrice, closingPrice, priceMovement,)
#Function Call Start Again
startAgain(choiceYes, choiceNo, bool, navigate=companyInfo(companyName, ceo, exchanges, marketCap, selection=list,))

print ("Success!")