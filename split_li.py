import sys
import os
path = sys.argv[1]

arr = []
with open(path, "r", encoding='utf-8') as f:
  s = f.read()
  s = s.replace('\r', '')
  arr = s.split("======")

print(len(arr))
for i in range(len(arr)):
  with open('./CHAPTER{}.md'.format(i+1), mode='w', encoding='utf-8', newline='\n') as f:
    f.write("  \n".join(arr[i].split('\n')))

with open("./CHAPTER1.md", "r", encoding='utf-8') as f:
  s = f.read()
  print(s)

# 変更前ファイル
path1 = './book_li.json'

# 変更後ファイル
path2= './book.json'

# ファイル名の変更
os.rename(path1, path2)
