#Task 1
# Even_Namber = [i for i in range(1,100) if i %2 == 0]
# Single_Namber = [i for i in range(1,100) if not i %2 == 0]
# print(Even_Namber,'\n',Single_Namber)
#--------------------------------
#Task 2
# x,y =5,20
# p = [i for i in range(1, 101) if i % x == 0 and i % y == 0]
# print(p)
#---------------------------------------
#Task 3
# while 1:
#     start=int(input('inter frist namer: '))
#     end=int(input('inter second namer: '))
#     for i in range(start,end+1):
#         for e in range(1,13):
#             print(i , ' x ',e,' = ' , i*e)
#         print('-' *20)
#-------------------------------------------
#Task 4
# text='Python is is an an easy language'
# text_word=text.split(' ')
# mylist=[]
# for i in text_word:
#     if not i in mylist:
#         mylist.append(i)
# print (' '.join(mylist))
#--------------------------------------------
#Task 5
# text='Python is an easy language'
# text_word=text.split(' ')
# print(len(text_word))
#-----------------------------------------
# Task 6
# text='Python is easy'
# text_word=text.split(' ')
# mylist= []
# for i in text_word:
#     if  'easy' == i:
#         continue
#     else:
#         mylist.append(i)
# print(' '.join(mylist))

#----------------------------------------
#Task 7
# text='Python is is is is easy '
# text_word=text.split(' ')
# repetition =0
# for i in text_word:   
#     if i=='is':
#         repetition+=1
# print(repetition)
#----------------------------------------------
#Task 8
# start = 2
# num = 6
# mylist=[i for i in range(start,101) if i%num == 0]
# print(mylist)
#----------------------------------------------------
#Task Level 2
#-------------------
#Task 1
# Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
# Capetal =[i.upper() for i  in Names]
# print(Capetal)
#----------------------------------------------------
#Task 2
# Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
# x =[i for i in Names if 'a' in i]
# print(x)
#----------------------------------------------------------
#Task 3
# Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
# x =[i for i in Names if 't' in i[0]]
# print(x)
#--------------------------------------------------------------------------
#Task 4
# Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
# x =[i for i in Names if i.count('a')>= 2]
# print(x)
#---------------------------------------------------------------------------
#Task 5
# Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
# x=[len(i) for i in Names]
# print(x)
#---------------------------------------------------------------------------------
#Task 6 , 7
# Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
# a,*b = Names
# print(a,b)
#------------------------------------------------------------------------------------------
#Task 8
# Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
# a,*z,b = Names
# print(a,b)
#--------------------------------------------------------------------------------
#Task 9
# Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
# a,b,*z = Names
# print(a,b)
#----------------------------------------------------------------------------
#Task Level 3
#-------------------
#Task 10
# import datetime
# start = datetime.datetime(2005,4, 27)
# end = datetime.datetime(2023, 9, 21)
# delta = end - start
# print(delta)
#------------------------------------------------------------------------------
#Task 11
# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5 / 9
  
# def celsius_to_fahrenheit(celsius):
#     return  celsius * 9 / 5 + 32

# def inches_to_centimeters(inches):
#     return  inches * 2.54

# def centimeters_to_inches(centimeters):
#     return centimeters / 2.54
#-----------------------------------------------------------------------------
#Task 12
# import re

# def email_slicer(email):
  
#     regex = r'([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)'
#     match = re.search(regex, email)
#     if match:
#         username = match.group(1)
#         domain = match.group(2)
#         return username, domain
#     else:
#         print('Invalid email address')
# email = 'ahmedalgohary1170@gmail.com'
# username, domain = email_slicer(email)
# print(username)
# print(domain)