#!/bin/bash

api_key="AIzaSyCXEkhn03F5NPcigpOwLl95X3Wro4otRik"

curl --header "Authorization: key=$api_key" --header Content-Type:"application/json" https://android.googleapis.com/gcm/send  -d "{\"registration_ids\":[\"APA91bHmkV-RCOlmIe2SfjWOe3IxVmJdpViRoJJnJeK-AO0TtPJZF_eMxjiBx15j0VUvdj5GVmpOxBYiRP3dR8Ei3EPhazUFaFTPXT-CIkEGv3E6lx5VDfpB9XCc81C_OS2kEzPQxCBqHL7f5NeWhMxIRrq6HsohZQ\"],\"data\":{\"message\":\"This is your message\",\"time\":\"44\"}}"

