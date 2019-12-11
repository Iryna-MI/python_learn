from collections import Counter
with open(r"D:\Book.txt", "r", encoding="utf-8-sig") as file_name:
    book = file_name.read()

f = open(r"D:\dictionary.txt", "w")
dictionary = Counter(book.replace(',','').replace('\'','').replace(':','').replace('-','').replace('--','').replace('?','').replace('!','').replace(';','').replace('.','').replace('[','').replace(']','').replace('&','').replace('"ACT +[IVXLCDM]"','ACT').replace('"SCENE +[IVXLCDM]+\\."','SCENE').lower().split())
f.write('\n'.join('{:15} {:8}'.format(*item)+ " times" for item in sorted(dictionary.items())))
f.close()



