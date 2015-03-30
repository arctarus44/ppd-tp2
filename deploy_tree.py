import os
import re
import subprocess as subp

BORNE_MAX = 20000
MACHINES_CMD = "cat $OAR_FILE_NODES | uniq | sort"
NB_MACHINES_CMD = "cat $OAR_FILE_NODES | uniq | wc -l"

SCRIPT_PI = "ppd-tp2/pi.py"

def extract_result():
	files = [f for f in os.listdir('/home/adewarumez/ppd-tp2/') if re.match(r'slice_[0-9]*', f)]
	result = 0
	for f in files:
		print f
		slicefile = open(f)
		result += eval(slicefile.read())
		slicefile.close()

	resultf = open("result.txt", 'w')
	resultf.write(str(result * 4))
	resultf.close()

if __name__ == "__main__":

	# Recuperation de la liste des machines
	machines = os.popen(MACHINES_CMD).read()
	nb_machines = int(str(os.popen(NB_MACHINES_CMD).read()))

	machines = re.split("\n", machines)

	intervalle = BORNE_MAX / nb_machines

	# Recuperation de la tache courante
	task = sys.argv[1]

	# Lancement de la tache local
	borne_min = task * intervalle
	borne_max = borne_min + intervalle
	print "tache " + str(task) + " : calcul pi."
	p[1] = subp.Popen(["oarsh", machines[task], "python " +  SCRIPT_PI + " "+ str(task1) +" " +  str(borne_min) + " " + str(borne_max)])

	# Determination des taches a lancer
	task1 = task * 2
	task2 = task1 + 1

	# Lancement des sous taches 1 et 2
	p = [None]*(3)
	if task1 <= len(machines) - 1:
		borne_min = task1 * intervalle
		borne_max = borne_min + intervalle
		print "tache " + str(task) + " : deploy task " + str(task1) + "."
		p[0] = subp.Popen(["oarsh", machines[task1], "python " +  SCRIPT_PI + " "+ str(task1) +" " +  str(borne_min) + " " + str(borne_max)])

	if task2 <= len(machines) - 1:
		borne_min = task1 * intervalle
		borne_max = borne_min + intervalle
		print "tache " + str(task) + " : deploy task " + str(task2) + "."
		p[1] = subp.Popen(["oarsh", machines[task2], "python " +  SCRIPT_PI + " "+ str(task1) +" " +  str(borne_min) + " " + str(borne_max)])

	# Attente des taches locales et des sous taches
	print "tache " + str(task) + " : attente resultats."
	for i in range(0, 3):
		p[i].wait()

	if task == 0:
		print "tache " + str(task) + " : extract result."
		extract_result()
