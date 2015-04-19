What you will need to make this Backend work:

- Install some required packages 
# apt-get install libapache2-mod-wsgi libapache2-mod-python python-setuptools python-pip libmysqlclient-dev python-dev

- Use PIP to add some spices to python (Django amongst them)
# pip install Django MySQL-python python-gcm

#cp skrik.conf /etc/apache2/sites-available/skrik.conf
#ln -s /etc/apache2/sites-available/skrik.conf /etc/apache2/sites-enabled/skrik.conf

You might then want to modify that file to your needs. If this is the only web you'll be serving, you might as well want to do the following cleanup:
# rm /etc/apache2/sites-enabled/000-default.conf

- Load the Database structure and user privileges
#myql -u root -p < skrik.sql

cp apache2.conf apache2.conf.orig



NO -> https://code.djangoproject.com/wiki/django_apache_and_mod_wsgi
http://stackoverflow.com/questions/18012456/deploying-django-with-apache




TWO TABLES NEEDED:

CREATE TABLE users ( id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
          name VARCHAR(50) NOT NULL,
          email VARCHAR(100) NOT NULL,
	  phone VARCHAR(20) NOT NULL,
          reg_id VARCHAR(200),
          pass VARCHAR(100),
          status VARCHAR(250) NOT NULL
        );


CREATE TABLE msgs ( id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
          userid_from BIGINT NOT NULL,
          userid_to BIGINT NOT NULL,
          message VARCHAR(250),
          status VARCHAR(14) NOT NULL,
          timestamp INT(14)
        );




http://www.epochconverter.com/programming/mysql-from-unixtime.php

select count( * ), userid_from, FROM_UNIXTIME(MAX(timestamp)) from msging where userid_to=16101848762844 group by userid_from;


Get current epoch time	SELECT UNIX_TIMESTAMP(NOW()) (now() is optional)
Today midnight	SELECT UNIX_TIMESTAMP(CURDATE())
Yesterday midnight	SELECT UNIX_TIMESTAMP(DATE_ADD(CURDATE(),INTERVAL -1 DAY))
Convert from date to epoch	SELECT UNIX_TIMESTAMP(timestring)
Time format: YYYY-MM-DD HH:MM:SS or YYMMDD or YYYYMMDD
Convert from epoch to date 	SELECT FROM_UNIXTIME(epoch timestamp, optional output format)
The default output is YYY-MM-DD HH:MM:SS
FROM_UNIXTIME doesn't work with negative timestamps

If anything fails drop me an e-Mail to angelalonso@fonseca.de.com
