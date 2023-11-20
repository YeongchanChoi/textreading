# 파일 경로 지정
file_path = 'test.txt'

# 파일 열기
with open(file_path, 'r', encoding='utf-8') as file:
    # 파일 내용 읽기
    file_content = file.read()

    # 파일 내용 출력
    print(file_content)

