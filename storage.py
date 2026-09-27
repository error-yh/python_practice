import json
from models import Employee,Developer,Manager,Company

#运行
def read_employee():
    
    company=Company()
    
    try:
        with open("Company_employee.json","r",encoding="utf-8") as f:
            data=json.load(f)

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

    with open("Company_employee.json","w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=2)