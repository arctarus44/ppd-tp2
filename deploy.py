import os
import re
import subprocess as subp

BORNE_MAX = 20000
MACHINES_CMD = "cat $OAR_FILE_NODES | uniq"
NB_MACHINES_CMD = "cat $OAR_FILE_NODES | uniq | wc -l"

SCRIPT_PI = "pi.py"

if __name__ == "__main__":
	machines = os.popen(MACHINES_CMD).read()
	nb_machines = str(os.popen(NB_MACHINES_CMD).read())

	machines = re.split("\n", machines)

	intervalle = BORNE_MAX / nb_machines

	borne_min = 0
	borne_max = intervalle

	p = []
	for i in range(0, nb_machines):
		p[i] = subp.Popen(["oarsh", machines[i], SCRIPT_PI, i, borne_min, borne_max])

	for i in range(0, nb_machines):
		p[i].terminate()

	files = [f for f in os.listdir('.') if re.match(r'slice_[0-9]*', f)]
	for f in files:
		file = open(f)
		result += eval(file.read())
		file.close()
	print(result * 4)
