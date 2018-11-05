
def _pretty_tree_helper(root, curr_index=0):
    if root is None:
        return [], 0, 0, 0

    line1 = []
    line2 = []
    node_repr = str(root.key)

    new_root_width = gap_size = len(node_repr)
    
    # Get the left and right sub-boxes, their widths, and root repr positions
    l_box, l_box_width, l_root_start, l_root_end = _pretty_tree_helper(root.left, 2 * curr_index + 1)
    r_box, r_box_width, r_root_start, r_root_end = _pretty_tree_helper(root.right, 2 * curr_index + 2)

    # Draw the branch connecting the current root to the left sub-box
    # Pad with whitespaces where necessary
    if l_box_width > 0:
        l_root = (l_root_start + l_root_end) // 2 + 1
        line1.append(' ' * (l_root + 1))
        line1.append('_' * (l_box_width - l_root))
        line2.append(' ' * l_root + '/')
        line2.append(' ' * (l_box_width - l_root))
        new_root_start = l_box_width + 1
        gap_size += 1
    else:
        new_root_start = 0

    # Draw the representation of the current root
    line1.append(node_repr)
    line2.append(' ' * new_root_width)

    # Draw the branch connecting the current root to the right sub-box
    # Pad with whitespaces where necessary
    if r_box_width > 0:
        r_root = (r_root_start + r_root_end) // 2
        line1.append('_' * r_root)
        line1.append(' ' * (r_box_width - r_root + 1))
        line2.append(' ' * r_root + '\\')
        line2.append(' ' * (r_box_width - r_root))
        gap_size += 1
    new_root_end = new_root_start + new_root_width - 1

    # Combine the left and right sub-boxes with the branches drawn above
    gap = ' ' * gap_size
    new_box = [''.join(line1), ''.join(line2)]
    for i in range(max(len(l_box), len(r_box))):
        l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
        r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
        new_box.append(l_line + gap + r_line)

    # Return the new box, its width and its root positions
    return new_box, len(new_box[0]), new_root_start, new_root_end
    
def pretty_tree(tree):
    lines = _pretty_tree_helper(tree.root, 0)[0]
    return '\n' + '\n'.join((line.rstrip() for line in lines))

class Node:
    # Constructor with a key parameter creates the Node object.
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0
        
    # Method to calculate the current nodes's balance factor node, 
    # defined as height(left subtree) - height(right subtree)
    def get_balance(self):
        # Get current height of left subtree, or -1 if None
        left_height = -1
        if self.left is not None:
            left_height = self.left.height
            
        # Get right subtree's current height, or -1 if None
        right_height = -1
        if self.right is not None:
            right_height = self.right.height
            
        # Calculate the balance factor.
        return left_height - right_height

    # Recalculates the current height of the subtree rooted at
    # the node, usually called after a subtree has been 
    # modified.
    def update_height(self):
        # Get current height of left subtree, or -1 if None
        left_height = -1
        if self.left is not None:
            left_height = self.left.height
            
        # Get current height of right subtree, or -1 if None
        right_height = -1
        if self.right is not None:
            right_height = self.right.height

        # Assign self.height with calculated node height.
        self.height = max(left_height, right_height) + 1

        
    # Assign either the left or right data member with a new
    # child. The parameter which_child is expected to be the
    # string "left" or the string "right". Returns True if
    # the new child is successfully assigned to this node, False
    # otherwise.
    def set_child(self, which_child, child):
        # Ensure which_child is properly assigned.
        if which_child != "left" and which_child != "right":
            return False

        # Assign the left or right data member.
        if which_child == "left":
            self.left = child
        else:
            self.right = child

        # Assign the new child's parent data member,
        # if the child is not None.
        if child is not None:
            child.parent = self

        # Update the node's height, since the structure
        # of the subtree may have changed.
        self.update_height()
        return True

    # Replace a current child with a new child. Determines if
    # the current child is on the left or right, and calls
    # set_child() with the new node appropriately.
    # Returns True if the new child is assigned, False otherwise.
    def replace_child(self, current_child, new_child):
        if self.left is current_child:
            return self.set_child("left", new_child)
        elif self.right is current_child:
            return self.set_child("right", new_child)
          
        # If neither of the above cases applied, then the new child
        # could not be attached to this node.
        return False

        
class AVLTree:
    def __init__(self):
        # Constructor to create an empty AVLTree. There is only
        # one data member, the tree's root Node, and it starts
        # out as None.
        self.root = None

    # Performs a left rotation at the given node. Returns the
    # subtree's new root.
    def rotate_left(self, node):
        # Define a convenience pointer to the right child of the 
        # left child.
        right_left_child = node.right.left
        
        # Step 1 - the right child moves up to the node's position.
        # This detaches node from the tree, but it will be reattached
        # later.
        if node.parent is not None:
            node.parent.replace_child(node, node.right)
        else:  # node is root
            self.root = node.right
            self.root.parent = None

        # Step 2 - the node becomes the left child of what used
        # to be its right child, but is now its parent. This will
        # detach right_left_child from the tree.
        node.right.set_child('left', node)
        
        # Step 3 - reattach right_left_child as the right child of node.
        node.set_child('right', right_left_child)
        
        return node.parent

    # Performs a right rotation at the given node. Returns the
    # subtree's new root.
    def rotate_right(self, node):
        # Define a convenience pointer to the left child of the 
        # right child.
        left_right_child = node.left.right
        
        # Step 1 - the left child moves up to the node's position.
        # This detaches node from the tree, but it will be reattached
        # later.
        if node.parent is not None:
            node.parent.replace_child(node, node.left)
        else:  # node is root
            self.root = node.left
            self.root.parent = None

        # Step 2 - the node becomes the right child of what used
        # to be its left child, but is now its parent. This will
        # detach left_right_child from the tree.
        node.left.set_child('right', node)

        # Step 3 - reattach left_right_child as the left child of node.
        node.set_child('left', left_right_child)
        
        return node.parent

    # Updates the given node's height and rebalances the subtree if
    # the balancing factor is now -2 or +2. Rebalancing is done by
    # performing a rotation. Returns the subtree's new root if
    # a rotation occurred, or the node if no rebalancing was required.
    def rebalance(self, node):
    
        # First update the height of this node.
        node.update_height()        
        
        # Check for an imbalance.
        if node.get_balance() == -2:
        
            # The subtree is too big to the right.
            if node.right.get_balance() == 1:
                # Double rotation case. First do a right rotation
                # on the right child.
                self.rotate_right(node.right)
                
            # A left rotation will now make the subtree balanced.
            return self.rotate_left(node)
                        
        elif node.get_balance() == 2:

            # The subtree is too big to the left
            if node.left.get_balance() == -1:
                # Double rotation case. First do a left rotation
                # on the left child.
                self.rotate_left(node.left)
                
            # A right rotation will now make the subtree balanced.
            return self.rotate_right(node)
            
        # No imbalance, so just return the original node.
        return node

    # Insert a new node into the AVLTree. When insert() is complete,
    # the AVL tree will be balanced.
    def insert(self, node):
        
        # Special case: if the tree is empty, just set the root to
        # the new node.
        if self.root is None:
            self.root = node
            node.parent = None

        else:
            # Step 1 - do a regular binary search tree insert.
            current_node = self.root
            while current_node is not None:
                # Choose to go left or right
                if node.key < current_node.key:
                    # Go left. If left child is None, insert the new
                    # node here.
                    if current_node.left is None:
                        current_node.left = node
                        node.parent = current_node
                        current_node = None
                    else:
                        # Go left and do the loop again.
                        current_node = current_node.left
                else:
                    # Go right. If the right child is None, insert the
                    # new node here.
                    if current_node.right is None:
                        current_node.right = node
                        node.parent = current_node
                        current_node = None
                    else:
                        # Go right and do the loop again.
                        current_node = current_node.right
            
            # Step 2 - Rebalance along a path from the new node's parent up
            # to the root.
            node = node.parent
            while node is not None:
                self.rebalance(node)
                node = node.parent

    # Searches for a node with a matching key. Does a regular
    # binary search tree search operation. Returns the node with the
    # matching key if it exists in the tree, or None if there is no
    # matching key in the tree.
    def search(self, key):
        current_node = self.root
        while current_node is not None:
            # Compare the current node's key with the target key.
            # If it is a match, return the current key; otherwise go
            # either to the left or right, depending on whether the 
            # current node's key is smaller or larger than the target key.
            if current_node.key == key: return current_node
            elif current_node.key < key: current_node = current_node.right
            else: current_node = current_node.left

    # Attempts to remove a node with a matching key. If no node has a matching key
    # then nothing is done and False is returned; otherwise the node is removed and
    # True is returned.
    def remove_key(self, key):
        node = self.search(key)
        if node is None:
            return False
        else:
            return self.remove_node(node)
            
    # Removes the given node from the tree. The left and right subtrees,
    # if they exist, will be reattached to the tree such that no imbalances
    # exist, and the binary search tree property is maintained. Returns True
    # if the node is found and removed, or False if the node is not found in
    # the tree.es return after directly removing the node.
    def remove_node(self, node):
        # Base case: 
        if node is None:
            return False
            
        # Parent needed for rebalancing.
        parent = node.parent
            
        # Case 1: Internal node with 2 children
        if node.left is not None and node.right is not None:
            # Find successor
            successor_node = node.right
            while successor_node.left != None:
                successor_node = successor_node.left
                
            # Copy the value from the node
            node.key = successor_node.key
                
            # Recursively remove successor
            self.remove_node(successor_node)
                
            # Nothing left to do since the recursive call will have rebalanced
            return True
        
        # Case 2: Root node (with 1 or 0 children)
        elif node is self.root:
            if node.left is not None:
                 self.root = node.left
            else:
                 self.root = node.right

            if self.root is not None:
                 self.root.parent = None

            return True
        
        # Case 3: Internal with left child only
        elif node.left is not None:
            parent.replace_child(node, node.left)
            
        # Case 4: Internal with right child only OR leaf
        else:
            parent.replace_child(node, node.right)
            
        # node is gone. Anything that was below node that has persisted is already correctly
        # balanced, but ancestors of node may need rebalancing.
        node = parent
        while node is not None:
            self.rebalance(node)            
            node = node.parent
        
        return True
   
    def __str__(self):
        return pretty_tree(self)

f = open("words.txt")
word_list = f.readlines()

for i in range(len(word_list)):
    word_list[i] = word_list[i][:-2]
    
counter = 0;
def print_anagrams(word, prefix=""): 
 
    if len(word) <= 1:
        strr = prefix + word
        
        if strr in word_list: 
            print(prefix + word)
            
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]
            after = word[i + 1:] 
            
            if cur not in before: 
                print_anagrams(before + after, prefix + cur)
              
def count_anagrams(word,prefix=""):
    global counter
    if len(word) <= 1:
        str = prefix + word
        if str in word_list: 
            counter +=1
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]  
            after = word[i + 1:] 
            
            if cur not in before: 
                count_anagrams(before + after, prefix + cur)  
    return counter       

def greatest_anagrams(file,tree):
    print()
    

def createTree(tree):
    counter = 0
    for ln in word_list:
        if counter == 10:
            break
        ln = ln.replace('\n','')
        print(ln)
        ln = Node(ln)
        tree.insert(ln)
        counter += 1
    return tree
    
print_anagrams('spot')
counter = count_anagrams("spot")
print("Number of anagrams",counter)
counter = count_anagrams("spot")
print("Number of anagrams",counter)
 
myTree = None
tree_type = raw_input('what type of tree do you want to use?, AVL or RBT \n')
if(tree_type == 'AVL'):
    myTree = AVLTree()
elif(tree_type == 'RBT'):
    myTree = RedBlackTree()
     
if(myTree != None):
    tree = createTree(myTree)
    

    
counter = 0
tree = AVLTree()
for ln in word_list:
    if counter == 10000:
        break
    ln = ln.replace('\n','')
    ln = Node(ln)
    tree.insert(ln)
    counter += 1
    
print(pretty_tree(tree))
if tree_type == 'AVL':
    tree_AVL = AVLTree()
    for ln in word_list:
        ln = ln.replace('\n','')
        words = Node(ln)
        tree_AVL.insert(words)
    print(tree_AVL)
    
if tree_type  == 'RBT':
    tree_RBT = RedBlackTree()
    for ln in word_list:
        tree_RBT.insert(ln)
    print( 'tree has height ' + str(tree_RBT.get_height()))