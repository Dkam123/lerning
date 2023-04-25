def save_data(words):
    with open("../data.txt", "w") as f:
        f.write(" ".join(words))

def read_data():
    with open("../data.txt") as f:
        return f.read().split()
