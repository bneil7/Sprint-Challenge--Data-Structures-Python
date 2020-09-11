import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare new value to main value (greater than or less than)
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:  # RECURSION
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:  # RECURSION
                self.right.insert(value)

    # if tree contains target value: return True, else: False
    def contains(self, target):
        if self.value == target:
            return True
        if self.value >= target:
            if self.left is None:
                return False
            return self.left.contains(target)
        if self.value < target:
            if self.right is None:
                return False
            return self.right.contains(target)
        else:
            return False


duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
bst_node = BSTNode("None")

for name in names_1:
    bst_node.insert(name)
for name in names_2:
    if bst_node.contains(name):
        duplicates.append(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
