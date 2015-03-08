import sys

if __name__ == "__main__":
	if len(sys.argv) == 1:		# Ici commence le master
		# reserver les ressources et lancer le script
		pass
	else:
		start = int(sys.argv[1])
		end = int(sys.argv[2])
		slice = sys.argv[3]
		res = 0
		for k in range(start, end):
			res += ((-1) ** k)/(2 * k + 1)
		f = open("slice_" +slice, 'w')
		f.write(str(res))
		f.close()
