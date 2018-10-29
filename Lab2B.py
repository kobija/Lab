


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
    def __init__(self , password):
        self.password = password
        self.count = 1
        self.next = None

 

class Linked_list:
    def __init__(self):
        self.head = None
        self.size = 0
        self.new_node = None

    def add(self,password):
        for i in range(len(password)):
            self.size = self.size + 1
            self.head = Node(password[i])
            self.head.next = self.new_node
            self.new_node = self.head     

    def get_prev_node(self, wanted_node):
        current = self.head
        while (current and current.next != wanted_node):
            current = current.next
        return current
         
    def printList(self):
        printval = self.head
        while printval:
            print(printval.password , printval.count)
            printval = printval.next

    def remove(self,node):
        previous = self.get_prev_node(node)
        if previous == None:
            self.head = self.head.next
        else:
            previous.next = node.next

    def swap(self, node1 , node2):
        prev1 = None
        curr1 = self.head 
        while curr1 != None and curr1 != node1: 
            prev1 = curr1 
            curr1 = curr1.next
  
        prev2 = None
        curr2 = self.head 
        while curr2 != None and curr2 != node2: 
            prev2 = curr2 
            curr2 = curr2.next
  
        if prev1 != None: 
            prev1.next = curr2
        else: 
            self.head = curr2 
 
        if prev2 != None: 
            prev2.next = curr1
        else: 
            self.head = curr1 
  
        temp = curr1.next
        curr1.next = curr2.next
        curr2.next = temp 
     

    
def takeDuplicates(mylist):
    curr_node = mylist.head
    while curr_node:
        curr_node2 = curr_node.next
        while curr_node2:
            if curr_node2.password == curr_node.password:
                curr_node.count = curr_node.count + 1
                mylist.remove(curr_node2)
            curr_node2 = curr_node2.next
        curr_node = curr_node.next
    


def bubble_sort(mylist):
     current = mylist.head
     while current:
           current2 = current.next
           while current2:
               if current.count < current2.count:
                   mylist.swap(current,current2)
               current2 = current2.next
           current = current.next
    
     
        


mylist = Linked_list()
mylist.add(passwords)
takeDuplicates(mylist)
bubble_sort(mylist)

mylist.printList()


  
        
 
  





    
    
    
    

    
    

    
    






    





   
   
    


    

   
    
    



