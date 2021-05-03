
Windows Terminal

# Be.Vegan  
Aplikacja na programowanie zespołowe 2k19/2k20  
  
Aby włączyć wirtualne środowisko użyj skryptu Be.Vegan/start  
```bash  
source start  
```  
Aby pobrać wszystkie potrzebne biblioteki do uruchomienia serwera Backendowego użyj  
```  
pip3 install -r requirements.txt --user  
```  
Aby uruchomić serwer Backendowy  
- przejdź do katalogu ``src`` 
- uruchom komendę ```python3 manage.py runserver```  
  
Aby pobrać wszystkie potrzebne biblioteki do uruchomienia serwera Frontendowego  
- przejdź do katalogu ```wegamania-web```  
- użyj komendy ```npm install```  
  
Aby uruchomić serwer Frontendowy  
- przejdź do katalogu ```wegamania-web```  
- użyj komendy ```npm start```  
  
  
# Virtualenv  
Ponieważ nasza aplikacja korzysta z wielu różnych bibliotek, korzystamy z virtualenv, aby ułatwić proces korzystania z a  
plikacji.  
Aktywacja środowiska:  
``` source env/bin/activate ```  
``` source nenv/bin/activate ```  
  
Po prawidłowym wykonaniu komend shell powinien wyglądać następująco:  
  
(nenv)(env) user@shell:~  
  
  
  
# MYSQL instalacja  
```sudo apt-get install python-dev default-libmysqlclient-dev  
sudo apt-get install mysql-server -y  
wget http://repo.mysql.com/mysql-apt-config_0.8.13-1_all.deb  
sudo dpkg -i mysql-apt-config_0.8.13-1_all.deb  
pip3 install mysqclient
``` 
  
Potem dajemy bazę ```Veggies_db``` do ```/var/lib/mysql/```
i włączamy  
  
baza w mysql powinna dać uprawnienia dla Django do logowania do niej:  
```ALTER USER root@localhost IDENTIFIED WITH mysql_native_password BY 'Veggies1982xxf';  ```
ale to powinno już być zrobione  
  
  
pomoc do mysql'a  
https://idroot.us/install-mysql-server-debian-10/  
  
# Mongo DB instalacja  
https://docs.mongodb.com/manual/tutorial/install-mongodb-on-debian/

# Docker deployment
It is possible to deploy veggies on docker using docker-compose.
## Requirements
* Installed docker and docker-compose 
* Installed npm  
## Start 
To start docker container use:
```sh docker-compose up```
in main directory.
## Troubleshooting
### Postgres database 
If there is en error inform that database isn't exist, change line from 'docker-compose.yml'

'command: python manage.py runserver 0.0.0.0:8000' to 'command: python manage.py migrate'.

Wait till migration will made and container will turn off. Then run again project with previous command.
### Nodejs 
If there is problems with web container go to `wegemania-web` directory and run: `npm install`. 
