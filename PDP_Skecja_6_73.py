#1
MIN_LIKES = 500
MIN_SHARES = 100

num_likes = 69999
num_shares = 1


if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
    print('GREAT! Today our prizes drop 10% !!!')
else:
    if num_likes < MIN_LIKES and num_shares < MIN_SHARES:
        print('We still need more likes and shares to start the promotion')
    else:
        if num_likes < MIN_LIKES:
            print('We still need more likes to start the promotion')
        else:
            print('We still need more shares to start the promotion')

#2
if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
    print('GREAT! Today our prizes drop 10% !!!')
elif num_likes < MIN_LIKES and num_shares < MIN_SHARES:
    print('We still need more likes AND more shares to start the promotion')
elif num_likes < MIN_LIKES:
     print('We still need more likes to start the promotion')
else:
     print('We still need more shares to start the promotion')

#3
isPizzaOrdered = True
isBigDrinkOrdered = True
isWeekend = True

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('Otrzymuejsz kupon na burgera!')
else:
  if isWeekend:
    print('Kupon nie jest dostepny w weekend.')
  else:
      print('You need to order Pizza or Big drink to have a Burger coupon')


#4
if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('Burger for FREE!!!')
elif isWeekend:
    print('Come back on non-Weekend day')
else:
    print('You need to order Pizza or Big drink to have a Burger coupon')