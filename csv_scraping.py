from csv import DictReader
from datetime import datetime

wb = xlrd.open_workbook('album_info_234345.csv')
wc = xlrd.open_workbook('apple_links.csv')
companies = wb.sheet_by_name('Companies')

with open('album_info_234345.csv') as document:
    reader = DictReader(document)
    for row in reader:
        day = datetime.strptime(row.get('START_DATE'), '%m/%d/%y')
        if 'PNC' in row.get('LOCATION') and day.weekday() > 4:
            print ' %s on %s' % (
                row.get('SUBJECT'), row.get('START_DATE'))
