# Chapter 4 Exercises
# 4.2 Surface Area of a Circle
radius=int(input('What is the radius of the circle:?'))
pi=3.14159

def surface_area_circle():
    sa=(pi*radius**2)
    print('The surface area of a circle is: '+str(sa))
surface_area_circle()