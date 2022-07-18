print('\n*****Birthday Invitation****')
print('Add a person and choice 1')
print('Update a invitation card any thing and choice 2')
print('Delete a invitation card any thing and choice 3')
print('See up comming invitation card any thing and choice 4')
print('See current invitation card  and choice 5')
print('Exit  and choice quit')
print('________________________________________________')
Add_book={}
B_list=['Description:I have a birthday Invitation','Date:18 October 2022','Place:KFC at Banani branch']


x = input("\nChoice:")
if x == '1':
 def add():
   size = int(input("Adding up comming birthday and press 1: "))
   if size==1:
      x = input('Description:')
      y = input('Date:')
      z = input('Place:')


      B_list.append('\nDescription:' + x)
      B_list.append('Date:' + y)
      B_list.append('Place:' + z)

      for i in B_list:
       print(i)

      with open('Birth.txt', 'w') as f:
          for item in B_list:
              f.write("%s\n" % item)

 add()

elif x == '2':
 def update():
    print('Update description and press1')
    print('Update Date and press2')
    print('Update Place and press3')
    x=input('Press:')
    if x=='1':
      x=input('Description name:')
      B_list[0] = x

      for i in B_list:
       print(i)

    elif x=='2':
        x = input('Date name:')
        B_list[1] = x

        for i in B_list:
            print(i)

    elif x=='3':
        x = input('Place:')
        B_list[2] = x

        for i in B_list:
            print(i)

 update()

elif x == '3':
 def delete():
     print('Description delete and press1')
     print('Date delete and press2')
     print('Place delete and press3')
     x=input('Press:')
     if x=='1':
      B_list.pop(0)
      print(B_list)

     elif x=='2':
      B_list.pop(1)
      print(B_list)

     elif x=='3':
      B_list.pop(2)
      print(B_list)

 delete()

elif x == '4':
 def txt_read():
    with open('Birth.txt','r') as f:
     contents = f.read()
    print(contents)
 txt_read()

elif x == '5':
  def current():
    for i in B_list:
        print(i)
  current()

elif x == 'quit':
  def quit():
    print('_____Exit_____')
  quit()