# 9. Basic Quiz App

# Basic Quiz App using dictionaries + scoring.
# Features
# Questions stored in a dictionary
# Loops through questions
# Takes user input
# Keeps score
# Shows final result

quiz = {
    "What is the capital of India?": "Delhi",
    "Which language is used for Data Analysis?": "Python",
    "What is 5 + 7?": "12",
    "Who developed Python?": "Guido van Rossum"
}

score = 0
total_questions = len(quiz)

print("Welcome to the Quiz App!")
print("--------------------------")

# Loop through dictionary
for question, answer in quiz.items():
    user_answer = input(question + " ")

    # Case insensitive check
    if user_answer.strip().lower() == answer.lower():
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!")
        print("Correct answer is:", answer, "\n")

# Final Result
print("--------------------------")
print("Quiz Finished!")
print("Your Score:", score, "/", total_questions)

percentage = (score / total_questions) * 100
print("Percentage:", percentage, "%")
