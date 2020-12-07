import csv

def getKey(item):
    return item[0]


def name_changer(line):
    newline = ''
    for ch in line:
        if ord(ch)<=0x7A:
            c = hex(ord(ch))
            c = c[2:len(c)]
            c = c.upper()
            c = '='+c
            newline = newline + c
        else:
            if ch == 'ç':
                c = '=C3=A7'
            elif ch == 'Ç':
                c = '=C3=87'
            elif ch == 'ğ':
                c = '=C4=9F'
            elif ch == 'Ğ':
                c = '=C4=9E'
            elif ch == 'ı':
                c = '=C4=B1'
            elif ch == 'İ':
                c = '=C4=B0'
            elif ch == 'ö':
                c = '=C3=B6'
            elif ch == 'Ö':
                c = '=C3=96'
            elif ch == 'ş':
                c = '=C5=9F'
            elif ch == 'Ş':
                c = '=C5=9E'
            elif ch == 'ü':
                c = '=C3=BC'
            elif ch == 'Ü':
                c = '=C3=9C'
            newline = newline + c
    return newline

def name_checker(line):
    for ch in line:
        if ord(ch)>0x7A:
            return 1
    return 0

with open('Kişiler.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    list2 = []
    for item in csv_reader:
        list2.append([item[0],item[1]])
    list2 = sorted(list2, key = getKey)

with open('Kişiler_sorted.csv','w') as f:
    for line in list2:
        f.write(line[0]+','+line[1]+'\n')


with open('Kişiler.vcf','w') as f:
    for line in list2:
        f.write('BEGIN:VCARD\n')
        f.write('VERSION:2.1\n')
        f.write('N')
        name = (line[0].split(' '))
        if name_checker(line[0]):
            newline = name_changer(line[0])
            name = newline.split('=20')
            f.write(';')
            f.write('CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:')
        else:
            f.write(':')

        if len(name) == 1:
            f.write(';')
            f.write(name[0])
            f.write(';;;\n')
        elif len(name) == 2:
            ending = name[len(name)-1]
            f.write(ending)
            f.write(';')
            f.write(name[0])
            f.write(';;;\n')
        elif len(name) == 3:
            ending = name[len(name)-1]
            f.write(ending)
            f.write(';')
            f.write(name[0])
            f.write(';')
            f.write(name[1])
            f.write(';;\n')
        else:
            ending = name[len(name)-1]
            f.write(ending)
            f.write(';')
            new_name = name[0]
            for counter in name:
                if counter != name[0] and counter != name[len(name)-1]:
                    new_name = new_name + ' ' + counter
            f.write(new_name)
            f.write(';;\n')
        f.write('FN')
        if name_checker(line[0]):
            f.write(';')
            f.write('CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:')
            f.write(newline)
        else:
            f.write(':')
            f.write(line[0])
        f.write('\n')
        f.write('TEL;CELL:')
        f.write(line[1])
        f.write('\n')
        f.write('END:VCARD\n')


'''
Not:
Bu programı kullanabilmek için öncelikle Kişiler.csv dosyasının olması gereklidir.
Kişiler.csv dosyasının formatı şu şekilde olmalıdır. Örneğin:
Halit Toklu,0123 123 1234
Ali Veli,0142 123 1234
Ömer,0133 123 1432
Mühendis Halit,1222 111 5452

Bu şekilde olduğu zaman Output olarak Kişiler.vcf dosyası çıkacaktır.
Aynı zamanda İsimleri Alfabetik sıraya göre dizip Kişiler_sorted.csv dosyasını buna göre oluşturacaktır.
'''
