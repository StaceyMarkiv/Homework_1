from itertools import permutations


def bananas(s) -> set:
    word = "banana"
    if s.count("b") >= 1 and s.count("a") >= 3 and s.count("n") >= 2:
        addition = "-" * (len(s) - len(word))
        test_word = word + addition
        variants = set(list(permutations(test_word)))

        result_list = []
        for var in variants:
            test_res_word = "".join(var)
            new_test_word = test_res_word.replace("-", "")
            # Проверяем, соответствует ли полученная комбинация букв без "-" слову "banana":
            if new_test_word == word:
                count = 0
                for i in range(len(s)):
                    # Проверяем, находятся ли буквы в полученной комбинации на тех же местах, что и в исходной строке:
                    if test_res_word[i] != "-" and test_res_word[i] == s[i]:
                        count += 1
                if count == len(word):
                    result_list.append(test_res_word)
        result = set(result_list)

    else:
        result = set()

    return result


if __name__ == "__main__":
    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                    "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                    "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
