import bs4, requests

res = requests.get('https://open.spotify.com/user/spotify/playlist/37i9dQZEVXcHtRRcrSdDK2')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "lxml")
art = soup.find('meta', property='music:song')
#print(art['content'])
res2 = requests.get(art['content'])
soup2 = bs4.BeautifulSoup(res2.text, "lxml")
sname = soup2.find('meta', property='og:title')
artistUrl = soup2.find('meta', property='music:musician')
artistReq = requests.get(artistUrl['content'])
artistSoup = bs4.BeautifulSoup(artistReq.text, "lxml")
artistName = artistSoup.find('meta', property='og:title')
print(sname['content']+' - ' + artistName['content'])

