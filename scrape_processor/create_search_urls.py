url = 'https://www.amazon.com/s?k=processor&i=computers-intl-ship&ref=nb_sb_noss'

f =  open('scrape_processor/search_urls.txt', 'w')
f.write(url)
f.write('\n')
for i in range(2,200):
    url= 'https://www.amazon.com/s?k=processor&i=computers-intl-ship&page='+ str(i) + '&qid=1594554220&ref=sr_pg_'+ str(i)
    f.write(url)
    f.write('\n')
f.close()