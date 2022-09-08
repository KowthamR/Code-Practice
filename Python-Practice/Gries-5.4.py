# Gries Chapter 5
# 5.4 Wildlife camera
# camera turns on if light lux is less than 0.01 or if temp is greater than 0 
# if both conditions true turn off

def turn_camera_on(light,temperture):
    if light<0.01 and temperture>0:
        return('OFF')
    elif light<0.01 or temperture>0:
        return('ON')
    else:
        return('OFF')

turn_camera_on(0,-5)