valid_score  = False

while not valid_score:
    score = input("Enter score: ")
    if len(score) == 0: #presense check
        print("Empty Input")
    elif not score.isdigit(): #data type check
        print("Please enter an integer")
    elif not 0 <= int(score) < 500:
        print("Score must be in btw 1 & 500")
    else:
        valid_score = True
        score = int(score)
    
