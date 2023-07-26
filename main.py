print("Welcome to Quiz Game!")

answer = input("Want to test your luck on some Gen 1 Pokemon questions? ")
if answer.lower() != "yes":
    print("Maybe next time then!")
    quit()

score = 0

answer = input("Question 1. What is the name of Ash Ketchum's first Pokemon? ")
if answer.lower() == "pikachu":
    score += 1
else:
    print("It was that little mouse Pokemon everyone loves, Pikachu!")

answer = input("Question 2. What is the name of Ash's main rival? ")
if answer.lower() == "gary":
    score += 1
else:
    print("How could you forget about Gary?")

answer = input("Question 3. What is the first Pokemon that Ash releases? ")
if answer.lower() == "butterfree":
    score += 1
else: 
    print("Aww, it was Butterfree, that sweet butterfly Ash caught as a Caterpi!")
    
answer = input("Question 4. What is Gary's main pokemon? ")
if answer.lower() == "eevee":
    score += 1
else:
    print("Actually, it was eevee!")

answer = input("Question 5. The trick question...What is Professor Oak's name in the past? ")
if answer.lower() == "sam":
    score += 1
else: 
    print("This one you had to know a bit more, but it was Sam! Oak met Ash as a child in time travel and grew up to be the Professor!")

percentage = float((score / 5) * 100)
print(f"You scored {score}/5!")
print(f"That equates to a {percentage}% you Poke master you!")
