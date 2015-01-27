CREATE TABLE msging ( id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
          userid_from BIGINT NOT NULL,
          userid_to BIGINT NOT NULL,
          message VARCHAR(250),
          status VARCHAR(4) NOT NULL,
          timestamp INT(14)
        );


http://www.epochconverter.com/programming/mysql-from-unixtime.php

select count(*), userid_from, FROM_UNIXTIME(MAX(timestamp)) from msging where userid_to=16101848762844 group by userid_from;


Get current epoch time	SELECT UNIX_TIMESTAMP(NOW()) (now() is optional)
Today midnight	SELECT UNIX_TIMESTAMP(CURDATE())
Yesterday midnight	SELECT UNIX_TIMESTAMP(DATE_ADD(CURDATE(),INTERVAL -1 DAY))
Convert from date to epoch	SELECT UNIX_TIMESTAMP(timestring)
Time format: YYYY-MM-DD HH:MM:SS or YYMMDD or YYYYMMDD
Convert from epoch to date 	SELECT FROM_UNIXTIME(epoch timestamp, optional output format)
The default output is YYY-MM-DD HH:MM:SS
FROM_UNIXTIME doesn't work with negative timestamps


