import json


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



#运行
def read_employee():
    try:
        with open("Company\\Company_employee.json","r",encoding="utf-8") as f:
            data=json.load(f)

        company=Company()

        for info in data:
            if info["工种"]=="员工":
                employee=Employee(info["name"],info["id"],info["wage"])
            elif info["工种"]=="开发者":
                employee=Developer(info["name"],info["id"],info["wage"],info["language"])
            elif info["工种"]=="经理":
                employee=Manager(info["name"],info["id"],info["wage"],info["department"])
            else:
                print(f"未知工种{info["工种"]}")
                continue

            company.add_Employee(employee)
    except FileNotFoundError:
        print("未找到文件")
        return company
    except json.JSONDecodeError:
        print("文件格式错误")
        return None

    return company

#保存新添加的员工为json文件
def save(company):
    
    data=[]

    for employee in company.Employee_list:
        info={
            "name": employee.name,
            "id": employee.id,
            "wage": employee.wage
        }

        if isinstance(employee,Manager):
            info["工种"]="经理"
            info["department"]=employee.department
        elif isinstance(employee,Developer):
            info["工种"]="开发者"
            info["language"]=employee.language
        else:
            info["工种"]="员工"

        data.append(info)

    with open("Company\\Company_employee.json","w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=2)
    
        


company=read_employee()

if company is not None:
    company.list_Employee()
    company.add_Employee(Manager("小陈", 4, 15000, "技术部"))
    company.list_Employee()
    save(company)
    company.del_Employee(4)
    company.list_Employee()
    save(company)
    company.add_Employee(Manager("小陈", 4, 15000, "技术部"))
    save(company)
    company.list_Employee()