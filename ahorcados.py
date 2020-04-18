import random
from os import system
system("cls")

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado','humanidad'
,'humano',
'persona',
'gente',
'hombre',
'mujer'
]

CLUES = [
  'Limpiar productos',
  'Secar productos',
  'Recostarse',
  'Ente controlador',
  'Representante de personas',
  'Tipo de gobierno',
  'Electrodomestico',
  'Accesorio de Electrodomestico',
  'Conjunto de seres',
  'Ser',
  'Ser vivo',
  'Agrupacion de humanos',
  'sexo',
  'sexo'
]

def random_word():
  idx = random.randint(0,len(WORDS) - 1)
  return idx

def run():
  num_word = random_word() 
  word = WORDS[num_word]
  hidden_word = ['-'] * len(word)
  tries = 0
  letter_indexes = []
  run=0
  while True:
    if(run==0):
      system("cls")
      clue=activate_clues()
    if(tries==7):
      display_board(hidden_word, tries)
      input("Perdiste,la palabra era " +word+"!")
      tries = 0
      run = 0
      letter_indexes = []
      num_word = random_word() 
      word = WORDS[num_word] 
      hidden_word = ['-'] * len(word)
    else:
      if(len(letter_indexes) == len(word)):
        display_board(hidden_word, tries)
        input("Felicitaciones la palabra era " +word+"!")
        tries = 0
        run = 0
        letter_indexes = []
        num_word = random_word() 
        word = WORDS[num_word]
        hidden_word = ['-'] * len(word)
      else:

        display_board(hidden_word, tries)
        if(clue==1):
         print("La pista es:'"+CLUES[num_word]+"'")
        current_letter = str(input('Escoge una letra: '))
        run +=1
        check = check_letter(current_letter,word)
        if(check == 1):
          for i in range(len(word)):
            if(current_letter==word[i]):
              letter_indexes.append(i)
              hidden_word[i] = current_letter

        else:
          tries += 1

    pass

def check_letter(letter,word):
  for i in range(len(word)):
    if(word[i]==letter):
      return 1
  
  return 0

def activate_clues():
  active = input("Deseas utilizar pistas? (si/no): ")
  a = 0
  if(active == "si"):
    a = 1
    
  return a


def display_board(hidden_word, tries):
  system("cls")
  print(IMAGES[tries])
  print('')
  print(hidden_word)
  print('-------------------------------------------------------------------------')


if __name__ == '__main__':
  print('Bienvenidos a "A H O R C A D O S"')
  run()