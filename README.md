## 프로젝트 소개
---
### 주제
- 코로나 여파로 OTT(Over The Top media service) 인기 급증
- OTT에서 최근 인기있는 방송 크롤링 & EDA 
- 슬랙으로 보고 싶은 프로그램 클립 링크 전송
![01](https://user-images.githubusercontent.com/46242120/81136724-58bf7f00-8f97-11ea-9cb8-8509d9fb7577.jpeg)

----
## 크롤링 방법
### 크롤링한 웹사이트
- NAVERTV : 지상파, 종합편성, 케이블TV 프로그램 클립
- Tving: TvN을 비롯한 케이블TV 프로그램 클립 & VOD
- Wavve: 지상파, 종합편성 프로그램
- Netflix : 인기 프로그램
- Nielsen : 지상파, 종합편성, 케이블TV 일일 시청률
![02](https://user-images.githubusercontent.com/46242120/81136726-5a894280-8f97-11ea-847b-0d58d3f3bc7e.jpeg)
![03](https://user-images.githubusercontent.com/46242120/81136729-5c530600-8f97-11ea-885c-e3b78a62cf72.jpeg)
![04](https://user-images.githubusercontent.com/46242120/81136732-5e1cc980-8f97-11ea-8a52-8281f3a1a26e.jpeg)

### 크롤링 계획
- 크롤링 기간 : 2020.04.01 - 2020.04.30
- 크롤링 주기 : 크론탭으로 하루 네 번 (출근시간, 점심시간, 퇴근시간 잠자기 전)
- 크롤링 방법 : scrapy & package
- 데이터 저장 : mysql
![05](https://user-images.githubusercontent.com/46242120/81136735-5eb56000-8f97-11ea-8c2e-47b8cb9cc6eb.jpeg)
![06](https://user-images.githubusercontent.com/46242120/81136736-5f4df680-8f97-11ea-9d00-87ecb3c956fa.jpeg)
![07](https://user-images.githubusercontent.com/46242120/81136738-5fe68d00-8f97-11ea-84df-95597bfc2359.jpeg)
---
## EDA
- 지상파에선 뉴스가 강세
- 출근 전엔 뉴스, 잠자기 전엔 드라마 인기 높아
- 1분 미리보기에서 VOD 구매로 이어지는 비율이 높은 프로그램이 실속있는 프로그램
- 인기드라마 "부부의 세계"로 본 VOD 판매주기
- 방콕 때문인가? 오래 전 드라마도 다시 주목
![08](https://user-images.githubusercontent.com/46242120/81136739-607f2380-8f97-11ea-9182-1fb58dd57237.jpeg)
![09](https://user-images.githubusercontent.com/46242120/81136740-607f2380-8f97-11ea-8756-8e680807f0a3.jpeg)
![10](https://user-images.githubusercontent.com/46242120/81136742-6117ba00-8f97-11ea-8109-57464abdf5f8.jpeg)
![11](https://user-images.githubusercontent.com/46242120/81136745-61b05080-8f97-11ea-81f0-2ec606ab3eaf.jpeg)
![12](https://user-images.githubusercontent.com/46242120/81136746-61b05080-8f97-11ea-87bf-96b0e41dd6c9.jpeg)

---

## 아쉬운 점 및 어려웠던 점
### 동적 페이지 넷플릭스 크롤링하기
- 셀레늄 + CSS selector + time sleep의 조합으로 해결
![13](https://user-images.githubusercontent.com/46242120/81136747-6248e700-8f97-11ea-9766-4bc7347b1968.jpeg)

### MySQL 인코딩
- 이모지까지 담을 수 있는 4바이트 utf8mb4으로 character set 설정
![14](https://user-images.githubusercontent.com/46242120/81136748-6248e700-8f97-11ea-89d6-17a9f5999537.jpeg)

---

### 결과
-[OTT crawling.pdf](https://github.com/CATERINA-SEUL/crawling-project/files/4734301/FINAL._._.pdf)

