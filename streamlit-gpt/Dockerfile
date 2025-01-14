# Base 이미지  이미지 연습
FROM python:3.12-slim

# 2. 작업 디렉토리를 /app으로 설정
WORKDIR /app

# 3. 현재 디렉토리의 requirements.txt 파일을 컨테이너의 /app으로 복사
COPY requirements.txt /app/

# 4. requirements.txt에 명시된 패키지 설치
RUN pip3 install -r requirements.txt

# 5. 실행할 streamlit_app.py를 컨테이너 /app으로 복사
COPY streamlit_gpt.py /app/

# 6. 컨테이너가 수신할 포트 오픈
EXPOSE 8090

#7. 실행될 컨테이너 구성
ENTRYPOINT [ "streamlit", "run", "streamlit_gpt.py", "--server.port=8090", "--server.address=0.0.0.0" ]
