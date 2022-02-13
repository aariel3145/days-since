from datetime import date

day0 = date(2022, 2, 3)
today = date.today()

print("Days since David has failed to watch In the Heights: ", end = "")
print(f"{(today - day0).days}")