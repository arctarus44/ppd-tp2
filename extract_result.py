import sys

slice = "slice_"

if __name__ == "__main__":
	nb_slice = int(sys.argv[1])
	result = 0
	for i in range(1, nb_slice):
		file = open(slice + str(i), 'r')
		result += eval(file.read())
		file.close()
	print(result * 4)
