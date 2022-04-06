from datetime import date

day0 = date(2022, 4, 5)
# end = date()
today = date.today()

print("Days David's phone screen has lasted: ", end = "")
print(f"{(today - day0).days}")