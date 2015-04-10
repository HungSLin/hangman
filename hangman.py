import random

HANGMAN=[
#0
    """








       ───""",
#1
    """
        ┌
        │       
        │      
        │      
        │      
        │      
        │      
        │      
        │      
        │
       ─┴─""",
#2
    """
        ┌───────
        │       
        │      
        │      
        │      
        │      
        │       
        │      
        │      
        │
       ─┴─""",
#3
    """
        ┌───────┐
        │       │
        │      
        │      
        │      
        │      
        │       
        │      
        │      
        │
       ─┴─""",
#4
    """
        ┌───────┐
        │       │
        │      ┌┴┐
        │      │ │
        │      └┬┘
        │      
        │   
        │      
        │      
        │
       ─┴─""",
#5
    """
        ┌───────┐
        │       │
        │      ┌┴┐
        │      │ │
        │      └┬┘
        │      ─┤
        │       
        │      
        │      
        │
       ─┴─""",
#6
    """
        ┌───────┐
        │       │
        │      ┌┴┐
        │      │ │
        │      └┬┘
        │      ─┼─
        │       
        │      
        │      
        │
       ─┴─""",
#7
    """
        ┌───────┐
        │       │
        │      ┌┴┐
        │      │ │
        │      └┬┘
        │      ─┼─
        │       │
        │      
        │      
        │
       ─┴─""",
#8
    """
        ┌───────┐
        │       │
        │      ┌┴┐
        │      │ │
        │      └┬┘
        │      ─┼─
        │       │
        │      ┌┘
        │      │
        │
       ─┴─""",
#9
    """
        ┌───────┐
        │       │
        │      ┌┴┐
        │      │ │
        │      └┬┘
        │      ─┼─
        │       │
        │      ┌┴┐
        │      │ │
        │
       ─┴─"""
]


def random_word_func(answer,print_answer):
    word=["apple"]
    random_word = word[random.randint(0,len(word)-1)]
    for x in random_word:
        answer.append(x)
        print_answer.append("__")
    return (answer,print_answer)

def player_guess():
    guess=input("Guess a letter!")
    return guess

def guess_judge(guess,print_hangman):
    print_hangman +=1
    if (guess in answer):
        print ("You guess a right letter!")
        print_hangman -= 1
        for x in range(len(answer)):
            if guess == answer[x]:
                print_answer[x] = guess
            else:
                pass
    elif (guess in used_letter):
        print("You have guessed this one already")
    else:
        print("Wrong answer!")
        used_letter.append(guess)
    return print_hangman

def dis_hangman(print_hangman):
    print(HANGMAN[print_hangman])
    return
def dis_print_answer(print_answer):
    dis = ""
    for i in print_answer:
        dis += i
        dis += " "
    return dis

answer=[]
print_answer=[]
used_letter=[]


def main():
    print_hangman = 0
    tries =0
    random_word_func(answer,print_answer)
    while tries<=9:
        guess = player_guess()
        print_hangman = guess_judge(guess,print_hangman)
        print ("Ans:"+dis_print_answer(print_answer))
        dis_hangman(print_hangman)
        print ("Used letter :"+ str(used_letter))
        print ("turn " + str(tries))
        tries += 1
        print ()
        if print_answer == answer:
            print ("You win")
            break
        else:
            if tries == 9:
                print("You ran out of turns")
                break
            else:
                pass

main()
        

