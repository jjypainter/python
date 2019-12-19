#랜덤으로 오늘의 점심메뉴르 추천
import random

phone_book=['새마을식당','초원삼겹살','멀캠20층','홍콩반점','순남시래기','KFC','TACOBELL']

lunch={
    '새마을식당':'010-1234-6789',
    '홍콩반점':'010-2352-3456',
    'KFC':'010-2356-9876',
    '초원삼겹살':'010-3826-8564',
    '멀캠20층':'010-2584-9537',
    '순남시래기':'010-6749-9256',
    'TACOBELL':'010-23867-2383'

}

print(phone_book['새마을식당'])
#menu의 요소 중 랜덤으로 골라서 lunch라고 하는 변수에 담는다.
lunch=random.choice(menu)
print(lunch)
print(phone_book[lunch])
