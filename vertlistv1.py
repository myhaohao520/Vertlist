#Python Script for printing list of names verticially (Replace the names in Step 2 with your own) V1

#Step 1. The list of names I will be using in this example
#list = Carlo Pineda, Eduardo Covarrubias, Ting-Yueh Liu, Matt Dulog, Jian Hao Tang, Son Tran

#Step 2. Put the list on names in '', run the code to split all the names into individual ''
list = 'Carlo Pineda, Eduardo Covarrubias, Ting-Yueh Liu, Matt Dulog, Jian Hao Tang, Son Tran'
print(list.split(','))

#Step 3. Copy the output of the previous code and put the list into []
list = ['Carlo Pineda', ' Eduardo Covarrubias', ' Ting-Yueh Liu', ' Matt Dulog', ' Jian Hao Tang', ' Son Tran']

#Step 4. Run this code to print the list of names vertically
print('\n'.join(list))


#Changelog:
#Create a draft code for the script
#All steps must be run independently
