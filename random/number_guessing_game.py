import random
MAX_TRIES = 4
count = 1

def get_guess():
    guess = int(input('Enter a number between 1 and 10, inclusive: '))
    return guess

def get_number_to_guess():
    random_num = random.randint(1,10)
    return random_num
    
number_to_be_guessed = get_number_to_guess()
guess = get_guess()

print('-'*40)
print('Welcome to the number guessing game')
print('-'*40)

while guess != number_to_be_guessed:
    if count < MAX_TRIES:
        if guess == number_to_be_guessed:
            break
        elif guess > number_to_be_guessed:
            print('You guessed higher')
        else:
            print('You guessed lower')
    else:
        break
        
    count += 1
    guess = get_guess()

if guess == number_to_be_guessed:
    print('You guessed correctly in {} chances'.format(count))
else: 
    print('The correct guess is {} and you took {} chances'.format(number_to_be_guessed, count))
