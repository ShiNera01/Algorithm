def solution(genres, plays):
    answer = []
    
    genre_total = dict()
    
    for i in range(len(genres)):
        if genres[i] in genre_total:
            genre_total[genres[i]] += plays[i]
        else:
            genre_total[genres[i]] = plays[i]
    
    genre_total = sorted(genre_total.items(), key = lambda x : -x[1])
    
    
    genres_index = [[] * 1 for _ in range(len(genre_total))]
    
    for i in range(len(genre_total)):
        for j in range(len(genres)):
            if genre_total[i][0] == genres[j]:
                genres_index[i].append(j)
    
    for i in range(len(genres_index)):
        genres_index[i] = sorted(genres_index[i], key = lambda x :  (-plays[x],x) )
    
    print(genres_index)
    
    for i in range(len(genres_index)):
        if len(genres_index[i]) == 1:
            answer.append(genres_index[i][0])
        else:
            answer.append(genres_index[i][0])
            answer.append(genres_index[i][1])
    
    
    return answer
