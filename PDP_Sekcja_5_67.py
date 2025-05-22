
#1
chanels = {'Google': 1480, 'Email': 300, 'Natural Traffic': 440, 'TV Spot': 700}

#2
print(chanels['Email'])

#3
chanelsUpdate = { 'Natural Traffic' : 520, 'News' : 600}

#4
chanels.update(chanelsUpdate)
print(chanels)
#5
print(chanels.keys())

#6
chanels.pop('Email')
print(chanels)

