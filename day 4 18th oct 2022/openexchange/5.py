usd_amount = 100
gbp_amount = usd_amount * exchange_rates['rates']['GBP']
#small_gbp='gbp_amount = %.2f pounds' % gbp_amount
inr_amount = usd_amount * exchange_rates['rates']['INR']
hkd_amount = usd_amount * exchange_rates['rates']['HKD']
print(f"USD{usd_amount} is GBP{gbp_amount}",":""gbp_amount = %.2f pounds" % gbp_amount)
#print(f"USD{usd_amount} is GBP{small_gbp}")
print(f"USD{usd_amount} is INR{inr_amount}")
print(f"USD{usd_amount} is HKD{hkd_amount}")