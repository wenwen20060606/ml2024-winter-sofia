def user_input
    N = input("Please input a positive intger:\n")
    input_list = []
    for index in range(N):
        input_list.append(input("Please type in a number:\n"))
    
    X = input("Please type an integer:\n"}
    found = False
    for index in range(N):
        if X == input_list[index]:
            print(index+1)
            found = True
    if not found:
        print(-1)            
        
 user_input