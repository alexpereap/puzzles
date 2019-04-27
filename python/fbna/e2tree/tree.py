import os

# Tree node definition, for our binary tree
class TreeNode:
    def __init__(self, value, color):
        self.color = color
        self.value = value # helper prop node value
        self.left = None
        self.right = None
        self.parent = None
    
    # links a branch to our tree, first tries first then right
    def link(self, node):
        node.parent = self # if parent is none then is the root node
        if self.left is None:
            self.left = node
        else:
            self.right = node

    def __str__(self):
        return str(self.value)

# helper function to get the path from the root to a given node using one traversal
def path_to_node(root, path, k): 
  
    # base case to stop recursive function 
    if root is None: 
        return False
  
    # append the node in path 
    path.append(root) 
   
    # See if the k is same as root's value 
    if root.value == k : 
        return True
   
    # Check if k is found in left or right  
    # sub-tree 
    if ((root.left != None and path_to_node(root.left, path, k)) 
        or  (root.right!= None and path_to_node(root.right, path, k))): 
        return True
   
    # If not present in subtree rooted with root,  
    # remove root from path and return False  
    path.pop() 
    return False

# helper function to get the path from node 1 to node 2
# and to get the colors beteween the path
def get_nodes_path_colors(root_node, node1, node2):

    # get the path from root to node 1
    path1 = [] 
    path_to_node(root_node, path1, node1.value)
    
    # get the path from root to node 2  
    path2 = [] 
    path_to_node(root_node, path2, node2.value)

    # gets the path from node_val2 to node_val2
    # we need to find the intersection point between the two paths
    # by comparing the two paths in parallel untill their values are different
    # when that happens, the intersection is the previous emtpy value (index - 1)

    i = 0
    while i < len(path1) and i < len(path2):
        if  path1[i].value == path2[i].value:
            intersection_index = i
            i += 1
        else:
            intersection_index = i - 1
            break
    
    i = len(path1) - 1
    path_a_b = []

    colors = []

    # first loop on path1, reversal, right before intersection index 
    for x in range (intersection_index + 1, len(path1)):
        path_a_b.append(path1[i])
        colors.append(path1[i].color)
        i -= 1
    
    # second loop on path2, from intersection index to the end of the path
    for i in range(intersection_index, len(path2)):
        path_a_b.append(path2[i])
        colors.append(path2[i].color)

    return {
            'path': path_a_b,
            'colors': colors
        }
    


def proccessInput(input_file):
    f = open(input_file)
    input = f.read().splitlines()
    n = int(input[0])
    colors = input[1].split(' ')
    
    # generate a dict of len n and empty values to store the nodes in each key
    # a dict key is the node #
    dict_of_nodes = dict.fromkeys(range(1, n + 1))

    # nodes delcaration, i + 1 = node #
    for i, v in enumerate(colors): # Linear Time complexity O(n): time execution proportional to nodes quantity
        dict_of_nodes[i + 1] = TreeNode(value=i + 1, color=v)

    # node linking
    for i in range(2, len(input)):
        assignment = input[i].split(' ') # gets assignment in form of list, idx0 = root node, idx1 = node to link 
        dict_of_nodes[int(assignment[0])].link(dict_of_nodes[int(assignment[1])])

    # summatory analysis
    sum = []
    for i in dict_of_nodes:
        s = 0
        for j in range (1, n + 1):
            # get the path between node(i) and node(j)
            # root node is always node 1
            # print('d({},{})'.format( str(dict_of_nodes[i].value), str(j) ))
            nodes_path = get_nodes_path_colors( dict_of_nodes[1], dict_of_nodes[i], dict_of_nodes[j] )
            colors = nodes_path['colors']
            # unique colors count
            s += len(set(colors))

        print(s)

            
    
        


proccessInput( os.path.dirname(os.path.abspath(__file__)) + '/input.txt')

node1 = TreeNode(1,1)
node2 = TreeNode(2,2)
node3 = TreeNode(3,3)
node4 = TreeNode(4,2)
node5 = TreeNode(5,3)
node6 = TreeNode(6,4)
node7 = TreeNode(7,4)
node8 = TreeNode(8,1)
node9 = TreeNode(9,2)
node10 = TreeNode(10,2)
node11 = TreeNode(11,2)
node12 = TreeNode(12,2)
node13 = TreeNode(13,2)
node14 = TreeNode(14,2)

# after linking the nodes 

node1.link(node2)
node2.link(node3)
node2.link(node4)
node1.link(node5)
node5.link(node6)
node5.link(node9)
node6.link(node7)
node6.link(node8)
node9.link(node10)
node7.link(node11)
node7.link(node12)
node11.link(node13)
node11.link(node14)

# root = node1
# p = get_nodes_path_colors(root, node1, node4)
# l = [ v.value for v in p['path'] ]
# print(l)
