# Healthcare Management System
> DSA (Data Structures and Algorithms) Final Assignment
> 
> Python-based healthcare management system

# Introduction
This project is the final assignment for the DSA (Data Structures and Algorithms) unit. This program is a Healthcare Management System implemented in Python to help users manage patient records, including adding, updating, and deleting records, as well as retrieving patients’ medical histories. Additionally, it allows users to sort records based on patient ID. The system provides a simple text-based menu interface for user interaction. It implements multiple data structures such as linked lists and hash tables for the efficient management of patient records.
<br/>
This project aims to achieve the following objectives:
- Implement a <b>Healthcare Management System</b> using Python.
- Adopt different ADTs to meet the conditions below:
  - Create a Patient class to represent each patient
  - Use a hash table for adding, updating, and deleting patient records
  - Implement a linked list to store patients' medical histories
- Apply various algorithms for the following:
  - Adopt linear probing for hash key collision handling
  - Sort the patient IDs using the Merge Sort algorithm
- Design a text-based interface for the system that provides different functionalities
- Create a test harness by organising test cases to cover the system's functionalities
- Describe the system by completing UML diagrams, complexity analysis, and a traceability matrix.

# Preview
<img width="500" alt="preview" src="https://github.com/user-attachments/assets/6a7d7f3e-5c6b-4eb7-82bb-cb6783252eed" />

# Execution
**Assumption: Python3 is installed**
1. Run the code by using the command below:
```
python3 Healthcare_Management.py
```
2. Enter a number between 1 and 6 to select a menu option
* Test data is provided with ID 'TEST1' for testing update and delete functionalities

# Dependencies

The program requires the following library to run properly:

* **numpy:** Used for creating arrays, such as creating hash array within PatientHashTable and creating arrays with hash entry keys to facilitate sorting.

# Terminologies and Abbreviations
- **MedicalHistoryException:** A custom base exception class for specifying errors related to medical history management.
- **EmptyMedicalHistoryException:** A custom exception class for specifying errors related to attempting operations on an empty medical history list.
- **PatientRecordException:** A custom base exception class for specifying errors related to patient record management.
- **PatientIdNotFoundException:** A custom exception class for specifying errors related to finding a patient Id that does not exist.
- **EmptyPatientRecordException:** A custom exception class for specifying errors related to attempting operations on an empty patient table.
- **PatientTableFullException:** A custom exception class for specifying errors related to attempting operations on a full patient table.
- **Patient:** A class that contains patient record, which is implemented using linked list, and personal information such as patient ID, name, age, and phone number. It has functionalities such as updating patient record, adding medical histories, and retrieving medical histories.
- **MedicalHistoryList:** Represents alinked list data structure implementation. Used to store medical histories for patients.
- **HistoryListNode:** Represents a list node in the linked list, containing a value (medical history as an object) and next pointer.
- **PatientHashTable:** A hash table data structure implementation designed to store and manage patient records using linear probing for collision resolution.
- **PatientHashEntry:** An entry in the hash table that contains key (patient ID), value (Patient object), state (whether it is empty, used, or deleted) information.
- **mergeSort:** A merge sorting algorithm implementation to arrange patient records based on their ID.
- **\_mergeSortRecurse:** A recursive function used for merge sorting algorithm implementation.
- **\_merge:** A method for actual merge algorithm used for merge sorting algorithm.
- **validate\_patient\_id:** A method responsible for validating patient ID input.
- **validate\_name:** A method responsible for validating patient name input.
- **validate\_age:** A method responsible for validating patient age.
- **validate\_phone\_number:** A method responsible for validating patient phone number.
- **main:** A main method responsible for displaying interactive text menu, receiving user inputs, and handling them.

# Future Directions

Several improvements can make the system more flexible and user friendly:

1. **Medical history details:** The current medical history only stores patient id and consultation date. Adding more details such as diagnosis and medication would be beneficial.
2. **Data storage:** The current system stores data in memory, which means it is hard to maintain data and use it when needed. Storing in database would allow safer storage and better data management for real life healthcare organisations.
3. **User interface:** The current interface is based on text. Implementing interface that has more visual graphics would make it easier for the users to access the features they need.
4. **Secure information:** The current system displays personal health information just by receiving patient’s ID. Adopting security measures such as separating user role into administrators and general users.

# UML Diagram
<img width="760" alt="UML diagram" src="https://github.com/user-attachments/assets/6ea47b71-4ca5-45bc-bd30-421827e46d7e" />

# Time Complexity of Functions

### Adding Patient Record

Complexity: O(1) to O(n)

Analysis: For adding patient record, hash table with linear probing is used. In the average case, as hash function distributes the keys evenly, insertion would be done in constant O(1). However, in the worst case where multiple keys hash to the same location, hash table must probe multiple times until finding an empty entry. Validation functions such as validate\_patient\_id, validate\_name, validate\_age, and validate\_phone\_number all run in O(1) since they simply check on inputs and do not go any further.

---

### Updating Existing Patient Record

Complexity: O(1) to O(n)

Analysis: Updating a patient record needs two main operations: finding the patient by using the hash table’s get() function, and updating the patient’s information. The hash table finds the key using linear probing, which takes O(1) on average and O(n) when it has to probe through all entries. Updating the record details (name, age, phone\_number) directly updates Patient object fields, so it is done in constant time.

---

### Deleting Patient Record

Complexity: O(1) to O(n)

Analysis: Deleting a patient record requires finding the patient in the hash table and removing the record using remove() function. The hash table finds the key by using linear probing and it takes O(1) time on average, but O(n) in the worst case where multiple entries are clustered. The actual deleting operation only takes constant time as it only needs to mark the entry as deleted. Remove function may trigger resize function if the load factor falls below the threshold, but this does not affect the individual operation complexity since resizing is a separated operation.

---

### Retrieving Medical History

Complexity: O(1+m+m) to O(n+m+m) = O(m) to O(n+m)

Analysis: This functionality needs to first find the patient using get() function of the hash table (O(1) to O(n) time complexity), then retrieves the medical history using to\_list() function of the linked list, which visits each medical history entry once, taking O(m) time. Printing the retrieved history also takes O(m^n) time since each entry must be displayed.

---

### Sorting Patients Based on Patient ID

Complexity: O(n + m log m + mn)

Analysis: This operation needs two main phases; first, converting the hash table to an array using to\_array() function, second, sorting the array using mergeSort() function. The to\_array() function needs to go through every entry in the hash table, taking O(n) time. The mergeSort() function takes O(m log m) time in every case. After sorting, displaying the results takes O(mn) to print each patient’s details by calling get() function inside.

---

### Exit

Complexity: O(1)

Analysis: This operation simple exits the loop. This needs no data processing or complex operations, making it take constant time that does not depend on the amount of data.

---

# Requirements

|  |  |
| --- | --- |
| **Req No.** | **Description** |
| **1.** | User should be able to add patient’s record |
| **2.** | User should be able to update existing patient’s record |
| **3.** | User should be able to delete patient record |
| **4.** | User should be able to retrieve medical history of patient |
| **5.** | User should be able to get a sorted patient list |
| **6.** | User should be able to exit the interactive menu |
| **7.** | System should be able to handle unexpected or invalid user inputs |

# Test Case

|  |  |
| --- | --- |
| **Test Case No.** | **Test Case** |
| **1.** | Successfully add a patient’s record with valid inputs |
| **2.** | Attempt to add a patient’s record with existing ID |
| **3.** | Attempt to add a patient’s record with blank ID |
| **4.** | Attempt to add a patient’s record with blank name |
| **5.** | Attempt to add a patient’s record with invalid age (not between 0 and 150) |
| **6.** | Attempt to add a patient’s record with invalid age (not a number) |
| **7.** | Successfully update a patient’s record with valid inputs |
| **8.** | Attempt to update a patient’s record with an ID that is not in the table an ID that is not in the table |
| **9.** | Attempt to update a patient’s record with blank ID |
| **10.** | Attempt to update a patient’s record with blank name |
| **11.** | Attempt to update a patient’s record with invalid age (not between 0 and 150) |
| **12.** | Attempt to update a patient’s record with invalid age (not a number) |
| **13.** | Successfully delete a patient’s record with valid input |
| **14.** | Attempt to delete a patient’s record with an ID that is not in the table |
| **15.** | Successfully retrieve a patient’s medical history with valid input |
| **16.** | Attempt to retrieve a patient’s medical history with an ID that is not in the table |
| **17.** | Attempt to retrieve a patient’s medical history with an ID that has no medical history |
| **18.** | Successfully sort patient ID and display sorted patient list |
| **19.** | Attempt to sort an empty table |
| **20.** | Attempt to sort a table that has only one record |
| **21.** | Successfully exit the interactive menu with valid input |
| **22.** | Attempt to exit the interactive menu with invalid input |

# Traceability Matrix

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Requirements** | | **Req 1** | **Req 2** | **Req 3** | **Req 4** | **Req 5** | **Req 6** | **Req 7** |
| **Test Cases** | **Total** | **1** | **1** | **1** | **1** | **1** | **1** | **16** |
| **1** | **1** | **X** |  |  |  |  |  |  |
| **2** | **1** |  |  |  |  |  |  | **X** |
| **3** | **1** |  |  |  |  |  |  | **X** |
| **4** | **1** |  |  |  |  |  |  | **X** |
| **5** | **1** |  |  |  |  |  |  | **X** |
| **6** | **1** |  |  |  |  |  |  | **X** |
| **7** | **1** |  | **X** |  |  |  |  |  |
| **8** | **1** |  |  |  |  |  |  | **X** |
| **9** | **1** |  |  |  |  |  |  | **X** |
| **10** | **1** |  |  |  |  |  |  | **X** |
| **11** | **1** |  |  |  |  |  |  | **X** |
| **12** | **1** |  |  |  |  |  |  | **X** |
| **13** | **1** |  |  | **X** |  |  |  |  |
| **14** | **1** |  |  |  |  |  |  | **X** |
| **15** | **1** |  |  |  | **X** |  |  |  |
| **16** | **1** |  |  |  |  |  |  | **X** |
| **17** | **1** |  |  |  |  |  |  | **X** |
| **18** | **1** |  |  |  |  | **X** |  |  |
| **19** | **1** |  |  |  |  |  |  | **X** |
| **20** | **1** |  |  |  |  |  |  | **X** |
| **21** | **1** |  |  |  |  |  | **X** |  |
| **22** | **1** |  |  |  |  |  |  | **X** |

# Successful Execution Example
1. **Adding Patient Record**

<img width="500" alt="adding patient record" src="https://github.com/user-attachments/assets/a7822647-c592-4634-a65d-401fd06d1beb" />

2. **Updating Patient Record**

<img width="500" alt="updating patient record" src="https://github.com/user-attachments/assets/5a8dba7f-05f8-428c-85cd-0fe107d2b685" />

3. **Deleting Patient Record**

<img width="500" alt="deleting patient record" src="https://github.com/user-attachments/assets/2a3b3a9c-d365-48ea-b5a3-03bb8365ecc3" />

4. **Retrieving Medical History**

<img width="500" alt="retrieving medical history" src="https://github.com/user-attachments/assets/edd433fe-8946-4ab9-9419-b7e419542e50" />

5. **Sorting Patient Records based on Patient ID**

<img width="500" alt="sorting patient records" src="https://github.com/user-attachments/assets/016fbb43-ab91-4069-99ba-dad1bda8a29f" />

6. **Exiting Menu**

<img width="500" alt="exiting menu" src="https://github.com/user-attachments/assets/f8b469c1-ccfe-454f-b892-6fb4f2ee5028" />

# References

GeeksforGeeks. 2025. “Ord() Function in Python.” GeeksforGeeks. https://www.geeksforgeeks.org/python/ord-function-python/.
