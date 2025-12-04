class Node:
    """A single node in the linked list."""
    def __init__(self, data_dict=None):
        self.data = data_dict
        self.next = None

class LinkedList:
    """The complete linked list structure."""
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data_dict):
        """Inserts a new node (with the given dictionary data) at the head of the list."""
        new_node = Node(data_dict=data_dict)
        new_node.next = self.head
        self.head = new_node

    def traverse_and_print(self):
        """Traverses the list from the head and prints the data in each node."""
        current_node = self.head
        print("\n=== Linked List Content ===")
        while current_node is not None:
           
            print(current_node.data)
            current_node = current_node.next
        print("===========================")


student_records = LinkedList()


student_data_1 = {
    'Name of Student': 'Alice Johnson',
    'Admission': 'CIM/00108/024',
    'Grades ': {'programming': 'A', 'python': 'B+'}
}

student_data_2 = {
    'Name of Student': 'Bob Ojwang',
    'Admission': 'CIM/00120/024',
    'Grades ': {'Programming': 'B', 'python': 'A-'}
}


student_records.insert_at_beginning(student_data_2) 
student_records.insert_at_beginning(student_data_1) 


student_records.traverse_and_print()
