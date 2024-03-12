'''

'''
import psutil
import ast
#cpu functionality
times_in_state = psutil.cpu_times()
print(times_in_state)
for thing in times_in_state:
    print(thing)
converted_dictionary = ast.literal_eval("{" + {str(times_in_state)} + "}")

for k, v in converted_dictionary.items():
    print(f"{k} {v}")