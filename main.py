import requests
from bs4 import BeautifulSoup

WIKI_URL = "https://en.wikipedia.org/wiki/"

def GetStartAndTarget():
    start = input("Start topic:\n")
    start = start.replace(" ", "_")
    target = input("Target topic:\n")
    target = target.replace(" ", "_")
    return start, target

def GetHtml(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

def GetAllLinks(topic):
    html = GetHtml(WIKI_URL + topic);
    links = []
    for link in html.find_all('a'):
        l = str(link.get('href'))
        if ("/wiki/" in l):
            links.append(l.split("/wiki/", 1)[1])
    return links

def BFS(start, end, links):
    queue = [(start, [start])]
    visited = set()
    while (queue):
        vertex, path = queue.pop(0)
        print(vertex, path)
        visited.add(vertex)
        for node in GetAllLinks(vertex):
            if (node == end):
                return path + [end]
            if (node not in visited):
                visited.add(node)
                queue.append((node, path + [node]))

def main():
    start, target = GetStartAndTarget()
    links = GetAllLinks(start)
    sol = BFS(start, target, links)
    print("\n\n--== Solution Found ==--")
    print(sol, sep=' -> ')

if __name__ == '__main__':
    main()