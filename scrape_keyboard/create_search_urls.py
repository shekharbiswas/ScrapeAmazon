f =  open('scrape_keyboard/search_urls.txt', 'w')
url = 'https://www.amazon.com/s?k=keyboard&i=computers-intl-ship&crid=S4CZCD6PTNU6&qid=1594377050&sprefix=key%2Caps%2C252&ref=sr_pg_1'
f.write(url)
f.write('\n')

for i in range(2,350):
    url= 'https://www.amazon.com/s?k=keyboard&i=computers-intl-ship&page='+ str(i) + '&crid=S4CZCD6PTNU6&qid=1594377044&sprefix=key%2Caps%2C252&ref=sr_pg_'+ str(i)
    f.write(url)
    f.write('\n')
f.close()