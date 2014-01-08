__author__ = 'spex'

# Import random to have randomized questions
import random

# This function generates a list of questions to a set of parameters
def getQuestions(amount,minimum, maximum):

    # Create an array to put the questions in
    output_questions = []

    # For each question to create
    for index in xrange(amount):
        # Create a tuple to save the question inside of (Just 2 random numbers)
        tmp_tuple = (random.randint(minimum,maximum),random.randint(minimum,maximum))
        # Append the tuple to the list
        output_questions.append(tmp_tuple)

    # Return our list of questions
    return output_questions



# Declare variables and set the default values of them, these are for the user input
amount_of_questions = 'error'
kind_of_questions = 'error'
difficulty = -1
array_of_question_numbers = []

# Print the welcome statement
print "\n=== Welcome to my math quiz! ===\n"

# Repeat asking the user for the quantity of questions they would like to question themselves on
while not(amount_of_questions.isdigit()):
    amount_of_questions = raw_input("How many questions would you like to quiz yourself on?\n>")

# Turn the input string into an integer
amount_of_questions = int(amount_of_questions)

# Make sure the amount is within reasonable boundraies
if(amount_of_questions < 3):
    print "The number you entered is too small, setting the amount to 3"
if(amount_of_questions > 30):
    print "The number you entered is too big, setting amount to 30"


# Create a list of possible kinds of questions the user can be asked
possible_kinds = ['+','-','*','/']

# Let the user choose what kind of question they would like to be asked
while kind_of_questions not in possible_kinds:
    kind_of_questions = raw_input("What kind of questions would you like to quiz yourself on?\n" +\
                                  "Enter +, -, *, or /\n>")


# Ask the user how difficult the quiz should be
while int(difficulty) < 1 or int(difficulty) > 5:
    difficulty = 'error'
    while not(difficulty.isdigit()):
        difficulty = raw_input("On a scale of 1 to 5, how difficult would you like the quiz?\n>")
    difficulty = int(difficulty)

# Now we have the difficulty and the length, we can create the list of answers
array_of_question_numbers = getQuestions(amount_of_questions,difficulty + 1, difficulty * difficulty)


# Let's create these variables to help us get the inputs from the user
total_questions = len(array_of_question_numbers)
array_of_answers = []

# For every question, get the input
for index in range(total_questions):

    # Get the tuple fromt he current part of the list
    tmp_tuple = array_of_question_numbers[index]
    answer = ''

    # Repeat asking until the answer is a digit
    while not(answer.isdigit()):
        answer = raw_input(("Question number %d out of %d:\n" + \
                           "What is %d " + kind_of_questions + " %d?\n" + \
                           ">") % ((index + 1), total_questions, tmp_tuple[0], tmp_tuple[1]))

    # Add the answer to the list of answers
    array_of_answers.append(int(answer))


# Now that we have finished asking the questions from the user, we have to grade the quiz
total_correct = 0
total_incorrect = 0


# Go through every question
for index in range(total_questions):

    # Get the current question's tuple
    tmp_tuple = array_of_question_numbers[index]

    # Create default variables for us to use
    is_correct = ''
    actual_answer = 0

    # Calculate the answers using the correct symbol
    if kind_of_questions == '+':
        actual_answer = tmp_tuple[0] + tmp_tuple[1]
    elif kind_of_questions == '-':
        actual_answer = tmp_tuple[0] - tmp_tuple[1]
    elif kind_of_questions == '*':
        actual_answer = tmp_tuple[0] * tmp_tuple[1]
    else:
        actual_answer = tmp_tuple[0] / float(tmp_tuple[1])


    # Match the actual answer to the user's answer
    if array_of_answers[index] == actual_answer:
        total_correct += 1
        is_correct = "Correct!"
    else:
        total_incorrect += 1
        is_correct = "Incorrect."


    # Output this question's status
    print ("#%d: %d " + kind_of_questions + " %d\nYour Answer: %d\nCorrect Answer: %d\n%s\n") % \
          ((index + 1),tmp_tuple[0],tmp_tuple[1],array_of_answers[index],actual_answer,is_correct)


# Finally, output the overall status of the user's quiz
print "You scored a %d/100 \nYou got %d out of %d correct!" % (((float(total_correct)/total_questions) * 100),total_correct,total_questions)


