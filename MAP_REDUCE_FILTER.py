


1. Temperature conversions

def fahrenheit(t):
    return ((float(9)/5)*t + 32)
def celsius(t):
    return (float(5)/9*(t - 32))
def to_fahrenheit(values):
	return map(fahrenheit, values)
def to_celsius(values):
	return map(celsius, values)
    

2. Return maximum value from list 
def max(values):
	return reduce(lambda a,b: a if (a>b) else b, values)

3. Return minimum value from list 
def min(values):
	return reduce(lambda a,b: a if (a<b) else b, values)

4. Return sum of values in list
def add(values):
	return reduce(lambda a,b: a+b, values)

5. Return value obtained by subtracting consecutive values in list from value of first item 
def sub(values):
	return reduce(lambda a,b: a-b, values)

6. Return product of values in a list
def mul(values):
	return reduce(lambda a,b: a*b, values)

7. Return average of values in a list
def ave(values):
	return reduce(lambda a,b: (a+b)/2, values)

8. Return value obtained by dividing consecutive values in list from value of first item - using reduce
def div(values):
	return reduce(lambda a,b: a/float(b) if (b != 0 and a != 'Nan') else 'Nan', values)

9. Return even values from list 
def is_even(values):
	return filter(lambda x: x % 2 == 0, values)

10. Return odd values from list 
def is_odd(values):
	return filter(lambda x: x % 2 , values)

11. Iterator
def get_triplets(n):
	for x in range(1, n):
		for y in range(x,n):
			for z in range(y,n):
				if x**2 + y**2 == z**2:
					yield (x,y,z)

12. Fibonacci iterator	
def fibonacci(n):
    """Fibonacci numbers generator, first n"""
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): return
        yield a
        a, b = b, a + b
        counter += 1

