def load_contents(filename):
    with open("file.txt", "r") as f:
        return f.read()

print(load_contents("file.txt"))
