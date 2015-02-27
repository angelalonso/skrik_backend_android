from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from sql_funcs import *



@csrf_exempt
def add_message(self, *args, **kwargs):
  message = kwargs.pop('message', None)
  userfrom = kwargs.pop('userfrom', None)
  userto = kwargs.pop('userto', None)
  timestamp = kwargs.pop('timestamp', None)

  query = ('insert into skrik.msgs (userid_from,userid_to,message,status,timestamp) values ("' + userfrom + '","' + userto + '","' + message + '","sent",' + timestamp + ');')

  result_aux = runquery(query)

  query_id = ('SELECT max(id) from skrik.msgs;')
  result_id = runquery(query_id)
  
  result = "received " + str(result_id[0])

  return HttpResponse(result)

