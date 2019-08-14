import random 

states = [
{
    "name": "Alabama",
    "capital": "Montgomery"
}, {
    "name": "Alaska",
    "capital": "Juneau"
}, {
    "name": "Arizona",
    "capital": "Phoenix"
}, {
    "name": "Arkansas",
    "capital": "Little Rock"
}, {
    "name": "California",
    "capital": "Sacramento"
}, {
    "name": "Colorado",
    "capital": "Denver"
}, {
    "name": "Connecticut",
    "capital": "Hartford"
}, {
    "name": "Delaware",
    "capital": "Dover"
}, {
    "name": "Florida",
    "capital": "Tallahassee"
}, {
    "name": "Georgia",
    "capital": "Atlanta"
}, {
    "name": "Hawaii",
    "capital": "Honolulu"
}, {
    "name": "Idaho",
    "capital": "Boise"
}, {
    "name": "Illinois",
    "capital": "Springfield"
}, {
    "name": "Indiana",
    "capital": "Indianapolis"
}, {
    "name": "Iowa",
    "capital": "Des Moines"
}, {
    "name": "Kansas",
    "capital": "Topeka"
}, {
    "name": "Kentucky",
    "capital": "Frankfort"
}, {
    "name": "Louisiana",
    "capital": "Baton Rouge"
}, {
    "name": "Maine",
    "capital": "Augusta"
}, {
    "name": "Maryland",
    "capital": "Annapolis"
}, {
    "name": "Massachusetts",
    "capital": "Boston"
}, {
    "name": "Michigan",
    "capital": "Lansing"
}, {
    "name": "Minnesota",
    "capital": "St. Paul"
}, {
    "name": "Mississippi",
    "capital": "Jackson"
}, {
    "name": "Missouri",
    "capital": "Jefferson City"
}, {
    "name": "Montana",
    "capital": "Helena"
}, {
    "name": "Nebraska",
    "capital": "Lincoln"
}, {
    "name": "Nevada",
    "capital": "Carson City"
}, {
    "name": "New Hampshire",
    "capital": "Concord"
}, {
    "name": "New Jersey",
    "capital": "Trenton"
}, {
    "name": "New Mexico",
    "capital": "Santa Fe"
}, {
    "name": "New York",
    "capital": "Albany"
}, {
    "name": "North Carolina",
    "capital": "Raleigh"
}, {
    "name": "North Dakota",
    "capital": "Bismarck"
}, {
    "name": "Ohio",
    "capital": "Columbus"
}, {
    "name": "Oklahoma",
    "capital": "Oklahoma City"
}, {
    "name": "Oregon",
    "capital": "Salem"
}, {
    "name": "Pennsylvania",
    "capital": "Harrisburg"
}, {
    "name": "Rhode Island",
    "capital": "Providence"
}, {
    "name": "South Carolina",
    "capital": "Columbia"
}, {
    "name": "South Dakota",
    "capital": "Pierre"
}, {
    "name": "Tennessee",
    "capital": "Nashville"
}, {
    "name": "Texas",
    "capital": "Austin"
}, {
    "name": "Utah",
    "capital": "Salt Lake City"
}, {
    "name": "Vermont",
    "capital": "Montpelier"
}, {
    "name": "Virginia",
    "capital": "Richmond"
}, {
    "name": "Washington",
    "capital": "Olympia"
}, {
    "name": "West Virginia",
    "capital": "Charleston"
}, {
    "name": "Wisconsin",
    "capital": "Madison"
}, {
    "name": "Wyoming",
    "capital": "Cheyenne"
}]


# this is the player object
playerStats = {
    'correctGuesses': 0,
    'incorrectGuesses': 0,
    'turns': 0,
    'name': ''
} 
# this is the start of the game where user input is gathered
print("  ")
print("Welcome to the US State Capitals Game! Keep in mind that every 8th grader in America knows this...")
print("  ")
print("Enter your name:")
print("  ")
name = input()
print(" ")
print("Hello, " + name)
playerStats['name'] = name
random.shuffle(states)

# this is the game function
def function_game():
    for i in range(0, 50):
        print(" ")
        print("What is the capital of " + states[i]['name'] + "?")
        response = input().title()
        if response == states[i]['capital']:
            print("good job, you're a genius!")
            print("  ")
            playerStats['correctGuesses'] += 1
            playerStats['turns'] += 1
            print("Correct Guesses: ", + playerStats['correctGuesses']) 
            print("Incorrect Guesses: ", + playerStats['incorrectGuesses']) 
            print("Remaining Turns ", (playerStats['turns'] - 50) * -1)
        elif response != states[i]['capital']:
            print("Wrong! you suck at this game!")
            playerStats['incorrectGuesses'] += 1
            playerStats['turns'] += 1
            print("Correct Guesses: ", + playerStats['correctGuesses']) 
            print("Incorrect Guesses: ", + playerStats['incorrectGuesses']) 
            print("Remaining Turns ", (playerStats['turns'] - 50) * -1)
            
# Running the game
function_game()

# Ending the game + asking to play again
print(" ")
print("Well " + playerStats['name'] + ", it is over.")
print(" ")
if playerStats['incorrectGuesses'] > 40:
    print("you are really bad at this... you should probably find an eigth grader to tutor your dumb ass...")
print(" ")
print("FINAL SCORE")
print("Correct Guesses: ", + playerStats['correctGuesses']) 
print("Incorrect Guesses: ", + playerStats['incorrectGuesses']) 
print(" ")
print("would you like to play again? (Y/N")
gameStatus = input().title()
if gameStatus == 'Y':
    random.shuffle(states)
    playerStats['correctGuesses'] = 0
    playerStats['incorrectGuesses'] = 0
    playerStats['turns'] = 0
    function_game()



