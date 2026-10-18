#Fake Headline Generator 

import random

subjects=[
    "MS Dhoni",
    "virat kohli",
    "Yash",
    "Sarukh khan",
    "Sudeep",
    "Allu arjun",
    "Narendra Modi",
    "Rahul gandi",
]

palces=[
    "Mars",
    "in india gate",
    "on moon",
    "in bengaluru",
    "in under water",
    "in Samosa City",
    "in No Network Village",

]
funny_actions = [
    "challenges 100 monkeys to a dance battle",
    "buys the Moon for ₹99",
    "opens a pani puri shop on Mars",
    "starts a world championship of sleeping",
    "races a tortoise in a Lamborghini",
    "learns coding from a talking potato",
    "declares war on Monday mornings",
    "builds a swimming pool full of Maggi",
    "teaches AI how to make chai",
    "becomes president of Meme City",
    "flies to Jupiter to eat biryani",
    "breaks the world record for doing nothing",
    "launches a rocket powered by samosas",
    "challenges aliens to a cricket match",
    "invents a homework-to-pizza machine",
    "opens a gym for lazy people",
    "starts a university for procrastinators",
    "dances with 500 robots",
    "tries to fix the internet with a spoon",
    "turns a village into a giant gaming zone"
]

while True:
    subject=random.choice(subjects)
    place=random.choice(palces)
    funny_action=random.choice(funny_actions)
    headline=(f"BREAKING NEWS:- {subject} {place} {funny_action} ")
    print("\n",headline)
    user_input=input("Do you want another headline (yes/no:- )").strip()
    if user_input=="no":
        break

print("thanks for using our Fake Headline Generator ")