# Cryptography
## Number theory module
Module contains functions used for number theory problems in cryprography. <br>
**Algorithms:**
1. Prime numbers test (Miller-Rabin)
2. greatest common divisor - gcd
3. multiplicative inverse mod n
4. Euler's function
5. matrix inverse mod n
6. primitive root mod n

## Classic chipers
1. Cesar chiper
2. Hill chiper
3. Affine chiper

## DES function f
Implementation of f function from DES using S-boxes. This function is used for 16 iterations in DES algorithm. Function f takes 2 array arguments A and J , the first one is 32 bits and the second is 48 bits long.<br>
There are 4 stages of calculating this function output.<br>
1.The first argument A is expanded with expand function E , such that it becomes array E(A) of the 48 bits. <br>
2.B = E(A) XOR J = B1B2...B8 <br>
3.For each Bj using S-box Sj  , Cj = Sj(Bj) is computed. <br>
4.f(A,J) = P(C1...C8) where P is final permutation.

## El Gamal chiper
Example of asymetric cryptosystem based on public-key cryptography. It is based on difficulty to solve **discrete-logarithm problem** in multiplicaition group of remainders mod p (p is prime number).This cryptosystem can be defined over any cyclic group G. The security depends on properties of chosen group G.
