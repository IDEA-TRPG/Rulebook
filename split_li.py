import sys
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
