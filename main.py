import sys, logging, json, os

from subprocess import call

# check to make sure we are running the right version of Python
version = (3, 7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0], version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

def clear_screen():
   _ = call('clear' if os.name =='posix' else 'cls')

def render(room):
    '''Print out a description of the current location.'''
    print("============")
    print(room['name'])
    print("============\n")
    print(room['desc'])
    print("-----------")
    print(room['options'])
    return True

def check_input():
    '''Request input from the user, validate the input.'''
    user_input = input("\n\nWhat would you like to do? ")
    return user_input.upper().strip()

def update(game, inventory, current, selection):
    '''Check if we need to move to a new location, etc.'''
    clear_screen()
    exits = game['rooms'][current]['exits']
    verbs = game['verbs']

    verb = verbs.get(selection, -1)

    if (verb != -1):
        direction = exits.get(verb, -1)
        if (direction != -1):
            target = direction['target']
            if (target == 'ITEM'):
                item = game['rooms'][current]['inventory'][0]
                print("----------------")
                print("ACQUIRED: {}".format(item))
                print("----------------\n")
                inventory.append(item)
                return current
            elif (exits[verb]['condition'] in inventory):
                return target
            else:
                print("!!!!!!!!!!!!!!!!!!!!")
                print(exits[verb]['failure'])
                print("\n")
                return current
        else:
            print("That is not a valid option.")
            return current
    else:
        print("That is not a valid verb.")
        return current

def main():
    game = {}
    with open('world.json') as json_file:
        game = json.load(json_file)
    # Your game goes here!

    clear_screen()
    moves = 0
    inventory = [""]
    current = 'ENTRY'
    print("Welcome to \"A Locked Room\". Type 'Q' at any time to quit!\n\n")

    while (True):
        render(game['rooms'][current])

        if (current == 'OMDOOR'):
            print("\n\n\n!!!!!!!!!!!\nCONGRATULATIONS, YOU HAVE WON IN {} MOVES.".format(moves))
            input()
            break

        selection = check_input()

        if (selection == 'Q'):
            break

        current = update(game, inventory, current, selection)
        moves += 1

    clear_screen()
    print("Thank you for playing!")
    return True



#if we are running this from the command line, run main
if __name__ == '__main__':
	main()
