# Holden Higgins
# 8-29-2022
# code based off of https://www.wired.com/story/how-many-times-do-you-have-to-slap-a-chicken-to-cook-it/ (homework assignments)

import time

#specific heat capacity of chicken
C=6.018 #J/(g*C)
#room temp
T1=23 + 273.15#K
#cooked temp
T2=74 + 273.15
#energy factor 
f=.5
# constant of proportionality, see https://en.wikipedia.org/wiki/Stefan%E2%80%93Boltzmann_law
sigma = 5.67*10**-8 #W(m^-2)(K^-4)
# surface area of a chicken, assuming 25cm spherical chicken: (4×π×(.25^2))
a = .785 # m^2

print("enter mass of chicken, in kg")
mc=float(input())*1000 #g

print("Enter mass of hand, in kg:")
mh=float(input()) #kg

print("Enter velocity of hand, in m/s:")
vh=float(input()) #m/s

print("Enter slap frequency, in slaps/second")
sf = float(input()) #Hz


#calculate change in T for one slap  
dT=f*mh*vh**2/(2*mc*C) # J/(J/C) = C
print("Change in T for 1 slap = ",dT," C")

N=(T2-T1)/dT
print("Number of slaps to cook = ",N)

cooktime = N/sf # s
h = int(cooktime/3600)
m = int(cooktime%3600/60)
s = int(cooktime%60)
print(f"Time to cook = {h}h, {m}m, {s}s")

time.sleep(2)

print("\nNow we let the chicken cool (calculations done using blackbody "
    "radiation each second)\n")

Tcur = T1
print(f"initial chicken temperature: {Tcur}K")

# calculate heat loss per second due to blackbody radiation
minute = 0
while Tcur < T2:
    minute +=1
    if minute >= 1200:
        
        break
    print(f"Chicken temp at minute {minute} = {Tcur:.3f}K")

    for _s in range(60):
        # heat flow in/out for 1s
        Tcur += dT * sf
        # flux power
        Wout = sigma*(Tcur**4)/a # W
        Jout = Wout # J
        Tcur -= Jout / (2*mc*C) # J/(J/C)



