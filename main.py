import csv
import random
import os
import faker

# Crear una instancia de Faker para generar datos aleatorios
fake = faker.Faker()

# Definir los nombres de los campos
fieldnames = [
    'Nombres', 'Documentos', 'Pais', 'Ciudad', 'Barrio', 'Telefono', 
    'Codigo_postal', 'nombre_padre', 'nombre_madre', 'ficha'
]

# Nombre del archivo CSV
filename = 'db_registros.csv'

# Obtener la ruta completa del archivo en la carpeta del proyecto
filepath = os.path.join(os.getcwd(), filename)

# Generar 10,000 registros
num_records = 10000
records = []

for _ in range(num_records):
    record = {
        'Nombres': fake.name(),
        'Documentos': fake.unique.random_int(min=10000000, max=99999999),
        'Pais': fake.country(),
        'Ciudad': fake.city(),
        'Barrio': fake.street_name(),
        'Telefono': fake.phone_number(),
        'Codigo_postal': fake.zipcode(),
        'nombre_padre': fake.first_name_male() + ' ' + fake.last_name(),
        'nombre_madre': fake.first_name_female() + ' ' + fake.last_name(),
        'ficha': f'{random.randint(1000, 9999):04d}'
    }
    records.append(record)

# Escribir los registros en el archivo CSV
with open(filepath, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)

print(f'Archivo CSV creado con {num_records} registros en {filepath}')
