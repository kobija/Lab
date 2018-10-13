
import hashlib
import sys
sys.setrecursionlimit(10000000)


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


########################################### NUMBER_GENERATOR_FUNCTION ####################################################


def num_gen(L,factor):
    num = '9'*L      # initialize the string with 9s 
    temp = list()    # create a list to store the value of the generated numbers
    lIndx = len(num)-1                               
    for i in range((int(num[lIndx]) + int(factor))-8):      #this loop increases by the factor parameter in order to prevent stackoverflow
        s = ("{0:0"+ str(L) + "}").format(int(num)-i)
        temp.append(s)                                      #appending the values to the list
    if int(temp[len(temp)-1]) <= int('0'*L):                #if the last index of the loop is less than or equal to 0*L which is the last value the program will return the list 
        return temp
    return num_gen(L, factor + '9')



########################################### MATCHING_PASSWORDS_HASHED_PASSWORD ####################################################

   
def match_hash_pass(L,salts,count,hash_password):
    
    numlis = num_gen(L,'9')        # create a list of of the generated numbers
    hash_emstr = list()        # create a list that is going to store a hased list 
    
    if count >= len(salts):
        return "finished...."

    for i in range(len(numlis)):
        hash_emstr.append( hash_with_sha256(str(numlis[i].strip()) + str(salts[count].strip())) )    # add the generated number to the salt value
        if hash_emstr[i].strip() == hash_password[count].strip():
            print("match")        # every time it matches one of the hash password is going to print match
            print(i)
    
    return  match_hash_pass(L,salts,count+1,hash_password)



    
def main():
    print(match_hash_pass(3,salts,0,hash_password))


main()