import zipfile
# 'w' will overwrite, 'a' will append.
newZip = zipfile.ZipFile('c:\\A\\new.zip', 'w')
newZip.write('c:\\A\\bFile.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
