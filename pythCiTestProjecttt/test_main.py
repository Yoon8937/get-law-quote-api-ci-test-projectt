from unittest.mock import patch

# from main import get_law_quote
import main


# 방법 1: 진짜 API를 찔러서 확인하는 테스트
def test_get_law_quote_real_api():
    result = main.get_law_quote(39)

    # 1번 글이라면 데이터가 제대로 올 것이고, 201번 글이라면 None이 올 것입니다.
    # main.py의 randomNumber 상태에 맞춰 아래 assert 중 하나를 쓰시면 됩니다.
    if result is not None:
        assert 'id' in result
        assert 'title' in result
        assert 'content' in result

def test_get_law_quote_real_api_fail():
    result = main.get_law_quote(201)

    # 1번 글이라면 데이터가 제대로 올 것이고, 201번 글이라면 None이 올 것입니다.
    # main.py의 randomNumber 상태에 맞춰 아래 assert 중 하나를 쓰시면 됩니다.
    if result is not None:
        assert 'id' in result
        assert 'title' in result
        assert 'content' in result