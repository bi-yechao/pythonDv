import requests

#github的searchapi的使用有改变跟书上不同
url = 'https://api.github.com/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)

response_dict = r.json()

#response_dict是包含多个字典的列表，书上直接访问response_dict.keys()是错的？
print(response_dict[0].keys())

print('Total repositories:'+response_dict[0]['total_count'])