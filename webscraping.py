from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
    <div id="section-1">
        <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquid odio nostrum maiores voluptatum, perferendis enim perspiciatis dolorum accusamus tempore suscipit porro magnam provident quam ab assumenda harum distinctio quae iusto?
        </p>
    </div>
    <div id="section-2">
        <ul class="items">
            <li class="item">11</li>
            <li class="item">22</li>
            <li class="item">33</li>
            <li class="item">44</li>
            <li class="item">55</li>
        </ul>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

## Direct

#print(soup.body)
#print(soup.head)
#print(soup.body.div)

## find()

#lol = soup.find(id='section-2')
#lol = soup.find(class_='items')
#lol = soup.find(attrs={"data-hello":"hi"})

## find_all() && findAll()

#lol = soup.findAll('div')
#lol = soup.findAll('div')[1]

## select
#lol = soup.select('#section-1')
#lol = soup.select('.item')[0]

## get_text()
#lol = soup.find(class_='item').get_text()

#for item in soup.select('.item'):
#    print(item.get_text())

# Navigation
#lol = soup.body.contents[1].contents[1].next_sibling.next_sibling  .find_next_sibling()
lol = soup.find(id='section-2').find_previous_sibling()
lol = soup.find(class_='item').find_parent()

print(lol)