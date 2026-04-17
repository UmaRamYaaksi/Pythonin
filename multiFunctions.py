class multipleFunctions():
    
    def subfield():##Subfields
        fieldlst=['Machine Learning','Neural Networks','Computer Vision','Robotics','Speech Processing','Natural Language Processing']
        print("Subfields in AI are:")
        for temp in fieldlst:
            print(temp)
    def oddEven():##OddorEvennumber find
        num12=int(input("Enter the Number for odd/even"))
        if(num12%2==0):
            print(num12,"is Even Number")
        else:
            print(num12,"is Odd Number")
    def checkWedElig():##Marraige Eligibility check
        gen1=input("Enter your gender")
        age=int(input("Enter your age"))
        if((gen1.casefold()=="male" and age>=21)or (gen1.casefold()=="female" and age>=18)):#casefold converts string into lower case
            print("You are Eligibile for Marriage")
        else:
            print("You are not Eligibile for Marriage")
    def marksCalculation():##Marks calculator
        subtotal=0
        NoofSub=int(input("Enter the number of subjects"))
        print("Enter the Marks for each subject out of 100")
        for temp in range(0,NoofSub):
            subjectMarks=int(input(f"\rSubject{temp+1}"))
            subtotal+=subjectMarks
        print("Total:",subtotal)
        print("Percentage:",subtotal/NoofSub)
    def AreaPerimeterOfTriangle():##tp find area and perimeter of triangle
        print("##To get Area of Triangle##")
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        print("Area Formula : (Height*Breadth)/2")
        Area = (Height*Breadth)/2
        print("Area of triangle:",Area)
        print("\n##To get Perimeter of Triangle##")
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth1=int(input("Breadth1:"))
        print("Perimeter Formula : (Height1+Height2+Breadth)")
        perimeter=Height1+Height2+Breadth1
        print("perimeter of triangle:",perimeter)
