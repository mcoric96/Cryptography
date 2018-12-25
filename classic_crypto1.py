import number_theory  #module for functions with numbers
from number_theory import alphabet       

def word_filter(text):#function for filtering text,we drop all nonletters
    a=""
    text = text.lower()
    for s in text:
        #for each sign in text we want to know is it a letter or something else(space,tab,.:;[]{}'"| ...)
        if s.isalpha(): #if it is letter
            if s in ['č','ć','ž','š','đ','dž']: #if its one of special croatian letters
                if s=='č' or s=='ć':
                    a+='c'
                elif s=='ž':
                    a+='z'
                elif s=='š':
                    a+='s'
                elif s=='đ':
                    a+='d' #we have to substitute 1 sign for 1 sign
                else:
                    a+='dz'
            else:
                a+=s
    return a

#numerical values of each letter in the word
def num_values(word):
    if type(word) != str:
        return
    word = word_filter(word)
    if word == "":
        return
    l = [alphabet.index(letter) for letter in word]
    return l

#this function returns a list of substituted words for cezar crypto algorithm
def substitute_letters(keyword,sub_position):
    sub_letters = ['' for i in range(0,26)]
    index = sub_position #we start substitution from this index
    for letter in keyword: #first part of substituting
        if letter not in sub_letters:
            sub_letters[index] = letter
            index+=1
            if index == 26:
                index = 0
    alphabet=number_theory.alphabet
    for letter in alphabet: #second part of substituting
        if letter not in sub_letters: #if current letter in alphabet doesnt have its substitution
            while sub_letters[index] != '': #we search for the next free place in alphabet
                index+=1
                if index == 26:
                    index=0
            sub_letters[index] = letter

    return sub_letters

#first task,cezars chiper with parameters plaintext, keyword and position for it,returns a chipertext
#program can take all croatian letters(č,ć,ž,š,đ) and turns it into c,z,s,dj. programs drops all nonletters like space,tab,and :;'"<>,._-+=\#
#key is a pair of english/croatian keyword and position in alphabet where it starts
def cezar(plaintext,keyword,key_position):
    if type(plaintext) != str or type(keyword) != str or type(key_position) != int:
        print("Wrong input!")
        return
    plaintext = plaintext.lower() #we want text with all small letters for easier operations
    plaintext = word_filter(plaintext) #we need to drop all nonletters
    keyword = keyword.lower()
    keyword = word_filter(keyword)
    #we need to check if we can do cezar crypto algorithm
    if len(plaintext) == 0 or len(keyword) == 0 or key_position > 25 or key_position < 0:
        print("Wrong input!")
        return
    #if everything was OK we can start algorithm
    alphabet = number_theory.alphabet #all letters in alphabet
    sub_letters = substitute_letters(keyword,key_position) #firt we substitute letters with keywords starting from index=key_position in alphabet
    chipertext = ''
    for letter in plaintext: # we take the letter and substitute it with its sub letter
        chipertext += sub_letters[alphabet.index(letter)]
    print(plaintext)
    print('-----------------------------------')
    print(chipertext)

#the second task is to return plaintext from chipertext using known keyword and its position
def cezar_decrypt(chipertext,keyword,key_position):
    if type(chipertext) != str or type(keyword) != str or type(key_position) != int:
        print("Wrong input!")
        return
    chipertext = chipertext.lower() #we want text with all small letters for easier operations
    chipertext = word_filter(chipertext) #we need to drop all nonletters
    keyword = word_filter(keyword)
    #we need to check if we can do cezar crypto algorithm
    if len(chipertext) < len(keyword) or len(chipertext) == 0 or len(keyword) == 0 or len(keyword) > 26 or key_position > 25 or key_position < 0:
        print("Wrong input!")
        return
    #if everything is OK we can start algorithm
    alphabet = number_theory.alphabet #all letters in alphabet
    sub_letters = substitute_letters(keyword,key_position) #firt we substitute letters with keywords starting from index=key_position in alphabet
    plaintext=''
    for letter in chipertext:
        plaintext+=alphabet[sub_letters.index(letter)]
    print(chipertext)
    print('-----------------------------------')
    print(plaintext)

#standard cezar chiper,with one key,number from {0,1,...,25}
def cezar_key(chipertext,key):
    if type(chipertext) != str or type(key) != int :
        print('Wrong input!')
        return
    chipertext = chipertext.lower()
    chipertext = word_filter(chipertext)
    if len(chipertext) == 0 or key < 0 or key >= 26 :
        print('Wrong input!')
        return
    alphabet = number_theory.alphabet
    plaintext=''
    for letter in chipertext:
        y=alphabet.index(letter) #for each letter in chipertext,we get its index in alphabet,number from {0,1,...,25}
        plaintext+=alphabet[number_theory.mod(y-key,26)] #standard decoding function for Cezars chiper with one key
    print(chipertext)
    print('-----------------------------------')
    print(plaintext)

#this function is algorithm for decryption of affine chyper,when key K=(a,b) is known
def affine_decrypt(a,b,chipertext):
    chipertext = chipertext.lower()
    chipertext = word_filter(chipertext)
    if len(chipertext) == 0 or type(chipertext) != str or type(a) != int or type(b) != int or a<0 or a>25 or b<0 or b>25:
        print('Wrong input!')
        return
    #we need to check first if a has inverse
    x = number_theory.mod_inverse(a,26)
    if x == -1:
        print('a must have inverse for multiplication mod 26 !')
        return
    #if a has inverse,we decrypt using known function for decryption d(y) = x*(y-b) mod 26
    alphabet = number_theory.alphabet
    plaintext = ''
    for letter in chipertext:
        y = alphabet.index(letter)
        index = x*(y-b) % 26
        plaintext += alphabet[index]
    print(chipertext)
    print('-----------------------------------')
    print(plaintext)
