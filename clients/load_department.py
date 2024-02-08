import requests
from csv import DictReader


def load_department():
    url = 'http://localhost:8009/api/departments/'

    with open('../external_files/departments.csv') as f:
        cf = DictReader(f, fieldnames=['id', 'department'])
        for row in cf:
            print(row)

            response = requests.post(
                url,
                data={
                    'id': int(row['id']),
                    'department': row['department']
                }
            )
            print(response.text)


if __name__ == '__main__':
    load_department()
