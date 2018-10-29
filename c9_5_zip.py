import zipfile
import os
# Zip 实例化.
exampleZip = zipfile.ZipFile('c:\\A\\15chs_000.zip')
print(exampleZip.namelist())
# Zip 里单个文件的实例化.
jsonInfo = exampleZip.getinfo('JSON.txt')
# Zip 里单个文件信息.
print(jsonInfo.file_size)
print(jsonInfo.compress_size)

# Extracting from Zip files.
# Check current work directory.
print(os.getcwd())
# Change cwd
# os.chdir('c:\\A')
exampleZip = zipfile.ZipFile('c:\\A\\15chs_000.zip')
# If the folder does not exist, Python will create one.
exampleZip.extractall('c:\\A')
exampleZip.close()
# Extract single file from Zip.
exampleZip.extract('JSON.txt', 'c:\\A\\folders')
exampleZip.close()

