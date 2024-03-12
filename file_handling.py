import os

def file_check(filename):
    exists = os.path.exists(filename)
    if not exists:
        print("file not found")
        return False
    else:
        return True


def read_a_file(filename):
    if file_check(filename):
        with open(filename,"r") as f:
            for line in f.readlines():
                print(line)

def add_to_a_file(filename,text):
    if file_check(filename):
        with open(filename,'a') as f:
            f.write(text)

def write_a_file(filename,text):
    with open(filename,"w") as f:
      f.write(text)


