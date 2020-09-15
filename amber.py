#!/opt/local/bin/python

import requests
import json

url = "https://api.amberelectric.com.au/prices/listprices"

# Replace with your postcode or network name.  Network Name is useful if there are multiple distributors in your postcode.
#d = { 'postcode': '3078' }
d = '{ "networkName": "Jemena" }'

r = requests.post(url, data = d, headers = { 'Content-Type': 'application/json' })

data = json.loads(r.text)

periodid = 47

period =  data["data"]["variablePricesAndRenewables"][periodid]["period"]
totalfixedKWHPriceE1 = float(data["data"]["staticPrices"]["E1"]["totalfixedKWHPrice"])
lossFactorE1 = float(data["data"]["staticPrices"]["E1"]["lossFactor"])
totalfixedKWHPriceB1 = float(data["data"]["staticPrices"]["B1"]["totalfixedKWHPrice"])
lossFactorB1 = float(data["data"]["staticPrices"]["B1"]["lossFactor"])
wholesaleKWHPrice = float(data["data"]["variablePricesAndRenewables"][periodid]["wholesaleKWHPrice"])

usage = totalfixedKWHPriceE1 + lossFactorE1 * wholesaleKWHPrice
feedin = totalfixedKWHPriceB1 - lossFactorB1 * wholesaleKWHPrice

print("Network:         ", data["data"]["networkProvider"])
print("Period:          ", period)
#print("Fixed Price:     ", round(totalfixedKWHPrice,1), "c/kWh")
#print("Loss Factor:     ", lossFactor)
#print("Wholesale Price: ", round(wholesaleKWHPrice,1), "c/kWh")
print("Usage Tariff:    ", round(usage,1), "c/kWh")
print("Feedin Tariff:   ", round(feedin,1), "c/kWh")
