#!/bin/bash

api_key="AIzaSyCXEkhn03F5NPcigpOwLl95X3Wro4otRik"

regid=$1 

message=$2

curl --header "Authorization: key=$api_key" --header Content-Type:"application/json" https://android.googleapis.com/gcm/send  -d "{\"registration_ids\":[\"$regid\"],\"data\":{\"message\":\"$message\",\"time\":\"44\"}}"

