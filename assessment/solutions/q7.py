def rotate_list(lst:list[int],n):
    result = []
    result.append(lst[-1])
    if n == 0:
        return result
    return rotate_list(lst[::len(lst)-1],n-1)

if __name__ == '__main__':
    print(rotate_list([1,2,3,4,5],2))
