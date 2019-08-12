sh = input ("Enter hours")
sr = input ("Enter rate")

try:
    fh=float(sh)
    fr=float(sr)
except:
    print("Error, please enter numeric input")
    quit()

#PRINT (fh, fr)
if fh > 40 :
    #PRINT ("OVERTIME")
    reg = fr * fh
    otp = ( fh - 40 ) * ( fr * 0.5 )
    #PRINT (REG,OTP)
    xp = reg + otp
else:
    #PRINT("REGULAR")
    xp = float(xh) * float(xr)

print("Pay:", xp)
