#!/usr/bin/python

import subprocess

def BD (workdir, login, password):
        try:
                subprocess.run('mysqldump -u '+login+' -p'+password+' wordpress > '+workdir+'dump-file.sql', shell=True)
        except:
                print("erreur")

def copie (workdir):
        try:
                subprocess.run('cp /etc/apache2/sites-available/wordpress.conf '+workdir, shell=True)
        except:
                print("erreur2")

def copie2 (workdir):
        try:
                subprocess.run('cp -r /var/www/html/wordpress '+workdir, shell=True)
        except:
                print('eee')

def tar (workdir):
        try:
                subprocess.run('tar -czvf archive.tar.gz '+workdir+'/wordpress.conf '+workdir+'/dump-file.sql '+workdir+'/wordpress', shell=True)
        except:
                print("erreur3")
def copiescp (workdir, distWorkdir, serveurDistant):
        try:
                subprocess.run('sudo -u alex scp '+workdir+'/archive.tar.gz '+serveurDistant+':'+distWorkdir+'/', shell=True)
        except:
                print("erreur4")


myWorkdir = "/home/alex/Documents"
distantWorkdir="/home/alex/Documents"
saveServer = "192.168.0.2"
login="root"
password="Alex0603!"
BD(myWorkdir, login, password)
copie(myWorkdir)
tar(myWorkdir)
copie2(myWorkdir)
copiescp(myWorkdir, distantWorkdir, saveServer)

