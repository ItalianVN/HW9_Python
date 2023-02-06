

def GetClasses():
    with open('C:\python\sem9\classes.txt', 'r') as file:
        temp = file.readlines()
        classes = {}
        for element in temp:
            classes[element[:element.index(' ')]] = element[element.index('[') + 1:-2].split(', ') 
            print(classes)



GetClasses()