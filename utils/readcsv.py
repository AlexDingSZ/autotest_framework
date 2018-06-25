import csv
import os
import sys
def get_csv_data(filename):
    users = []
    with open(filename,'r',encoding='utf-8') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            users.append(row)
    return users

if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    root_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
    file_path = os.path.join(root_path,"data","user.csv")
    print(get_csv_data(file_path))