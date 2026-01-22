import random

print(' choose your pokemon')
print ( ' charmendar type [fire]')
print (' squirtle type [water]')
print (' bulbasaur type [grass]')



you = int(input('enter your choice '))


pokemon = {
    1:1, #fire
    2:0 ,#water
    3:-1 # grass
}


pokemon_name={ 
    1:'charmendar',
    2:'squirtle',
    3:'bulbasaur'

}

computer = random.choice([1,2,3])

you_type = pokemon[you]
computer_type = pokemon[computer]

print(f'you choose {pokemon_name[you]}')
print(f'computer choose {pokemon_name[computer]}')


if you_type == computer_type:
    print('the battle is draw ')


else:
    
    if you_type == 1 and computer_type == -1:
        print('you won the battle ,,/fire beats grass')
    elif you_type == 0 and computer_type ==1:
        print('you wonthe battle computer ')
    

    elif you_type == -1 and computer_type == 0:
        print('you won the battle')

    else:
        print('you lost')

    



