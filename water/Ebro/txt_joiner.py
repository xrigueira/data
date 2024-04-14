"""This program gets the 4 different files of a
variable, joins them consequtively and makes some
format changes (header, dots, first and last line)"""

import os
# Define the files to join
folderNames = ['966 - EQ - Bombeo Les Olles Delta Ebro']

# List file names
archivos = os.listdir(folderNames[0])
archivos = list(dict.fromkeys([i[:-9] for i in archivos]))
print(archivos)

fileNames = ['absorbance', 'ammonium', 'conductivity', 'dissolved_oxygen', 'nitrates', 'pH', 'turbidity', 'water_flow_canal_A', 'water_flow_canal_B', 'water_flow_canal_C', 'water_flow_canal_D', 'water_level_canal_A', 'water_level_canal_B', 'water_level_canal_C', 'water_level_canal_D', 'water_temperature']


# Read a file and delete the first 10 lines
def rowDel(file_in, n_rows):

    # Define the name of the out file with the temp string added
    index = file_in.find('/') + 1
    file_out = file_in[:index] + 'temp_' + file_in[index:]

    with open(file_in, 'r', encoding='utf-8') as fin, open(file_out, 'w') as fout:
        # Skip the first n_rows lines
        for _ in range(n_rows):
            try:
                next(fin)
            except StopIteration:
                break
        # Copy the rest of the lines to the output file
        for line in fin:
            fout.write(line)

# Concatenates the clean files (without the firts 10 rows)
def concatenator(files, folderName, fileName):

    conc_file_name = f'{folderName}/{fileName}_{folderName[0:3]}.txt'
    with open(conc_file_name, 'w') as fout:
        for f in files:
            with open(f) as fin:
                for line in fin:
                    fout.write(line)
    
    return conc_file_name

# Add header and change the commas for dots
def header_doter(file_in):
    with open(file_in, 'r+') as fin:
        # Read the existing contents of the file
        contents = fin.read().replace(',', '.')

    # Insert a new line at the beginning of the file
    new_line = 'Date;Value\n'
    contents = new_line + contents

    with open(file_in, 'w') as fout:
        # Write the updated contents back to the file
        fout.write(contents)

# Check if first lines is 01-01-1999 00:00:00
def first_liner(file_in):
    with open(file_in, 'r+') as fin:
        # Read the existing contents of the file
        lines = fin.readlines()
        second_line = lines[1]
        
        if second_line[0:20] != '01-01-1999 00:00:00;':
            lines.insert(1, '01-01-1999 00:00:00;\n')
            fin.seek(0) # Move the file pointer to the beginning of the file
            fin.writelines(lines) # Write the rest of the lines

# Check if last line is 31-12-2022 23:45:00
def last_liner(file_in):
    with open(file_in, 'r+') as fin:
        # Read the existing contents of the file
        lines = fin.readlines()
        last_line = lines[-1]
        
        if last_line[0:20] != '31-12-2022 23:45:00;':
            lines.insert(-1, '31-12-2022 23:45:00;\n')
            fin.seek(0)
            fin.writelines(lines)


if __name__ == '__main__':

    for folderName in folderNames:

        for fileName in fileNames:
            print(fileName)
            files = [f'{folderName}/{fileName} 9904.txt', f'{folderName}/{fileName} 0510.txt',
                    f'{folderName}/{fileName} 1116.txt', f'{folderName}/{fileName} 1722.txt']

            files_temp = [f'{folderName}/temp_{fileName} 9904.txt', f'{folderName}/temp_{fileName} 0510.txt',
                        f'{folderName}/temp_{fileName} 1116.txt', f'{folderName}/temp_{fileName} 1722.txt']
            
            for f in files:
                print(f)
                rowDel(file_in=f, n_rows=11)

            conc_file_name = concatenator(files=files_temp, folderName=folderName, fileName=fileName)

            header_doter(file_in=conc_file_name)

            first_liner(file_in=conc_file_name)

            last_liner(file_in=conc_file_name)

            # Delete temp files
            for f in files_temp:
                os.remove(f)
