import random

num_of_friends = int(input('Enter the number of friends joining (including you):\n'))
friends = {}

if num_of_friends < 1:
    print('No one is joining for the party')
else:
    print('\nEnter the name of every friend (including you), each on a new line:')
    for _ in range(num_of_friends):
        name = input()
        friends[name]=0
    print("\nEnter the total bill value:")
    bill_amount = float(input())
    bill_split = bill_amount / len(friends)
    for key in friends:
        friends.update({key: round(bill_split,2)})
    print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
    decision = input()
    if decision in ['Yes', 'y', 'yes', 'yeah', 'Y']:
        rand_friend = random.choice(list(friends))
        print('\n'+rand_friend + ' is the lucky one!\n')
        bill_split = bill_amount / (len(friends)-1)
        for key in friends:
            if key != rand_friend:
                friends.update({key: round(bill_split,2)})
            else:
                friends.update({key: 0})
        print(friends)
    else:
        print('No one is going to be lucky')
        print(friends)
