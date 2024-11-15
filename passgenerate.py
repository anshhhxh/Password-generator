import random
import string as st
def pass_generate(min_length,numbers=True,special_characters=True):
    letters=st.ascii_letters
    digits=st.digits
    special=st.punctuation
    character=letters
    if numbers:
        character+=digits
    if special_characters:
        character+=special
    pwrd=""    
    meet_criteria=False
    has_num=False
    has_special=False
    while not meet_criteria or len(pwrd)<min_length:
        new_char=random.choice(character)
        pwrd+=new_char
        if new_char in digits:
            has_num=True
        elif new_char in special:
            has_special=True
        meet_criteria=True
        if numbers:
            meet_criteria=has_num
        if special_characters:
            meet_criteria= meet_criteria and has_special
    return pwrd


print("Include numbers and special characters:  ",pass_generate(8))

print("Include special characters:  ",pass_generate(8,False))

print("Include numbers :  ",pass_generate(8,True,False))

print("Doesn't include numbers and special characters:  ",pass_generate(8,False,False))

