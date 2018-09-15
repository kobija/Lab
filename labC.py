import hashlib
import sys
sys.setrecursionlimit(1500)


def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


#separate file in a list of users,salts, and hashes 
f = "C:/Users/kevin/Desktop/1.3 Passwords/password_file.txt"
List = list()                                  
users = list()
salts = list()
hash_password = list()
count = 0
with open(f) as file:
    for line in file:
         List.append(line.split(","))
         users.append(List[count][0])
         salts.append(List[count][1])
         hash_password.append(List[count][2])
         count = count + 1


#print(hash_password[0].strip())

########################################### NUMBER_GENERATOR_FUNCTION ####################################################

def num_gen(L):
    num = ""                             # start by creating an empty string 
    temp = list()                        # creating a list to store the generated values
    s = ("{0:0"+ str(L) + "}").format(0) # filling with zeros before start generating numbers proportional to the length
    for i in range(L):   
        num = num + "9"                  # start by adding 999 or 9999999 
    for j in range(int(num)+1):
        s = ("{0:0"+ str(L) + "}").format(int(num)-j)   # decrease with every iteration
        temp.append(s)                                  # append the generated decreased number to "temp" list 
    num  = ""
    return temp
  
######################################## MATCHING_PASSWORDS_HASHED_PASSWORD ###############################################

def match_hash_pass(L,salts,count,hash_password):
    
    numlis = num_gen(L)        # create a list of of the generated numbers
    hash_emstr = list()        # create a list that is going to store a hased list 

    if count >= len(salts):
        return "finished...."

    for i in range(len(numlis)):
        hash_emstr.append( hash_with_sha256(str(numlis[i].strip()) + str(salts[count].strip())) )    # add the generated number to the salt value
        if hash_emstr[i].strip() == hash_password[count].strip():
            print("match")                                          # every time it matches one of the hash password is going to print match

    
    return  match_hash_pass(L,salts,count+1,hash_password)



    
def main():
    print(match_hash_pass(3,salts,0,hash_password))


main()
    


    