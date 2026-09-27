from storage import read_employee,save
from models import Employee,Manager,Developer,Company

company=read_employee()

if company is not None:
    company.list_Employee()
    company.add_Employee(Manager("小陈", 4, 15000, "技术部"))
    save(company)
    company.list_Employee()
  