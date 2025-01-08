import random

with open("nouns.txt",'r') as file:
    nouns = [line.strip() for line in file]

with open("verbs.txt", 'r') as file:
    verbs = [line.strip() for line in file]

with open("articles.txt",'r') as file:
    articles = [line.strip() for line in file]

with open("prepositions.txt", 'r') as file:
    prepositions = [line.strip() for line in file]

def sentence():
    return nounPhrase() + " " + verbPhrase()
    
def nounPhrase():
    return random.choice(articles) + " " + random.choice(nouns)
    
def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()
    
def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    while True:
        
        try:
            number = int(input("Enter the number of sentences: "))
        
        except ValueError:
            print(f"Please enter an integer\n")
            continue
        
        if number < 0:
            print(f"Please input a positive integer\n")
            continue

        elif number == 0:
            print("No sentences will be formed since input is 0")
            break
        
        else:
            break
        
    for count in range(number):
        print(sentence())

if __name__ == "__main__":
    main()