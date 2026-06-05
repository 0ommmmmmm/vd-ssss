# Create hash table with 10 empty lists
hash_table = [[] for i in range(10)]

# Insert function
def insert(key, value):
    index = key % 10
    hash_table[index].append(value)

# Display function
def display():
    for i in range(len(hash_table)):
        print(i, end=" ")

        for j in hash_table[i]:
            print("-->", j, end=" ")

        print()

# Insert values
insert(10, "Allahabad")
insert(25, "Mumbai")
insert(20, "Mathura")
insert(9, "Delhi")
insert(21, "Punjab")
insert(21, "Noida")

# Display hash table
display()