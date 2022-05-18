import keyboard

def counter():
    end=1
    negative = 0
    positive = 0
    while end <= 1000:
        end += 1
        score = input("input here:")
        if score == "f":
            negative += 1
            print(negative)
        if score == "k":
            positive +=1
            print(positive)
        if score == "q":
            print ("positive", positive)
            print ("negative", negative)
            break
counter()