filename = "main.bfart"
with open(filename, "r") as file:
	code = file.read()

cells = [0]
pointer = 0
lim = 256
clim = 16
out = ""

def move_pointer(n):
	global pointer, cells, lim
	pointer += n
	if pointer < 0:
		pointer = len(cells) - 1
	elif pointer >= len(cells):
		pointer = 0

for c in code:
	match c:
		case "!":
			if not len(cells) == clim:
				cells.append(0)
		case "?":
			if len(cells) > 1:
				cells.pop()
		case "x":
			cells = [0 for i in range(clim)]
		case "r":
			move_pointer(1)
		case "l":
			move_pointer(-1)
		case "a":
			cells[pointer] += 1
			cells[pointer] %= lim
		case "A":
			cells[pointer] += 10
			cells[pointer] %= lim
		case "s":
			cells[pointer] -= 1
			if cells[pointer] < 0:
				cells[pointer] = lim + cells[pointer]
		case "S":
			cells[pointer] -= 10
			if cells[pointer] < 0:
				cells[pointer] = lim + cells[pointer]
		case "m":
			cells[pointer] *= 10
			cells[pointer] %= lim
		case "d":
			cells[pointer] //= 10
		case "o":
			out += chr(cells[pointer])
		case "O":
			for i in cells:
				out += chr(i)
		case "c":
			cells[pointer] = 0
		case "C":
			cells = [0 for i in range(len(cells))]
		case "@":
			print(cells[pointer])
		case "#":
			print(*cells)
			print(pointer)
		case ">":
			_pointer = (pointer + 1) if pointer + 1 < len(cells) else 0
			cells[_pointer] = cells[pointer]
		case "<":
			_pointer = (pointer - 1) if pointer - 1 >= 0 else len(cells) - 1
			cells[_pointer] = cells[pointer]
		case "=":
			move_pointer(-1)
			val1 = cells[pointer]
			move_pointer(1)
			val2 = cells[pointer]
			if val1 != val2:
				move_pointer(1)
			else:
				move_pointer(2)
		case "i":
			inp = input("> ")
			cells[pointer] = ord(inp[0]) if len(inp) > 0 else ord(" ")
		case other:
			continue

print(out)