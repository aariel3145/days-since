from datetime import date

day0 = date(2022, 2, 11)
today = date.today()

print("Days since the last VCU Wi-Fi incident: ", end = "")
print(f"{(today - day0).days}")