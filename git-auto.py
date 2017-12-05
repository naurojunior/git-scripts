import sys
from subprocess import check_output

if (len(sys.argv) > 1):
	print ("---- Pull ----")
	print (check_output("git pull").decode())
	print ("---- Add ----")
	print (check_output("git add -A").decode())
	print ("---- Commit ----")
	print (check_output('git commit -m "' + sys.argv[1] + '"').decode())
	print ("---- Push ----")
	print (check_output("git push").decode())
else:
	print ("Insira a mensagem de commit")