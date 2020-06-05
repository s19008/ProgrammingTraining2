def extWord(i, word):
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        return (word[0], i)
    else:
        return (word[:2], i)

Text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also sign Peace Security Clause. Arthur King Can.'

newtext = Text.replace('.','').replace(',','')

result = [extWord(i, w) for i, w in enumerate(newtext.split(), 1)]

print(dict(result))
