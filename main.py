# lines 2-4 of the code asks the user to input the dimensions
User_Input_Length = int(input ("please select the length: "))
User_Input_Width = int(input ("please select the width: "))
User_Input_Area = int(input ("please select the area: "))
# line 6 calculates the true area
area = User_Input_Length * User_Input_Width
# lines 8-13 do the calculations
if User_Input_Area == area:
 print ("this is correct ")
if User_Input_Area < area:
 print ("the answer is smaller then the area ")
if User_Input_Area > area:
 print ("this answer is bigger then the area ")