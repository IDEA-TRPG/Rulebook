import sys
path = sys.argv[1]

arr = []
with open(path) as f:
  s = f.read()
  arr = s.split("======")

print(len(arr))
for i in range(len(arr)):
  with open('./CHAPTER{}.md'.format(i+1), mode='w') as f:
    f.write("  \n".join(arr[i].split('\n')))
