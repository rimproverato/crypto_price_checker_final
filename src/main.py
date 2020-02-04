# import tkinter 
import tkinter
import requests

# initialize tkinter
main_window = tkinter.Tk()
# make the window size
main_window.geometry("500x800")

# main window title
main_window.title("Crypto Price Checker")

# coin marketcap url
coin_marketcap_api = "https://api.coinmarketcap.com/v1/ticker/"
# get marketcap
def get_marketcap(coin_name):
    web_response = requests.get(coin_marketcap_api + coin_name)
    web_response_json = web_response.json()
    return (web_response_json[0]["market_cap_usd"])

# get price
def get_price(coin_name):
    web_response = requests.get(coin_marketcap_api + coin_name)
    web_response_json = web_response.json()
    return round(float((web_response_json[0]["price_usd"])))
# coin name
coin_name = tkinter.Label(main_window, text="Coin Name", font =  ("times", 16), padx = 40, pady = 20)
coin_name.grid(row = 0, column = 0)

# Market cap
market_cap = tkinter.Label(main_window, text="Market Cap", font =  ("times", 16), padx = 40, pady = 20)
market_cap.grid(row = 0, column = 1)

# Price
price = tkinter.Label(main_window, text="Price", font =  ("times", 16), padx = 40, pady = 20)
price.grid(row = 0, column = 2)

# number 1
number_one = tkinter.Label(main_window, text = "1.", font = ("times", 15), pady = 20)
number_one.grid(row = 1, column = 0, sticky = tkinter.W)

# bitcoin
bitcoin = tkinter.Label(main_window, text = " Bitcoin", font = ("times", 15))
bitcoin.grid(row = 1, column = 0)

# bitcoin marketcap
bitcoin_marketcap = tkinter.Button(main_window, text = f"USD {get_marketcap('bitcoin')}", font = ("times", 15))
bitcoin_marketcap.grid(row = 1, column = 1)

# bitcoin price
bitcoin_price = tkinter.Button(main_window, text = f"USD {get_price('bitcoin')}", font = ("times", 15))
bitcoin_price.grid(row = 1, column = 2)

# number 2
number_two = tkinter.Label(main_window, text = "2.", font = ("times", 15), pady = 20)
number_two.grid(row = 2, column = 0, sticky = tkinter.W)

# Ethereum
ethereum = tkinter.Label(main_window, text = " Ethereum", font = ("times", 15))
ethereum.grid(row = 2, column = 0)

# Ethereum marketcap
ethereum_marketcap = tkinter.Button(main_window, text = f"USD {get_marketcap('ethereum')}", font = ("times", 15))
ethereum_marketcap.grid(row = 2, column = 1)

# Ethereum price
ethereum_price = tkinter.Button(main_window, text = f"USD {get_price('ethereum')}", font = ("times", 15))
ethereum_price.grid(row = 2, column = 2)

# number 3
number_three = tkinter.Label(main_window, text = "3.", font = ("times", 15), pady = 20)
number_three.grid(row = 3, column = 0, sticky = tkinter.W)

# Monero
monero = tkinter.Label(main_window, text = "Monero", font = ("times", 15))
monero.grid(row = 3, column = 0)


# Monero marketcap
monero_marketcap = tkinter.Button(main_window, text = f"USD {get_marketcap('monero')}", font = ("times", 15))
monero_marketcap.grid(row = 3, column = 1)

# Monero price
monero_price = tkinter.Button(main_window, text = f"USD {get_price('monero')}", font = ("times", 15))
monero_price.grid(row = 3, column = 2)

# create main loop
main_window.mainloop()