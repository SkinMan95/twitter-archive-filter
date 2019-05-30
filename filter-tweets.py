from sys import stdout
from unidecode import unidecode
import json

PLACES_FILE = "colombia-lugares.txt"
INPUT_FILE = "json-files.txt"

def read_places():
    places = []
    with open(PLACES_FILE, "r") as f:
        places = [i.strip() for i in f.readlines()]

    return places

def read_input_file():
    input_files = None
    with open(INPUT_FILE, "r") as f:
        input_files = [i.strip() for i in f.readlines()]

    return input_files

def key_generator(dict_var, key):
      for k, v in dict_var.items():
            if k == key:
                 yield v
            elif isinstance(v, dict):
                 for val in key_generator(v, key):
                       yield val

def include_line(line, places) -> bool:
    d = json.loads(unidecode(line))
    found = False
    if any([lang == "es" for lang in key_generator(d, "lang")]):
        for location in key_generator(d, "location"):
            for place in places:
                if location != None:
                    if place in location.lower():
                        found = True
                        break
    return found

def proc_file(filename, places, output_file=stdout):
    with open(filename, "r") as f:
        line = f.readline().strip()
        while len(line) != 0:
            if include_line(line, places):
                output_file.write(line + "\n")
            line = f.readline().strip()

def main():
    places = read_places()
    input_files = read_input_file()

    output_file = open("out.dat", "w+")
    
    i = 0
    for f in input_files:
        print("File #%d: %s" % (i, f))

        proc_file(f, places, output_file)
        i += 1

    output_file.close()

if __name__ == "__main__":
    main()
