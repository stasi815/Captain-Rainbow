"""Checklist."""
# Created Checklist
# Jessica Trinh helped with int(index) and mark_completed
checklist = list()


# Define Functions
def create(item):
    """Create item code."""
    checklist.append(item)


# READ
def read(index):
    """Read code."""
    item = checklist[index]
    return item


# UPDATE
def update(index, item):
    """Update code."""
    checklist[int(index)] = str(item)


# DESTROY
def destroy(index):
    """Delete code."""
    checklist.pop(int(index))


# LIST
def list_all_items():
    """List all items in code."""
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1


# Marking Item Complete
def mark_completed(index):
    """My code here."""
    # Add code here that marks an item as completed
    checklist[int(index)] = "{} {}".format("√", checklist[int(index)])


# User Input
def select(function_code):
    """User selection code."""
    # Create item
    if function_code == "C":
        input_item = user_input("Append item: ")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?: ")
    # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Delete item
    elif function_code == "D":
        item_index = user_input("Index Number?: ")
        destroy(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Catch all
    else:
        print("Unknown Option")


def user_input(prompt):
    """Accept user input."""
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input


# TEST
def test():
    """Test functions."""
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    # print(read(1))
    # Your testing code here
    # ...
    # Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
# Continue until all code is run


user_value = user_input("Please Enter a value:")
print(user_value)

# Run tests
test()
