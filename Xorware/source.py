
import random
from datetime import datetime
from secret import msgtxt

def keyGen():
    KEY_LENGTH = 8  # encrypt key size 

    # create char pool for key gen 
    charPool=""
    for i in range(65,127):
        charPool+=chr(i)
     
    kwy = ""

    date = datetime.today().strftime("%Y%m%d")
    random.seed(int(date))

    for c in range(KEY_LENGTH):
        key += random.choice(charPool) 
         
    return key


def encrypt(data,key): 
        keyIndex = 0
        encryptData  = ""
        for d in data:
            # Reset to key Index 
            if keyIndex == len(key):
                keyIndex = 0
            
            encryptData  += chr(ord(d) ^ ord(key[keyIndex]))
            keyIndex += 1
        
        return encryptData 
     

def main():
    key = keyGen()

    cyper = bytes(encrypt(msgtxt,key),"UTF-8")

    file = open("massage.enc","wb")
    file.write(cyper)
    file.close()



if __name__ == "__main__":
     main()


