from bs4 import BeautifulSoup

with open(r"D:\Python\Python Workshop\Books .html",'r') as file:
    soup = BeautifulSoup(file, 'lxml')
    
# print(soup.contents)  

tag=soup.find('title')
print(tag)

# find=soup.find(id='product_pod')
# print(find)

# for tag in soup.find_all(True):
#     print(tag.name)
#     print(tag.get('class'))
#     print(tag.get('id'))


