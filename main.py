morse_map = {
    "A":".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "N": "--",
    "O": "-.",
    "P": "---",
    "Q": ".--.",
    "R": "--.-",
    "S": "...",
    "T": "-",
    "U": "..-",
    "v": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": " / "
}

text = input("Enter some text to get equivalent morse code of it: ")

morse_code = ""
for letter in text.upper():
    if letter in morse_map:
        morse_code += morse_map.get(letter)

print(morse_code)