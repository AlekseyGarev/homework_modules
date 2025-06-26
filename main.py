# import sys
# sys.path.append("C:/project/Buxgalteria")

from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    calculate_salary()
    get_employees()
