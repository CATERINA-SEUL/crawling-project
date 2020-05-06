{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 프로젝트 소개\n",
    "### 주제\n",
    "- 코로나 여파로 OTT(Over The Top media service) 인기 급증\n",
    "- OTT에서 최근 인기있는 방송 크롤링 & EDA \n",
    "- 슬랙으로 보고 싶은 프로그램 클립 링크 전송\n",
    "![crawling](./슬라이드3.JPG)\n",
    "\n",
    "----\n",
    "## 크롤링 방법\n",
    "### 크롤링한 웹사이트\n",
    "- NAVERTV : 지상파, 종합편성, 케이블TV 프로그램 클립\n",
    "- Tving: TvN을 비롯한 케이블TV 프로그램 클립 & VOD\n",
    "- Wavve: 지상파, 종합편성 프로그램\n",
    "- Netflix : 인기 프로그램\n",
    "- Nielsen : 지상파, 종합편성, 케이블TV 일일 시청률\n",
    "![crawling](./슬라이드6.JPG)\n",
    "![crawling](./슬라이드7.JPG)\n",
    "![crawling](./최종발표_ver05.jpg)\n",
    "\n",
    "### 크롤링 계획\n",
    "- 크롤링 기간 : 2020.04.01 - 2020.04.30\n",
    "- 크롤링 주기 : 크론탭으로 하루 네 번 (출근시간, 점심시간, 퇴근시간 잠자기 전)\n",
    "- 크롤링 방법 : scrapy & package\n",
    "- 데이터 저장 : mysql\n",
    "![crawling](./슬라이드10.JPG)\n",
    "![crawling](./슬라이드11.JPG)\n",
    "![crawling](./슬라이드12.JPG)\n",
    "\n",
    "---\n",
    "## EDA\n",
    "- 지상파에선 뉴스가 강세\n",
    "- 출근 전엔 뉴스, 잠자기 전엔 드라마 인기 높아\n",
    "- 1분 미리보기에서 VOD 구매로 이어지는 비율이 높은 프로그램이 실속있는 프로그램\n",
    "- 인기드라마 \"부부의 세계\"로 본 VOD 판매주기\n",
    "- 방콕 때문인가? 오래 전 드라마도 다시 주목\n",
    "![crawling](./슬라이드21.JPG)\n",
    "![crawling](./슬라이드24.JPG)\n",
    "![crawling](./슬라이드26.JPG)\n",
    "![crawling](./슬라이드28.JPG)\n",
    "![crawling](./슬라이드29.JPG)\n",
    "\n",
    "---\n",
    "\n",
    "## 아쉬운 점 및 어려웠던 점\n",
    "### 동적 페이지 넷플릭스 크롤링하기\n",
    "- 셀레늄 + CSS selector + time sleep의 조합으로 해결\n",
    "![crawling](./슬라이드15.JPG)\n",
    "\n",
    "### MySQL 인코딩\n",
    "- 이모지까지 담을 수 있는 4바이트 utf8mb4으로 character set 설정\n",
    "![crawling](./슬라이드17.JPG)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
