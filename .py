import simplegui
import random

#global variable
secret_number = 0
count = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global count 
    count = 7
    secret_number = random.randrange(0,100)
    print "\nNew Game. Range is from 0 to 100"
    print "Number of guesses is 7\n"
  

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number 
    global count 
    count = 7
    secret_number = random.randrange(0,1000)
    print "\nNew Game. Range is from 0 to 100"
    print "Number of remaining guesses is 7\n"


def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number 
    global count 
    count = 10
    secret_number = random.randrange(0,1000)
    print "\nNew Game. Range is from 0 to 1000"
    print "Number of remaining guesses is 10\n"
    
def input_guess(guess):
    # main game logic goes here  
    global count
    global secret_number
    guess = float(guess)
    print "\nGuess was", guess
    
    if count:
        count -= 1
        print "Number of remaining guesses is", count
        if secret_number == guess:
            print "Correct"
            new_game()
        elif count != 0 and secret_number > guess:
            print "Higher"
        elif count != 0 and secret_number < guess:
            print "Lower"
        if count == 0:
            print "Out of guesses"
            new_game()

    
# create frame
f = simplegui.create_frame("Guess the Number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range: 0-100", range100, 100)
f.add_button("Range: 0-1000", range1000, 100)
f.add_input("Guess",input_guess, 100)


# call new_game 
new_game()
f.start()
