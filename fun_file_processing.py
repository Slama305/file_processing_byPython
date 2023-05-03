def writeStudent():
    with open('student.txt','a') as file :
        c = 'y'
        
        while c == 'y' :
            id = input('Enter The Student id :')
            name = input('Enter The Student name :')
            age = input('Enter The Student age :')
            file.write(id +'\t'+ name +'\t'+ age + '\n')
            c = input ('Do You Want To Enter Records Again(y/n)?')
        print('File Saved Successfully')
def readStudent():
    with open('student.txt','r') as file :
        print('ID\tName\tAge')
        print('--------------------------')
        for line in file:
            print(line,end='')
def searchStudent():
    id = input('Enter The id of The Student You Search For:')
    with open('student.txt','r') as file :
        flag= False
        for line in file:
            fields=line.split('\t')
            if fields[0]==id:
                flag=True
                print('ID\tName\tAge')
                print('--------------------------')
                print(line)
        if not flag:
            print('The ID Student not Found')
def updatStudent():
    import os
    id = input('Enter The id of The Student You Want to Updat:')
    file =open('student.txt','r')
    tempfile=open('tempstudent.txt','w')
    flag = False
    for line in file:
        st = line.split('\t')
        if st[0]==id:
            flag=True
            age=input('Enter The New Age For '+ st[1])
            line=st[0] +'\t'+ st[1] +'\t'+ age +'\n'
        tempfile.write(line)
    file.close()
    tempfile.close()
    os.remove('student.txt')
    os.rename('tempstudent.txt','student.txt')
    if not flag:
        print('The ID Student not Found ')
    else:
        print('Update Successfully')
def deleteStudent():
    import os
    id = input('Enter The id of The Student You Want to Delete:')
    file =open('student.txt','r')
    tempfile=open('tempstudent.txt','w')
    flag = False
    for line in file:
        st = line.split('\t')
        if st[0]==id:
            flag=True
        else:
            tempfile.write(line)
    file.close()
    tempfile.close()
    os.remove('student.txt')
    os.rename('tempstudent.txt','student.txt')
    if not flag:
        print('The ID Student not Found ')
    else:
        print('Update Successfully')
def home():
    c = 'y'
    while c=='y':
        print('1:Too Add a New Student.')
        print('2:Too Read All Students.')
        print('3:Too Search For Student.')
        print('4:Too Updat a Record For Student.')
        print('5:Too Delete Student.')
        c = input('Enter Your Choice:')
        if c=='1':
            writeStudent()
        elif c=='2':
            readStudent()
        elif c=='3':
            searchStudent()
        elif c=='4':
            updatStudent()
        elif c=='5':
            deleteStudent()
        c = input('DO You Want To do Other Operation (y/n)')
home()
