print('\n**********Dictionary******')
print('\n')
print('Press 1 for  add a new new_keyword in dictionary.')
print('Press 2 update an existing keyword in the dictionary.')
print('Press 3 Delete a keyword from the dictionary.')
print('Press 4  display all the keyword in the dictionary.')
print('Press 5  Search keyword in the dictionary.')
print('Press 6  See storing keyword in the dictionary.')
print('Press quit  Exit from the dictionary.')
# while True:
#P_book = {}
#Insert_book = {}
P1book = {'Keyword1': 'Research', 'Description1':'They are carrying out/conducting/.','Keyword2': 'Hard',
          'Description2':'Difficult/Hard.','Keyword3': 'Trap','Description3':'Snare'}


print('\n')
choice=input('Enter your choice:')



if choice == '1':
 def add_a_new_keyword():
    size = int(input("Add a new keyword press 1: "))
    if size==1:
     Keyword4 = input("Keyword4:")
     Description4 = input("Description4:")


     P1book["\nKeyword4"] = Keyword4
     P1book["Description4"] = Description4
    for key, value in P1book.items():
        print(key.title(), ' : ', value.title())


    with open('Dictionary.txt', 'w') as f:
           for key,value in P1book.items():
               f.write("%s\n" % key)
               f.write("%s\n" % value)
 add_a_new_keyword()


elif choice == '2':
 def update():
    print('1st keword update press 1:')
    print('2nd keword update press 2:')
    print('3rd keword update press 3:')
    x=input('press:')
    if x=='1':
      x = input("Enter the keyword:")
      P2book = {'Keyword1':x}

      P1book.update(P2book)

      for key, value in P1book.items():
        print(key.title(), ' : ', value.title())

      with open('Dictionary.txt', 'w') as f:
        f.write(f"\nUpdate Keyword1:{x.title()}")

    elif x=='2':
      y = input("Enter the keyword:")
      P3book = {'Keyword2':y}

      P1book.update(P3book)

      for key, value in P1book.items():
        print(key.title(), ' : ', value.title())

    elif x=='3':
      z = input("Enter the keyword:")
      P2book = {'Keyword3':z}

      P1book.update(P2book)

      for key, value in P1book.items():
        print(key.title(), ' : ', value.title())
 update()

elif choice == '3':
 def delete():
  x = input("Delete keyword:")
  dlt = P1book.pop(x)
  print('Delete element keyword name is:',dlt)
  for key, value in P1book.items():
      print(key.title(), ' : ', value.title())

 delete()

elif choice == '4':
 def display_all_keyword():
     for key, value in P1book.items():
         print(key, ' : ', value)

 display_all_keyword()

elif choice == '5':
 def search():
     key = input("Enter keywords(Keyword1,Keyword2,Keyword3): ")

     if key in P1book:
         print('{}:{}'.format(key, P1book[key]))


     else:
         print('The keyword is not present in the dictionary')
         print('Add keyword press1 or press any key for exit.')
         a =(input("Press: "))

         if a == '1':
             Keyword4 = input("Keyword4:")
             P1book["Keyword4"] = Keyword4

         for key, value in P1book.items():
             print(key.title(), ' : ', value.title())
         else:
          print('___Exit____')
 search()

elif choice == '6':
 def store():
     with open('Dictionary.txt', 'r') as f:
      contents=f.read()
     print(contents)
 store()



elif choice == 'quit':
 def exit():
     print('____Exit____')
 exit()