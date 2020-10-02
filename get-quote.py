import random

def quote():
    print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    count = len(quotes)


    randQuote = random.randint(0,(count - 1))
    print(quotes[randQuote],end="")

if __name__== "__main__":
    quote()
