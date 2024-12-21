# 1.calculation of GCD
def z(a,b,c):
    if b==0 or c==0:
        return'infinity'
    y=b*c
    return a//y
print(z(18,6,3))
print(z(30,5,2))
print(z(48,8,2))
print(z(12,4,3))
print(z(24,6,4))
print(z(1,1,0))
# 2.calcution of compound interest
import math
def i(p,r,t):
    b=p*(1+r/100)**t
    return round(b,2)
print(i(1000,5,2))
print(i(2000,3,5))
print(i(1500,4,3))
print(i(5000,6,1))
print(i(10000,7,4))
print(i(0,5,10))
# 3.calculation of fibionacci series
def generate_fibonacci_sequence(n):
    """
    Generate the Fibonacci sequence up to the nth term.

    Parameters:
        n (int): The number of terms in the Fibonacci sequence.

    Returns:
        list: A list containing the Fibonacci sequence up to the nth term.
    """
    if n <= 0:
        # Return an empty list for non-positive values of n
        return []
    
    # Initialize the sequence with the first two Fibonacci numbers
    fibonacci_sequence = [0, 1]
    
    # Generate the sequence up to n terms
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    
    # Return the first n terms
    return fibonacci_sequence[:n]

# Example usage
print("Input 1:", generate_fibonacci_sequence(5))   # Output: [0, 1, 1, 2, 3]
print("Input 2:", generate_fibonacci_sequence(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print("Input 3:", generate_fibonacci_sequence(1))   # Output: [0]
print("Input 4:", generate_fibonacci_sequence(0))   # Output: []
print("Input 5:", generate_fibonacci_sequence(15))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

# Edge Case
print("Edge Case:", generate_fibonacci_sequence(-5)) # Output: []

# 4.calculation of factriol
def f (a):
    c=1
    for y in range (1,a+1):
        c=c*y
    return c
print(f(5))
print(f(7))
print(f(3))
print(f(1))
print(f(0))
print(f(20))
# 5.gcd calculation
def g(y,z):
    while z!=0:
        c=y%z
        y=z
        z=c
    return y
print(g(12,8))
print(g(36,60))
print(g(7,5))
print(g(100,25))
print(g(54,24))
print(g(0,15))
