from itertools import combinations


def solution(snapshots, transactions):
    answer = []
    dict = {}
    visited = []
    for snapshot in snapshots:
        dict[snapshot[0]] = int(snapshot[1])

    for id, action, target, money in transactions:
        if id not in visited:
            visited.append(id)
            if target in dict:
                dict[target] = dict[target] + \
                    int(money) if action == 'SAVE' else dict[target] - int(
                        money)
            else:
                dict[target] = int(money) if action == 'SAVE' else 0
    for key, value in dict.items():
        answer.append([key, str(value)])
    return answer


def main():
    snapshots1 = [["ACCOUNT1", "100"], ["ACCOUNT2", "150"]]
    transactions1 = [["1", "SAVE", "ACCOUNT2", "100"], ["2", "WITHDRAW", "ACCOUNT1", "50"],
                     ["1", "SAVE", "ACCOUNT2", "100"], ["4", "SAVE", "ACCOUNT3", "500"], ["3", "WITHDRAW", "ACCOUNT2", "30"]]

    print('test1 : ', solution(snapshots1, transactions1))


main()
