# # 파일 경로 지정
# file_path = 'test.txt'
#
# # # 파일 열기
# with open(file_path, 'r', encoding='utf-8') as file:
#     # 파일 내용을 한 글자씩 읽어와서 출력
#     for char in file.read():
#         char=char+"a"
#         print(char)

# 또는 다음과 같이 사용할 수도 있습니다.
# with open(file_path, 'r', encoding='utf-8') as file:
#     file_content = file.readlines()
#     for line in file_content:
#         print(line, end='')


from datetime import datetime

# 현재 날짜와 시간을 가져오기
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 텍스트 파일에 현재 시간 추가
file_path = 'text.txt'
with open(file_path, 'a') as file:
    file.write(current_time + '\n')

print(f'현재 시간이 {file_path} 파일에 추가되었습니다.')

