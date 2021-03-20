import re


def solution(program, flag_rules, commands):
    answer = []
    flag_dict = {}
    MAXIMUM_FLAG_COUNT = 1
    PATTERNS = {
        "FLAG": "-[a-zA-Z]+",
        "STRING": "-[a-zA-Z]+ [a-zA-Z]+",
        "STRINGS": "(-[a-zA-Z]+([\s][a-zA-Z]+){1,})",
        "NUMBER": "-[a-zA-Z]+ [0-9]+",
        "NUMBERS": "(-[a-zA-Z]+([\s][0-9]+){1,})",
        "NULL": "-[a-zA-Z]+"
    }

    for flag_rule in flag_rules:
        [flag_name, flag_arg_type] = flag_rule.split()
        flag_dict[flag_name] = flag_arg_type

    for command in commands:
        items = []
        results = re.finditer(
            f'{PATTERNS["NUMBERS"]}|{PATTERNS["NUMBER"]}|{PATTERNS["STRINGS"]}|{PATTERNS["STRING"]}|{PATTERNS["NULL"]}|\S+', command)
        for result in results:
            items.append(result.group())

        first_word, flags = items[0], items[1:]

        if isStartWithProgram(first_word, program) == False:
            answer.append(False)
            continue

        if isFlagArgTypeMatch(flags, flag_dict) == False:
            answer.append(False)
            continue

        if isUnderMaxTimes(flags, PATTERNS["FLAG"], MAXIMUM_FLAG_COUNT) == False:
            answer.append(False)
            continue

        answer.append(True)

    return answer

# 1. command가 program으로 시작하는지 판별하는 함수


def isStartWithProgram(first_word, program):
    return first_word == program

# 2. 각 대응하는 flag의 flag_argument_type이 일치하는지 판별


def isFlagArgTypeMatch(flags, flag_dict):
    for flag in flags:
        # arg가 없는 경우
        if len(flag.split()) == 1:
            if flag_dict.get(flag) == None or flag_dict[flag] != "NULL":
                return False
            continue

        flag_items = flag.split()
        flag_name, flag_args = flag_items[0], flag_items[1:]
        # 4. flag_rules에 존재하는 flag만 나타나는지 판별
        if flag_dict.get(flag_name) == None:
            return False

        flag_arg_type = flag_dict[flag_name]
        if flag_arg_type == 'NUMBER':
            if len(flag_args) > 1:
                return False
            for arg in flag_args:
                if arg.isdigit() == False:
                    return False
        elif flag_arg_type == 'STRING':
            if len(flag_args) > 1:
                return False
            for arg in flag_args:
                if arg.isalpha() == False:
                    return False
        elif flag_arg_type == 'NULL':
            return False
        elif flag_arg_type == 'NUMBERS':
            for arg in flag_args:
                if arg.isdigit() == False:
                    return False
        elif flag_arg_type == 'STRINGS':
            for arg in flag_args:
                if arg.isalpha() == False:
                    return False
        elif flag_arg_type not in ['NUMBER', 'STRING', 'NULL', 'NUMBERS', 'STRINGS']:
            return False
    return True

# 3. 각 flag가 0번이나 1번 나타나는지 판별하는 함수


def isUnderMaxTimes(flags, FLAG_PATTERN, MAXIMUM_FLAG_COUNT):
    flag_count_dict = {}
    for flag in flags:
        flag_name = re.findall(FLAG_PATTERN, flag)
        if flag_name:
            if flag_count_dict.get(flag_name[0]) == None:
                flag_count_dict[flag_name[0]] = 1
            else:
                flag_count_dict[flag_name[0]] += 1
            if flag_count_dict[flag_name[0]] > MAXIMUM_FLAG_COUNT:
                return False
    return True
