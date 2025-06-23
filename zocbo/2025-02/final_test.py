class Book(object):
    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.borrower_id = None

class Member(object):
    def __init__(self, member_id, name, address, contact):
        self.member_id = member_id
        self.name = name
        self.address = address
        self.contact = contact

class BookManager(object):
    def __init__(self):
        self.books = {} # 전체 책이 담긴 딕셔너리. title: [Book 객체, 대출자(없으면 None)]로 이루어져 있음.

    def register_book(self, book):
        self.books[book.title] = [book, None]

    def borrow_book(self, book, id):
        self.books[book.title][1] = id

    def return_book(self, book):
        return_member = self.books[book.title][1]
        self.books[book.title][1] = None
        return return_member

    def search_book(self, title):
        return self.books[title]

    def list_books(self):
        return self.books

class MemberManager(object):
    def __init__(self):
        self.members = [] # 전체 사용자가 담긴 리스트. 각 요소는 Member 객체로 이루어져 있음

    def register_member(self, member):
        self.members.append(member)

    def delete_member(self, id):
        for i in range(len(self.members)):
            if self.members[i].member_id == id:
                deleted_member = self.members[i]
                self.members.pop(i)
                return deleted_member
        return []

    def search_member(self, name):
        for i in range(len(self.members)):
            if self.members[i].name == name:
                return self.members[i]
        return []

    def list_members(self):
        return self.members

def main_menu():
    print("===== 도서관 관리 시스템 =====")
    print("1. 회원관리")
    print("2. 책관리")
    print("3. 종료")
    menu = int(input("메뉴를 선택하세요 (1~3): "))
    return menu

def manage_members_menu():
    print("--- 회원 관리 ---")
    print("1. 회원 등록")
    print("2. 회원 삭제")
    print("3. 회원 검색")
    print("4. 회원 목록 보기")
    print("5. 회원 정렬 (이름)")
    print("0. 이전 메뉴로 돌아가기")
    menu = int(input("원하는 메뉴를 선택하세요 (0~5): "))
    return menu

def manage_books_menu():
    print("--- 책관리 ---")
    print("1. 책 등록")
    print("2. 책 대출")
    print("3. 책 반납")
    print("4. 책 검색")
    print("5. 책 목록 보기")
    print("6. 책 정렬 (제목)")
    print("0. 이전 메뉴로 돌아가기")
    menu = int(input("원하는 메뉴를 선택하세요 (0~6): "))
    return menu

def main():
    bookManager = BookManager()
    memberManager = MemberManager()

    while True:
        main_menu_selected = main_menu()

        if main_menu_selected == 1:
            manage_members_selected = manage_members_menu()
            if manage_members_selected == 1:
                id = input("회원 ID 입력: ")
                name = input("이름 입력: ")
                address = input("주소 입력: ")
                contact = input("연락처 입력: ")
                new_member = Member(member_id=id, name=name, address=address, contact=contact)
                memberManager.register_member(member=new_member)
                print("회원 등록 완료: " + name)
            elif manage_members_selected == 2:
                delete_id = input("삭제할 회원 ID 입력: ")
                delete_member = memberManager.delete_member(id=delete_id)
                print(delete_member.name + " 회원 삭제 완료")
            elif manage_members_selected == 3:
                search_name = input("검색할 회원 이름 입력: ")
                search_result = memberManager.search_member(name=search_name)
                print("'" + search_name + "'로 검색한 회원 목록: ")
                print("- ID: " + search_result.member_id + ", 이름: " + search_result.name + ", 주소: " + search_result.address + ", 연락처: " + search_result.contact)
            elif manage_members_selected == 4:
                total_list = memberManager.list_members()
                print("전체 회원 목록: ")
                for member in total_list:
                    print("- ID: " + member.member_id + ", 이름: " + member.name + ", 주소: " + member.address + ", 연락처: " + member.contact)
            elif manage_members_selected == 0:
                continue

        elif main_menu_selected == 2:
            manage_books_selected = manage_books_menu()
            if manage_books_selected == 1:
                title = input("책 제목 입력: ")
                author = input("저자 입력: ")
                publisher = input("출판사 입력: ")
                new_book = Book(title=title, author=author, publisher=publisher)
                bookManager.register_book(book=new_book)
                print("책 등록 완료: " + title)
            elif manage_books_selected == 2:
                title = input("대출할 책 제목: ")
                id = input("대출자 회원 ID: ")
                borrowed_book = bookManager.search_book(title=title)[0]
                bookManager.borrow_book(book=borrowed_book, id=id)
                print("'" + title + "' 대출 완료 (대출자: " + id + ")")
            elif manage_books_selected == 3:
                title = input("반납할 책 제목: ")
                return_book = bookManager.search_book(title=title)[0]
                return_member = bookManager.return_book(book=return_book)
                print("'" + title + "' 반납 완료 (반납자: " + return_member + ")")
            elif manage_books_selected == 4:
                title = input("검색할 책 제목 입력: ")
                book = bookManager.search_book(title=title)
                print("'" + title + "'로 검색한 책 목록: ")
                able_to_borrow = True
                if book[1] != None:
                    able_to_borrow = False
                if able_to_borrow == True:
                    print("- " + book[0].title + " / " + book[0].author + " / " + book[0].publisher + " (대출 가능)")
                if able_to_borrow == False:
                    print("- " + book[0].title + " / " + book[0].author + " / " + book[0].publisher + " (대출자 : " + book[1] + ")")

            elif manage_books_selected == 5:
                total_list = bookManager.list_books()
                for key, value in total_list.items():
                    able_to_borrow = True
                    if value[1] != None:
                        able_to_borrow = False
                    if able_to_borrow == True:
                        print("- " + value[0].title + " / " + value[0].author + " / " + value[0].publisher + " (대출 가능)")
                    if able_to_borrow == False:
                        print("- " + value[0].title + " / " + value[0].author + " / " + value[0].publisher + " (대출자 : " + value[1] + ")")
            elif manage_books_selected == 0:
                continue

        elif main_menu_selected == 3:
            break
main()