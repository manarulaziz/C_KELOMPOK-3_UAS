def selection(lst, j=0, bool=True):
    for i in range(len(lst)):
        index_terkecil = i

        if bool:
            for x in range(i + 1, len(lst)):
                if lst[x][j] < lst[index_terkecil][j]:
                    index_terkecil = x
        else:
            for x in range(i + 1, len(lst)):
                if lst[x][j] > lst[index_terkecil][j]:
                    index_terkecil = x
        temp = lst[i]
        lst[i] = lst[index_terkecil]
        lst[index_terkecil] = temp