# Oscar AG - 2024

import random

class Words:
    def __init__(self, path: str):
        '''
        Initialize words from path
        '''
        self.words = []
        with open(path, encoding='utf-8') as handle:
            for i in handle:
                self.words.append(i.strip())
    
    def stats(self):
        '''
        Show stats of loaded words
        '''
        print('{} words were loaded.\nFirst 3 are: {}\nLast 3 are: {}'.format(len(self.words), self.words[:3], self.words[-3::]))

    def choice(self) -> str:
        '''
        Compute a random word
        '''
        return str(random.choice(self.words)).lower()
