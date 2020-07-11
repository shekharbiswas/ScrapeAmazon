f =  open('scrape_mouse/search_urls.txt', 'w')
url = 'https://www.amazon.com/s?k=mouse&i=computers-intl-ship&ref=nb_sb_noss_2'
f.write(url)
f.write('\n')

for i in range(2,200):
    url= 'https://www.amazon.com/s?k=mouse&i=computers-intl-ship&page='+ str(i) + '&qid=1594378041&ref=sr_pg_'+ str(i)
    f.write(url)
    f.write('\n')
    
f.close()