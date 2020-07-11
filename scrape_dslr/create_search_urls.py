f =  open('scrape_dslr/search_urls.txt', 'w')
for i in range(2,282):
    url= 'https://www.amazon.com/s?k=dslr+camera&i=electronics-intl-ship&page='+ str(i) + '&crid=S9NG40B69HIE&qid=1594465841&sprefix=DSL%2Celectronics-intl-ship%2C244&ref=sr_pg_'+ str(i)
    f.write(url)
    f.write('\n')
f.close()