from insurance_rates_data import national_insurance_rates
import csv

print(national_insurance_rates)
for key in national_insurance_rates:
    print(key)
    print(national_insurance_rates[key])

for key in national_insurance_rates:
    if None in national_insurance_rates[key]:
        print(f"the value is found in entry {key}")

'''with open('insurance_rates.csv') as csv_file:
    for line in csv_file.readlines():
        print(line)
'''
# (monthly_salary *12) / (National_insurance / rate)