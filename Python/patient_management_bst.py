# Class to represent a patient node in the BST
class Patient:
    def __init__(self, patient_id, name, age, condition):
        self.patient_id = patient_id  # Unique ID for each patient (used as BST key)
        self.name = name              # Name of the patient
        self.age = age                # Age of the patient
        self.condition = condition    # Medical condition
        self.left = None              # Left child node
        self.right = None             # Right child node


# Binary Search Tree to manage patients
class PatientBST:
    def __init__(self):
        self.root = None  # Initially, the tree is empty

   #Insert a new patient into the BST.
    def insert(self, patient_id, name, age, condition):
        new_patient = Patient(patient_id, name, age, condition)
        if not self.root:
            self.root = new_patient  # First patient becomes root
        else:
            self._insert(self.root, new_patient)

    #Recursive insert helper method.
    def _insert(self, current, new_patient):
        if new_patient.patient_id < current.patient_id:
            if current.left is None:
                current.left = new_patient
            else:
                self._insert(current.left, new_patient)
        else:
            if current.right is None:
                current.right = new_patient
            else:
                self._insert(current.right, new_patient)

    
    # Search for a patient by ID. Returns the patient object or None if not found. 
    def search(self, patient_id):
        return self._search(self.root, patient_id)

    def _search(self, current, patient_id):
        if not current:
            return None
        if current.patient_id == patient_id:
            return current
        elif patient_id < current.patient_id:
            return self._search(current.left, patient_id)
        else:
            return self._search(current.right, patient_id)

    # Delete a patient by ID.
    def delete(self, patient_id):
        self.root = self._delete(self.root, patient_id)

    def _delete(self, current, patient_id):
        if not current:
            return current
        if patient_id < current.patient_id:
            current.left = self._delete(current.left, patient_id)
        elif patient_id > current.patient_id:
            current.right = self._delete(current.right, patient_id)
        else:
            # Node with only one child or no child
            if not current.left:
                return current.right
            elif not current.right:
                return current.left
            
            # Node with two children: Get the inorder successor (smallest in right subtree)
            temp = self._min_value_node(current.right)
            current.patient_id = temp.patient_id
            current.name = temp.name
            current.age = temp.age
            current.condition = temp.condition
            current.right = self._delete(current.right, temp.patient_id)
        return current


    #Find the node with the minimum patient_id in a given subtree.  
    def _min_value_node(self, node):
       
        while node.left:
            node = node.left
        return node

    #INORDER TRAVERSAL
    def inorder_traversal(self):
    #Return a list of all patients in sorted order (by patient_id).
        patients = []
        self._inorder(self.root, patients)
        return patients

    def _inorder(self, current, patients):
        if current:
            self._inorder(current.left, patients)
            patients.append((current.patient_id, current.name, current.age, current.condition))
            self._inorder(current.right, patients)

    #Return the patient with the maximum age.
    def find_oldest_patient(self): 
        return self._find_extreme_patient(self.root, max)

      #Return the patient with the minimum age.
    def find_youngest_patient(self):

        return self._find_extreme_patient(self.root, min)


    #Find patient based on comparator (max or min age).
    def _find_extreme_patient(self, current, comparator):
        
        if not current:
            return None
        extreme_patient = current
        stack = [current]
        while stack:
            node = stack.pop()
            if comparator(node.age, extreme_patient.age) == node.age:
                extreme_patient = node
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return extreme_patient

    # Count the total number of patients in the BST.
    def count_patients(self):
        return self._count_patients(self.root)

    def _count_patients(self, current):
        if not current:
            return 0
        return 1 + self._count_patients(current.left) + self._count_patients(current.right)

     #Find the height of the BST (max depth).
    def find_height(self):
        return self._find_height(self.root)

    def _find_height(self, current):
        if not current:
            return -1  # Height of an empty tree is -1
        left_height = self._find_height(current.left)
        right_height = self._find_height(current.right)
        return 1 + max(left_height, right_height)

   
    #VALID BST CHECK
    def is_valid_bst(self):
        
        #Check if the tree is a valid Binary Search Tree.
        return self._is_valid_bst(self.root, float('-inf'), float('inf'))

    def _is_valid_bst(self, current, min_val, max_val):
        if not current:
            return True
        if not (min_val < current.patient_id < max_val):
            return False
        return (self._is_valid_bst(current.left, min_val, current.patient_id) and
                self._is_valid_bst(current.right, current.patient_id, max_val))
