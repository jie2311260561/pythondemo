import requests
import webbrowser

# param = {"wd","莫凡Python"} #搜索信息
# r = requests.get('http://www.baidu.com/s', params=param)
# print(r.url)
# webbrowser.open(url)
#都封装成字典类型
# data = {'firstname':'莫烦','lastname':'周'}
# r = requests.post('http://pythonscraping.com/files/processing.php', data=data)
# print(r.text)

#上传图片 封装成字典类型
# file = {'urloadFile',open('./imanger.png','rb')}
# r=requests.post('http://pythonscraping.com/files/processing2.php', files=file)

payload = {'username': 'Morvan', 'password': 'password'}
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())

# {'username': 'Morvan', 'loggedin': '1'}
r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
print(r.text)