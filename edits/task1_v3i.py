from collections import Counter
import re
import tkinter.filedialog

words = re.findall(r'\w+', open(tkinter.filedialog.askopenfilename()).read().replace(',','').replace('\'','').replace(':','').replace('-','').replace('--','').replace('?','').replace('!','').replace(';','').replace('.','').replace('[','').replace(']','').replace('&','').replace('"ACT +[IVXLCDM]"','ACT').replace('"SCENE +[IVXLCDM]+\\."','SCENE').lower())
with open(tkinter.filedialog.asksaveasfilename(defaultextension = 'txt'), "w", encoding="utf-8-sig") as f:
    f.write('\n'.join('{:15} {:8}'.format(*item)+ " times" for item in sorted(Counter(words).items())))


