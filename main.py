# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 
# 프로젝트 주제: 

# 1. 데이터 구조 정의 (음식 이름, 종류, 가격)
food_data = [
    ["김치찌개", "한식", 8000],
    ["비빔밥", "한식", 9000],
    ["짜장면", "중식", 7000],
    ["탕수육", "중식", 15000],
    ["초밥", "일식", 12000],
    ["라멘", "일식", 9500],
    ["파스타", "양식", 13000],
    ["피자", "양식", 18000]
]

# 2. 메뉴 표시 함수
def display_menu():
    print("=== 음식 종류를 선택하세요 ===")
    print("1. 한식  2. 중식  3. 일식  4. 양식")
    print("==============================")

# 3. 핵심 음식 추천 함수
def recommend_food(foods, choice, budget):
    # 번호에 따른 카테고리 매칭
    category = ""
    if choice == 1: category = "한식"
    elif choice == 2: category = "중식"
    elif choice == 3: category = "일식"
    elif choice == 4: category = "양식"
    else:
        print("잘못된 번호를 선택하셨습니다.")
        return
        
    print(f"\n--- [{category}] 중 {budget}원 이하의 추천 메뉴 ---")
    
    count = 0  # 추천된 음식 개수 세기
    
    # 2차원 리스트 탐색
    for food in foods:
        # food[0]은 이름, food[1]은 종류, food[2]는 가격입니다.
        
        # 💡 [빈칸 채우기 완료] 
        # 음식 종류(food[1])가 category와 같고, 음식 가격(food[2])이 budget 이하일 때
        if food[1] == category and food[2] <= budget:
            print(f"- {food[0]} (가격: {food[2]}원)")
            count += 1
            
    # 조건에 맞는 음식을 하나도 찾지 못했을 때
    if count == 0:
        print("조건에 맞는 음식을 찾지 못했습니다.")
        
    print(f"==========================================")
    print(f"총 {count}개의 음식을 추천해 드렸습니다.")

# 4. 메인 실행 흐름
display_menu()
user_choice = int(input("원하는 음식 종류의 번호를 입력하세요: "))
user_budget = int(input("현재 가용한 최대 예산을 입력하세요(원): "))

# 함수 호출
recommend_food(food_data, user_choice, user_budget)
