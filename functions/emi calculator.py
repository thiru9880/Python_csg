def emi_calculator(principle,rate,time):
    r = rate/12/100
    emi = principle * r * ((1+r)**time)/((1+r)**time -1)
    return emi

print(emi_calculator(200000,8.12,60))