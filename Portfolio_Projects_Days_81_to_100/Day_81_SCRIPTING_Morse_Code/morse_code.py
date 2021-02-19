code = {'a':'.-','b': '-...', 'c': '-.-.', 'd': '-..', 'e':'.' ,'f': '..-.', 'g': '--.', 'h':'....',
'i': '..', 'j': '.---', 'k': '-.-','l': '.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.',
's':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..','1':'.----', '2':'..---',
'3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----' }

def convert_word(word):
    code_string = [code[l] for l in word]
    return ' '.join(code_string)

sentence = input("Enter a sentence to encode: ")
print("encoding...")
coded_sentence = [convert_word(w) for w in sentence.lower().split(' ')]


print('|'.join(coded_sentence))