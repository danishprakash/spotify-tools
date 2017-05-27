import bs4
import requests

playlist = open('playlist.txt', 'w')

playlistReq = requests.get('https://open.spotify.com/user/danishprakash/playlist/4MsaDGPQ8SX7k2tvaHAU36')
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
    temp = (str(i+1) + '. ' + songName['content']+' - ' +
            artistName['content']+ '\n')
    playlist.write(temp)

playlist.close()
