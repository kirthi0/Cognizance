from collections import Counter

with open('about.txt') as f1:
  fcon = f1.read().strip().split()
  f1.close()

l = []
for i in fcon:
  if len(i) >= 6:
    l.append(i)


count1 = Counter(l)
print(count1.most_common(1))
