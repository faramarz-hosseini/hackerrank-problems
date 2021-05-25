def workbook(n, k, arr):
    page = 1
    special_question = 0
    max_question_on_page = 0
    for problems in arr:
        for problem_num in range(1, problems + 1):
            if max_question_on_page == k:
                page += 1
                max_question_on_page = 0
            max_question_on_page += 1
            if problem_num == page:
                special_question += 1
        max_question_on_page = 0
        page += 1

    return special_question


print(workbook(5, 3, [4, 2, 6, 1, 10]))
