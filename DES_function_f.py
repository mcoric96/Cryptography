from DES_matrices import *
Sboxes = [s1,s2,s3,s4,s5,s6,s7,s8]
#DES function f(A,J)
#A is array of bits, 32 bits long(here represented as hex value) , J is array of bits, 48 bits long(represented as hex value)
def f(A,J):
    if type(A) != str or type(J) != str:
        return
    if len(A) > 8 or len(J) > 12:#if represented as hex values,must be at most 8 and 12 long
        return
    #turning A and J in binary
    A = bin(int(A,16))[2:]
    J = bin(int(J,16))[2:]
    a = len(A)
    j = len(J)
    #algorithm works for 32-bit A and 48-bit J ,if their lenghts are not 32 and 48 we must add zeros
    if a < 32:
        A = "0"*(32-a) + A
    if j < 48:
        J = "0"*(48-j) + J
    #first step
    #exted A to the size of 48 bits with function E
    B = ""
    for i in E:
        B += A[i]
    A = B # A = E(A) , A is now 48 bits long
    #2nd step , calculate E(A)xorJ
    B = "" #B = E(A)xorJ
    for i in range(0,48):
        if(A[i] == J[i]): #computationaly better that convert string into integer and do xor
            B += "0"
        else:
            B += "1"
    #3rd step => using S-boxes , 48 bit long B = B1B2...B8 (each Bi is 6 bit long)
    #for each Bj = b1b2b3b4b5b6 6-bit long,compute Sj(Bj) = Cj
    C = ""  # C = C1C2...C8
    j = 0 #for each S box
    for i in [0,6,12,18,24,30,36,42]:
        Bi = B[i:i+6]
        r = int(Bi[0]+Bi[5],2) #first and last bit r=b1b6 for row number
        c = int(Bi[1:5],2) #c=b2b3b4b5 for column number
        x = bin(Sboxes[j][r][c])[2:]
        n = len(x)
        if n < 4:
            x = '0'*(4-n) + x
        C += x
        j += 1
    #4th step = > permuting C with final permutation P ,that is f(A,J)
    F = ""
    for i in p:
        F += C[i]
    return hex(int(F,2))[2:] # F = f(A,J) return hex value
