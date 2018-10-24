

#read the file 
f = "C:/Users/kevin/Desktop/10-million-combos.txt"
List = list()                                  
passwords = list()

count = 0
with open(f) as file:
    for line in file:
         List.append(line.split(" "))
         passwords.append(List[count][0])
         count = count + 1
 
class Node(object):
    password = ""
    count = -1
    next = None

    def __init__(self, password, count, next):
        self.password = password
        self.count = count
        self.next = next


########################################### LINK-LIST #################################################

i = 0
count = 1
node  = Node("", count, None)
node1 = Node("", count, None)

while i != len(passwords):
  node = Node(passwords[i].strip(),count,node)
  if  node.password == passwords[i].strip():
    for j in range(i+1,len(passwords)):
      node1 = Node(passwords[j],count,node1)
      if node.password == node1.password:
          node.count = node.count + 1
  print(node.password , node.count)        
  i = i + 1


###################################### DICTIONARIES LINK-LIST #########################################

#nodeDic = {}
#nodeDic1 = {}


#ctr = 1
#node  = Node("",ctr,None)
#node1 = Node("",ctr,None)
#i = 0

#while i != len(passwords):
#    nodeDic[i] = Node(passwords[i],ctr,node)
#    node = nodeDic[i]
#    if nodeDic[i].password == passwords[i].strip():
#       for j in range(i+1,len(passwords)):
#         nodeDic1[i] = Node(passwords[j],count,node1)
#         if nodeDic[i].password == nodeDic1[i].password:
#             nodeDic[i].count = nodeDic[i].count + 1         
#    print(nodeDic[i].password,nodeDic[i].count)   
#    i = i + 1
    





   
   
    


    

   
    
    



