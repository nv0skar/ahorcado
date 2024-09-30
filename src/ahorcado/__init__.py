# Oscar AG - 2024

try: from typing import List, Tuple # For static type checking
except: pass

from words import *

import sys

from enum import Enum, auto
from pathlib import Path

DEF_WORD_PATH = '{}/data/words_tilde.txt'.format(Path.cwd())

TILDE_MAPPING = {
    'á': 'a',
    'é': 'e',
    'í': 'i',
    'ó': 'o',
    'ú': 'u'
}

def normalize_tilde(chars: str | List[str]) -> str | List[str]:
    normalized = []
    for ch in chars: normalized += ch if ch not in TILDE_MAPPING else TILDE_MAPPING[ch]
    if isinstance(chars, str): return ''.join(normalized)
    else: return normalized

def clear():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

class State(Enum):
    DISCOVERED = auto()
    UNDISCOVERED = auto()

class Ahorcado:
    def __init__(self, word: str | None = None):
        '''
        Initialize `Ahorcado` instance
        '''
        self.chars = set()
        if isinstance(word, str): self.word = word
        else:
            words = Words(DEF_WORD_PATH)
            self.word = words.choice()

    def state(self) -> State:
        '''
        Check whether the word has been discovered
        '''
        _discovered = 0
        _normalized_chars = normalize_tilde(self.chars)
        for ch in normalize_tilde(self.word):
            if ch in _normalized_chars: _discovered += 1
        return State.DISCOVERED if _discovered == len(self.word) else State.UNDISCOVERED

    def hidden_word(self) -> List[str]:
        '''
        Compute the hidden word with found characters
        '''
        _hidden = []
        _normalized_chars = normalize_tilde(self.chars)
        for i, ch in enumerate(self.word):
            if normalize_tilde(ch) in _normalized_chars: _hidden.insert(i, ch)
            else: _hidden.insert(i, '_')
        return _hidden
    
    def invalid_words(self) -> List[str]:
        '''
        List of invalid words
        '''
        _chars = list(self.chars)
        for ch in _chars:
            if ch in normalize_tilde(self.word): _chars.remove(ch)
        return _chars

    def attempts(self) -> int:
        '''
        Compute the failed attempts
        '''
        _attempts = 0
        _normalized_word = normalize_tilde(self.word)
        for ch in normalize_tilde(self.chars):
            if ch not in _normalized_word: _attempts += 1
        return _attempts

    def add_char(self, ch: str | None = None) -> Tuple[bool, str]:
        _ch_given = ch is not None
        while True:
            if not _ch_given:
                try:
                    ch = str(input('Introduzca una letra >> ')).lower()
                    clear()
                except:
                    clear()
                    print("La entrada no es válida.")
                    continue
                if len(ch) != 1:
                    clear()
                    print("La entrada debe ser exactamente una letra.")
                    continue
            is_in_word = True if ch in normalize_tilde(self.word) else False
            if ch not in self.chars:
                self.chars.add(ch)
                return (is_in_word, ch)
            elif not _ch_given: continue
            else: raise Exception('Character has been given!')

    def game_loop_cli(self):
        '''
        Enter the game loop in cli mode
        '''
        print(self.word)
        while self.state() is State.UNDISCOVERED and self.attempts() <= 11:
            print('{}'.format(' '.join(self.hidden_word()).upper()))
            print('Intentos {} - Palabras intentadas {} - Intentos restantes {}'.format(self.attempts(), ', '.join(self.invalid_words()), 11 - self.attempts()))
            (is_in_word, _) = self.add_char()
            print('Palabra {}!'.format('descubierta' if is_in_word else 'no válida'))
            for _ in range(3): clear()
        print('{}'.format('Has ganado' if self.attempts() <= 11 else 'Has perdido'))
