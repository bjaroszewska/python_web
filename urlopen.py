import urllib.request
import urllib.parse

f = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
counts=dict()
for line in f:
	words = line.decode().split()
	entirePage = line.decode().strip()
	#print(entirePage)
	for word in words:
		counts[word] = counts.get(word,0) +1

print(counts)