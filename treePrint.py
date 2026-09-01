#Use a for loop to print a triangular pine tree of a size the user asks for. 
# The tree branches should be printed as a number of rows of ^ characters, 
# while the trunk should always be two # characters. 
# For example, if the user enters 5 for the size, the program should print this:

# Enter the tree size: 5
#    ^
#   ^^^
#  ^^^^^
# ^^^^^^^
#^^^^^^^^^
#   #
#   #

print("--- My Tree Program ---")

size = int(input("Please enter the size of the tree:"))

for row_num in range(1,size+1):
    branch_chars = (row_num * 2 - 1)
    space_chars = (size - row_num)
    print('.' * space_chars, '^' * branch_chars)

print('.' * (size - 1), '#')
print('.' * (size - 1), '#')

print('End of program.')