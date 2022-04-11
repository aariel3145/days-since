from datetime import date

day0 = date(2022, 2, 16)
today = date.today()

print("Days since Kody said he should invite us over to bask in his expensive TV: ", end = "")
print(f"{(today - day0).days}")