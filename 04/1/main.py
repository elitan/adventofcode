import hashlib

s_template = "iwrupvqb"
i = 0
while hashlib.md5("%s%d" % (s_template, i)).hexdigest()[:5] != "00000":
	i += 1

print(hashlib.md5("%s%d" % (s_template, i)).hexdigest())
print("%d" % (i))
