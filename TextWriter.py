import file_handling as fh
import time

file = "test.txt"
text_thing = "\nThis is my lil text thing Good innit"

fh.write_a_file(file,f"Hello file created at {time.time()}")

fh.add_to_a_file(file,text_thing)

fh.read_a_file(file)