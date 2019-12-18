from DontKnowKeys import AffineEncryptionString
from DontKnowKeys import AffineDecryptionString
import DontKnowKeys
global DecodeString
DontKnowKeys.DecodeString = ''
AKeys=[1,3,5,7,9,11,13,15,17,19,21,23,25]
BKeys=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
#AKeys=[1,3,5]
#BKeys=[3,4,5]
for i in AKeys:
    for r in BKeys:
        #Enther the coded message in CodedMessage
        CodedMessage='rywarfvpoqkrwfzrqqpocbzrqqbk'
        AffineDecryptionString(i,r,CodedMessage)
        print i,r
print DontKnowKeys.DecodeString
