import bs4, requests

playlistReq = requests.get('https://open.spotify.com/user/danishprakash/playlist/0IafjIgTPz03TMIAkll402')
playlistReq.raise_for_status()
playlistSoup = bs4.BeautifulSoup(playlistReq.text, "lxml")
songUrl = playlistSoup.find_all('meta', property='music:song')

for i in range(len(songUrl)):
    songReq = requests.get(songUrl[i]['content'])
    songSoup = bs4.BeautifulSoup(songReq.text, "lxml")
    songName = songSoup.find('meta', property='og:title')

    artistUrl = songSoup.find('meta', property='music:musician')
    artistReq = requests.get(artistUrl['content'])
    artistSoup = bs4.BeautifulSoup(artistReq.text, "lxml")
    artistName = artistSoup.find('meta', property='og:title')
    print(songName['content']+' - ' + artistName['content'])

