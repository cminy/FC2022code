# DESCRIPTION : Python 웹크롤링 : request 라이브러리 사용하여 연관검색어 추출
# -*- coding: utf-8 -*-
import requests
import json
import openpyxl


# 자음 리스트 생성
kor_letters = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ',
            'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']


# request 사용
def miny_search(main_keyword):
    print(f'>>>> {main_keyword}에 관한 연관키워드 검색 중')
    sub_keyword = []
    for l in kor_letters:
        keyword = main_keyword + ' ' + l
        response = requests.get(
            f"https://ac.search.naver.com/nx/ac?q={keyword}&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100&_callback=_jsonp_5")
        origin_data = response.text

        # json 안에 내용 추출하고, [:-1]해서 ) 제거
        str_data = origin_data.split("_jsonp_5(")[1][:-1]
        # dictionary 파싱
        dic_data = json.loads(str_data)

        for data in dic_data['items'][0]:
            # 해당 자음에 속하는 연관검색어가 있는 경우만 리스트에 저장
            if data[0] != main_keyword: 
                sub_keyword.append(data[0])

    if len(sub_keyword) > 0 :
        create_xls(main_keyword, sub_keyword)
    else :
        print('[!] {}에 관한 연관키워드가 없어 파일을 저장하지 않습니다.'.format(main_keyword))


def create_xls(main_keyword, sub_keyword):
    # 엑셀파일 만들기
    print('>>>> {}에 관한 연관키워드 {}개가 검색되었습니다.'.format(main_keyword, len(sub_keyword)))
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = main_keyword
    # 시트에 내용 추가
    ws['A1'] = main_keyword + "로 시작하는 한글 연관키워드 추출 결과"
    ws.append(['#', '연관키워드'])
    for i, sub_ in enumerate(sub_keyword):
        ws.append([i+1, sub_])
    # 엑셀 저장
    wb.save(f'{main_keyword} 연관키워드.xlsx')
    print('[!] {}에 관한 연관키워드({}개) 목록이 저장되었습니다.'.format(main_keyword, len(sub_keyword)))


main_keyword = input("검색어를 입력해주세요:")
miny_search(main_keyword)
