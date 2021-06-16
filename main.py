from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# Create the Stacks

stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks += [left_stack, middle_stack, right_stack]

# Set up the Game

num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))

for disk in range(num_disks, 0, -1):
    left_stack.push(disk)

left_stack.print_items()

num_optimal_moves = (2 ** num_disks) - 1
print("\nThe fastest you can solve this game is in {0} moves\n".format(num_optimal_moves))

# Get User Input


def get_input():

    choices = [stack.get_name()[0] for stack in stacks]
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print("Enter {0} for {1}".format(letter, name))

        user_input = input("\nMake Selection: ")

        if user_input in choices:

            for stack in stacks:
                if user_input.upper() == stack.get_name()[0]:
                    print('Match found')
                    print(user_input, stack.get_name()[0], stack.get_name())
                    return stack


# Play the Game

num_user_moves = 0

while right_stack.get_size() != num_disks:

    print("\n\n\n...Current Stacks...")
    for stack in stacks:
        stack.print_items()

    while True:

        print("\nFROM?\n")
        from_stack = get_input()
        print('from_stack', from_stack.get_name())
        print("\nTO?\n")
        to_stack = get_input()
        print("to_stack", to_stack.get_name())

        if from_stack.get_size() == 0:
            print("\n\n!!!!!!!!! Invalid Move. Try Again - NOTHING TO MOVE (FROM) !!!!!!!!!!")
        elif to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print("\n\nInvalid Move. HIGH DISK CANNOT BE PLACED ON A LOWER DISK")

print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves,
                                                                                                num_optimal_moves))
