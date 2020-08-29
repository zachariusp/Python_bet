#Homework 1: Mad Lib
#Program By: Jenkins, Kevin
#File Name: H1_Mad_Lib.py
#Function: This program will create a Mad Lib from user input
#AKA - The Donald Trump Speech Generator


P1 = print

P1('Welcome to Mad Libs!'),
P1("list two adverbs"),
av1 = input("1st Adverb: "),
av2 = input("2nd adverb: "),
no1 = input("1st Noun:"),
no2 = input("2nd Noun:"),
vb1 = input("1st Verb(Past Tense):"),
vb2 = input("2nd Verb(Past Tense):"),
aj1 = input('Adjective 1:'),
aj2 = input('Adjective 2:'),
pn1 = input('Pronoun 1:'),
pn2 = input('Pronoun 2:'),
P1('Your Final Mad Lib!:'),
P1("%s walked in a hurry towards the" %pn1, "%s.They were going to be late. Suddenly, a" %no1 , "%s " %aj1, "%s" %no2, "%s" %vb1, "in front of them. "),
P1("%s" %pn1,"started %s" %av1, "towards the %s." %no2, "That’s when %s" %pn2, "%s towards them." %vb2),
P1("Very %s." %av2, "It was very %s." %aj2)