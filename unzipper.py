import zipfile
import os

def unzip_recursive(zip_file_path, output_dir, iterations):
    for i in range(iterations):
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
            zip_file_path = os.path.join(output_dir, zip_ref.namelist()[0])

# Sostituisci 'tuo_file.zip' con il percorso effettivo del tuo file zip
zip_file_path = 'C:\\Users\\qualc\\Desktop\\flag3000.zip'

# Sostituisci 'output_directory' con la directory in cui desideri estrarre i file
output_directory = 'C:\\Users\\qualc\\Desktop\zip'

# Sostituisci 300 con il numero effettivo di iterazioni
numero_iterazioni = 3000

unzip_recursive(zip_file_path, output_directory, numero_iterazioni)
