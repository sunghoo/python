import sys

print(sys.getdefaultencoding())

username = input("사용자 이름을 입력하세요: ")


# f = open("userScores.txt", "r", encoding="utf8")
f = open("userScores.txt", "r", encoding="utf8")

for index, line in enumerate(f):

    content = line.split(", ")

    if index > 0:
        if content[0] == username:
            print(index, "y", content[0], username)
        else:
            print(index, "n", content[0], username)


f.close()
