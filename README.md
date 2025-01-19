# **백엔드 개발 온보딩 과제 (Python)**

이 프로젝트는 **JWT 토큰 발행 및 검증**, **회원가입 및 로그인 API** 구현과 유닛 테스트를 포함합니다. 아래에서 주요 기능과 테스트 방법에 대해 안내합니다.

---

## **1. 토큰 발행 및 유효성 테스트**

### 주요 테스트 항목:
1. **AccessToken 발행**  
   - Access Token이 정상적으로 발행되는지 확인합니다.

2. **RefreshToken 발행**  
   - Refresh Token이 정상적으로 발행되는지 확인합니다.

3. **AccessToken 검증**  
   - 발급된 Access Token이 유효한지 검증합니다.

4. **만료된 AccessToken 테스트**  
   - 만료된 Access Token 사용 시 예외가 발생하는지 확인합니다.

5. **잘못된 토큰 검증 테스트**  
   - 형식이 잘못된 토큰 디코딩 시 예외가 발생하는지 확인합니다.

### 유닛 테스트 실행:

- **테스트 파일 실행**
   ```bash
   pytest test_JWT.py
   ```

- **테스트 결과를 자세히 보기**
   ```bash
   pytest -v
   ```

- **실패한 테스트만 다시 실행**
   ```bash
   pytest --lf
   ```

---

## **2. 회원가입 및 로그인 API**

### **회원가입**
- **Endpoint**: `/signup`  
- **Request**:  
   ```json
   {
       "username": "testuser",
       "password": "12341234",
       "nickname": "testuser"
   }
   ```  
- **Response**:  
   ```json
   {
       "username": "example",
       "nickname": "testuser",
       "roles": [
          {"role": "USER"}
       ]
   }
   ```  

### **로그인**
- **Endpoint**: `/login`  
- **Request**:  
   ```json
   {
       "username": "testuser",
       "password": "12341234"
   }
   ```  
- **Response**:  
   ```json
   {
       "token": "string"
   }
   ```  

### 테스트 실행:
- **회원가입 및 로그인 테스트**  
   ```bash
   python manage.py test
   ```  

---

## **3. 배포**

- **Public IPv4 주소**: `3.35.205.226`  

API 서버는 위의 주소에서 배포 및 실행됩니다.

---

### **기타 참고 사항**
- 프로젝트를 시작하기 전에 **의존성 패키지 설치**가 필요합니다.  
  ```bash
  pip install -r requirements.txt
  ```  

- `SECRET_KEY`, `ALGORITHM` 등 프로젝트의 환경 파일에 정의가 필요합니다.  