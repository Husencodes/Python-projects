#Quize game 

print("Welcome to AI Quize ")

score=0 #Storing Points when answerd correct!

playing=input("Do you want to Play? (yes/no):- ").title().strip()
if playing != 'Yes':
    quit()

# Attention Here We can use same variable name in diffrent if conditions

#Question 1
print('''
1.What is the full form of AI?
A) Automated Intelligence
B) Artificial Intelligence
C) Advanced Internet
D) Artificial Integration''')
Question=input("").title()#I use tittle() function Instead of Upper()function
if Question=='B':
    print("Correct!")
    score+=1
else:
    print("Incorrect!")  

#Question 2
print('''
2.What is the full form of ML?
A) Machine Learning
B) Modern Logic
C) Multiple Languages
D) Machine Logic ''')
Question=input("").title()
if Question=='A':
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


#Question 3
print('''
3.What is the full form of NLP?
A) Natural Learning Program
B) Neural Language Processing
C) Natural Language Processing
D) Network Language Protocol''')
Question=input("").title()
if Question=='C':
    print("Correct!")
    score+=1
else:
    print("Incorrect!")  

#Question 4
print('''
4.What is the full form of LLM?
A) Large Language Model
B) Long Learning Machine
C) Logical Language Method
D) Large Learning Machine''')
Question=input("").title()
if Question=='A':
    print("Correct!")
    score+=1
else:
    print("Incorrect!")  

#Question 5
print('''
5.What is the full form of DL in AI?
A) Data Logic
B) Deep Learning
C) Digital Language
D) Dynamic Learning''')
Question=input("").title()
if Question=='B':
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

#Question 6
print('''
6.What is the full form of ANN?
A) Automated Neural Network
B) Artificial Network Node
C) Artificial Neural Network
D) Advanced Neural Notation''')
Question=input("").title()
if Question=='C':
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

#Question 7
print('''
7.What is the full form of CNN in deep learning?
A) Computer Neural Network
B) Convolutional Neural Network
C) Connected Network Node
D) Central Neural Network''')
Question=input("").title()
if Question=='B':
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


#Question 8
print('''
8.What is the full form of RNN?
A) Recurrent Neural Network
B) Recursive Network Node
C) Random Neural Network
D) Real-time Network''')
Question=input("").title()
if Question=='A':
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

#Question 9
print('''
9.What is the full form of GAN?
A) General Artificial Network
B) Generative Adversarial Network
C) Global Automated Network
D) Generated Algorithm Node''')
Question=input("").title()
if Question=='B':
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

#Question 10
print('''
10.What is the full form of AGI?
A) Automated General Integration
B) Artificial Generated Intelligence
C) Artificial General Intelligence
D) Advanced Generative Interface''')
Question=input("").title()
if Question=='C':
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print(f"Your Score is {score}/10")