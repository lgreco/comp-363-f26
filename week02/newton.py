
# initialize stuff

def f(x, a):
    return x*x - a

def f_prime(x):
    return 2*x

a = float(input("Number whose sqrt you want? a = "))
epsilon = 0.001
current_guess = 1
lifetime = 1_000
counter = 0

while (abs(current_guess*current_guess - a) > epsilon 
       and counter < lifetime):  # no convergence yet
    next_guess = current_guess - f(current_guess, a)/f_prime(current_guess)
    current_guess = next_guess
    print(current_guess)
    counter += 1

print(f"Success! sqrt({a}) = {current_guess}")

