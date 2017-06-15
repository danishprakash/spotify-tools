import bs4, requests, re, sys

playlistReq =requests.get(sys.argv[1])
playlistSoup = bs4.BeautifulSoup(playlistReq.text, "lxml")
songUrl = playlistSoup.find_all('meta', property='music:song')

reg = re.sub(r', a playlist.*', '', playlistSoup.find('meta', property='og:title')['content'])

playlist = open(str(reg+'.txt'), 'w')
playlist.write(reg+'\n\n')

print('Working...')
for i in range(len(songUrl)):
    songReq = requests.get(songUrl[i]['content'])
    songSoup = bs4.BeautifulSoup(songReq.text, "lxml")
    songName = songSoup.find('meta', property='og:title')

    artistUrl = songSoup.find('meta', property='music:musician')
    artistReq = requests.get(artistUrl['content'])
    artistSoup = bs4.BeautifulSoup(artistReq.text, "lxml")
    artistName = artistSoup.find('meta', property='og:title')
    playlist.write(str(i+1) + '. ' + songName['content']+' - ' +
            artistName['content']+ '\n')
print('Done')

playlist.close()
