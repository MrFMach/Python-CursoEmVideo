phrase = "The python language is awesome"
print(phrase)
print(phrase[7:15])
print(phrase[6:22:2])
print(phrase[:15])
print(phrase[20:])

print('awesome' in phrase)
print(len(phrase))

print(phrase.count('e'))
print(phrase.find('language'))
print(phrase.find('Language'))
print(phrase.replace('python', 'Raku'))
print(phrase.title())
print(phrase.upper())

splitPhrase = phrase.split()
print(splitPhrase)
print(splitPhrase[4] [1])

phrase = phrase.replace('python', 'C++')
print(phrase)

print("""\nPython is a programming language 
that lets you work quickly 
and integrate systems more 
effectively.""")
