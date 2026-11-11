class customer:
    def __init__(self,id,name,number,email):
        self.__id=id
        self.__name=name
        self.__number=number
        self.__email=email

    def get_id(self):
        return self.__id

    def set_id(self,id):
        self.__id=id

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name=name

    def get_number(self):
        return self.__number

    def set_number(self,number):
        self.__number=number

    def get_email(self):
        return self.__email
    
    def set_email(self,email):
        self.__email=email

    def __str__(self):
        return f'{self.__id} ,{self.__name},{self.__number},{self.__email}'
    def __lt__(self,other):
        return self.__name<other.__name


def main():
    l=[]
    n=int(input('enter custmer'))
    for i in range(0,n):
        s=input("enter the customer detailes\n 1.name\n2.number\n3.email\n")
        lst=s.split(',')
        c=customer(1001+i,lst[0],lst[1],lst[2])     
        l.append(c)

        for c in l:
            print(c)

        l.sort()
        print("after sorting")

        for c in l:
            print(c)
        

if __name__=='__main__':
    main()
        

# encapsulation

# class criketer:
#     def __init__(self,name,team,avg,strikerate):
#         self.__name=name
#         self.__team=team
#         self.__avg=avg
#         self.__strikerate=strikerate


#     def get_name(self):
#         return self.__name

#     def get_team(self):
#         return self.__team

#     def get_avg(self):
#         return self.__avg

#     def get_strikerate(self):
#         return self.__strikerate


# def main():
#     c1=criketer("rohith","mi",56,200)
#     print(c1.get_name())
#     print(c1.get_team())
#     print(c1.get_avg())
#     print(c1.get_strikerate())


# if __name__=="__main__":
#     main()