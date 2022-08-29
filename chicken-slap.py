# Holden Higgins
# 8-29-2022
# code based off of https://www.wired.com/story/how-many-times-do-you-have-to-slap-a-chicken-to-cook-it/ (homework assignments)

#specific heat capacity of chicken
C=6.018 #J/(g*C)
#room temp
T1=23 + 273.15#K
#cooked temp
T2=74 + 273.15

#mass of chicken
mc=2000 #g

#mass of hand
mh=.8 #kg

#hand velocity
vh=35 #m/s

#energy factor 
f=.5

# slap frequency
sf = 3 #Hz

# constant of proportionality
sigma = 5.67*10**-8 #W(m^-2)(K^-4)

# surface area of a chicken (4×π×(.25^2))
a = .785 # m^2

#calculate change in T for one slap  
dT=f*mh*vh**2/(2*mc*C) # J/(J/C) = C
print("Change in T for 1 slap = ",dT," C")

N=(T2-T1)/dT
print("Number of slaps to cook = ",N)

cooktime = N*sf # s
h = int(cooktime/3600)
m = int(cooktime%3600/60)
s = int(cooktime%60)
print(f"Time to cook = {h}h, {m}m, {s}s")

print("\nNow we let the chicken cool (calculations done using blackbody "
    "radiation each second)\n")

Tcur = T1
print(f"temp initial = {Tcur}K")

step = 1 #s

import time
# calculate heat loss per second due to blackbody radiation
minute = 0
while Tcur < T2:
    minute +=1
    if minute >= 1200:
        break
    print(f"temp at minute {minute} = {Tcur:.3f}K")
    for _s in range(60):
        Tcur += dT * sf * step
        # print(f"temp after slap    = {Tcur}K")
        # flux
        Wout = sigma*(Tcur**4)/a # W
        Jout = Wout*step # J
        Tcur -= Jout / (2*mc*C) # J/(J/C)
        # print(f"temp after cooling = {Tcur}K")



