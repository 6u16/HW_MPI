# Домашнее задание к лекции 1. «Import. Module. Package»
from datetime import datetime
from tqdm import tqdm

from apps.salary import calculate_salary
from apps.db.people import get_employees

def main():
    dt_nw = str(datetime.now())
    print(dt_nw[:10])
    calculate_salary()
    get_employees()
    for i in tqdm(range(55)):
        pass
    

if __name__ == '__main__':
    print(__name__)
    main()