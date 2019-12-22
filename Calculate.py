import json

class Calculation:
    def __init__(self):
        pass
    def specCalc():
        #declaring variables
        new_dict = {"x0": 1,
                    "x1": 0,
                    "x2": 0,
                    "t": 0,
                    "y_in": 0,
                    "y": 0,
                    "w0": 0,
                    "w1": 0,
                    "w2": 0,
                    }
        theta = 0
        alpha = 1



        #loading json file into dictionary 
        try:
            with open("And_Data.json") as f:
                some_dict = json.load(f)
        except Exception:
            print("File not found")
        #printing data in json file
        print(some_dict)

        #executing external while loop for perceptron algo
        while True:
            #initializing counter to be used for observing change in for loop
            counter = 0

            #printing column names in proper indentation
            for keys in new_dict.keys():
                    print(keys, end = "\t")

            #starting for loop of calculation        
            for i in range(0,len(some_dict['A'])):

                #assigning x^i = S^i
                new_dict["x1"] = some_dict["A"][i]
                new_dict["x2"] = some_dict["B"][i]
                new_dict["t"] = some_dict["C"][i]
                new_dict["y_in"] = (new_dict["x0"]*new_dict["w0"]) + (new_dict["x1"]*new_dict["w1"]) + (new_dict["x2"]*new_dict["w2"])

                #checking for the condition of y_input to assign a value to y
                if new_dict["y_in"] > theta:
                    new_dict["y"] = 1
                elif new_dict["y_in"] == theta:
                    new_dict["y"] = 0
                else:
                    new_dict["y"] = -1

                #checking for the condition for changing of the weight's value    
                if new_dict["y"] != new_dict["t"]:
                    new_dict["w0"] = new_dict["w0"] + (alpha * new_dict["t"] * new_dict["x0"])
                    new_dict["w1"] = new_dict["w1"] + (alpha * new_dict["t"] * new_dict["x1"])
                    new_dict["w2"] = new_dict["w2"] + (alpha * new_dict["t"] * new_dict["x2"])
                    #adding the value of counter for every attempt to change in the weigth's value
                    counter += 1

                #printing out all the resultant values in proper indentation
                print("\n",new_dict["x0"],"\t", new_dict["x1"],"\t", new_dict["x2"],end = "\t")
                print(new_dict["t"],"\t", new_dict["y_in"],"\t", new_dict["y"], end = "\t")
                print(new_dict["w0"],"\t", new_dict["w1"],"\t", new_dict["w2"],end = "\n")
            print(end = "\n")

            #exiting the loop if change any change in for loop occurs else set the counter to 0
            if counter == 0:
                break
            else:
                counter = 0


