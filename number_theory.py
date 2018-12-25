# we use this number_theory module for other cryptography modules
from math import sqrt
from random import randrange
from numpy import array,zeros
from numpy.linalg import det
#we use this algorithm only for odd numbers
def miller_rabin(number,k):
    r, s = 0, number - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = randrange(2, number) #some random number from [2,n-1]
        x = pow(a, s, number) # (a^s) mod number
        if x == 1 or x == number - 1:
            continue
        nextLoop = False #flag
        for _ in range(r - 1):
            x = pow(x, 2, number) #x = (x^2) mod number
            if x == 1 :
                return False # number is composite
            if x == number - 1: #if x==number - 1 do next loop for _ in range(k)
                nextLoop = True
                break
        if nextLoop :
            continue
        return False #number is composite
    return True #number is prime

def isPrime(number): #return True if prime,else return False
    if number <= 1 or type(number) != int : #if its not integer or <=1 return nothing(1 is not prime)
        return
    if number in [2,3,5,7]:
        return True
    if number in [4,6,8,9,10]:
        return False
    #simple cases
    if (number % 2 == 0) or (number % 3 == 0):
        return False
    #for the rest of algorithm we assume that number is odd and not divisible with 3
    #for small numbers ,if it is not divisible with 2 or 3
    if number <= 5000:
        for i in range(5,int(sqrt(number))+1,2):
            if number % i == 0:
                return False
        return True
    #for numbers >= 5000 we use Miller-Rabin test for prime numbers
    return miller_rabin(number,10)

def gcd(a,b): #Euclid algorithm,return greatest common divisor od 2 positive integers
    while b:
        a, b= b, a%b
    return a

def mod(number,n): # return x ,such as x is from {0,1,...,n-1} and n divide (number-x)
    if type(n) != int or n<=1 or type(number) != int:
        return
    return number % n

def relprime_list(number): #for SMALL positive integer number , returns list of relative primes from {1,2,...,n-1}
    if type(number) != int or number < 1:
        return
    l = []
    for i in range(1,number):
        if gcd(number,i) == 1:
            l.append(i)
    return l

#variable - list that contains all english letters
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#this function return inverse for multiplication mod n (if exists)
#brute force is good for our small mod n problem because those are small integers,otherwise we need to calculate inverse with algorithms from numbertheory
# modular inverse using extended Euclid algorithm :returns modulo inverse of a with respect to m using extended Euclid algorithm
# algorithm assumption: a and m are coprimes -> gcd(a, m) = 1
def modInverse(a, m) :
    if gcd(a,m) != 1 or (m == 1): #if inverse does not exist
        return
    m0 = m 
    y = 0
    x = 1
    while (a > 1) : 
        #q is quotient 
        q = a // m 
        t = m 
        #m is remainder now process the same as Euclid's algorithm
        m = a % m 
        a = t 
        t = y 
        #update x and y 
        y = x - q * y 
        x = t 
    #x positive 
    if (x < 0) : 
        x = x + m0 
    return x

# Euler's function 
def phi(n):
    result = n # initialize result as n 
    p = 2 #consider all prime factors of n and subtract their multiples from result 
    while(p * p <= n):  
        if (n % p == 0):# check if p is a prime factor.
            #if yes then update n and result 
            while (n % p == 0): 
                n = int(n / p)
            result -= int(result / p)
        p += 1
    #if n has a prime factor greater than sqrt(n) there can be at-most  one such prime factor
    if (n > 1): 
        result -= int(result / n)
    return result

#matrix A with the i-th row and j-th column deleted , i and j in {0,...,n-1}
def minor(A,i,j):
  A = array(A)
  n = len(A)
  minor = zeros((n-1,n-1),dtype = int) #for problems in cryptography integers are used
  p = 0
  for s in range(0,n-1):
      if p == i:
          p = p+1
      q = 0
      for t in range(0,n-1):
          if q == j:
              q = q+1
          minor[s][t] = A[p][q]
          q = q+1
      p = p+1
  return minor

#function for computing matrix inverse modulo n , input: matrix A and modulo m
def matrixInverse_modn(A,m):
    if m <= 1:
        print("Modulo n must be greater or equal 2 !")
    n = len(A)
    for i in range(0,n):
        for j in range(0,n):
            A[i][j] = (A[i][j] % m)
    # we calculate matrix inverse (if it exists) with equation A_inverse = (1/detA) * adj(A) ,where adj(A) is adjugate of matrix A
    #adjugate of A is transpose matrix of cofactors of A. Cofactor of element A(i,j) is determinant of matrix A where i-th row and j-th column
    #are deleted
    d = int(round(det(A)) % m) #we need to know if our matrix is regular(gcd(d,m) = 1). int because of floating point arithmetic
    if gcd(d,m) != 1:
        print("Inverse modulo "+str(m)+" does not exist because matrix A is singular!")
        return None
    #calculate adjugate of A
    adj = zeros((n,n),dtype = int)
    for i in range(n):#rows
        for j in range(n):#columns
            #calculate cofactor of A(i,j)
            M = minor(A,i,j)
            #we use A[j][i] so we don't need to use transpose function
            adj[j][i] = int((round(det(M)) % m)) #int , because function det returns floating point value(for example 4.0 instead of 4)
            if (i+1+j+1)%2 == 1:
                adj[j][i] = (-1*adj[j][i]) % 26
    return ((modInverse(d,m)*adj) % m)
