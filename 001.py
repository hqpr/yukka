# -*- coding: utf-8 -*-
#! /usr/bin/env python

import urllib
import re
import csv
import lxml.html

page = 'page.htm'

# Saving to csv list of titles and urls from page
# First cycle on category page

#writer = csv.writer(open('list_of_products.csv', 'wb+'), delimiter=';', quotechar='"')
#c = urllib.urlopen(page)
#doc = lxml.html.document_fromstring(c.read())
#for item in doc.cssselect('h2.product-name a'):
#        name = item.text
#        urls = item.get('href')
#        writer.writerow([name, urls])
#print 'File created'

# Second cycle with reading list of urls
product = {}
reader = csv.reader(open('list_of_products.csv', 'rb'), delimiter=';', quotechar='"')
for row in reader:
    c1 = urllib.urlopen(row[1])     # [1] == url // [0] == Product title
    doc1 = lxml.html.document_fromstring(c1.read())
    for img in doc1.cssselect('div.more-views a'):
        images = img.get('href')        # Images
        if not row[0] in product:
            product.update({row[0]: []})
        product[row[0]].append(images)
    for desc in doc1.cssselect('div.product-tabs-content div'):
        description = desc.text
        description = description.encode('utf-8')
        description = description.replace('-', '')
        product[row[0]].append(description)

    c1 = urllib.urlopen(row[1])
    match = re.findall(r'SKU(\d+)| Brand\:[<]\/span[>](.*)', c1.read())
    for m in match:
        sku = 'SKU%s' % m[0]       # SKU
        product[row[0]].append(sku)
        brand = m[1]        # Brand
        product[row[0]].append(brand)
    product[row[0]].append(row[1])
writer2 = csv.writer(open('product_details.csv', 'wb+'), delimiter=';', quotechar='"')
for k, v in product.items():
    writer2.writerow([k, v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7], v[8], v[9], v[10], v[11], v[12], v[13], v[14], v[15], v[16]])
print 'All done'







# Pagination
# Сделать, чтобы сначала была проверка на наличие страниц
#for pagination in doc.cssselect('div.pages li a'):
#    print pagination.get('href')
