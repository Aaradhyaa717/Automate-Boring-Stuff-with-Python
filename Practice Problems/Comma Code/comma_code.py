def comma_code(lst):
  # lst -- list of items given by user
  try:

    #when user enter only one item
    if len(lst)==1:
      print(lst[0])

    # for multiple items
    else:    
      for item in range(len(lst)-1):
        print(lst[item], end = ', ')
      print('and '+ lst[-1])

 # for empty list     
  except IndexError:
    return 'Please enter a list of items'  

# taking the input from the user  
user_entry = input('Enter a list of items: ')

#splitting the input before passing it through the comma_code function
user_list = user_entry.split()

#passing the user list in the comma_code function
comma_code(user_list)


#trying other test cases
comma_code(['apple','banana','cat'])
comma_code(['apple'])
comma_code([])  