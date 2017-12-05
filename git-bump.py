import sys
from subprocess import check_output

arg = sys.argv[1]

if (len(arg) > 1):
	version_array = check_output("git tag --sort=-creatordate").decode().split('\n')
	last_version = version_array[0].split('.')
	
	if(len(last_version) < 2):
		last_version.append('0')
	
	if(len(last_version) < 3):
		last_version.append('0')
	
	if(arg == '-b'):
		last_version[2] = str(int(last_version[2])+1)
		next_version = last_version[0] + '.' + last_version[1] + '.' + last_version[2]
	elif (arg == '-f'):
		last_version[1] = str(int(last_version[1])+1)
		next_version = last_version[0] + '.' + last_version[1] + '.0'
	elif (arg == '-v'):
		last_version[0] = str(int(last_version[0])+1)
		next_version = last_version[0] + '.0.0'
	else:
		print ('Parâmetro Inválido')
		
		
	print (check_output("git tag " + next_version).decode())
		
	print ('--- Versão Criada ----')
	print (next_version)
	
	print (check_output("git push origin " + next_version).decode())
		
else:	
	print ("Especifique se é -b bug -f feature ou -v version")