import time
from functools import lru_cache

def count_palindromic_substrings_with_memo(string: str) -> int:
    if not string:
        return 0

    @lru_cache(maxsize=None)
    def is_palindrome(i: int, j: int) -> bool:
        if i >= j:
            return True
        if string[i] != string[j]:
            return False
        return is_palindrome(i + 1, j - 1)

    count = 0
    n = len(string)
    for i in range(n):
        for j in range(i, n):
            if is_palindrome(i, j):
                count += 1
    return count

def count_palindromic_substrings_without_memo(string: str) -> int:
    if not string:
        return 0

    def is_palindrome(i: int, j: int) -> bool:
        if i >= j:
            return True
        if string[i] != string[j]:
            return False
        return is_palindrome(i + 1, j - 1)

    count = 0
    n = len(string)
    for i in range(n):
        for j in range(i, n):
            if is_palindrome(i, j):
                count += 1
    return count

def compare_execution_time(string: str) -> None:
    print(f"String: {string[:10]}{'...' if len(string) >= 10 else ''} (tamanho: {len(string)})")

    start_time = time.perf_counter()
    count_with_memo = count_palindromic_substrings_with_memo(string)
    time_with_memo = time.perf_counter() - start_time

    start_time = time.perf_counter()
    count_without_memo = count_palindromic_substrings_without_memo(string)
    time_without_memo = time.perf_counter() - start_time

    time.sleep(1)
    print(f"Resultado (com memoização): {count_with_memo} substrings palíndromas")
    time.sleep(1)
    print(f"Tempo (com memoização): {time_with_memo:.6f} segundos")
    time.sleep(1)
    print(f"Resultado (sem memoização): {count_without_memo} substrings palíndromas")
    time.sleep(1)
    print(f"Tempo (sem memoização): {time_without_memo:.6f} segundos")
    time.sleep(1)
    print(f"Razão de tempo: {time_without_memo / time_with_memo:.2f}x mais lento sem memoização")

string = 'a' * 500
compare_execution_time(string)