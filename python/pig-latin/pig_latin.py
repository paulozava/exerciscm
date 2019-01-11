#### unfinished

def translate(text):
    new_text = [word if(word in '!?.;') else word[1:] + word[0] + 'ay' for word in text.split()]
    return ' '.join(new_text)