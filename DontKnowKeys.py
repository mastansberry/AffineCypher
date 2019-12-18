alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# how to get index number               alph.index('m')
#how to get letter from index number    alph[12]
#updatedA=3
#encmath=((a*c)+b)%26

#NewString=''
def AffineEncryption(a,b,c):
    c=alph.index(c)
    encmath=((a*c)+b)%26
    #print encmath
    encletter=alph[encmath]
    print encletter


        
def AffineDecryption(a,b,c):
    c=alph.index(c)
    foundinv=0
    for i in alph:
        decrypmath=(alph.index(i)*a)%26
        if decrypmath == 1:
            foundinv= alph.index(i)
    decry=foundinv*(c-b)%26
    decryLetter=alph[decry]
    print decryLetter


    
def AffineEncryptionString(a,b,c):
    NewString=''
    for letter in c:
        c=alph.index(letter)
        encmath=((a*c)+b)%26
        encletter=alph[encmath]
        NewString += encletter
    print NewString

DecodeString= ''      
def AffineDecryptionString(a,b,c):
    NewString=''
    foundinv=0
    global DecodeString
    for i in alph:
        decrypmath=(alph.index(i)*a)%26
        if decrypmath == 1:
            foundinv= alph.index(i)
    for letter in c:
        c=alph.index(letter)
        decry=foundinv*(c-b)%26
        decryLetter=alph[decry]
        NewString += decryLetter
    print NewString
    #enter KeyWord To help Code
    Keyword='boat'
    if Keyword in NewString:
        DecodeString += NewString

    
    

        
        
    
        