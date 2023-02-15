'''
instruksi
1. bikin file kodingan di direktori yang sama
2. sesuaikan "soal1.py dengan nama file contoh : akbar.py""
3. Jalankan
'''

import re

python_file = 'soal1.py'
work_file = None

basic_conversion_rules = {"kepada": "untuk", "=": "pada", "jika": "JIKA", "==": "setara", "sedang": "SEDANG", "sampai": "SAMPAI", "masukan": "MASUKAN", "class": "MEMBUAT CLASS", "Mendeklarasikan fungsi": "MEMBUAT FUNCTION", "selainnya:": "SELAINNYA:", "selainnya jika": "SELAINNYA JIKA", "kecuali:": "KECUALI:", "mencoba:": "MENCOBA:", "melewati": "MELEWATI", "didalam": "DIDALAM"}
prefix_conversion_rules = {"=": "mengatur ", "#F": "Panggil "}
advanced_conversion_rules = {"cetak": "OUTPUT", "kembali": "KEMBALI", "input": "INPUT"}

def f2list(to_list):
    return to_list.readlines()

def l2pseudo(to_pseudo):
    for line in to_pseudo:
        line_index = to_pseudo.index(line)
        line = str(line)
        line = re.split(r'(\s+)', line)
        for key, value in prefix_conversion_rules.items():
            if key in line:
                if not str(line[0]) == '':
                    line[0] = value + line[0]
                else:
                    line[2] = value + line[2]
        for key, value in basic_conversion_rules.items():
            for word in line:
                if key == str(word):
                    line[line.index(word)] = value
        for key, value in advanced_conversion_rules.items():
            for word in line:
                line[line.index(word)] = word.replace(key, value)
        for key, value in prefix_conversion_rules.items():
            for word in line:
                if word == key:
                    del line[line.index(word)]
        to_pseudo[line_index]= "".join(line)
    return(to_pseudo)

def p2file(to_file):
    file = open(python_file + '_pseudo.txt', 'w', encoding="utf8")
    for line in to_file:
        print(line, file=file)

def main():
    main_file = open(python_file, 'r+')
    work_file = f2list(main_file)
    work_file = l2pseudo(work_file)
    p2file(work_file)
    

main()