# Chapter 9 Excercises
# 9.2 Add Depth Parameter

def fibo( n, depth ):
    indent = 6 * depth * " "
    print( "{}fibo({})".format( indent , n ) )
    if n <= 2:
        print( "{}return {}".format( indent , 1 ) )
        return 1
    value = fibo( n-1, depth+1 ) + fibo( n-2, depth+1 )
    print( "{}return {}".format( indent , value ) )
    return value
print( fibo( 4, 0 ) )