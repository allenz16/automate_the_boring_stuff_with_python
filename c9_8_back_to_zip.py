import zipfile
import os
import shutil


def backup_to_zip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number = number + 1
    # Create the zip file.
    print('Creating %s...' % zip_filename)
    backup_zip = zipfile.ZipFile(zip_filename, 'w')
    for folder_name, sub_folders, file_names in os.walk(folder):
        print('Adding files in %s...' % folder_name)
        # Add the current folder to the zip file.
        backup_zip.write(folder_name)
        # Add all the files in this folder to the zip file.
        for filename in file_names:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue  # Don't backup the zip files
            backup_zip.write(os.path.join(folder_name, filename))
    backup_zip.close()
    print('Done.')


backup_to_zip('c:\\A')




