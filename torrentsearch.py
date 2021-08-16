import requests
import bs4

def torrentsearch(search,default=1):
    search = search.replace(' ','+')
    search = 'https://1337x.to/search/' + search + '/1/'

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

    result = requests.get(search, headers=headers)

    soup = bs4.BeautifulSoup(result.text,'lxml')
    link = soup.select('tr a', href = True)
    link = link[default]['href']

    search = 'https://1337x.to' + link
    result = requests.get(search, headers=headers)
    soup = bs4.BeautifulSoup(result.text,'lxml')
    name = soup.select('h1')[0].getText()
    li = soup.select('li a',href = True)[29]['href']
    seeders = soup.select('.seeds')[0].getText()
    return search,name,li,seeders

s = input('Enter the torrent to search(Any game/movie or tv series): ')
default = 1
while default!=0:
    torrent = torrentsearch(s,default)
    print(f'\nName of torrent is: {torrent[1]}')
    print(f'\nLink of torrent is: {torrent[0]}')
    print(f'\nMagnet link of torrent is: {torrent[2]}')
    print(f'\nNumber of seeders is: {torrent[3]}')
    check = input("Are you satisfied with the torrent: (Y or N): ")
    if check.capitalize() == 'Y':
        default = 0
    elif check.capitalize() == 'N':
        default +=3
    else:
        print('Wrong input')