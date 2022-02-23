from datetime import date

day0 = date(2021, 6, 11)
end = date(2022, 2, 16)
today = date.today()

print("Days since David has failed to watch In the Heights: ", end = "")
print(f"{(end - day0).days}")