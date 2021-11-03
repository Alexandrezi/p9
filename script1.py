#!/usr/bin/python

import subprocess
import sys
import yaml
import requests
import tarfile


def readconf(monFichierYaml):
	try:
		with open (monFichierYaml, 'r') as stream:
			return yaml.safe_load(stream)
	except yaml.YAMLError as exc:
		print(exc)
		exit(1)

def installpackage (package):
	try:
		subprocess.call("apt install -y " + package, shell=True)
	except:
		print("erreur")
#def installmysql ():
#	try:
#		subprocess.call("apt install -y default-mysql-server", shell=True)
#	except:
#		print("erreur")

def telechargement (url, download):
	try :
		response = requests.get(url, allow_redirects=True)
		with open(download,'wb') as file:
			file.write(response.content)
	except:
		print("erreur")

def untar (file, path):
	try:
		if file.endswith("tar.gz"):
			tar = tarfile.open(file,"r:gz")
			tar.extractall(path)
			tar.close()
	except:
		print("erreur")
def copie (VarDir):
	try:
		subprocess.call('mv /tmp/wordpress/ '+VarDir+'', shell=True)
	except:
		print("erreur1")

def permission (VarDir):
	try:
		subprocess.call('chown -R www-data:www-data '+VarDir+'/wordpress/', shell=True)
	except:
		print("erreur2")

def permission1 (VarDir):
	try:
		subprocess.call('chmod 755 -R '+VarDir+'/wordpress/', shell=True)
	except:
		print("erreur3")

def donnee (identification):
	try:
		subprocess.call('scp '+IPUSER+':/home/alex/Documents/archive.tar.gz /tmp/archive.tar.gz', shell=True)
	except:
		print("erreur4")

def untar2 (file, path):
        try:
                if file.endswith("tar.gz"):
                        tar = tarfile.open(file,"r:gz")
                        tar.extractall(path)
                        tar.close()
        except:
                print("erreur")

def copiewp (workdir, siteenab):
	try:
		subprocess.call("mv '+workdir+'/wordpress.conf '+siteenab+'/", shell=True)
	except:
		print("erreur2")

def mysqlinstall (password):
	try:
		subprocess.run('mysql -e "CREATE DATABASE wordpress"', shell=True)
		subprocess.run('mysql -e "GRANT ALL PRIVILEGES ON wordpress.* TO wordpress_user@localhost IDENTIFIED BY \'"'+ password + '"\'"', shell=True)

	except:
		print("erreur création database")

def BD1 (workdir):
	try:
		subprocess.run('mysql wordpress < '+workdir+'/dump-file.sql', shell=True)
	except:
		print("erreur bd")

def repertory (workdir, VarDir):
	try:
		subprocess.run('cp -r '+workdir+'/wordpress '+VarDir+'/', shell=True)
	except:
		print("oooo")

def a2enmod ():
	try:
		subprocess.run('a2enmod rewrite', shell=True)
	except:
		print("erreur")

def suppression (siteenab):
	try:
		subprocess.run('rm '+siteenab+'/000-default.conf', shell=True)
	except:
		print("erreur")

def reload ():
	try:
		subprocess.run('systemctl restart apache2', shell=True)
	except:
		print("erreur")

file = sys.argv[1]
vars = readconf(file)
for package in vars['packages']:
	installpackage(package)
#installmysql()
telechargement(vars['URLWP'], vars['downloadFile'])
untar(vars['downloadFile'], vars['extractdir'])
copie(vars['varDirectory'])
permission(vars['varDirectory'])
permission1(vars['varDirectory'])
donnee(vars['addipuser'])
untar2(vars['downloadFile2'], vars['extractdir'])
copiewp(vars['WorkDirectory'], vars['dirsitesenab'])
mysqlinstall(vars['Passwordmysql'])
BD1(vars['WorkDirectory'])
repertory(vars['WorkDirectory'], vars['varDirectory'])
a2enmod()
reload()
suppression(vars['dirsitesenab'])

