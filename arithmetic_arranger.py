def split_element(list):
    i = 0
    for cal in list:
        if " " in cal:
            element = cal.split()
            if len(element) == 2:
                if "+" in element[0]:
                    element[0] = element[0].replace("+","")
                    element.insert(1,"+")
                elif "-" in element[0]:
                    element[0] = element[0].replace("-","")
                    element.insert(1,"-")
                elif "+" in element[1]:
                    element[1] = element[1].replace("+","")
                    element.insert(1,"+")
                elif "-" in element[1]:
                    element[1] = element[1].replace("-","")
                    element.insert(1,"-")
        else:
            if "+" in cal:
                element = cal.split("+")
                element.insert(1,"+")
            else:
                element = cal.split("-")
                element.insert(1,"-")
        list[i] = element
        i+=1
    return list

def valid(list):
    if len(list) > 4:
        raise ValueError("Too many problems")
    for cal in list:
        try:
            int(cal[0])
            int(cal[2])
        except:
            raise ValueError("Numbers must only contain digits")
        if cal[1] not in["+","-"]:
            raise KeyError("Operator must be + or -")
        for element in cal:
            if len(element) >= 5:
                raise ValueError("Number cannot be more than 4 digits")
    print("All problems are valid")
    return list


def calculate(problem):
    if "+" in problem:
        problem.append(str(int(problem[0])+int(problem[2])))
    else:
        problem.append(str(int(problem[0])-int(problem[2])))


def space(list):
    print("Here is the result:")
    # first line
    for i in range(len(list)):
        list[i][0] = (" "*(6-len(list[i][0])))+list[i][0]
        print(list[i][0], end="    ")
        list[i][2] = (" "*(5-len(list[i][2])))+list[i][2]       # prepare number of the second line
    print()
    
    # second line
    for i in range(len(list)):
        print(list[i][1], list[i][2], sep="", end="    ")
    print()

    # --- line
    for i in range(len(list)):
        print("-"*6, end="    ")
    print()

    # result line
    for i in range(len(list)):
        list[i][3] = (" "*(6-len(list[i][3])))+list[i][3]
        print(list[i][3], end="    ")     

    print("\nAll done!")   


def arithmetic_arranger(list):
    split_element(list)
    valid(list)
    for prob in list:
        calculate(prob)
    space(list)



test = ["100+ 3","2000-4000", "9999 +10", "1 + 300"]
arithmetic_arranger(test)