import requests
url = 'http://web.cmdm.tw:9999/upload'
url2 = 'http://httpbin.org/post'

files = {'files':open('./data/success.jpg','rb')}
files2 = {'files':open('./data/TestCompounds.sdf','rb')}

data = {'filename':'success.jpg'}
data2 = {'filename':'TestCompounds.sdf'}

r = requests.post(url, files=files, data=data)
print(r.text)
r = requests.post(url2, files=files, data=data)
print(r.text)

r = requests.post(url, files=files2, data=data2)
print(r.text)
with open('result.txt','w') as f:
    f.write(r.text)
    f.close()
r = requests.post(url2, files=files2, data=data2)
print(r.text)
