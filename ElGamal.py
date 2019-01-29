from number_theory import primitiveRoot,modInverse
#ElGamal enctyption
#p is a prime number,a is a secret value , x is a message and k is secret key
def elgamal_encrypt(p,a,x,k):
    if type(k) != int or type(p) != int:
        return
    if k < 0 or k > (p-2):
        print("Secret key k must be from {0,1,...,p-2}")
        return
    pRoot = primitiveRoot(p) #primitive root of p(the smallest)
    print("Public key ",pRoot)
    b = pow(pRoot,a,p) #beta value
    y1 = pow(pRoot,k,p)
    y2 = (x*pow(b,k)) % p
    return y1,y2

def elgamal_decrypt(p,a,y1,y2):
    return (y2 * modInverse(pow(y1,a,p),p)) % p
