from BitVector import *
import binascii
from copy import copy, deepcopy
from datetime import datetime
import time
def CreateSbox():
    mySbox = [0x63]
    for i in range(1,256):
        multiplicativeInv = BitVector(intVal=i,size=8).gf_MI(AES_modulus,8)
        sboxElement = BitVector(intVal=0x63,size=8) ^ multiplicativeInv ^ (multiplicativeInv << 1) ^ (multiplicativeInv << 1) ^ (multiplicativeInv << 1) ^ (multiplicativeInv << 1)
        mySbox.append(sboxElement.int_val())
    return mySbox

def Create_InvSbox():
    myInvSbox = [0x52]
    for c in range(1,256):
        s = BitVector(intVal=c,size=8)
        b = (s<<1) ^ (s<<3) ^ (s<<6) ^ BitVector(intVal=0x05,size=8)
        #print(type(b))
        invSboxElement = b.gf_MI(AES_modulus,8)
        print(invSboxElement.int_val())
        print(type(invSboxElement))
        myInvSbox.append(invSboxElement.int_val())
    return myInvSbox

'''Sbox = [
       [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
       [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
       [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
       [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
       [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
       [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
       [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
       [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
       [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
       [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
       [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
       [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
       [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
       [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
       [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
       [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]
       ]'''

InvSbox = [
    [0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB],
    [0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB],
    [0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E],
    [0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25],
    [0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92],
    [0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84],
    [0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06],
    [0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B],
    [0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73],
    [0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E],
    [0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B],
    [0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4],
    [0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F],
    [0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF],
    [0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61],
    [0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D]
]


Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]
AES_modulus = BitVector(bitstring='100011011')



def circByteLeftShift( root_word ):
    t = []
    for i in range(3):
        t.append(root_word[i+1])
    t.append(root_word[0])
    return t

def substituteBytes( root_word ):
    r_w = []
    for i in range(4):
        #t = list(root_word[i])
        #a = int(t[0],16)
        #b = int(t[1], 16)
        #r_w.append(format(Sbox[a][b],"02x"))
        num = int(root_word[i], 16)
        r_w.append(format(Sbox[num],"02x"))
    return r_w

def addRoundConstant( root_word, rndConst):
    #roundConstant = 2**(rnd-1)
    roundConstant = int(rndConst, 16)
    root_word_msbyte = int(root_word[0], 16)
    root_word_msbyte = root_word_msbyte ^ roundConstant
    root_word[0] = format(root_word_msbyte,"02x")
    return root_word
    #print(root_word)
    #print(roundConstant)
def g_func(root_word, round):
    #print("at g function")
    rt_word = circByteLeftShift(root_word)
    #print('after circByteLeftShift : '+ str(rt_word))
    rt_word = substituteBytes(rt_word)
    #print('after substituteBytes : '+ str(rt_word))
    rt_word = addRoundConstant(rt_word, round)
    #print('after addRoundConstant : '+ str(rt_word))
    return rt_word

def bitwiseXor(word1, word2):
    #print(word1)
    #print(word2)
    for i in range(4):
        num = int(word1[i], 16) ^ (int(word2[i], 16))
        word1[i] = format(num,"02x")
    #print("result to return\n")
    #print(word1)
    return word1

wordList = []
rcList = []
def rc_init():
    rc = "01"
    rc_list = []
    rc_list.append("01")
    for i in range(9):
        bv1 = BitVector(hexstring="02")
        bv2 = BitVector(hexstring=rc_list[i])
        bv3 = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
        rc_list.append(bv3.get_bitvector_in_hex())
    return rc_list

def keyScheduling(word):
    rcList = rc_init()
    print(len(rcList))
    wordList.append(deepcopy(word))
    temp = word
    #print("\n")
    for i in range(10):
        #print("round no. "+ str(i+1))
        g = g_func(temp[3], rcList[i])
        #print('g : ' + str(g))
        temp_temp = []
        temp_temp.append(bitwiseXor(temp[0], g))
        for j in range(3):
            temp_temp.append(bitwiseXor(temp[j+1], temp_temp[j]))
        #print(temp_temp)
        #print()

        wordList.append(deepcopy(temp_temp))
        temp = temp_temp

    #print(wordList)
    '''for i in range(11):
        print("Round no : "+ str(i))
        print(wordList[i])
        print("")'''


'''st = "Thats my Kung Fu"
st_charArr = list(st)

iter = 0
w = []
for i in range(4):
    w.append([])
    for j in range(4):
        print(hex(ord(st_charArr[iter])))
        w[i].append(format(ord(st_charArr[iter]),"02x"))
        #w[i].append(hex(ord(st_charArr[iter])))
        #w[i].append(ord(st_charArr[iter]))
        iter= iter + 1
#print(w)
'''

def addRoundKey(text, roundKey):
    var = []
    for i in range(4):
        var.append(bitwiseXor(deepcopy(text[i]), deepcopy(roundKey[i])))
    return var

def substituteBytes128(text):
    var = []
    for i in range(4):
        var.append(substituteBytes(text[i]))
    return var

def shiftRow(text):
    var = deepcopy(text)
    for i in range(4):
        for j in range(4):
            num = (j+i)%4
            var[j][i] = deepcopy(text[num][i])
    return var

def bitwiseXor8(word1, word2):
    num = int(word1, 16) ^ (int(word2, 16))
    word1 = format(num,"02x")
    return word1


def mixColumn(text):
    temp = []
    for i in range(4):
        temp.append([])
        for j in range(4):
            temp[i].append(BitVector(hexstring=text[i][j]))
    var = []
    for i in range(4):
        var.append([])
        for j in range(4):
            a = temp[i][0].gf_multiply_modular( Mixer[j][0]  ,AES_modulus,8)
            b = temp[i][1].gf_multiply_modular( Mixer[j][1]  ,AES_modulus,8)
            c = temp[i][2].gf_multiply_modular( Mixer[j][2]  ,AES_modulus,8)
            d = temp[i][3].gf_multiply_modular( Mixer[j][3]  ,AES_modulus,8)

            #print(type(format(a.intValue(), "02x")))
            var[i].append(bitwiseXor8(bitwiseXor8(format(a.intValue(), "02x"), format(b.intValue(), "02x")),bitwiseXor8(format(c.intValue(), "02x"),format(d.intValue(), "02x"))))
            #print(var[i][j])
    #print(var)
    return var

def encrypt(plainText):
    #print("size of plainText" + str(len(plainText)))
    plainTextcharArr = list(plainText)
    plainTextHexByte = []
    iter = 0
    for i in range(4):
        plainTextHexByte.append([])
        for j in range(4):
            plainTextHexByte[i].append(format(ord(plainTextcharArr[iter]),"02x"))
            iter = iter + 1
    #plainText converted to hex array as required in plainTextByte
    print(plainTextHexByte)

    '''print("round keys")
    for i in range(11):
        print("roundKey "+str(i)+" : ")
        print(wordList[i])
        print()'''
    #extra addRoundKey before starting rounds
    plainTextHexByte = addRoundKey(plainTextHexByte, deepcopy(wordList[0]))
    #print(plainTextHexByte)
    for i in range(10):
        plainTextHexByte = substituteBytes128(plainTextHexByte)
        #print("round no. "+ str(i+1))
        #print("after substituteBytes")
        #print(plainTextHexByte)
        plainTextHexByte = shiftRow(plainTextHexByte)
        #print("after shiftRow")
        #print(plainTextHexByte)
        if i!=9 :
            plainTextHexByte = mixColumn(plainTextHexByte)
        #print("after mixColumn")
        #print(plainTextHexByte)
        plainTextHexByte = deepcopy(addRoundKey(deepcopy(plainTextHexByte), deepcopy(wordList[i+1])))
        #print("after addRoundKey")
        #print(plainTextHexByte)
        #print()
        #print()
    return plainTextHexByte

def inverseShiftRow(ciphertext):
    var = deepcopy(ciphertext)

    for i in range(4):
        for j in range(4):
            num = (j-i)%4
            if num<0:
                num = num + 4
            var[j][i] = deepcopy(ciphertext[num][i])
    return var

def inverseSubBytes32(text):
    temp_text = []
    for i in range(4):
        t = list(text[i])
        a = int(t[0],16)
        b = int(t[1], 16)
        temp_text.append(format(InvSbox[a][b],"02x"))
    return temp_text

def inverseSubBytes(ciphertext):
    var = []
    for i in range(4):
        var.append(inverseSubBytes32(ciphertext[i]))
    return var

def inverseMixCol(text):
    temp = []
    for i in range(4):
        temp.append([])
        for j in range(4):
            temp[i].append(BitVector(hexstring=text[i][j]))
    var = []
    for i in range(4):
        var.append([])
        for j in range(4):
            a = temp[i][0].gf_multiply_modular( InvMixer[j][0]  ,AES_modulus,8)
            b = temp[i][1].gf_multiply_modular( InvMixer[j][1]  ,AES_modulus,8)
            c = temp[i][2].gf_multiply_modular( InvMixer[j][2]  ,AES_modulus,8)
            d = temp[i][3].gf_multiply_modular( InvMixer[j][3]  ,AES_modulus,8)

            #print(type(format(a.intValue(), "02x")))
            var[i].append(bitwiseXor8(bitwiseXor8(format(a.intValue(), "02x"), format(b.intValue(), "02x")),bitwiseXor8(format(c.intValue(), "02x"),format(d.intValue(), "02x"))))
            #print(var[i][j])
    #print(var)
    return var

def decrypt(ciphertext):
    ciphertext = addRoundKey(deepcopy(ciphertext), wordList[10])
    #print(ciphertext)

    for i in range(10):
        ciphertext = inverseShiftRow(ciphertext)
        #print("after inverseShiftRow")
        #print(ciphertext)
        ciphertext = inverseSubBytes(ciphertext)
        #print('after inverseSubBytes')
        #print(ciphertext)
        ciphertext = addRoundKey(deepcopy(ciphertext), wordList[9-i])
        #print('after addRoundKey')
        #print(ciphertext)
        if i!=9:
            ciphertext = inverseMixCol(ciphertext)
            #print('after inverseMixCol')
            #print(ciphertext)
    #print()
    #print('text')
    #print(ciphertext)

    return ciphertext




def AES_Demo():
    key = input("Enter the key : ")
    #print(len(key))
    global Sbox
    Sbox= deepcopy(CreateSbox())
    start=time.time()
    if len(key)<16:
        while len(key)!=16:
            key= key + str(0)
    if len(key)>16:
        key = key[:16]

    st_charArr = list(key)

    iter = 0
    w = []
    for i in range(4):
        w.append([])
        for j in range(4):
            w[i].append(format(ord(st_charArr[iter]),"02x"))
            iter= iter + 1

    #print(len(Sbox))
    keyScheduling(w)
    print("Key Scheduling time : "+ str(time.time()-start))
    '''ciphertext = encrypt(deepcopy(plainText))
    print('ciphertext : ')
    print(ciphertext)class (object):
        """docstring for ."""

        def __init__(self, arg):
            super(, self).__init__()
            self.arg = arg

    text = decrypt(deepcopy(ciphertext))
    print('text')
    print(text)

    getText = ""
    for i in range(len(text)):
        for j in range(len(text[i])):
            getText = getText + chr(int(text[i][j], 16))

    print('getText')
    print(getText)'''
    choice = input("Enter choice. (1-text,2-file)")
    if int(choice)==1:
        textToEncrypt = input("Enter the text to decrypt : ")
    else:
        filename = input("Enter file name:")
        with open(filename, 'rb') as f:
            textToEncrypt = str(f.read())
        #print(binascii.hexlify(content))
        #print(len(textToEncrypt))
        #print(textToEncrypt)

    ciphertext = []
    toGetText = deepcopy(textToEncrypt)
    start=time.time()
    print()
    print("Text in hex : ")
    for i in range(int(len(textToEncrypt)/16)):
        ciphertext.append(encrypt(textToEncrypt[16*i:16*(i+1)]))

    if len(textToEncrypt)>(i+1)*16:
        textToEncrypt = textToEncrypt[(i+1)*16:]
        while len(textToEncrypt) < 16:
            textToEncrypt = textToEncrypt + str(" ")
        ciphertext.append(encrypt(textToEncrypt))
    print()
    print("Encription time : "+str(time.time() - start))
    print("ciphertext in hex")
    for m in range(len(ciphertext)):
        print(ciphertext[m])
    print()


    returnedText = []
    start= time.time()
    for i in range(len(ciphertext)):
        returnedText.append(decrypt(ciphertext[i]))
    #print(len(returnedText))
    getText = ""

    print("Decryption time : "+str(time.time() - start))
    print("Decrypted text in hex :")
    for i in range(len(returnedText)):
        print(returnedText[i])
        for j in range(len(returnedText[i])):
            for k in range(len(returnedText[i][j])):
                getText = getText + chr(int(str(returnedText[i][j][k]), 16))
        #print(getText)
    print()
    print('Deciphered Text : ')
    print(getText)

AES_Demo()
#inv = Create_InvSbox()
