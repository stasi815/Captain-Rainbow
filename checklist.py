"""Checklist."""
# Created Checklist
# Jessica Trinh helped me make int(index), mark_completed,
# and uppercase variable
checklist = list()


# From https://www.geeksforgeeks.org/print-colors-python-terminal/
# Python program to print colored text and background
def prRed(skk):
    """Red."""
    return("\033[91m {}\033[00m" .format(skk))


def prGreen(skk):
    """Green."""
    return("\033[92m {}\033[00m" .format(skk))


def prYellow(skk):
    """Yellow."""
    return("\033[93m {}\033[00m" .format(skk))


def prLightPurple(skk):
    """Light Purple."""
    return("\033[94m {}\033[00m" .format(skk))


def prPurple(skk):
    """Purple."""
    return("\033[95m {}\033[00m" .format(skk))


def prCyan(skk):
    """Cyan."""
    return("\033[96m {}\033[00m" .format(skk))


def prLightGray(skk):
    """Light Gray."""
    return("\033[97m {}\033[00m" .format(skk))


def prBlack(skk):
    """Black."""
    return("\033[98m {}\033[00m" .format(skk))


# Define Functions
def create(item):
    """Create item code."""
    checklist.append(item)


# READ
def read(index):
    """Read code."""
    return checklist[int(index)]


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
        print(prPurple("{} {}".format(index, list_item)))
        index += 1


# Marking Item Complete
def mark_completed(index):
    """My code here."""
    # Add code here that marks an item as completed
    checklist[int(index)] = "{} {}".format("√", checklist[int(index)])


# Select Functions
def select(function_code):
    """User selection code."""
    # Append item
    if function_code == "A":
        input_item = user_input(prGreen('Add item.: '))
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input(prGreen('Index Number?: '))
    # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # User UPDATE
    elif function_code == "U":
        item_index = user_input(prGreen('Index Number?: '))
        input_item = user_input("Input Item: ")
        update(item_index, input_item)

    # Mark list item with check
    elif function_code == "C":
        item_index = user_input(prGreen('Index Number?: '))
        mark_completed(item_index)

    # Delete item
    elif function_code == "D":
        item_index = user_input(prGreen('Index Number?: '))
        destroy(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Quit Function
    elif function_code == "Q":
        # This is where we want to stop our loop
        return False
    # Catch all
    else:
        print("Unknown Option. Choose from list of approved actions.")
    return True


# User Input
def user_input(prompt):
    """Accept user input."""
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input
    # user_value = user_input("Please Enter a value:")
    # print(user_value)


# TEST
# def test():
#    """Test functions."""
    # create("purple sox")
    # create("red cloak")

    # print(read(0))
    # print(read(1))

    # update(0, "purple socks")
    # destroy(1)

    # print(read(0))
    # print(read(1))
    # Your testing code here
    # ...
    # Call your new function with the appropriate value
    # select("A")
    # View the results
    # list_all_items()
    # Call function with new value
    # select("R")
    # View results
    # list_all_items()
    # select("U")
    # View results
    # list_all_items()
    # select("Q")
    # View results
    # list_all_items()
    # select("D")
    # View results
    # list_all_items()
    # select("P")
    # View results
    # list_all_items()
# Continue until all code is run


# Run tests
# test()

running = True
while running:
    selection = user_input(prCyan(
        "Press:A=add; C=checkitem; U=update; D=delete; R=read;P=list;Q=quit "))
    selection_lowerAndUpper = selection.upper()
    running = select(selection_lowerAndUpper)
