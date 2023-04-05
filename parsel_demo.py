from parsel import Selector

html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

selector = Selector(text=html)
result = selector.css('.item-0').getall()
print(result)

result = selector.css('.item-1.active').re('href="(.*?)"')
print(result)
result = selector.xpath('//li[contains(@class,"active")]').re('href="(.*?)"')
print(result)