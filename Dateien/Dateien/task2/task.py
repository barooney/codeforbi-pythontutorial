def load_chat(filename):
    with open(filename, "r") as chat:
        for line in chat.readlines():
            line = line.strip()
            print(line)

load_chat("chat.txt")
