import requests
import random

def get_law_quote(randomNumber:int):
    base_url = 'https://koreanjson.com/posts/'
    # randomNumber = random.randint(1,200)
    full_url = base_url + "/" + str(randomNumber)

    try:
        response = requests.get(full_url)

        if response.status_code == 200:
            data = response.json()
            if data is None:
                print('Result is Null. Please try again.')
                return None
            else:
                print(data)
                print("번호 :", data['id'])
                print("제목 :", data['title'])
                print("내용 :", data['content'])
                return data
        else:
            print("!!!실패!!! 상태 코드 :", response.status_code)
            return None

    except requests.exceptions.RequestException as e:
        print(f"네트워크 에러: {e}")
        return None



if __name__ == '__main__':
    num = random.randint(1, 200)
    tmp = get_law_quote(num)
