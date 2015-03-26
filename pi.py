import os
import sys

if __name__ == "__main__":
	if len(sys.argv) == 1:		# Ici commence le master
		# reserver les ressources et lancer le script
		pass
	else:
		slice = sys.argv[1]
		start = int(sys.argv[2])
		end = int(sys.argv[3])
		res = 0
		for k in range(start, end):
			res += ((-1) ** k)/(2 * k + 1)
		f = open(os.path.join(os.getcwd(), "slice_" + slice)  , 'w')
		f.write(str(res))
		f.close()
