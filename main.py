import string 
import random
if __name__ == "__main__":
   s1 = string.ascii_lowercase
   #print(s1)
   s2 = string.ascii_uppercase
   #print(s2)
   s3 = string.digits
   #print(s3)   
   s4 = string.punctuation
   #print(s4) 
   while True:
        plen = input("Enter the length of the Password:\n")
        if plen.isdigit():
            plen = int(plen)
            break
        else:
            print("Enter a valid number: ")
        
   s = []
   s.extend(list(s1))
   s.extend(list(s2))
   s.extend(list(s3))
   s.extend(list(s4))
   #print(s)
   random.shuffle(s)
   print("Your Password is : ")
   print("".join(s[0:plen]))
   #print("".join(random.sample(s,plen)))_(AlternateOption)

  