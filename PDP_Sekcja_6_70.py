#1
MIN_LIKES = 500
MIN_SHARES = 100

num_likes = 499
num_shares = 111

prices = 100

if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
    prices = prices * 0.9
    print('Ceny spadają o 10%')
else:
    print("Ceny pozostaja bez zmian, za mało like'ów i share'ów")

#2
isPizzaOrdered = True
isBigDrinkOrdered = True
isWeekend = True

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('Otrzymuejsz kupon na burgera!')
else:
    print('Nie otrzymujesz kuponu.')

#3
diskSize = 50
diskSizeUsed = 30
fileSize = 30

if diskSizeUsed + fileSize <= diskSize:
    print("File can be downloaded.")
else :
    print("File cannot be downloaded, not enough space od disc.")


