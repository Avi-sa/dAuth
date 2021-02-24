from django.shortcuts import render 
from json import dumps 
  
  
def send_dictionary(request): 
    
    usr = request.user.username 
    dataDictionary = { 
        'hello': usr
    } 
    # dump data 
    dataJSON = dumps(dataDictionary) 
    return render(request, 'pic.html', {'data': dataJSON}) 
