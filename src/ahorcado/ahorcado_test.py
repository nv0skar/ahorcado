# Oscar AG - 2024

from ahorcado import *

def test_cargar_palabras() -> Words:
    print('Testeando Words.__init__()... ')
    words = Words(DEF_WORD_PATH)
    words.stats()
    return words

def test_elegir_palabra(words: Words):
    print('Testeando Words.choice()... ')
    word = words.choice()
    print('Palabra elegida: {}'.format(word))

def test_enmascarar_palabra(word, chars):
    print(f"Testeando Ahorcado.hidden_word() con la palabra '{word}' y las letras ({','.join(chars)})... ")
    ahorcado = Ahorcado(word)
    ahorcado.chars = chars
    resultado = ahorcado.hidden_word()
    print(f"Palabra enmascarada: {resultado}")
    print()

def test_pedir_letra(chars):
    print(f"Testeando Ahorcado.request_word() con las letras ({','.join(chars)})... ")
    ahorcado = Ahorcado()
    ahorcado.chars = chars
    (_, ch) = ahorcado.add_char()
    print(f"Letra introducida: {ch}")

def test_comprobar_letra(word, ch):
    print(f"Testeando Ahorcado.request_word() con la palabra '{word}' y la letra '{ch}'... ")
    ahorcado = Ahorcado(word)
    (is_in_word, _) = ahorcado.add_char(ch)
    print(f"Resultado: {'Acierto' if is_in_word else 'Fallo'}")

def test_compobar_palabra_completa(word, chars):
    print(f"Testeando Ahorcado.state() con la palabra '{word}' y las letras ({','.join(chars)})... ")
    ahorcado = Ahorcado(word)
    ahorcado.chars = chars
    state = ahorcado.state()
    print(f"Resultado: {'Completa' if state == State.DISCOVERED else 'Incompleta'}")

def test_ejecutar_turno(word, chars):
    print(f"Testeando Ahorcado.add_char() con la palabra '{word}' y las letras ({','.join(chars)})... ")
    ahorcado = Ahorcado(word)
    ahorcado.chars = chars
    (is_in_word, _) = ahorcado.add_char()
    print(f"Resultado: {'Acierto' if is_in_word else 'Fallo'}")

if __name__ == "__main__":
    words = test_cargar_palabras()
    test_elegir_palabra(words)
    test_enmascarar_palabra('python', {})
    test_enmascarar_palabra('python', {'p', 'y', 't', 'h', 'o', 'n'})
    test_enmascarar_palabra('python', {'a', 'b', 'c', 'd', 'e'})
    test_enmascarar_palabra('python', {'a', 'e', 'i', 'o', 'u'})
    test_pedir_letra({'a', 'b', 'c'})
    test_comprobar_letra('python', 'p')
    test_comprobar_letra('python', 'a')
    test_compobar_palabra_completa('python', {'p', 'y', 't', 'h', 'o', 'n'})
    test_compobar_palabra_completa('python', {'a', 'b', 'c', 'd', 'e'})
    test_compobar_palabra_completa('python', {})
    test_ejecutar_turno('python', {'a', 'b', 'c', 'd', 'e'})
    test_ejecutar_turno('python', {'p', 'y', 't', 'h', 'o'})