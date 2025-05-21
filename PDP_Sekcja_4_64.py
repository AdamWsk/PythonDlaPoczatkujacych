#Tuple
#nawiasy zwykłe, brak możliwoscci insert, append, revert, sort
#tuple można zrobić konwersję na listę i w druga stronę też.

marketing=['loyality program','client promotion','market research']
print(marketing)
marketing.append('public relations')
print(marketing)
print(marketing[3])
marketing.insert(2,'investor relations')
print(marketing)
emailMarketing = marketing.copy()
print(emailMarketing)
emailMarketing.sort()
print(emailMarketing)
internalEmails = ['internal comunication']
emailMarketing.extend(internalEmails)
print(emailMarketing)
emailTuple = tuple(emailMarketing)
print(emailTuple)



