def mode():
    f = open(fileName, 'r')
    words = []
    for line in f:
        wordsInLine = line.split()
        for word in wordsInLine:
            words.append(word.upper())
        
    theDictionary = {}
    for word in words:
        number = theDictionary.get(word, None)
        if number == None:
            theDictionary[word] = 1
        else:
            theDictionary[word] = number + 1
        
    theMaximum = max(theDictionary.values())
    for key in theDictionary:
        if theDictionary[key] == theMaximum:
            print("The mode is", key)
            break
            

def median():
    f = open(fileName, 'r')
        
    numbers = []
    for line in f:
        words = line.split()
        for word in words:
            numbers.append(float(word))
        
    numbers.sort()
    midpoint = len(numbers) // 2
    print("The median is", end=" ")
    if len(numbers) % 2 == 1:
        print(numbers[midpoint])
    else:
        print((numbers[midpoint] + numbers[midpoint - 1]) / 2)
        
        
def mean():
    f = open(fileName, 'r')

    numbers = []
    for line in f:
        words = line.split()
        for word in words:
            numbers.append(float(word))
    print("The mean is", end=" ")
    print(sum(numbers)/(len(numbers)))
    
x = 1

while x <= 3:
    print("Trial",x)
    fileName = input("Enter the file name: ")
    mean()
    median()
    mode()
    print("\n")
    x+=1    
