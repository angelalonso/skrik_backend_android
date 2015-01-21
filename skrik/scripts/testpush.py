import urllib
import urllib2

url = 'https://android.googleapis.com/gcm/send'

api_key="AIzaSyCXEkhn03F5NPcigpOwLl95X3Wro4otRik"
regid="APA91bHmkV-RCOlmIe2SfjWOe3IxVmJdpViRoJJnJeK-AO0TtPJZF_eMxjiBx15j0VUvdj5GVmpOxBYiRP3dR8Ei3EPhazUFaFTPXT-CIkEGv3E6lx5VDfpB9XCc81C_OS2kEzPQxCBqHL7f5NeWhMxIRrq6HsohZQ"
#regid="APA91bHk_tEMCoRUGKYwSN2yCYD3g_SGO1rst7cDy0sQm_dSvahcsO8oiPxXXB5YrTu91ZNLaihEIAHy0XaLLdhraAIybuDyrlaQ9JDZgv7Pz-aiJ2ohKks05pDClAj8Q2t3mRndxUym8vNN9TUL-BRzaG1Pcp6KdA"

values = { 'registration_ids' : [ regid ], 'data' : { 'message' : 'Coni, hola!!!!!' , 'time' : '44'} }

data = urllib.urlencode(values)

#req = urllib2.Request(url, data)
req = urllib2.build_opener()
req.addheaders = [('Authorization', api_key)]
req.addheaders = [(' Content-Type', 'application/json')]
#response = urllib2.urlopen(req)
req.open(url)
 
