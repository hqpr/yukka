# -*- coding: utf-8 -*-
#! /usr/bin/env python

import urllib
import re
import csv
import lxml.html
import time


page = 'http://www.yukka.co.uk/men/mens-clothing/hats-caps.html'

# Saving to csv list of titles and urls from page
# First cycle on category page

writer = csv.writer(open('list_of_products.csv', 'wb+'), delimiter=';', quotechar='"')
c = urllib.urlopen(page)
doc = lxml.html.document_fromstring(c.read())
for item in doc.cssselect('h2.product-name a'):
        name = item.text
        urls = item.get('href')
        writer.writerow([name, urls])
print 'CSV File created (Category Page was Successfully Parsed)'

# Second cycle with reading list of urls

product = {}        # Main dict with all data
reader = csv.reader(open('list_of_products.csv', 'rb'), delimiter=';', quotechar='"')
print 'Open the CSV File'

for row in reader:
    time.sleep(2)
    c1 = urllib.urlopen(row[1])     # [1] == url // [0] == Product title
    doc1 = lxml.html.document_fromstring(c1.read())
    for img in doc1.cssselect('div.more-views a'):
        images = img.get('href')        # Images
        if not row[0] in product:
            product.update({row[0]: []})
        product[row[0]].append(images)
    print '[IN WORK] %s' % row[0]

    for desc in doc1.cssselect('div.product-tabs-content div'):
        description = desc.text
        try:
            description = description.encode('utf-8')
        except:
            pass
        try:
            description = description.replace('-', '')
        except:
            pass
        try:
            product[row[0]].append(description)
        except:
            pass

    c1 = urllib.urlopen(row[1])
    match = re.findall(r'SKU(\d+)| Brand\:[<]\/span[>](.*)', c1.read())
    for m in match:
        sku = 'SKU%s' % m[0]       # SKU
        product[row[0]].append(sku)
        brand = m[1]        # Brand
        product[row[0]].append(brand)
    try:
        product[row[0]].append(row[1])
    except:
        pass
writer2 = csv.writer(open('product_details.csv', 'ab+'), delimiter=';', quotechar='"')
for k, v in product.items():
#        print '%s -> %s' % (k, len(v))
    if len(v) == 18:
        writer2.writerow([k, v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7], v[8], v[9], v[10], v[11], v[12], v[13], v[14], v[15], v[16], v[17]])
    elif len(v) == 17:
        writer2.writerow([k, v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7], v[8], v[9], v[10], v[11], v[12], v[13], v[14], v[15], v[16]])
    elif len(v) == 16:
        writer2.writerow([k, v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7], v[8], v[9], v[10], v[11], v[12], v[13], v[14], v[15]])
    elif len(v) == 15:
        writer2.writerow([k, v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7], v[8], v[9], v[10], v[11], v[12], v[13], v[14]])
    elif len(v) == 14:
        writer2.writerow([k, v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7], v[8], v[9], v[10], v[11], v[12], v[13]])
    elif len(v) == 13:
        writer2.writerow([k, v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7], v[8], v[9], v[10], v[11], v[12]])
    elif len(v) == 12:
        writer2.writerow([k, v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7], v[8], v[9], v[10], v[11]])
    elif len(v) == 11:
        writer2.writerow([k, v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7], v[8], v[9], v[10]])
    elif len(v) == 10:
        writer2.writerow([k, v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7], v[8], v[9]])
    elif len(v) == 9:
        writer2.writerow([k, v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7], v[8]])
    elif len(v) == 8:
        writer2.writerow([k, v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7]])
    elif len(v) == 7:
        writer2.writerow([k, v[0], v[1], v[2], v[3], v[4], v[5], v[6]])
    elif len(v) == 6:
        writer2.writerow([k, v[0], v[1], v[2], v[3], v[4], v[5]])
    elif len(v) == 5:
        writer2.writerow([k, v[0], v[1], v[2], v[3], v[4]])
    elif len(v) == 4:
        writer2.writerow([k, v[0], v[1], v[2], v[3]])
    else:
        pass
#            print '[ERROR] %s' % k



# Pagination
# Сделать, чтобы сначала была проверка на наличие страниц
#for pagination in doc.cssselect('div.pages li a'):
#    print pagination.get('href')
