from pathlib import Path


def names():
    names_file = Path(__file__).parent / "names.txt"
    with open(names_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
    names_list = []
    for line in lines:
        line = line.strip()
        if line:
            if "→" in line:
                name = line.split("→")[1]
            else:
                name = line
            names_list.append(name)
    return names_list


def last_names():
    lastnames_file = Path(__file__).parent / "lastnames.txt"
    with open(lastnames_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
    lastnames_list = []
    for line in lines:
        line = line.strip()
        if line:
            if "→" in line:
                name = line.split("→")[1]
            else:
                name = line
            lastnames_list.append(name)
    return lastnames_list
