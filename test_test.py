NAME_AND_PRICE = {
        "bread": [
            ["밀빵", 1000],
            ["호밀빵", 1200]
        ],
        "cheese": [
            ["슈레드치즈", 300],
            ["모짜렐라치즈", 300]
        ],
        "topping": [
            ["햄", 1000],
            ["에그마요", 800],
            ["베이컨", 1500],
            ["참치마요", 800]
        ],
        "vegi": [
            ["양상추", 500],
            ["토마토", 500],
            ["양파", 200],
            ["피클", 100]
        ],
        "sauce": [
            ["케첩", 50],
            ["마요네즈", 50],
            ["머스타드", 50]
        ],
        "drink": [
            ["음료", 500]
        ]
    }

ELEMENTS = ["bread", "cheese", "topping", "vegi", "sauce"]

class Sandwich(object):
    def __init__(self, bread, cheese, topping, vegi, sauce): # vegi 빼고는 다 index 번호, vegi만 각 index 별 0과 1로 유무 판정
        self.bread = bread
        self.cheese = cheese
        self.topping = topping
        self.vegi = vegi
        self.sauce = sauce

    def get_price(self):
        price = NAME_AND_PRICE['bread'][self.bread][1] + NAME_AND_PRICE['cheese'][self.cheese][1] + NAME_AND_PRICE['topping'][self.topping][1] + NAME_AND_PRICE['sauce'][self.sauce][1]
        for i in range(len(self.vegi)):
            if self.vegi[i] == 1:
                price += NAME_AND_PRICE['vegi'][i][1]
        return price

class Customer(object):
    def __init__(self, sandwich, drink): # drink의 유무는 0과 1
        self.sandwich = sandwich
        self.drink = drink

    def get_price(self):
        price = self.sandwich.get_price()
        if self.drink == 1:
            price += NAME_AND_PRICE['drink'][0][1]
        return price

class Store(object):
    def __init__(self, bread, cheese, topping, vegi, sauce): # 각 매개변수는 수량 가진 리스트로 되어있음
        self.bread = bread
        self.cheese = cheese
        self.topping = topping
        self.vegi = vegi
        self.sauce = sauce
        self.customers = []
        self.total_price = 0

    def order(self, customer):
        self.bread[customer.sandwich.bread] -= 1
        self.cheese[customer.sandwich.cheese] -= 1
        self.topping[customer.sandwich.topping] -= 1
        self.sauce[customer.sandwich.sauce] -= 1
        for i in range(len(self.vegi)):
            if customer.sandwich.vegi[i] == 1:
                self.vegi[i] -= 1
        self.total_price += customer.get_price()
        self.customers.append(customer)

    def is_able_to_open(self):
        for bread in self.bread:
            if bread <= 0:
                return False
        for cheese in self.cheese:
            if cheese <= 0:
                return False
        for topping in self.topping:
            if topping <= 0:
                return False
        for vegi in self.vegi:
            if vegi <= 0:
                return False
        for sauce in self.sauce:
            if sauce <= 0:
                return False
        return True

def init_store():
    print("안녕하세요\n오늘의 식재료 준비를 시작합니다.")

    meal_bread = int(input("밀빵의 수량을 설정해주세요: "))
    homeal_bread = int(input("호밀빵의 수량을 설정해주세요: "))
    shred_cheese = int(input("슈레드치즈의 수량을 설정해주세요: "))
    mozar_cheese = int(input("모짜렐라치즈의 수량을 설정해주세요: "))
    ham = int(input("햄의 수량을 설정해주세요: "))
    egg_mayo = int(input("에그마요의 수량을 설정해주세요: "))
    bacon = int(input("베이컨의 수량을 설정해주세요: "))
    tuna_mayo = int(input("참치마요의 수량을 설정해주세요: "))
    cabbage = int(input("양상추의 수량을 설정해주세요: "))
    tomato = int(input("토마토의 수량을 설정해주세요: "))
    onion = int(input("양파의 수량을 설정해주세요: "))
    pikle = int(input("피클의 수량을 설정해주세요: "))
    ketchup = int(input("케첩의 수량을 설정해주세요: "))
    mayo = int(input("마요네즈의 수량을 설정해주세요: "))
    mustard = int(input("머스터드의 수량을 설정해주세요: "))

    store = Store(bread=[meal_bread, homeal_bread], cheese=[shred_cheese, mozar_cheese], topping=[ham, egg_mayo, bacon, tuna_mayo], vegi=[cabbage, tomato, onion, pikle], sauce=[ketchup, mayo, mustard])
    print("\n가게 오픈 준비가 완료되었습니다.")
    return store

def order(store):
    while True:
        print("어서오세요. 인곽샌드입니다.")
        print("======================")
        for element in ELEMENTS:
            for ingredient in NAME_AND_PRICE[element]:
                print(ingredient[0] + "         " + str(ingredient[1]))
        print("======================")
        answer = input("주문하시겠습니까? (Y/N): ").lower()
        if answer == 'y':
            break
    print("샌드위치 주문을 시작합니다.")
    bread = int(input("빵의 종류를 선택하세요(1.밀빵 2.호밀빵): ")) - 1
    cheese = int(input("치즈의 종류를 선택하세요(1.슈레드 2.모짜렐라): ")) - 1
    topping = int(input("토핑의 종류를 선택하세요(1.햄 2.에그마요 3.베이컨 4.참치마요): ")) - 1
    cabbage = int(input("양상추 추가하시겠습니까? (0.추가 안함 1.추가): "))
    tomato = int(input("토마토 추가하시겠습니까? (0.추가 안함 1.추가): "))
    onion = int(input("양파 추가하시겠습니까? (0.추가 안함 1.추가): "))
    pikle = int(input("피클 추가하시겠습니까? (0.추가 안함 1.추가): "))
    sauce = int(input("소스의 종류를 선택하세요(1.케첩 2.마요네즈 3.머스터드): ")) - 1
    drink = int(input("음료 추가하시겠습니까? (0.추가 안함 1.추가): "))

    sandwich = Sandwich(bread=bread, cheese=cheese, topping=topping, vegi=[cabbage, tomato, onion, pikle], sauce=sauce)
    customer = Customer(sandwich=sandwich, drink=drink)
    store.order(customer=customer)
    return customer

def reciept(customer):
    print("🧾영수증🧾")
    print("======================")
    print("주문한 항목: ")
    print(NAME_AND_PRICE['bread'][customer.sandwich.bread][0] + " - " + str(NAME_AND_PRICE['bread'][customer.sandwich.bread][1]) + "원")
    print(NAME_AND_PRICE['cheese'][customer.sandwich.cheese][0] + " - " + str(NAME_AND_PRICE['cheese'][customer.sandwich.cheese][1]) + "원")
    print(NAME_AND_PRICE['topping'][customer.sandwich.topping][0] + " - " + str(NAME_AND_PRICE['topping'][customer.sandwich.topping][1]) + "원")
    for i in range(len(customer.sandwich.vegi)):
        if customer.sandwich.vegi[i] == 1:
            print(NAME_AND_PRICE['vegi'][i][0] + " - " + str(NAME_AND_PRICE['vegi'][i][1]) + "원")
    print(NAME_AND_PRICE['sauce'][customer.sandwich.sauce][0] + " - " + str(NAME_AND_PRICE['sauce'][customer.sandwich.sauce][1]) + "원")
    if customer.drink == 1:
        print(NAME_AND_PRICE['drink'][0][0] + " - " + str(NAME_AND_PRICE['drink'][0][1]) + "원")
    print("----------------------")
    print("총 가격 : " + str(customer.get_price()) + "원")
    print("======================")

def print_finish(store):
    print("식재료가 소진되었습니다.\n금일 영업을 종료합니다.")
    print("======================")
    print("금일 방문 고객 수: " + str(len(store.customers)))
    print("금일 총 매출: " + str(store.total_price))
    print("======================")
    print("\n식자재 재고 현황")
    for i in range(2):
        print(NAME_AND_PRICE['bread'][i][0] + " : " + str(store.bread[i]) + "개")
    for i in range(2):
        print(NAME_AND_PRICE['cheese'][i][0] + " : " + str(store.cheese[i]) + "개")
    for i in range(4):
        print(NAME_AND_PRICE['topping'][i][0] + " : " + str(store.topping[i]) + "개")
    for i in range(4):
        print(NAME_AND_PRICE['vegi'][i][0] + " : " + str(store.vegi[i]) + "개")
    for i in range(3):
        print(NAME_AND_PRICE['sauce'][i][0] + " : " + str(store.sauce[i]) + "개")
    print("----------------------")

def main():
    ishs_sandwich = init_store()
    while True:
        if not ishs_sandwich.is_able_to_open():
            break
        customer = order(ishs_sandwich)
        reciept(customer=customer)
    print_finish(ishs_sandwich)

main()