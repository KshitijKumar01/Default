# # Simpson's 1/3 Rule

# # Define function to integrate
# def f(x):
#     return 5 + 0.25*(x**2)

# # Implementing Simpson's 1/3 
# def simpson13(x0,xn,n):
#     # calculating step size
#     h = (xn - x0) / n
    
#     # Finding sum 
#     integration = f(x0) + f(xn)
    
#     for i in range(1,n):
#         k = x0 + i*h
        
#         if i%2 == 0:
#             integration = integration + 2 * f(k)
#         else:
#             integration = integration + 4 * f(k)
    
#     # Finding final integration value
#     integration = integration * h/3
    
#     return integration
    
# # Input section
# lower_limit = float(input("Enter lower limit of integration: "))
# upper_limit = float(input("Enter upper limit of integration: "))
# sub_interval = int(input("Enter number of sub intervals: "))

# # Call trapezoidal() method and get result
# result = simpson13(lower_limit, upper_limit, sub_interval)
# print("Integration result by Simpson's 1/3 method is: %0.6f" % (result) )


# Trapezoidal Method

# Define function to integrate
def f(x):
    return 5 + 0.25*(x**2)

def trapezoid_rule(f, a, b, n):
    h = (b - a) / n  # step size
    x = [a + i*h for i in range(n+1)]  # n+1 equally spaced points between a and b
    y = [f(xi) for xi in x]  # function values at the n+1 points
    T = h * (sum(y) - (y[0] + y[n])/2)  # Trapezoid rule formula
    return T

# Implementing trapezoidal method
def trapezoidal(x0,xn,n):
    # calculating step size
    h = (xn - x0) / n
    
    # Finding sum 
    integration = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        integration = integration + 2 * f(k)
    
    # Finding final integration value
    integration = integration * h/2
    
    return integration
    
# Input section
lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))
sub_interval = int(input("Enter number of sub intervals: "))

# Call trapezoidal() method and get result
# result = trapezoidal(lower_limit, upper_limit, sub_interval)
result = trapezoid_rule(f, lower_limit, upper_limit, sub_interval)
print("Integration result by Trapezoidal method is: %0.6f" % (result) )