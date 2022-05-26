import urllib.request

import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyANluorGzK8UVYVr1aZP5jyUuC5TUVyE6w",
  'authDomain': "brain-tumor-classificati-305af.firebaseapp.com",
  'databaseURL': "https://brain-tumor-classificati-305af-default-rtdb.firebaseio.com",
  'projectId': "brain-tumor-classificati-305af",
  'storageBucket': "brain-tumor-classificati-305af.appspot.com",
  'messagingSenderId': "884686939879",
  'appId': "1:884686939879:web:797f734679ef6ac6f3e442",
  'measurementId': "G-0ZY4WCGW0K"


}

firebase=pyrebase.initialize_app(firebaseConfig)
# db=firebase.database()
# auth=firebase.auth()
storage=firebase.storage()

path='model.json'
print(storage.child(path).get_url(None))
url=storage.child(path).get_url(None)
f=urllib.request.urlopen(url).read()

#print(f)
#load model from firebase

