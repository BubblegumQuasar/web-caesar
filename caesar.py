def alphabet_position(letter):
    lowerAlpha = "abcdefghijklmnopqrstuvwxyz"
    upperAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter.islower():
        cypher = lowerAlpha
    else:
        cypher = upperAlpha
    return cypher.index(letter)

def rotate_character(char, rot):
    lowerAlpha = "abcdefghijklmnopqrstuvwxyz"
    upperAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if not char.isalpha():
        return char

    if char.islower():
        cypher = lowerAlpha
    else:
        cypher = upperAlpha
    newPos = (alphabet_position(char) + rot) % 26
    return cypher[newPos]

def encrypt(text, rot):
    newMess = ""
    for char in text:
        newMess += rotate_character(char, rot)
    return newMess