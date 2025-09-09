class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


class Tree:
    def __init__(self):
        self.root = None
    
    def add_node(self, parent_data, child_data):
        if not self.root:
            self.root = TreeNode(parent_data)
            return
        
        parent = self.find_node(parent_data)
        if parent:
            child = TreeNode(child_data)
            parent.children.append(child)
    
    def find_node(self, data):
        if not self.root:
            return None
        return self._find_node_recursive(self.root, data)
    
    def _find_node_recursive(self, node, data):
        if node.data == data:
            return node
        
        for child in node.children:
            result = self._find_node_recursive(child, data)
            if result:
                return result
        return None
    
    def display_tree(self):
        if not self.root:
            print("Tree is empty")
            return
        self._display_recursive(self.root, 0)
    
    def _display_recursive(self, node, level):
        indent = "  " * level
        print(f"{indent}{node.data}")
        for child in node.children:
            self._display_recursive(child, level + 1)
    
    def get_height(self):
        if not self.root:
            return 0
        return self._get_height_recursive(self.root)
    
    def _get_height_recursive(self, node):
        if not node.children:
            return 1
        
        max_child_height = 0
        for child in node.children:
            child_height = self._get_height_recursive(child)
            max_child_height = max(max_child_height, child_height)
        
        return max_child_height + 1
    
    def count_nodes(self):
        if not self.root:
            return 0
        return self._count_nodes_recursive(self.root)
    
    def _count_nodes_recursive(self, node):
        count = 1
        for child in node.children:
            count += self._count_nodes_recursive(child)
        return count


if __name__ == "__main__":
    tree = Tree()
    
    tree.add_node("Root", "Child1")
    tree.add_node("Root", "Child2")
    tree.add_node("Child1", "Grandchild1")
    tree.add_node("Child1", "Grandchild2")
    tree.add_node("Child2", "Grandchild3")
    
    print("Tree structure:")
    tree.display_tree()
    
    print(f"\nTree height: {tree.get_height()}")
    print(f"Total nodes: {tree.count_nodes()}")
    
    found = tree.find_node("Child1")
    print(f"Found node 'Child1': {found.data if found else 'Not found'}")
