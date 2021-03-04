# ---- key 값을 기준으로 정렬
# 공백을 기준으로 문자열을 나누어 리스트로 변환한다
# 리스트로 변환시
sorted("This is a test string from Andrew".split(), key=str.lower)
["a", "Andrew", "from", "is", "string", "test", "This"]


# ---- 딕셔너리 자료형 정렬하기 (람다)
student_tuples = [...("john", "A", 15), ...(
    "jane", "B", 12), ...("dave", "B", 10), ...]
sorted(student_tuples, key=lambda student: student[2])
# sort by age
[("dave", "B", 10), ("jane", "B", 12), ("john", "A", 15)]


# ---- 내림차순 (역순으로) 정렬
num_list = [3, 5, 1, 2, 4]
# sorted
new_num_list = sorted(num_list, reverse=True)
# sort
num_list.sort(reverse=True)
