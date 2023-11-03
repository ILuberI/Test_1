def N_to_B (N, B):
    A = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []

    while N > 0:
        N, X = divmod(N, B)
        result.append(A[X])

    return "".join(result[::-1])

N, B = map(int, input().split())
result = N_to_B(N, B)
print(result)