def main():

    l=["Math","hindi","english","science","Art","computer"]
    name_list=[]
    all_data=[]
    while True:
        name= get_name()
        if name=='Done':
             break
        else:
             name_list.append(name)
    
    for i in name_list:
        mark_sum=0
        t1=[]
        t1.append(i)
        t2=[]
        print(f'''Welcom you ! {i}''')
        for i in l:
                temp= get_subject_mark(i)
                t2.append(temp)
                mark_sum+=temp
        t1.append(t2)
        grade=get_grade(mark_sum/6)
        t1.append(grade)
        all_data.append(t1)
    print(all_data)
                


# this method retun the grade
def get_grade(avg):

    if avg>90:
         return "A"
    elif avg>80:
         return "B"
    elif avg>70:
         return "C"
    elif avg>60:
         return "D"
    else :
         return "Fail"




# this function return the valid name taking form the user and return after checking
def get_name():
    
    while True:
        name=input("Enter Your Name : \n").title()
        if name in [0,1,2,3,4,5,6,7,8,9]:
            print("Enter Valid Name :")
        elif name =='Done':
            return name
        else:
             return name
        
# return the subject marks form the user
def  get_subject_mark(s):
    while True:
        try:
            mark=int(input(f'''{s}  marks :'''))
            if mark<0 or mark>101:
                print("Enter positive marks : ")
            else:
                return mark
        except ValueError:
                print("Enter Valid marks :")

main()

