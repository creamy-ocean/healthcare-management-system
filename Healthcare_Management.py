"""
DSA Final Assignment

Introduction: Python implementation for healthcare management system.
It allows users to add patient records, update records, and retrieve patients' medical histories.

Author name: Hyeyoung Yun
"""

import numpy as np

# Custom Exceptions
class MedicalHistoryException(Exception):
    """Exception for medical history related errors"""
    pass

class EmptyMedicalHistoryException(MedicalHistoryException):
    """Exception raised when MedicalHistory is empty"""
    pass

class PatientRecordException(Exception):
    """Exception for patient record related errors"""
    pass

class PatientIdNotFoundException(PatientRecordException):
    """Exception raised when patient ID is not found"""
    pass

class EmptyPatientRecordException(PatientRecordException):
    """Exception raised when patient hash table is empty"""
    pass

class PatientTableFullException(PatientRecordException):
    """Exception raised when patient hash table is full"""
    pass

class Patient:
    """
    Patient class for saving patient record
    It uses LinkedList for medical history
    """
    def __init__(self, patient_id, name, age, phone_number):
        self._patient_id = patient_id
        self._name = name
        self._age = age
        self._phone_number = phone_number
        self._medical_history = MedicalHistoryList()

    def get_record(self):
        return self._name, self._age, self._phone_number

    def update_record(self, name, age, phone_number):
        """Update patient's record"""
        self._name = name
        self._age = age
        self._phone_number = phone_number

    def add_medical_history(self, consult_date):
        """Add list node to MedicalHistoryList"""
        self._medical_history.insert_first({
            'patient_id': self._patient_id,
            'consult_date': consult_date
        })

    def get_medical_history(self):
        """Retrieve medical history Linkedlist"""
        return self._medical_history.to_list()

# Reference - Copied basic ListNode and LinkedList code from previous assessment Practical 06
class HistoryListNode:
    """
    ListNode for MedicalHistoryList(LinkedList)
    Receives object for in_value to save medical history in this scenario
    """
    def __init__(self, in_value):
        self.value = in_value
        self.next = None

class MedicalHistoryList:
    """
    LinkedList to save medical history
    New history is stored at the front by using insertFirst function
    """
    def __init__(self):
        self._head = None
        self._count = 0

    def insert_first(self, new_value):
        """Insert new node to the first"""
        if new_value is None:
            raise MedicalHistoryException("Cannot insert empty value")

        new_nd = HistoryListNode(new_value)

        if self.is_empty():
            self._head = new_nd
        else:
            new_nd.next = self._head
            self._head = new_nd

        self._count += 1

    def is_empty(self):
        """Check if Linkedlist is empty"""
        empty = self._head is None
        return empty

    def to_list(self):
        """Convert linkedlist to a list (to make it easier to print)"""
        if self.is_empty():
            raise EmptyMedicalHistoryException("No medical history found")

        results = []
        curr_nd = self._head

        while curr_nd is not None:
            results.append(curr_nd.value)
            curr_nd = curr_nd.next

        return results

# Reference - Copied basic HashTable and HashEntry code from previous assessment Practical 07
class PatientHashEntry:
    """
    Hash entry for PatientHashTable
    It mainly contains;
    1. key, which is a unique key for each entry, saves patient ID in this scenario
    2. value, which is actual value inside entry, saves Patient object in this scenario
    2. state, 0 for empty, 1 for used, -1 for deleted
    """
    def __init__(self, in_key = "", in_value = None):
        if in_key == "" and in_value is None:
            self.key = ""
            self.value = None
            self.state = 0
        else:
            self.key = in_key
            self.value = in_value
            self.state = 1

class PatientHashTable:
    """
    Hash table to save hash entries (patients' records) in this scenario
    """
    def __init__(self, table_size):
        # Use prime number to avoid clustering and improve distribution
        self._actual_size = self._next_prime(table_size)
        self._hash_array = np.empty(self._actual_size, dtype=object)

        # Initialise hash_array with empty hash entries
        for idx in range(self._actual_size):
            self._hash_array[idx] = PatientHashEntry()

        # Variables to track number of entries and load factor thresholds
        self._count = 0
        self._low_thr = 0.3
        self._high_thr = 0.7

    def put(self, in_key, in_value):
        """Insert new entry or update existing entry"""
        if not in_key or in_value is None:
            raise ValueError("Key and value must be available")

        try:
            hash_idx = self._find_insertion_loc(in_key)
            curr_entry = self._hash_array[hash_idx]

            if curr_entry.state == 1 and curr_entry.key == in_key:
                # Update existing entry
                curr_entry.value = in_value
            else:
                # Insert new entry
                self._hash_array[hash_idx] = PatientHashEntry(in_key, in_value)
                self._count += 1

                # Resize if load factor exceeds high threshold
                if self.get_load_factor() > self._high_thr:
                    self._resize(self._actual_size * 2)

        except Exception as e:
            print(f"Error inserting key '{in_key}'- {e}")

    def get(self, in_key):
        """Retrieve value using key"""
        if not in_key:
            raise ValueError("Key cannot be empty")

        try:
            hash_idx = self._find(in_key)
            hash_entry = self._hash_array[hash_idx]
            value = hash_entry.value
        except Exception:
            raise PatientIdNotFoundException(f"ID '{in_key}' not found")

        return value

    def remove(self, in_key):
        """Remove entry using key"""
        if not in_key:
            raise ValueError("Key cannot be empty")

        try:
            hash_idx = self._find(in_key)
            hash_entry = self._hash_array[hash_idx]

            # Marking that it is deleted
            hash_entry.state = -1
            hash_entry.key = ""
            hash_entry.value = None
            self._count -= 1

            # Resize if load factor gets smaller than low threshold
            if self.get_load_factor() < self._low_thr:
                self._resize(self._actual_size // 2)
        except Exception as e:
            raise Exception(f"Error occurred removing key '{in_key}' - {e}")

    def get_load_factor(self):
        """Calculate current load factor"""
        return self._count / self._actual_size

    def has_key(self, in_key):
        """Check if key exists in the table"""
        try:
            self._find(in_key)
            result = True
        except Exception:
            result = False

        return result

    def to_array(self):
        """Convert hash table to numpy array to make sorting easier"""
        if self._count == 0:
            raise EmptyPatientRecordException("Patient table is empty")

        array = np.empty(self._count, dtype=object)
        array_idx = 0
        for entry in self._hash_array:
            if entry.state == 1:
                array[array_idx] = entry.key
                array_idx += 1

        return array

    def _resize(self, new_size):
        """Resize hash table and rehash all entries"""
        old_array = self._hash_array
        self._actual_size = self._next_prime(new_size)
        self._hash_array = np.empty(self._actual_size, dtype=object)

        for idx in range(self._actual_size):
            self._hash_array[idx] = PatientHashEntry()

        self._count = 0

        # Rehash all entries that are active
        for entry in old_array:
            if entry.state == 1:
                self.put(entry.key, entry.value)

    # Reference - How to get Unicode code of a character
    # GeeksforGeeks. 2025. “Ord() Function in Python.” GeeksforGeeks. https://www.geeksforgeeks.org/python/ord-function-python/.
    def _hash(self, key):
        """Primary hash function"""
        hash_idx = 0

        # ord function returns Unicode code of a single character (e.g., 'a' -> 97)
        for k in key:
            hash_idx = (33 * hash_idx) + ord(k)

        # Use modulo to ensure even distribution
        return hash_idx % self._actual_size

    def _find(self, in_key):
        """Find index of existing key"""
        hash_idx = self._hash(in_key)
        orig_idx = hash_idx
        found = False
        give_up = False

        while not found and not give_up:
            hash_entry = self._hash_array[hash_idx]

            if hash_entry.state == 0:
                # key not found
                give_up = True
            elif hash_entry.state == 1 and hash_entry.key == in_key:
                # key found
                found = True

            if not found and not give_up:
                # Linear probing - move to next location
                hash_idx = (hash_idx + 1) % self._actual_size
                if hash_idx == orig_idx: # Completed full circle
                    give_up = True

        if not found:
            raise PatientIdNotFoundException(f"ID '{in_key}' not found")

        return hash_idx

    def _find_insertion_loc(self, in_key):
        hash_idx = self._hash(in_key)
        orig_idx = hash_idx
        found_existing = False
        give_up = False
        insertion_idx = None

        while not found_existing and not give_up:
            hash_entry = self._hash_array[hash_idx]

            if hash_entry.state == 0:
                # Insertion point found (save insertion_idx and exit)
                if insertion_idx is None:
                    insertion_idx = hash_idx
                give_up = True
            elif hash_entry.state == -1:
                if insertion_idx is None:
                    # Saves insertion_idx but keep finding
                    insertion_idx = hash_idx
            elif hash_entry.state == 1 and hash_entry.key == in_key:
                found_existing = True

            if not found_existing and not give_up:
                # Linear probing - moving to next location
                hash_idx = (hash_idx + 1) % self._actual_size
                if hash_idx == orig_idx:  # Completed full circle
                    give_up = True

        result_idx = None

        if found_existing:
            result_idx = hash_idx
        elif insertion_idx is not None:
            result_idx = insertion_idx

        if result_idx is None:
            raise PatientTableFullException(f"Hash table is full")
        else:
            return result_idx

    def _next_prime(self, start_val):
        """Find next prime number after start_val"""
        if start_val % 2 == 0:
            prime_val = start_val - 1
        else:
            prime_val = start_val

        is_prime = False

        while is_prime is False:
            prime_val = prime_val + 2
            ii = 3
            is_prime = True
            root_value = int(np.sqrt(prime_val))

            while ii <= root_value and is_prime:
                if prime_val % ii == 0:
                    is_prime = False
                else:
                    ii = ii + 2

        return prime_val

# Reference - Copied mergeSort, _mergeSortRecurse, _merge functions from previous assessment Practical 09
def mergeSort(arr):
    """mergeSort - front-end for kick-starting the recursive algorithm"""
    if len(arr) <= 1:
        raise ValueError("Array size must be at least 2") # Exit the function because it means the array is already sorted

    _mergeSortRecurse(arr, 0, len(arr) - 1)

    return arr

def _mergeSortRecurse(arr, left_idx, right_idx):
    """Recursive function for mergeSort"""
    if left_idx < right_idx:
        mid_idx = (left_idx + right_idx) // 2

        _mergeSortRecurse(arr, left_idx, mid_idx)
        _mergeSortRecurse(arr, mid_idx + 1, right_idx)
        _merge(arr, left_idx, mid_idx, right_idx)

def _merge(arr, left_idx, mid_idx, right_idx):
    """Merge left and right parts using given indices"""
    temp_arr = np.empty(right_idx - left_idx + 1, dtype=arr.dtype)
    ii = left_idx
    jj = mid_idx + 1
    kk = 0

    while ii <= mid_idx and jj <= right_idx:
        if arr[ii] <= arr[jj]:
            temp_arr[kk] = arr[ii]
            ii += 1
        else:
            temp_arr[kk] = arr[jj]
            jj += 1
        kk += 1

    for i in range (ii, mid_idx + 1):
        temp_arr[kk] = arr[i]
        kk += 1

    for j in range (jj, right_idx + 1):
        temp_arr[kk] = arr[j]
        kk += 1

    for k in range (left_idx, right_idx + 1):
        arr[k] = temp_arr[k - left_idx]

def validate_patient_id(id):
    """Validate patient ID input"""
    if not id:
        raise ValueError("Patient ID must not be empty")
    return id

def validate_name(name):
    """Validate name input"""
    if not name:
        raise ValueError("Name must not be empty")
    return name

def validate_age(age_str):
    """Validate age input"""
    try:
        age = int(age_str)
    except ValueError:
        raise ValueError("Age is not a valid number")

    if age < 0 or age > 150:
        raise ValueError("Age must be between 0 and 150")

    return age

def validate_phone_numer(number_str):
    """Validate phone number input"""
    length = len(number_str)
    if length < 9 or length > 15:
        raise ValueError("Phone number's length must be between 9 and 15")
    return number_str

def test_harness():
    """
    Test harness function for the entire program.
    Displays interactive menu and receives user inputs and validate them.
    """
    patient_table = PatientHashTable(10)

    # Put test data for testing medical history
    test_patient = Patient("TEST1", "Jane Doe", 30, "1234567890")
    test_patient.add_medical_history("2024-01-15")
    test_patient.add_medical_history("2024-02-20")
    test_patient.add_medical_history("2024-03-10")
    patient_table.put("TEST1", test_patient)

    menu_arr = np.array(["Add patient's record", "Update existing patient record", "Delete patient record", "Retrieve medical history",  "Sort patients based on patient ID", "Exit"])

    print("===Healthcare Management System===")
    print("** You can use id 'TEST1' to test **")

    for idx, option in enumerate(menu_arr):
        print(f"{idx + 1}.{option}")

    choice = input("Please enter the number of option from the menu above (1-6): ")

    while choice != "6":
        try:
            if choice == "1":
                # Add patient record
                patient_id = validate_patient_id(input("Please enter patient's ID: "))

                if patient_table.has_key(patient_id):
                    raise Exception("Patient ID already exists")

                name = validate_name(input("Please enter patient's name: "))
                age = validate_age(input("Please enter patient's age: "))
                phone_number = validate_phone_numer(input("Please enter patient's phone number: "))

                patient = Patient(patient_id, name, age, phone_number)
                patient_table.put(patient_id, patient)

                print("Patient record successfully added!")

            if choice == "2":
                # Update patient record
                patient_id = validate_patient_id(input("Please enter patient's ID to update: "))
                patient = patient_table.get(patient_id)

                name = validate_name(input("Please enter patient's name: "))
                age = validate_age(input("Please enter patient's age: "))
                phone_number = validate_phone_numer(input("Please enter patient's phone number: "))

                patient.update_record(name, age, phone_number)
                print("Patient record successfully updated!")

            if choice == "3":
                # Delete patient record - remove function checks if the key exists in the table
                patient_id = validate_patient_id(input("Please enter patient's ID to delete: "))
                patient_table.remove(patient_id)
                print("Patient record successfully removed!")

            if choice == "4":
                # Retrieve medical history
                patient_id = input("Please enter patient's ID to retrieve histories: ")
                patient = patient_table.get(patient_id)

                medical_history = patient.get_medical_history()
                name, _, _ = patient.get_record()
                print(f"===Patient {name}'s history===")

                for history in medical_history:
                    print(f"Consultation date: {history['consult_date']}")

            if choice == "5":
                # Sort patients by ID
                sorted_arr = mergeSort(patient_table.to_array())
                print("===Sorted patient list===")

                for patient_id in sorted_arr:
                    patient = patient_table.get(patient_id)
                    name, age, phone_number = patient.get_record()
                    print(f"ID: {patient_id} Name: {name} Age: {age} Phone number: {phone_number}")

            elif choice not in ["1","2","3","4","5"]:
                print("Input is invalid. Please try again.")

        except Exception as e:
            print(f"Error occurred: {e}. Please try again.")

        print()

        for idx, option in enumerate(menu_arr):
            print(f"{idx + 1}.{option}")

        choice = input("Please enter the number of option from the menu above (1-6): ")

    print("===System ended===")

if __name__ == "__main__":
    test_harness()
