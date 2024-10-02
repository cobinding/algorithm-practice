# 년월일 추출 함수
def parse_date(date_str):
        year, month, day = map(int, date_str.split("."))
        return year, month, day
    

# 문서 날짜와 오늘 날짜를 비교하는 함수
def compare_dates(date_str1, date_str2, limit):
        y1, m1, d1 = parse_date(date_str1)
        y2, m2, d2 = parse_date(date_str2)
    
        dates_day = y1*12*28 + m1*28 + d1 + limit*28
        today_day = y2*12*28 + m2*28 + d2

        return today_day - dates_day


def solution(today, terms, privacies):
    
    dic = {}
    ans = []
    
    # term는 유형에 따라 해시맵에 저장
    for item in terms:
        key, value = item.split(" ")
        dic[key] = value
    
    idx = 0   
    for item in privacies:
        days, type = item.split(" ")
        limit = int(dic[type])
        
        # 오늘 날짜가 더 크다면 유효기간이 지난 것이므로, 파기하는 배열에 추가
        if compare_dates(days, today, limit) >= 0 :
            ans.append(idx+1)
        
        idx += 1

    return ans
    