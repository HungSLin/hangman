import random



def random_word_func(answer,print_answer):
    word=["apple"]
    random_word = word[random.randint(0,len(word)-1)]
    for x in random_word:
        answer.append(x)
        print_answer.append("__ ")
    return (answer,print_answer)

def player_guess():
    guess=input("Guess a letter!")
    if guess in used_letter :
        pass
    else:
        used_letter.append(guess)
    return guess

def guess_judge(guess):
    if (guess in answer):
        print ("You guessed a right letter!")
        for x in range(len(answer)):
            if guess == answer[x]:
                print_answer[x] = guess
            else:
                pass
    elif (guess in print_answer or guess in used_letter):
        print("You have guessed this one already")
    else:
        print("Wrong answer!")
    return

def dis_hangman(tries):
    HANGMAN

#used_letter_function()

#dis_hangman(tries):
#    print (HANGMAN[tries-1])

#win_or_not(answer)



tries=10

answer=[]
print_answer=[]
used_letter=[]

"""
main():
    random_word_func()
    dis_hangman()
    player_guess()
    guess_judge
"""



random_word_func(answer,print_answer)
guess = player_guess()
guess_judge(guess)
print (answer)
print (print_answer)
print (used_letter)
print ("")
