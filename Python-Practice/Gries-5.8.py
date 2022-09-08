# Gries Chapter 5
# 5.8 Convert Temperture Function
# units=[celsius ,kelvin, farheinet, rankine, delisle, newton, reaumu, romer]
#         C         K      F          RA        D        N       RE      RO

def convert_temp(t,source,target):
    # Convert to C no matter the source
    if source=='C':
        C=t
    elif source=='K':
        C=t-273
    elif source=='F':
        C=(t-32)*5/9
    elif source=='RA':
        C=(t-491)*5/9
    elif source=='D':
        C=(100-t)*2/3
    elif source=='N':
        C=t*100/33
    elif source=='RE':
        C=t*5/4
    elif source=='RO':
        C=(t-7.5)*40/21
    # Translate C vaule to Target unit
    if target=='C':
        return C
    elif target=='K':
        return C+273
    elif target=='F':
        return C*9/5+32
    elif target=='RA':
        return (C+273)*9/5
    elif target=='D':
        return (100-C)*3/2
    elif target=='N':
        return C*33/100
    elif target=='RE':
        return C*4/5
    elif target=='RO':
        return C*21/40 +7.5

convert_temp(100,'C','K')
