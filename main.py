from tools.files_control import read_data, save_data
from tools import read_data, save_data

action = input("action: ")

if action == "s":
    save_data(["test", "itstep", "Kamrat"])

if action == "r":
    l = read_data()
    print(l)
