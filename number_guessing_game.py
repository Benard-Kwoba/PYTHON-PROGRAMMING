def guessing_game():
    """3-attempts number-guessing game"""
    from random import randint
    guess_total = 1
    while guess_total < 2:
        try:
            user_input = int(input(f'''							
You have three attempts to guess a random number between 10(inclusive) to 25(inclusive)							
Enter guess: '''))
            correct_guess_0 = randint(10, 25)
            if user_input == correct_guess_0:
                print(f'Correct number is {correct_guess_0}, you have won \U0001F60D')
                break
            else:
                print(f'Wrong guess, correct guess was {correct_guess_0} \U0001F612')
                guess_2 = int(input('Second last chance to win\nEnter guess: '))
                correct_guess_1 = randint(10, 25)
                if guess_2 == correct_guess_1:
                    print(f'Correct number is {correct_guess_1}, you have won \U0001F60D')
                    break
                else:
                    print(f'Incorrect guess, the correct guess was {correct_guess_1} \U0001F612')
                    last_guess = int(input('Last chance \U0001F606\nEnter guess: '))
                    correct_guess_2 = randint(10, 25)
                    if last_guess == correct_guess_2:
                        print(f'Correct number is {correct_guess_2}, you have won \U0001F60D')
                        break
                    else:
                        user_retrial = input(f'''							
Incorrect. Correct number was {correct_guess_2} \U0001F612							
You have exhausted all your attempts. Do you want to replay? \U0001F602							
Press 1 to continue or 0 to exit: 							
''')
                        if user_retrial == str(0):
                            print('Bye...')
                            break
                        elif user_retrial == str(1):
                            guessing_game()
                        else:
                            print('Bye...')
                            break
        except ValueError:
            user_error = input(f"""							
\U0001F61E Oh!!!, do not ruin my game please \U0001F62D.							
Kindly use numbers,							
Press Press 1 to continue or 0 to exit: 							
""")
            if user_error == str(0):
                print('Bye...')
                break
            elif user_error == str(1):
                guessing_game()
            else:
                print('Bye...')
                break
        guess_total += 1


guessing_game()


