## 프로젝트 소개
---
### 주제
- 코로나 여파로 OTT(Over The Top media service) 인기 급증
- OTT에서 최근 인기있는 방송 크롤링 & EDA 
- 슬랙으로 보고 싶은 프로그램 클립 링크 전송
![01](https://user-images.githubusercontent.com/46242120/81136281-16e20900-8f96-11ea-97b8-2d6b929b4ff8.jpeg)


----
## 크롤링 방법
----
### 크롤링한 웹사이트
- NAVERTV : 지상파, 종합편성, 케이블TV 프로그램 클립
- Tving: TvN을 비롯한 케이블TV 프로그램 클립 & VOD
- Wavve: 지상파, 종합편성 프로그램
- Netflix : 인기 프로그램
- Nielsen : 지상파, 종합편성, 케이블TV 일일 시청률
![02](https://user-images.githubusercontent.com/46242120/81136403-74765580-8f96-11ea-9112-507ad1f3ac71.jpeg)
![03](https://user-images.githubusercontent.com/46242120/81136415-7b9d6380-8f96-11ea-8a17-e890bea7d8ef.jpeg)
![04](https://user-images.githubusercontent.com/46242120/81136433-87892580-8f96-11ea-8342-f75c87d3e291.jpeg)


### 크롤링 계획
- 크롤링 기간 : 2020.04.01 - 2020.04.30
- 크롤링 주기 : 크론탭으로 하루 네 번 (출근시간, 점심시간, 퇴근시간 잠자기 전)
- 크롤링 방법 : scrapy & package
- 데이터 저장 : mysql
![05](https://user-images.githubusercontent.com/46242120/81136447-9079f700-8f96-11ea-8c97-7fe5947fdc44.jpeg)
![06](https://user-images.githubusercontent.com/46242120/81136458-97086e80-8f96-11ea-997b-4be630f7fdc5.jpeg)
![07](https://user-images.githubusercontent.com/46242120/81136461-996ac880-8f96-11ea-93dd-6b55a2d4b339.jpeg)

---

## EDA
- 지상파에선 뉴스가 강세
- 출근 전엔 뉴스, 잠자기 전엔 드라마 인기 높아
- 1분 미리보기에서 VOD 구매로 이어지는 비율이 높은 프로그램이 실속있는 프로그램
- 인기드라마 "부부의 세계"로 본 VOD 판매주기
- 방콕 때문인가? 오래 전 드라마도 다시 주목
![08](https://user-images.githubusercontent.com/46242120/81136463-9a035f00-8f96-11ea-9164-c24ca2ee15f8.jpeg)
![09](https://user-images.githubusercontent.com/46242120/81136464-9a9bf580-8f96-11ea-9cec-add6c450312a.jpeg)
![10](https://user-images.githubusercontent.com/46242120/81136465-9a9bf580-8f96-11ea-85ab-db328f8f8b48.jpeg)
![11](https://user-images.githubusercontent.com/46242120/81136467-9b348c00-8f96-11ea-833d-092458c79f3f.jpeg)
![12](https://user-images.githubusercontent.com/46242120/81136469-9b348c00-8f96-11ea-9714-ec6f872b3e16.jpeg)

---

## 아쉬운 점 및 어려웠던 점
----
### 동적 페이지 넷플릭스 크롤링하기
- 셀레늄 + CSS selector + time sleep의 조합으로 해결
![13](https://user-images.githubusercontent.com/46242120/81136470-9bcd2280-8f96-11ea-8d13-2dcd3ad2b130.jpeg)

### MySQL 인코딩
- 이모지까지 담을 수 있는 4바이트 utf8mb4으로 character set 설정
![14](https://user-images.githubusercontent.com/46242120/81136472-9bcd2280-8f96-11ea-9ffa-1c61fdb42d02.jpeg)
