print('\n**********Phone Book******')
print('\nPress 1 for  See a phonebook list.')
print('Press 2 for  add a new person in phonebook list.')
print('Press 3 update or edit any existing person in the phonebook.')
print('Press 4 Delete person in the phonebook.')
print('Press 5 Searching for person in the phonebook.')
print('Press 6 Storing for person in the phonebook.')
print('Press quit For exit.')
# while True:
P_book = {}
Insert_book = {}
P1book = {'Name': 'Sakline', 'Address': 'Dhaka', 'Email': 'Sakline51@gmail.com', 'Phone_Number': '01748164525'}
P2book = {'Name': 'Heemel', 'Address': 'Pabna', 'Email': 'heemel51@gmail.com', 'Phone_Number': '01748164525'}
P3book = {'Name': 'Shuvo', 'Address': 'Pabna', 'Email': 'shuvo51@gmail.com', 'Phone_Number': '01748164525'}
P4book = {'Name': 'Munim', 'Address': 'Barishal', 'Email': 'munim51@gmail.com', 'Phone_Number': '01748164525'}
P5book = {'Name': 'Jihad', 'Address': 'Pabna', 'Email': 'jihad@gmail.com', 'Phone_Number': '01748164525'}
P_book = [P1book, P2book, P3book, P4book, P5book]
choice = input('Enter your choice:')

if choice == '1':
 def see_phonebook_list():
    for i in P_book:
        print(i)


 with open('P_book.txt', 'w') as f:
     for item in P_book:
      f.write("%s\n" % item)
 see_phonebook_list()


elif choice == '2':
 def add_a_new_person():
    size = int(input("Add a person and press1: "))
    if size==1:
        Name = input("Name: ")
        Address = input("Address: ")
        Email = input("Email: ")
        Phone_number = input("Phone_number: ")

        Insert_book["Name"] = Name
        Insert_book["Address"] = Address
        Insert_book["Email"] = Email
        Insert_book["Phone_Number"] = Phone_number
    print('\n ******Your Current Phone book is*****')
    P_book.append(Insert_book)
    for list in P_book:
     print(list)

    with open('P_book.txt', 'w') as f:
        for item in P_book:
            f.write("%s\n" % item)
 add_a_new_person()

elif choice == '3':
 def update_or_edit():
    print('\n First person Update:Press 1.\n Second person Update:Press 2.\n Third person Update:Press 3.\n Fourth person Update:Press 4.\n Fifth person Update:Press 5.')
    select = input('Press:')
    if select == '1':

        print('\nWhich you want to update:\n***Name choose for 1***\n***Address choose for 2***\n***Email choose for 3***\n***Phone_number choose for 4***')
        choose = input('Enter your choice:')
        if choose == '1':
            x = input('Name:')
            if (x != ''):
                P1book['Name'] = x
            for k in P_book:
                print(k)

        if choose == '2':
            x = input('Address:')
            if (x != ''):
                P1book['Address'] = x
            for k in P_book:
                print(k)

        if choose == '3':
            x = input('Email:')
            if (x != ''):
                P1book['Email'] = x
            for k in P_book:
                print(k)

        if choose == '4':
            x = input('Phone_number:')
            if (x != ''):
                P1book['Phone_number'] = x
            for k in P_book:
                print(k)

    elif select == '2':

        print('\nWhich you want to update:\n***Name choose for 1***\n***Address choose for 2***\n***Email choose for 3***\n***Phone_number choose for 4***')
        choose = input('Enter your choice:')
        if choose == '1':
            x = input('Name:')
            if (x != ''):
                P2book['Name'] = x
            for k in P_book:
                print(k)

        if choose == '2':
            x = input('Address:')
            if (x != ''):
                P2book['Address'] = x
            for k in P_book:
                print(k)

        if choose == '3':
            x = input('Email:')
            if (x != ''):
                P2book['Email'] = x
            for k in P_book:
                print(k)

        if choose == '4':
            x = input('Phone_number:')
            if (x != ''):
                P2book['Phone_number'] = x
            for k in P_book:
                print(k)

    elif select == '3':

        print('\nWhich you want to update:\n***Name choose for 1***\n***Address choose for 2***\n***Email choose for 3***\n***Phone_number choose for 4***')
        choose = input('Enter your choice:')
        if choose == '1':
            x = input('Name:')
            if (x != ''):
                P3book['Name'] = x
            for k in P_book:
                print(k)

        if choose == '2':
            x = input('Address:')
            if (x != ''):
                P3book['Address'] = x
            for k in P_book:
                print(k)

        if choose == '3':
            x = input('Email:')
            if (x != ''):
                P3book['Email'] = x
            for k in P_book:
                print(k)

        if choose == '4':
            x = input('Phone_number:')
            if (x != ''):
                P3book['Phone_number'] = x
            for k in P_book:
                print(k)

    elif select == '4':

        print('\nWhich you want to update:\n***Name choose for 1***\n***Address choose for 2***\n***Email choose for 3***\n***Phone_number choose for 4***')
        choose = input('Enter your choice:')
        if choose == '1':
            x = input('Name:')
            if (x != ''):
                P4book['Name'] = x
            for k in P_book:
                print(k)

        if choose == '2':
            x = input('Address:')
            if (x != ''):
                P4book['Address'] = x
            for k in P_book:
                print(k)

        if choose == '3':
            x = input('Email:')
            if (x != ''):
                P4book['Email'] = x
            for k in P_book:
                print(k)

        if choose == '4':
            x = input('Phone_number:')
            if (x != ''):
                P4book['Phone_number'] = x
            for k in P_book:
                print(k)

    elif select == '5':

        print('\nWhich you want to update:\n***Name choose for 1***\n***Address choose for 2***\n***Email choose for 3***\n***Phone_number choose for 4***')
        choose = input('Enter your choice:')
        if choose == '1':
            x = input('Name:')
            if (x != ''):
                P5book['Name'] = x
            for k in P_book:
                print(k)

        if choose == '2':
            x = input('Address:')
            if (x != ''):
                P5book['Address'] = x
            for k in P_book:
                print(k)

        if choose == '3':
            x = input('Email:')
            if (x != ''):
                P5book['Email'] = x
            for k in P_book:
                print(k)

        if choose == '4':
            x = input('Phone_number:')
            if (x != ''):
                P5book['Phone_number'] = x
            for k in P_book:
                print(k)

 update_or_edit()

elif choice == '4':
 def delete():
     for index in range(len(P_book)):
         x = input('Delete name:')
         if P_book[index]["Name"] == x:
             del P_book[index]
             print("After delete phpnebook is:")
             for i in P_book:
              print(i)
 delete()

elif choice == '5':
 def search():
  try:
    a = input('Enter the search of the itme:')
    result = next(z for z in P_book
                  if z["Name"] == a or z["Address"] == a or z["Email"] == a or z["Phone_Number"] == a)
    print(result)

  except:
    print('Not Found')
    pass
    print('If you add a person press 1 or exit press quit')
    x=input("\nPress:")
    #for j in range(x):
    if x == '1':
        Name = input("Name: ")
        Address = input("Address: ")
        Email = input("Email: ")
        Phone_number = input("Phone_number: ")

        Insert_book["Name"] = Name
        Insert_book["Address"] = Address
        Insert_book["Email"] = Email
        Insert_book["Phone_Number"] = Phone_number
        print('\n ******Insert Successfull*****')
        print(Insert_book)
    else:
      print('____Exit____')
 search()

elif choice == '6':
 def store():
     with open('P_book.txt', 'r') as f:
      contents=f.read()
     print(contents)
 store()

elif choice == 'quit':
 def exit():
  print('_____Exit_____')

 exit()