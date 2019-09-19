import sys, logging, json

# check to make sure we are running the right version of Python
version = (3, 7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0], version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

def render(room):
    '''Print out a description of the current location.'''
    print(room['name'])
    print(room['desc'])
    print(room['options']);
    return True

def check_input():
    '''Request input from the user, validate the input.'''
    user_input = input("What would you like to do? ")
    return user_input

def update(game, inventory, current, selection):
    '''Check if we need to move to a new location, etc.'''
    game[rooms][current];

def main():
    game = {}
    inventory = []
    with open('world.json') as json_file:
        game = json.load(json_file)
    # Your game goes here!
    current = 'ENTRY'

    quit = False

    while (not quit):
        render(game['rooms'][current])
        selection = check_input()
        current = update(game, current, selection)



    return True



#if we are running this from the command line, run main
if __name__ == '__main__':
	main()
