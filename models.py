#员工
class Employee:
    def __init__(self,name,id,wage):
        self.name=name
        self.id=id
        self.wage=wage
    def bonus(self):
        return 0

    def __str__(self):
        return f"员工姓名：{self.name} | 员工编号：{self.id} | 工资：{self.wage}"

#开发者
class Developer(Employee):

    def __init__(self, name, id, wage,language):
        super().__init__(name, id, wage)
        self.language=language

    def bonus(self):
        return 0.1*self.wage

#经理
class Manager(Employee):

    def __init__(self, name, id, wage,department):
        super().__init__(name, id, wage)
        self.department=department

    def bonus(self):
        return 0.2*self.wage


#公司
class Company:

    def __init__(self):
        self.Employee_list=[]

    #添加员工
    def add_Employee(self,new_name):
        for name in self.Employee_list:
            if new_name.id==name.id:
                print("该员工已经在公司了")
                return 
            
        self.Employee_list.append(new_name)

    #按编号删除员工
    def del_Employee(self,id):
        for name in self.Employee_list: 
            if name.id==id: 
                self.Employee_list.remove(name) 
                break
        
    #查看所有员工
    def list_Employee(self):
        for employee in self.Employee_list:
            print(employee)

        print()

    #需要发放的奖金总额
    def need_bonus(self):
        total_bonus=0
        for employee in self.Employee_list:
            total_bonus+=employee.bonus()
        return total_bonus
