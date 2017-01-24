"""Write a code that will take (AnyString) and substitute all vowels with
character's like $#%^&* etc..... but DO NOT USE ' or " as any of your characters."""
def novowel(AnyString):
    phrase = ""
    for ch in AnyString:
        if ch == 'a' or ch  == 'A':
            phrase =  phrase + '@'
        elif ch == 'e' or ch == 'E':
            phrase = phrase + '('
        elif ch == 'i' or ch == 'I':
            phrase = phrase + '!'
        elif ch == 'o' or ch == 'O':
            phrase = phrase + "*"
        elif ch == 'u' or ch == 'U':
            phrase = phrase + "^"
        else:
            phrase = phrase + ch
    return phrase
print(novowel('sequioa'))
