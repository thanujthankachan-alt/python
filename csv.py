import csv


field_name = ['No', 'Company', 'Car Model']


car = [
    {'No': 1, 'Company': 'Ferrari', 'Car Model': 'GH'},
    {'No': 2, 'Company': 'BMW', 'Car Model': 'X5'},
    {'No': 3, 'Company': 'Maruti Suzuki', 'Car Model': 'Swift'},
    {'No': 4, 'Company': 'Audi', 'Car Model': 'RS7'},
    {'No': 5, 'Company': 'Toyota', 'Car Model': 'Fortuner'}
]


csvfile = open('car.csv', 'w', newline='')
writer = csv.DictWriter(csvfile, fieldnames=field_name)
writer.writeheader()
writer.writerows(car)
csvfile.close()


csvfile = open('car.csv', newline='')
reader = csv.reader(csvfile)
for r in reader:
    print(','.join(r))
    print(r)
csvfile.close()
