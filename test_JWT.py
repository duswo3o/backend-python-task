import pytest
import jwt
from datetime import datetime, timedelta, timezone
from pathlib import Path
import environ
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

# setting env
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# JWT 테스트용 비밀 키와 알고리즘 설정
SECRET_KEY = env("JWT_SECRET_KEY")
ALGORITHM = env("ALGORITHM")


# access token 발급
def generate_access_token(id, expires_delta):
    payload = {
        "id": id,  # user id
        "iat": datetime.now(timezone.utc),  # 토큰 발급 시간
        "exp": datetime.now(timezone.utc)
        + expires_delta,  # 토큰 만료 시간 : 발급 30분 후
    }
    return jwt.encode(payload, key=SECRET_KEY, algorithm=ALGORITHM)


# refresh token 발급
def generate_refresh_token(id):
    payload = {
        "id": id,  # user id
        "iat": datetime.now(timezone.utc),  # 토큰 발급 시간
        "exp": datetime.now(timezone.utc)
        + timedelta(days=7),  # 토큰 만료 시간 : 발급 7일 후
    }
    return jwt.encode(payload, key=SECRET_KEY, algorithm=ALGORITHM)


# 테스트케이스
@pytest.fixture
def token_id():
    return 1


@pytest.fixture
def access_token(token_id):
    return generate_access_token(token_id, timedelta(minutes=30))


@pytest.fixture
def refresh_token(token_id):
    return generate_refresh_token(token_id)


# access token 발행 테스트
def test_generate_access_token(token_id):
    token = generate_access_token(token_id, timedelta(minutes=30))
    decoded = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
    assert decoded.get("id") == token_id
    assert "iat" in decoded, "no token issued at"
    assert "exp" in decoded, "no token expired at"


# refresh token 발생 테스트
def test_generate_refresh_token(token_id):
    token = generate_refresh_token(token_id)
    decoded = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
    assert decoded.get("id") == token_id
    assert "iat" in decoded, "no token issued at"
    assert "exp" in decoded, "no token expired at"


# access token 검증 테스트
def test_access_token_validation(access_token, token_id):
    decoded = jwt.decode(access_token, key=SECRET_KEY, algorithms=[ALGORITHM])
    assert decoded.get("id") == token_id, "not valid token"


# expired access token test
def test_expired_access_token(token_id):
    expired_token = generate_access_token(token_id, timedelta(seconds=-1))
    # return jwt.decode(expired_token, key=SECRET_KEY, algorithms=[ALGORITHM])

    # 특정 예외가 발생할 때만 테스트가 통과
    # expired_token을 디코딩 할 때 jwt.ExpiredSignatureError 예외가 발생하는지 확인
    with pytest.raises(jwt.ExpiredSignatureError):
        jwt.decode(expired_token, key=SECRET_KEY, algorithms=[ALGORITHM])


# invalid token test
def test_invalid_token():
    invalid_token = "invalid.token.test"
    with pytest.raises(jwt.DecodeError):
        jwt.decode(invalid_token, key=SECRET_KEY, algorithms=[ALGORITHM])
