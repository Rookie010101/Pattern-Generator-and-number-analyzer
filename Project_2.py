print("Welcome to the Pattern Generator and Number Analyzer!")
while True:
    print("\nSelect an option: ")
    print('''1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit''')
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            n = int(input("Enter the number of rows for pattern: "))
            print("\nPattern: ")
            for i in range (1,n+1):
                for j in range(1,i+1):
                    print("*", end = " ")
                print()
        case 2:
            a1 = int(input("Enter the start of the range: "))
            a2 = int(input("Enter the end of the range: "))
            add = 0
            for a in range (a1, a2+1):
                if a%2==0:
                    print("Number", a, "is Even")
                else:
                    print("Number", a, "is Odd")
            for a in range (a1, a2+1):
                add+=a
            print("Sum of all numbers from", a1, "to", a2, "is: ", add)
        case 3:
            print("Exiting the program. Goodbye!")
            break
        case _:
            print("Invalid choice")
            break
        
