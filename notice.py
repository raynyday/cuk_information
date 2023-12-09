# !pip install requests
# !pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

# 웹 페이지에서 공지사항 목록을 가져오는 함수
def get_notice_list(page_number):
    url = f"https://cukai.catholic.ac.kr/front/boardlist.do?bbsConfigFK=542&cmsDirPkid=5902&cmsLocalPkid=0&searchField=ALL&searchValue=&currentPage={page_number}&searchLowItem=ALL"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    notice_list = soup.select('.rbbs_list_normal_sec li')
    return notice_list

# 기본 URL
your_base_url = "https://cukai.catholic.ac.kr"

# 시작 페이지와 끝 페이지 설정
start_page = 1
end_page = 16  # 원하는 끝 페이지로 변경

# 시작 페이지부터 끝 페이지까지 반복하며 공지사항 목록 크롤링
for page_number in range(start_page, end_page + 1):
    notice_list = get_notice_list(page_number)

    # 각 공지사항에 대해 정보 출력
    for notice in notice_list:
        title = notice.select_one('.title .text').get_text(strip=True)
        link = notice.select_one('a')['href']
        full_link = f"{your_base_url}{link}"
        print(f"""
          <li>
            <a href="{full_link}">
              <div class="text">
                  {title}</div>
            </a>
          </li>
          <br>
              """)
    # print(len(notice_list))