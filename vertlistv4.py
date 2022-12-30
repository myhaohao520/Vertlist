#Python Script for printing list of names verticially (Replace the names with yours) V4

#1. The list of names I will be using in this example
#list = Carlo Pineda, Eduardo Covarrubias, Ting-Yueh Liu, Matt Dulog, Jian Hao Tang, Son Tran

#2. Put the list on names in '', run the code to split all the names into individual '' and name the new list new_list
#list = 'Carlo Pineda, Eduardo Covarrubias, Ting-Yueh Liu, Matt Dulog, Jian Hao Tang, Son Tran'
list = input('Enter the list of names here: ')
#print(list.split(','))
new_list = list.split(',')

#3. Copy the output of the previous code and put the list into []
#new_list = ['Carlo Pineda', ' Eduardo Covarrubias', ' Ting-Yueh Liu', ' Matt Dulog', ' Jian Hao Tang', ' Son Tran']
#new_list = list

#4. Run this code to print the list of names vertically
#vertical_list = input("Enter the list above here: ")
print('\n'.join(new_list))

#Changelog: 
#Removed print() new_list and created the variable new_list, to instead of printing the result of list.split(), store the result in a variable
#Removed step 3 entirely
