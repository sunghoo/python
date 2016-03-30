from os import remove, rename
from random import randint

def get_user_point(user_name):
    try:
        org_file = open("점수.txt", "r", encoding="utf8")
        for line in org_file:
            content = line.split(", ")
            if content[0] == user_name:
                org_file.close()
                return content[1]
        return "-1"
    except IOError:
        print("점수.txt 파일이 없습니다.\n파일이 생성됩니다.")
        org_file = open("점수.txt", "w", encoding="utf8")
        org_file.close()
        return "-1"

def update_user_points(new_user, user_name, user_score):

    user_name = str(user_name)

    if new_user:
        org_file = open("점수.txt", "a", encoding="utf8")
        org_file.write("\n" + user_name + ", " + user_score)
        org_file.close()
    else:
        org_file = open("점수.txt", "r", encoding="utf8")
        temp_file = open("점수.tmp", "w", encoding="utf8")

        line_dic = {}

        for index, line in enumerate(org_file):
            content = line.split(", ")
            if content[0] == user_name:
                content[1] = user_score

            if content[0] != "\n":
                line_dic[content[0].strip()] = content[1].strip()

        # 첫 줄 입력
        temp_file.write("\n")
        i = 0
        for val in line_dic:
            if i < len(line_dic) - 1:
                open_line = "\n"
            else:
                open_line = ""
            temp_file.write(val + ", " + line_dic[val] + open_line)
            i += 1

        org_file.close()
        temp_file.close()

        remove("점수.txt")
        rename("점수.tmp", "점수.txt")

def generate_question():
    operand_list = [0, 0, 0, 0, 0]
    operator_list = ["", "", "", ""]
    operator_dic = {1: "+", 2: "-", 3: "*", 4: "**"}
    question_string = ""

    for i in range(len(operand_list)):
        operand_list[i] = randint(1, 9)

    for i in range(len(operator_list)):

        operator_index = randint(1, len(operator_dic))
        operator_list[i] = operator_dic[operator_index]

        if operator_index == len(operator_dic):
            del operator_dic[len(operator_dic)]

    for index, num in enumerate(operand_list):
        question_string += str(num)
        if index < len(operator_list):
            question_string += str(operator_list[index])

    result = eval(question_string)
    print("\n" + question_string.replace("**", "^"))

    user_result = input("답: ")

    while True:
        try:
            if int(user_result) == result:
                print("정답입니다.")
                return 1
            else:
                print("틀렸습니다. 답은", result, " 입니다.")
                return 0
        except Exception as e:
            print("숫자만 입력해 주세요.", e)
            user_result = input("답: ")
