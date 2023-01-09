import requests

APP_ID = "cd3c41798514464bbc47d2e027806e25"
ENDPOINT = "https://openexchangerates.org/api/latest.json"

response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
exchange_rates = response.json()

usd_amount = 1000
gbp_amount = usd_amount * exchange_rates['rates']['GBP']
inr_amount = usd_amount * exchange_rates['rates']['INR']
print(f"USD{usd_amount} is GBP{gbp_amount}")
print(f"USD{usd_amount} is INR{inr_amount}")