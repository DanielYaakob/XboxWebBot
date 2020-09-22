from selenium import webdriver
from colorama import Fore, Back, Style
import time

your_price = float(400.00)

print("Initiating webdriver")
driver = webdriver.Chrome()

print("Loading amazon.com product page")
driver.get("https://www.amazon.com/Microsoft-Xbox-Console-Wireless-Controller/dp/B07P19XP84/ref=sr_1_1?dchild=1&keywords=xbox+one&qid=1599780027&sr=8-1")


print("finding price")
elem = driver.find_element_by_id("priceblock_ourprice").text

print(Fore.BLUE + "Price = ", elem + Style.RESET_ALL)

with open('prices.txt') as file1:
    for line in file1:
        pass
    last_price = line

elem = float(elem[1:])

if elem <= your_price:
    print(Fore.GREEN + "time to buy" + Style.RESET_ALL)
if elem > your_price:
    print(Fore.RED + "Price too high" + Style.RESET_ALL)

price_diff = elem - float(last_price)

if price_diff < 0:
    print(Fore.GREEN + "Down $" + str(price_diff) + " since last check" + Style.RESET_ALL)
if price_diff > 0:
    print(Fore.RED + "Up $" + str(price_diff) + " since last check" + Style.RESET_ALL)
if price_diff == 0:
    print(Fore.BLUE + "No price change since last check" + Style.RESET_ALL)

print("Terminating webdriver")
driver.quit()

print("Saving price data")
if price_diff != 0:
    file1 = open("prices.txt", "a") 
    file1.write(str(elem) + "\n") 
    file1.close() 