def CheckStudentName():
    while 1>0:
        StudentName = input("Enter student name:")
        if str.isalpha(StudentName) == True:
            return(StudentName)
        else:
            print("Invalid name, please try again.")
def CheckSID():
    while 1>0:
        StudentID=input("Enter student ID:")
        if len(StudentID) == 8 and str.isdigit(StudentID) == True :
            return(StudentID)
        else:
            print("Please enter Student ID again")
def CheckTMark():
    while 1>0:
        TMark=input("Enter test marks:") 
        if str.isdigit(TMark) == True and int(TMark) >= 0 and int(TMark) <= 100:
                return(TMark)
        else:
            print("Please enter again")
def CheckPMark():
    while 1>0:
        PMark=input("Enter project marks:") 
        if str.isdigit(PMark) == True and int(PMark) >= 0 and int(PMark) <= 100:
            return(PMark)
        else:
            print("Please enter again")
def CheckWMark():
    while 1>0:
        WMark=input("Enter workshop marks:") 
        if str.isdigit(WMark) == True and int(WMark) >= 0 and int(WMark) <= 100:
            return(WMark)
        else:
            print("Please enter again")
def CheckEMark():
    while 1>0:
        EMark=input("Enter workshop marks:") 
        if str.isdigit(EMark) == True and float(EMark) >= 0 and float(EMark) <= 100:
            return EMark
        else:
            print("Please enter again")
def CalculateCAMarks():
    CAMarks=float(TestMark)*0.4+float(ProjectMark)*0.3+float(WorkshopMark)*0.3
    return CAMarks
def CalculateModMarks():
     ModuleMarks = float(CaMark)*0.5 + float(ExamMark)*0.5
     return int(CaMark)
def CheckGrade():
    if int(CaMark) < 40 and int(ExamMark) < 40:
        Grade = "F"
        print("Module Marks: "+str(ModMark)+","+"Module Grade: F,"+"Remarks: Pass with F grade")
        return Grade
    elif int(ModMark) < 65:
        Grade = "C"
        print("Module Marks: "+str(ModMark)+","+"Module Grade: C,"+"Remarks: Pass with C grade")
        return Grade
    elif int(ModMark) < 75:
        Grade = "B"
        print("Module Marks: "+str(ModMark)+","+"Module Grade: B,"+"Remarks: Pass with B grade")
        return Grade
    else:
        Grade = "A"
        print("Module Marks: "+str(ModMark)+","+"Module Grade: A,"+"Remarks: Pass with A grade")
        return Grade
def comment():
    if StudentGrade == "A":
        print("Well done!")
    elif StudentGrade == "B":
        print("Almost can get an A grade, work harder!")
    elif StudentGrade == "C":
        print("Please be careful, you only qualified for a C.")
    elif StudentGrade == "F":
        print("Don't get discouraged, keep trying!")
def Runagain():
    while 1 >0:
        Choice = input("Do you want to enter another student record? [Y/y] for Yes, [N/n] for No: ")
        if Choice.upper() == "Y" or Choice.upper() == "N":
            return Choice.upper()
        else:
            print("Please enter [Y/y] or [N/n]")   

RunProgramme= "Y"  
AGrade = 0
BGrade = 0
CGrade = 0
FGrade = 0
Student = 0
AllMark = 0
while RunProgramme == "Y": 
    Student += 1  
    print("*************** Enter information ***************")
    Name=CheckStudentName()
    SID=CheckSID()
    TestMark=CheckTMark()
    ProjectMark=CheckPMark()
    WorkshopMark=CheckWMark()
    ExamMark=CheckEMark()
    print("*************** Result ***************")
    print("Student name:"+Name)
    print("Student ID:"+str(SID))
    print("Test Marks: "+str(TestMark)+","+"Project Marks: "+str(ProjectMark)+","+"Workshop Marks: "+str(WorkshopMark)+","+"Exam Marks: "+str(ExamMark))
    CaMark=CalculateCAMarks()
    ModMark=CalculateModMarks()
    StudentGrade=CheckGrade()
    comment()
    print("*************** Result ***************")
    if StudentGrade == "A":
        AGrade += 1
    elif StudentGrade == "B":
        BGrade += 1
    elif StudentGrade == "C":
        CGrade += 1
    else:
        FGrade += 1
    AllMark += ModMark 
    AVGMark = AllMark/Student 
    RunProgramme=Runagain()
    if RunProgramme == "N":
        print("There is/are "+str(Student)+" students' record(s) inputted, and the average marks is: "+str(AVGMark))
        for i in range(0,4):
            if i == 0:
                print("Total number of A grade: "+str(AGrade))
            elif i == 1:
                print("Total number of B grade: "+str(BGrade))
            elif i == 2:
                print("Total number of C grade: "+str(CGrade))
            elif i == 3:
                print("Total number of F grade: "+str(FGrade))
        