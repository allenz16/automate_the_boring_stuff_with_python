# Usage : py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#         py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#         py.exe mcb.pyw list - Loads all keywords to clipboard.
#         py.exe mcb.pyw delete - Deletes all keywords.

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')
# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] == pyperclip.paste()
    print(mcbShelf)
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    #if sys.argv[1].lower() == 'delete':
        #mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()




