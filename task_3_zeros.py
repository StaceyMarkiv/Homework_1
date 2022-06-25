def zeros(n):
    i = 5
    result = 0
    while n >= i:
        result += n // i
        i *= 5
    return result


if __name__ == "__main__":
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7
