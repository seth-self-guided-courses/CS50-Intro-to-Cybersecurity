from string import digits
from string import ascii_letters, punctuation

def letters(): # 56**24
    for i in ascii_letters:
        for j in ascii_letters:
            for k in ascii_letters:
                for l in ascii_letters:
                    print(i,j,k,l)
        
def all_4(): # 78,000,000 ... 4 characters
    for i in ascii_letters + digits + punctuation:
        for j in ascii_letters + digits + punctuation:
            for k in ascii_letters + digits + punctuation:
                for l in ascii_letters + digits + punctuation:
                    print(i,j,k,l)
                    

                    
all_4()