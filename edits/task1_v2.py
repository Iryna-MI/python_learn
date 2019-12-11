from collections import Counter
import tkinter.filedialog

with open(tkinter.filedialog.askopenfilename(), "r", encoding="utf-8-sig") as f:
    book = f.read()
dictionary = Counter(book.replace(',','').replace('\'','').replace(':','').replace('-','').replace('--','').replace('?','').replace('!','').replace(';','').replace('.','').replace('[','').replace(']','').replace('&','').replace('"ACT +[IVXLCDM]"','ACT').replace('"SCENE +[IVXLCDM]+\\."','SCENE').lower().split())
file_to_save = tkinter.filedialog.asksaveasfilename(defaultextension = 'txt')
f = open(file_to_save, "w")
f.write('\n'.join('{:15} {:8}'.format(*item)+ " times" for item in sorted(dictionary.items())))
