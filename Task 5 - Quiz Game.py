import random
repeat=input("Do you want to play (y/n):-")
questions = [
    {
        'text': 'Python is a high-level __________ language.',
        'options': ['Markup', 'Programming', 'Scripting', 'Query'],
        'answer': 2,
    },
    {
        'text': 'Who developed Python Programming Language.',
        'options': ['Wick van Rossum', 'Guido van Rossum', 'Niene Strom', 'Rasmus Lerdorf'],
        'answer': 2,
    },
    {
        'text': 'Which type of programming does python support.',
        'options': ['structured programming', 'Funtional programming', 'Object-oriented programming', 'all of the above'],
        'answer': 4,
    },
    {
        'text': 'Is Python case sensitive when dealing with identifiers.',
        'options': ['Yes', 'No', 'machine dependent', 'none of the above'],
        'answer': 1,
    },
    {
        'text': 'Which of the following is the correct extension of python file.',
        'options': ['.python', '.pl', '.py', '.p'],
        'answer': 3,
    },
]

while repeat in "Yy":
    print("Welcome to Python Quiz Game.")
    print("You will be asked",len(questions),"question related to python.")
    print("And for each question there are four options.")
    print("You have to give the option number of the option which you think is correct.")
    print("For each correct answer you will be given 1 point and there is no negative marking.")
    print("---------------------------------------------------------------------------------------")
    random.shuffle(questions)
    score=0
    count=1
    for question in questions:
        print("Q.",count,question['text'])
        for i in range(1,5):
            print(i,question['options'][i-1])
        try:
            ans=int(input("Enter correct option :- "))
        except ValueError:
            print("--------------------------------------------------------")
            print("ERROR : Enter option number to give answer")
            print("--------------------------------------------------------")
            continue
        if ans==question['answer']:
            print("--------------------------------------------------------")
            print("Yes it is the correct answer.")
            score +=1
        else:
            print("--------------------------------------------------------")
            print("No, the correct answer is option",question['answer'],question['options'][question['answer']-1])
        print("--------------------------------------------------------")
        count +=1
    print("Your Final Score is",score)
    repeat=input("Do you want ot play again(y/n):-")
    