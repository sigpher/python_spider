from lxml import etree

# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''

# result = html.xpath('//ul/li/a/@href');
# print(result[-1])
# result = html.xpath('//*')
# for r in result:
#     print(r)
# print('---------------------------------')

# result = html.xpath('//li/..')
# print(result)
# print('---------------------------------')
# result = html.xpath('//li/a[@href]/../@class')
# print(result)

# result = html.xpath('//li[@class="item-0"]/a/text()')
# print(result)

# text = '''
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[@class="li"]/a/text()') 属性多值匹配:class = "li li-first"用这种写法是错误的
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//li[contains(@class, "li")]/a/text()')

print(result)

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[contains(@class, "li")  and @name="item"]/a/text()')
print(result)

result = html.xpath('//li[last()-1]/a/text()')
print(result)

result = html.xpath('//li[1]/ancestor::*')
print(result)