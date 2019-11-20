class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

class LL:
    def __init__(self):
        self.head = None

    def display_ll(self, func_name=None):
        node = self.head
        count = 1
        print("%s : " % func_name)
        while node.next_node is not None:
            print("%s-->" % node.value, end="")
            node = node.next_node
            count += 1

        print("%s-->None" % node.value)
        print("This LL has total elem : ", count)

    def add_elm_to_ll(self, elm):
        node = self.head
        while node.next_node is not None:
            node = node.next_node
        node.next_node = elm

    def delete_node(self, node_val):
        node = self.head
        previous_node = None
        while node.value != node_val and node.next_node is not None:
            previous_node = node
            node = node.next_node
        if node.value == node_val:
            if not previous_node:
                self.head = node.next_node
                print("Warning : Head Change !!!")
            else:
                previous_node.next_node = node.next_node
            self.display_ll(self.delete_node.__name__)
            return 0
        self.display_ll()
        return 1

def create_node(value):
    return Node(value)

my_ll = LL()
snode = create_node(10)
my_ll.head = snode
my_ll.display_ll()
my_ll.add_elm_to_ll(Node(90))
my_ll.add_elm_to_ll(Node(80))
my_ll.display_ll()
d_node_val = 10
# print(my_ll.delete_node(d_node_val))
assert (my_ll.delete_node(d_node_val) == 0), "Delete Node failed : Node not present with value %s. " % d_node_val

# temp = create_node(20)
# add_elm_to_ll(snode, temp)
# add_elm_to_ll(snode, create_node(90))
# add_elm_to_ll(snode, create_node(80))
# add_elm_to_ll(snode, create_node(50))
# display_ll(snode)
