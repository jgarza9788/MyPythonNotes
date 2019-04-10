import requests



url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL'

r = requests.get(url)

# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
# print(r.text)
# print(r.json())

indicators = ['Open','Bid','Ask','52 Week Range','Avg. Volume']


print(r.text)
# htmltxt = r.text

# s = htmltxt.split("Previous Close")
# print(len(s))
# print(s[1][:500])

# s = htmltxt.split("\"Previous Close\"")
# print(len(s))
# print(s[1][:2000])


# import re
# s = re.findall(">.*<",htmltxt)
# # print(s)

# for i in s:
#     print(i)