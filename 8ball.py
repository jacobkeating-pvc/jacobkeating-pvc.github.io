import random
answers_8_ball = ("As I see it, yes", "Ask again later",
                  "Better not tell you now", 
                  "Cannot predict now", 
                  "Concentrate and ask again",
                  "Don't count on it",
                  "It is certain",
                  "It is decidedly so",
                  "Most likely",
                  "My reply is no",
                  "My sources say no",
                  "Outlook good",
                  "Outlook is not so good",
                  "Reply hazy try again",
                  "Signs point to yes",
                  "Very doubtfull", 
                  "Without a doubt",
                  "Yes", 
                  "Yes definately",
                  "You may rely on it")

def main():

    print("\nI am the MAGIC-8 Ball and I can answer any yes or no question!")
    
    more = True
    while more:
        answer = random.choice(answers_8_ball)

        print("\nShake MAGIC-8 BALL")
        print(" ...and now... ")

        question = input("\nWhat is your YES or NO question?")

        print("The MAGIC-8 BALL says: " + answer)

        askAgain = input("\nWould you like to ask another question? (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain.upper() == "NO": 
            more = False

    print("\nCome back again when you have more questions.")
    print(" ...MAGIC-8 BALL OUT... ")

main()