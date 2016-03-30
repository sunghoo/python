try:
    import myPythonFunctions as myFn

    user_name = input("사용자 이름을 입력하세요: ")
    user_score = int(myFn.get_user_point(user_name))

    if user_score == -1:
        newUser = True
        user_score = 0
    else:
        newUser = False

    user_choice = 0

    while user_choice != '-1':
        user_score += myFn.generate_question()
        print("현재점수 = ", user_score)
        user_choice = input("계속 하려면 Enter, 끝내려면 -1: ")

    myFn.update_user_points(newUser, user_name, str(user_score))

except Exception as e:
    # print("예기치 않은 오류가 발생했습니다. 프로그램이 종료됩니다.")
    print(e)
