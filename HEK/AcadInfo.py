import requests
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self, keyword):
        self.baseURL = "https://www.kangwon.ac.kr"
        self.URL = "https://www.kangwon.ac.kr/search.do?cate=&query=" + keyword

    #html추출
    def getHtml(self, URL):
        html = requests.get(URL)

        return BeautifulSoup(html.content, "html.parser")

    #검색결과 메뉴검색건이 있는지 확인
    def srchMenuCountIsZero(self, soup):
        srchResult = soup.find_all('div', class_ = "para_box first")[0].find("span").get_text()
    
        if(srchResult[3] == '0'):
            return True
        else:
            return False

    #추출한 링크를 베이스링크와 연결하여 풀링크 반환
    def fullURL(self, link):
        return self.baseURL + link

    #링크가 저장된 리스트를 모두 풀링크로
    def listFullURL(self,links):
        List = []
        for link in links:
            temp = self.fullURL(link)
            List.append(temp)
    
        return List

    #해당 링크의 페이지가 한국 페이지인지 체크
    def checkWebLanguageKo(self, checkURL):
        checkSoup = self.getHtml(checkURL)
        langguage = checkSoup.find("html").get("lang")
    
        if(langguage == 'ko'):
            return True
        else:
            return False

    #검색결과 나온 메뉴링크 추출
    def getMenuURL(self):
        soup = self.getHtml(self.URL)
        menuLink = []

        if(not self.srchMenuCountIsZero(soup)):   
            menu = soup.find_all("ul", class_ = "bu padding_0")

            for index in menu[0].find_all("li"):
                link = index.find('a').get("href")
        
                if(self.checkWebLanguageKo(self.fullURL(link))):
                    menuLink.append(link)
            return self.listFullURL(menuLink)

        else:
            return 0