# Prompt the user to choose a data type to perform operations on
print("Choose a data type to perform operations on:")
print("1. Strings")
print("2. Numbers")
print("3. Booleans")
print("4. Additional Data Types (List, Tuple, Dictionary)")

# Get the user's choice and store it in a variable
choice = input("Enter the number of your choice (1-4): ")

if choice == '1': # If the user chooses Strings (choice == '1'):
    sentence = "Learning Python is fun!"
    print(f"Example of string: {sentence}")
    sentence_list = sentence.split()
    substring = sentence_list[1]
    print(f"The second word in the sentence is: {substring}") # Extract and print a substring, such as the word "Python" from the sentence.
    sentence_upper = sentence.upper()
    print(f"The string with capital letters: {sentence_upper}") # Convert the entire sentence to uppercase and print it.
    replacement = "awesome"
    sentence_new = sentence.replace("fun", replacement)
    print(f"If we replace fun with {replacement}, we get: {sentence_new}") # Replace a word in the sentence (e.g., replace "fun" with "awesome") and print the modified sentence.

elif choice == '2': # If the user chooses Numbers (choice == '2'):
    print("Input two numbers!") # Prompt the user to input two numbers, e.g., num1 and num2.
    num1 = int(input("Input first number: "))
    num2 = int(input("Input second number: "))
    print(f"Sum of numbers = {num1 + num2}") # Perform and print the results of addition, subtraction, multiplication, and division.
    print(f"Difference of numbers = {num1 - num2}")
    print(f"Product of numbers = {num1 * num2}")
    if num2 == 0:
        print("Error: Division by zero") # Handle division by zero (e.g., print an error message if num2 is zero).
    else:
        print(f"Division of numbers = {num1 / num2}")
    print(f"Power of numbers = {num1 ** num2}") # Perform a power operation, raising num1 to the power of num2, and print the result.

elif choice == '3': # If the user chooses Booleans (choice == '3'):
    is_python_fun = True
    is_sunny = False # Declare two boolean variables, e.g.,
    print(f"is_python_fun = {is_python_fun}")
    print(f"is_sunny = {is_sunny}")
# Perform and print the results of logical operations: AND, OR, NOT.
    print(f"is_python_fun AND is_sunny = {is_python_fun and is_sunny}")
# Perform and print the results of comparison operations (e.g., 10 > 5 and 5 == 5).
    print(f"10 > 5 AND 5 == 5 = {10 > 5 and 5 == 5}")
    print(f"is_python_fun OR is_sunny = {is_python_fun or is_sunny}")
    print(f"not is_python_fun = {not is_python_fun}")

elif choice == '4': # If the user chooses Additional Data Types (choice == '4'):
# ### List Operations ###
    list1 = [1, 3, 8, 'apple','cherry', True, False, 1.23, 4.56] # Create a list with mixed data types (e.g., numbers, strings, booleans).
    print(f"List example: {list1}")
    new_element = 'strawberry'
    print(f"New element: {new_element} ")
    print("Adding the new element to the list:")
    list1.append(new_element) # Append a new element to the list and print the updated list.
    print(f"The new list is: {list1}")
    print(f"The fifth element in the list is: {list1[4]}") # Access and print the 4th element in the list.

 # ### Tuple Operations ###
    tuple1 = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango') # Create a tuple with some string elements (e.g., fruits).
    print(f"Tuple example: {tuple1}")
    print(f"The length of the tuple is: {len(tuple1)}") # Print the length of the tuple.
    print(f"The third element in the tuple is: {tuple1[2]}")
    replacement = 'watermelon'
    print(f"If we try to change it with {replacement}, we get:")
    print(f"TypeError: 'tuple' object does not support item assignment") # Try to modify one element in the tuple and handle the resulting TypeError.

# ### Dictionary Operations ###
    dict1 = {'name': 'John', 'age': 36, 'city': 'New York'} # Create a dictionary with some key-value pairs (e.g., name, age, city).
    print(f"Dictionary example: {dict1}")
    print(f"The value for 'age' is: {dict1['age']}") # Access and print the value for one of the keys (e.g., "age").
    dict1['profession'] = 'software developer'
    print(f"New key-value pair added: {dict1['profession']}")
    print(f"The updated dictionary is: {dict1}") # Add a new key-value pair to the dictionary and print the updated dictionary.

# If the user enters an invalid choice:
else:
    print("Error: Invalid selection") # Print an error message indicating an invalid selection.