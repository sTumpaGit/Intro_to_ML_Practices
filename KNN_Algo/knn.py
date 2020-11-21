import math

def get_distance(age,gender,sqrtlist,train_age,train_gender):
    l = len(age)
    print("Square roots using Euclidean Distance----")
    for i in range(0,l):
        distance = math.sqrt(((age[i]-train_age)**2) - ((gender[i]-train_gender)**2)) 
        sqrtlist.append(distance)
        print(distance)
#-----------------------------------------------------------------------------

def classification(sqrtlist,sports,nearest,k):
    cricket=0
    football=0
    neither=0
    position = []
    l = len(sqrtlist)
    for i in range(0,k):
        minimum = sqrtlist[0]
        pos = 0
        for j in range(l-1):
            if(sqrtlist[j] < minimum):
                minimum = sqrtlist[i]
                pos = j
            if(sqrtlist[j] == 9223372036854775807):
                continue
        nearest.append(minimum)
        position.append(pos)
        sqrtlist[pos] = 9223372036854775807 # maximum integer according to sys.maxint

    for i in range(0,k):
        s = sports[position[i]]
        if(s == 'Cricket'):
            cricket += 1
        elif(s == 'Football'):
            football +=1
        else:
            neither += 1

    if(cricket==football  and football==neither):
        c1 = sports[position[0]]
        result = ("The new member loves Cricket" if c1=='Cricket' else "The new member loves Football" if c1=='Football' else "the new member loves neither cricket nor football")
    
    result = max(cricket,football,neither)
    
    if(result == cricket):
        print('The new member loves Cricket')
    elif(result == football):
        print('the new member loves Football')
    elif(cricket == football):
        print('the new member loves both games')
    elif(result == neither):
    
        print('the new member loves neither cricket nor football')

#-------------------------------------------------------------------------------------

age = [32,40,16,34,55,40,20,15,55,15]
#male = 0
#female = 1
gender = [0,0,1,1,0,0,1,0,1,0]
#football = f
#cricket = c
# None of them = not
sports = ['Football','Neither','Cricket','Cricket','Neither','Cricket','Neither','Cricket','Football','Football']
sqrt_list = []
train_age,train_gender = [int(x) for x in input("Enter two data for age and gender for classification: ").split()]
get_distance(age,gender,sqrt_list,train_age,train_gender)
k = int(input("Enter the k value : "))
nearest = []
classification(sqrt_list,sports,nearest,k)

