from Calculate import Calculation
import WriteData

while True:
    choice = ""
    choice = input("""Enter choice \n1:\tWrite data examples
2:\tCalculate perceptron table""")

    if choice == '1':
        writingData = WriteData.writing_file()

    elif choice == '2':
        calculation = Calculation
        calculation.specCalc()

    elif choice == 'e':
        break
    else:
        print("Invalid Choice")

