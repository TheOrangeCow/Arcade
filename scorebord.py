def order_scores(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    sorted_lines = sorted(lines, key=lambda x: int(x.split(":")[1]), reverse=True)
    with open(file_name, "w") as file:
        file.writelines(sorted_lines)

def fiel(file, wrightorread, name, score=None):
    if wrightorread == "r":
        with open(file, "r") as file:
            return file.readline()
    else:
        with open(file, "a") as file:
            file.write(f"{name.strip()}:{score}\n")

def add(game, score):
    name = fiel("logged_in_users.txt", "r", "none")
    fiel(f"scorebords/{game}.txt", "a", name, score)
    order_scores(f"scorebords/{game}.txt")




