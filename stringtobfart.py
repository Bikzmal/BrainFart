import sys

if len(sys.argv) < 2:
	print("Usage: python3 stringtobfart.py <string>")
	sys.exit(1)

string = " ".join(sys.argv[1:])

code = "c"

for c in string:
	x = ord(c)
	y = 0
	while y != x:
		if (y+10) * 10 <= x:
			code += "A"
			y += 10
		elif (y+1) * 10 <= x:
			code += "a"
			y += 1
		elif y * 10 <= x:
			code += "m"
			y *= 10
		elif y + 10 <= x:
			code += "A"
			y += 10
		elif y + 1 <= x:
			code += "a"
			y += 1
	code += "oc"

print(code)
