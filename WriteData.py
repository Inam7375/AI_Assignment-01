import json
def writing_file():
    listA = []
    listB = []
    listC = []
    while True:
        A = input("Enter values for A")
        if A == 'e':
            break
        listA.append(int(A))
        
    while True:
        B = input("Enter values for B")
        if B == 'e':
            break
        listB.append(int(B))
        
    while True:
        C = input("Enter values for C")
        if C == 'e':
            break
        listC.append(int(C))
        
    dict1 = {
        "A": listA,
        "B": listB,
        "C": listC,
            
        }

    if listA == [] or listB == [] or listC == []:
        print("Empty lists")
    else:
        try:
            with open("And_Data.json", 'w') as f:
                json.dump(dict1, f)
        except Exception:
            print("Invalid file name")


