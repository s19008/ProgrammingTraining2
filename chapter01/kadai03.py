list = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
newtext = list.replace('.', '').replace(',', '')
result = [len(i) for i in newtext.split()]
print(result)
