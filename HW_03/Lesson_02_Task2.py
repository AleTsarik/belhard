# Код Морзе для представления цифр и букв использует тире и точки. Напишите
# функцию для кодирования текстового сообщения в соответствии с кодом Морзе.


morze_table = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
}


def morze(text1: str):
    s1 = ''.join(c for c in text1 if c.isalnum())
    input_text = list(s1.upper())
    # input_text = list(text.replace(' ', '').upper())
    morze_text = []
    for i in input_text:
        morze_text.append(morze_table[i])
    return morze_text


text = str(input('Enter text to encode: '))
print(morze(text))
