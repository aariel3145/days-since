from datetime import date

# 12/7/2021- cut line
# 2/11/2022 - failed edge router
# 3/31/2022 - tornado
# 4/14/2022 - AP authentication issue

day0 = date(2022, 4, 14)
today = date.today()

print("Days since the last VCU Wi-Fi incident: ", end = "")
print(f"{(today - day0).days}")