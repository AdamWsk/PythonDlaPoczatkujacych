musclePain = False
fever = True
weakness = True


#2
if musclePain and fever and weakness:
    print("Suspicion of influenza.")
else:
    print('The flu is unlikely.')

#3
if musclePain and fever and weakness:
    print("Suspicion of influenza.")
elif weakness and not (musclePain or fever):
    print('Just take a rest.')
else:
    print('You might be cold')

#4
isMan = True

#5
if (musclePain and fever and weakness) or (isMan and (fever or musclePain or weakness)):
    print("Suspicion of influenza.")
elif weakness and not (musclePain or fever):
    print('Just take a rest')
else:
    print('You might be cold')

#6
isCheckCompleted = False

print('CHECK IS COMPLETED' if isCheckCompleted else 'CHECK NOT DONE YET')