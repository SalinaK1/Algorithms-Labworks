class BinarySearchTree:
    def __init__(self):
        self.size= 0
        self._root = None

    class BST_Node:
        def __init__(self,key,value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.parent = None
    
    def size(self):
        return self.size

    def add(self,key,value):
        node_x = self._root
        node_y = None
        new_node = self.BST_Node(key,value)
        while node_x is not None:
            node_y = node_x
            if new_node.key < node_x.key:
                node_x = node_x.left 
            else :
                node_x = node_x.right

        new_node.parent = node_y
        if node_y is None:
            self._root = new_node
        elif new_node.key < node_y.key:
            node_y.left  = new_node
        else :
            node_y.right  = new_node
        self.size+=1
      
    def search(self,key):
        nodes = self._root
        while nodes is not None:
            if key == nodes.key:
                print(f"{key} Found")
                return nodes.value
            elif key < nodes.key:
                nodes = nodes.left
            else:
                nodes = nodes.right
        return False 

    def smallest(self):
        nodes = self._root
        while nodes.left is not None:
            nodes = nodes.left
        return (nodes.key, nodes.value)

    def largest(self):
        nodes = self._root
        while nodes.right is not None:
            nodes = nodes.right
        return (nodes.key, nodes.value)
    
    def _inorder_walk(self,node, in_list):
        if node:
            self._inorder_walk(node.left, in_list)
            in_list.append(node.key)
            self._inorder_walk(node.right, in_list)

    def inorder_walk(self):
        output_list = []
        root = self._root
        self._inorder_walk(root, output_list)
        return output_list  

    def _preorder_walk(self,node, pre_list):
        if node:
            pre_list.append(node.key)
            self._preorder_walk(node.left, pre_list)
            self._preorder_walk(node.right, pre_list)

    def preorder_walk(self):
        output_list = []
        root = self._root
        self._preorder_walk(root, output_list)
        return output_list
    
    def _postorder_walk(self,node, post_list):
        if node:
            self._postorder_walk(node.left, post_list)
            self._postorder_walk(node.right, post_list)
            post_list.append(node.key)

    def postorder_walk(self):
        output_list = []
        root = self._root
        self._postorder_walk(root, output_list)
        return output_list



if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.add(5,"Five")
    print(bst.size)
    bst.add(6,"Six")
    print(bst.size)
    bst.add(8,"Eight")
    print(bst.size)
    bst.add(2,"Two")
    print(bst.size)
    bst.add(4,"Four")
    print(bst.size)
    print(bst.search(5))
    print(bst.search(6))
    print(bst.search(8))
    print(bst.search(2))
    print(bst.search(4))
    print(bst.smallest())
    print (bst.largest())
    print(bst.inorder_walk())
    print(bst.preorder_walk())
    print(bst.postorder_walk())





