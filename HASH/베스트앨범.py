def solution(genres, plays):
    answer = []
    my_dict = {}
    n = len(genres)
    for i in range(n):
        genre = genres[i]
        play = plays[i]
        if my_dict.get(genre) == None:
            my_dict[genre] = [(i, play)]
        else:
            my_dict[genre].append((i, play))
    for key in my_dict:
        my_dict[key].sort(key=lambda x: -x[1])

    albums = []
    for value in my_dict.values():
        total_play = sum([play[1] for play in value])
        albums.append([total_play, [play[0] for play in value]])
    albums.sort(key=lambda x: -x[0])

    for album in albums:
        answer += album[1][:2]

    return answer
