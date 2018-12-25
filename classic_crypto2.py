from number_theory import alphabet , gcd , matrixInverse_modn #greatest common divisor and matrix inverse modulo n
from numpy import matmul,zeros,array #matrix multiplication
from numpy.linalg import det #determinant and inverse of a matrix
from classic_crypto1 import word_filter
from random import randint

def check(text,key,m):
    if(m > len(text)) or (len(text) == 0):
        print("Input parameters are wrong!")
        return False
    for x in key:
        if type(x) != list or (len(x) != m):
            print("Invalid key value!")
            return False
    return True

#Hill chiper , input: plaint text and key(1D vector)
def hill(plaintext,key):
    # m is the length od the key(1st dimension of matrix)
    #check if all inputs are OK (text on Croatian allowed)
    if type(key) != list:
        print("Invalid key value!")
        return
    m = len(key)
    plaintext = word_filter(plaintext)
    x = check(plaintext,key,m) #checking if paramteres are good
    if x == False:
        return
    #if lenght of plaintext is not divisible with m we need to add random letters
    if (len(plaintext) % m) != 0 :
        while((len(plaintext) % m) != 0):
            plaintext += alphabet[randint(0,25)] #adding random letter
    a = len(plaintext)
    num_vector = [alphabet.index(l) for l in plaintext] #numerical representation of plaintext
    chipertext = ""
    for i in range(0,a-m+1,m):
        x = num_vector[i:i+m]
        #now calculate x*key (matrix multiplication)
        y = list(matmul(x,key) % 26)
        for n in y:
            chipertext += alphabet[n]
    return chipertext.upper()

#Hill chiper decryption function
def hill_decrypt(chipertext,key):
    if type(chipertext) != str or type(key) != list:
        return
    chipertext = word_filter(chipertext)
    m = len(key)
    a = check(chipertext,key,m) #checking if paramteres are good
    if a == False:
        return
    #if lenght of chipertext is not divisible with m we need to add random letters
    if (len(chipertext) % m) != 0 :
        while((len(chipertext) % m) != 0):
            chipertext += alphabet[randint(0,25)] #adding random letter
    #calculate inverse of matrix key(if it exists)
    d = int(round(det(key)) % 26)
    if(gcd(d,26) != 1): #if determinant of matrix is not invertible in Z26
        print("Key is not invertible matrix!")
        return
    inverse = matrixInverse_modn(key,26) #inverse mod26 of key matrix
    num_vector = [alphabet.index(l) for l in chipertext] #numerical representation of chipertext
    plaintext = ""
    a = len(chipertext)
    for i in range(0,a-m+1,m):
        x = num_vector[i:i+m]
        #calculate x*key_inverse (matrix multiplication)
        y = list(matmul(x,inverse) % 26)
        for n in y:
            plaintext += alphabet[n]
    return plaintext
