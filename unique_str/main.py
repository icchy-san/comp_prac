def is_unique_char(word: str) -> bool:
    """
    与えられた文字列に重複があるかを判定する関数

    :param word: str
    :rtype: bool
    """

    unique_char_list = set(word)
    return len(word) == len(unique_char_list)


if __name__ == '__main__':
    # modify input_str value
    input_str = 'sample'
    print(is_unique_char(input_str))
