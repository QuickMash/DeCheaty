import requests
# DO NOT CHANGE THIS
version = '0.0.1'
# Download location
r = requests.get('http')
print(version,'\nGetting Version...')
print(r.status_code)
if r.status_code == '200':
  print('Connected!')
# More code to download this github repo
else:
  print('Failed')
