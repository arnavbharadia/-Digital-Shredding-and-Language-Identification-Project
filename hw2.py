'''
Credits:
    1. OpenAI. (2023). ChatGPT [Large language model]. https://chat.openai.com/chat
'''
import sys
import math


def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def shred(filename):
    #Using a dictionary here. You may change this to any data structure of
    #your choice such as lists (X=[]) etc. for the assignment

# TODO: add your code here for the assignment
# You are free to implement it as you wish!
# Happy Coding!

    X = dict() #dictionary to store the letter counts
    with open(filename,'r',encoding='utf-8') as f:
        text=f.read() #read the entire file
    for i in ascii_uppercase: #initialize the dictionary
        X[i]=0 #set the count of each letter to 0
    for i in text: #iterate over each character in the text
        if i.strip()=='': #ignore spaces
            continue #continue to the next character
        elif i.upper() in X: #if the character is a letter
            X[str(i).upper()]+=1 #increment the count of that letter
    return X #return the dictionary

def F(y, e, s): #y is the dictionary of letter counts, e and s are the parameter vectors
    F_eng = math.log(0.6) + sum(y[letter] * math.log(e[ord(letter) - ord('A')]) for letter in ascii_uppercase) #sum over all letters
    F_spa = math.log(0.4) + sum(y[letter] * math.log(s[ord(letter) - ord('A')]) for letter in ascii_uppercase) #sum over all letters

    return F_eng, F_spa #return the F values

def P(F_eng, F_spa): #F_eng and F_spa are the F values

    if F_spa - F_eng >= 100: #if the difference is too large, return 0.0
        return 0.0 #return 0.0
    elif F_spa - F_eng <= -100: #if the difference is too small, return  1.0
        return 1.0
    else: #otherwise, return the probability
        return ((1.0) / (1.0 + math.exp(F_spa - F_eng)))

def main(): 
    input = 'letter.txt' #accepts the input file

    e, s = get_parameter_vectors() #stores the e and s values

    letter = shred(input) #stores the letter counts

    F_eng, F_spa = F(letter, e, s) #finds F(y)

    print("Q1") # print header for Q1
    for i in letter: #iterate over each letter
        print(f'{i} {letter[i]}') #print the letter and its count

    print("Q2") # print header for Q2
    print(f"{math.log(e[0]) * letter['A']:.4f}") 
    #print the log of the probability of the letter times the count of the letter
    print(f"{math.log(s[0]) * letter['A']:.4f}") 
    #print the log of the probability of the letter times the count of the letter

    print("Q3") # print header for Q3
    print("{:0.4f}".format(F_eng)) #print the F value for English
    print("{:0.4f}".format(F_spa)) #print the F value for Spanish

    print("Q4") # print header for Q4
    print("{:0.4f}".format(P(F_eng, F_spa))) #print the probability

if __name__ == "__main__": #call main function
    main()