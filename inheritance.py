class plane:
    def fly(self):
        print("plane is fying")

    def land(self):
        print("palne is landng")

    def takeoff(self):
        print("plane take off")

class cargoplane(plane):
    def fly(self):
        print("crgo plane is fying")

    def land(self):
        print(" cargo palne is landng")

    def takeoff(self):
        print("cargo plane take off")


class fighterplane(plane):
    def fly(self):
        print("figter plane is fying")
    
    def land(self):
        print("figter palne is landing")
    
    def takeoff(self):
        print("plane take off")


def main():
    print("1.cargoplane\n2.fighterplane\n")
    choice=int(input("enter a choice"))
    if choice==1:
        p=cargoplane()
    elif choice==2:
        p=fighterplane()
    else:
        print("invalied")

    p.fly()
    p.takeoff()
    p.land()

if __name__=='__main__':
    main()



# class employee:
#     def __init__(self,name):
#         self.name=name
#         print(self.name,"i'm a developer")


# class developer(employee):
#     def work(self):
#         print("writting python code")


# class tester(employee):
#     def work(self):
#         print("testing python code")

# def main():
#     p=employee("kechu")
#     employees=[developer("ajju"),tester("rajuuu")]
#     for emp in employees:
#         emp.work()

# if __name__=='__main__':
#     main()