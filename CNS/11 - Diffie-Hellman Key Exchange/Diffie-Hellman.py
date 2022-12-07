from random import randint

# P = 941
# G = 627
P = int(input("Enter a prime number P: "))
G = int(input("Enter a primitive root for P: "))

# a = 347
a = int(input("Enter a private key for A: "))
x = int(pow(G, a, P))

# b = 781
b = int(input("Enter a private key for B: "))
y = int(pow(G, b, P))

ka = int(pow(y, a, P))
kb = int(pow(x, b, P))

print('Secret key for A is : %d' % (ka))
print('Secret Key for B is : %d' % (kb))
