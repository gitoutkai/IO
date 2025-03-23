#Condtionals0.1

var1= 3
var2= 54
#here are my two variables  this sucks i couldn't do the one before this and i been working for 4 hours

if var1 > var2:
	#this is the if statement, I experimented with these to create a bot that could kind of talk, 
	print("var1 is bigger!")
	#This is more or less how it worked, but it would print different things depending on who won F1

print("Done!")


if var1 == var2:
	print("var1 is equal to var2")
#on my first try the print out said, you spent 30 million to tie with stroll

if var1 >= var2:
	print ("var1 is greater then or equal to var 2")
	#og print out said "Ferarri cant  win by more than (Print(var3)) points?"
	# hey rob some sources are ssaying that I should not have brackets around the variables after the if statement  is that true?

if var1 > var2 and var 1 == var2:
	print ("This is never true!")
#because the number needs to be greater than the other or equal to each other because logic
else:
	print("This is always true")
#I used this when I wanted to create a bot that would talk with semi normal dialogue
#prompted to answer a yes or no answer and the "no" was the else, ie: input(do u breakthelaw?) 
#if then statement
#if yes then more text
#if no then end of conversation

var3= input("enter your own number")
try:
	var4 = int(var3)
	if (var1>var4):
		print("var1 is bigger")
	elif (var1 < var4):
		print("Var1 is smaller")
	else:
		print("this is not a number")

#i had to remove the bit that was your first try from the lecture. now it has the second bit you told us to type with the elif and the except


except:
	print("that is not a number")


#i agree the except thing is super cool and I should have asked about it because I wasted a lot of time #without it

print(var4)




