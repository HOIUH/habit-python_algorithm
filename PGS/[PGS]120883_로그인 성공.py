# 231008
# [PGS] 로그인 성공 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120883

def solution(id_pw, db):
    id, pw = id_pw[0], id_pw[1]

    for e in db:
        if e[0] == id:
            if e[1] == pw:
                return "login"
            else:
                return "wrong pw"

    return "fail"
