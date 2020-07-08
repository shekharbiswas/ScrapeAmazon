f =  open('scrape_monitor/search_urls.txt', 'w')
for i in range(2,282):
    url= 'https://www.amazon.com/s?k=monitor&i=electronics-intl-ship&page='+ str(i) + '&qid=1594132600&ref=sr_pg_'+ str(i)
    f.write(url)
    f.write('\n')
f.close()