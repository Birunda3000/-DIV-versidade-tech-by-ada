import random
import os

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def return_body(n):
    if n == 0:
        return """
        |-------
        |      |
        |    
        |    
        |    
        |     
        |     
        |______ 
        """
    if n == 1:
        return """
        |-------
        |      |
        |      _
        |     |_|
        |      
        |     
        |     
        |______ 
        """
    if n == 2:
        return ("""
        |-------
        |      |
        |      _
        |     |_|
        |      |
        |      |
        |     
        |______ 
        """)
    if n == 3:
        return ("""
        |-------
        |      |
        |      _
        |     |_|
        |    --|
        |      |
        |     
        |______ 
        """)
    if n == 4:
        return ("""
        |-------
        |      |
        |      _
        |     |_|
        |    --|--
        |      |
        |     
        |______ 
        """)
    if n == 5:
        return ("""
        |-------
        |      |
        |      _
        |     |_|
        |    --|--
        |      |
        |     / 
        |______ 
        """)
    if n == 6:
        return ("""
        |-------
        |      |
        |      _
        |     |_|
        |    --|--
        |      |
        |     / \\
        |______ 
        """)

class DB:
    def __init__(self):
        self.data = []
    def load_data (self, arq_name : str ='frutas.txt') -> None:
        self.data = []
        try:
            with open(arq_name, 'r') as arq:
                for line in arq:
                    self.data.append(line.strip())
        except FileNotFoundError:
            print('File not found')

    def show_data (self) -> None:
        for i in self.data:
            print(i)
    
    def choose_random (self) -> str:
        return random.choice(self.data)

class Game:
    def __init__(self, DB):
        self.db = DB
        self.db.load_data()
        self.word = ''
        self.word_len = 0
        self.wrong_letters = []
        self.right_letters = []
        self.word_show = []
        self.game_over = False
    
    def start (self) -> None:
        self.word = self.db.choose_random()
        self.word = self.word.upper()
        self.word_len = len(self.word)
        self.word_show = ['_' for i in range(self.word_len)]
        self.wrong_letters = []
        self.right_letters = []      
        self.game_over = False

    def guess (self) -> None:
        while True:
            letter = input('Choose a letter: ').upper()
            if letter in self.right_letters or letter in self.wrong_letters:
                print('You already choose this letter')
            else:
                break
        if letter in self.word:
            self.right_letters.append(letter)
            for i in range(self.word_len):
                if self.word[i] == letter:
                    self.word_show[i] = letter
        else:
            self.wrong_letters.append(letter)
        self.check(letter)

    def check (self, letter) -> None:
        clean_screen()
        if self.word_show == list(self.word):
            self.show()
            print('You win!')
            self.game_over = True
        elif len(self.wrong_letters) >= 6:
            self.show()
            print('\n--',self.word,'--\n')
            print('You lose!')
            self.game_over = True
    
    def show (self) -> None:
        print('Word: ', end='')
        for i in self.word_show:
            print(i, end=' ')
        print()
        print('Wrong letters: ', end='')
        for i in self.wrong_letters:
            print(i, end=' ')
        print(return_body(len(self.wrong_letters)))

    def play (self) -> None:
        self.start()
        self.word_show = ['_' for i in range(self.word_len)]
        while not self.game_over:
            self.show()
            self.guess()

if __name__ == '__main__':
    game = Game(DB())
    while True:
        game.play()
        if input('Play again? (y/n) ') == 'n':
            break
        clean_screen()

