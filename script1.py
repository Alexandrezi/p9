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
def copie ():
	try:
		subprocess.call("mv /tmp/wordpress/ /var/www/html/", shell=True)
	except:
		print("erreur1")

def permission ():
	try:
		subprocess.call("chown -R www-data:www-data /var/www/html/wordpress/", shell=True)
	except:
		print("erreur2")

def permission1 ():
	try:
		subprocess.call("chmod 755 -R /var/www/html/wordpress/", shell=True)
	except:
		print("erreur3")

def donnee ():
	try:
		subprocess.call("scp alex@192.168.0.3:/home/alex/Documents/archive.tar.gz /tmp/archive.tar.gz", shell=True)
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

def copiewp ():
	try:
		subprocess.call("mv /tmp/home/alex/Documents/wordpress.conf /etc/apache2/sites-enabled/", shell=True)
	except:
		print("erreur2")

def mysqlinstall (password):
Définition pour créer la base de donnée mysql pour GLPI
	try:
		subprocess.run('mysql -e "CREATE DATABASE wordpress"', shell=True)
		subprocess.run('mysql -e "GRANT ALL PRIVILEGES ON wordpress.* TO wordpress_user@localhost IDENTIFIED BY \'"'+ password + '"\'"', shell=True)
	
	except:	
		print("erreur création database")
		
def BD1 ():
	try:
		subprocess.run('mysql wordpress < /tmp/home/alex/Documents/dump-file.sql', shell=True)
	except:
		print("erreur bd")
		
def a2enmod ():
	try:
		subprocess.run('a2enmod rewrite', shell=True)
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
copie()
permission()
permission1()
donnee()
untar2(vars['downloadFile2'], vars['extractdir'])
copiewp()
#mysqlinstall(vars['Passwordmysql'])
BD1()
a2enmod()
reload()
