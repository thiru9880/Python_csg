principle = int(input("enter the principle amount: "))
years = int(input("enter the time in years: "))
rate = int(input("enter the rate of intrest: "))


# intrest = principle * years * rate  /100
month =  principle * rate /100


# print("intrest:",intrest)

print(f"the intrest for one monthe for the principle amount $ {principle + 2} for the time {years} years with rate of intrest {rate} is ${month}")