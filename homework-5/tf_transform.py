from typing import List


def tf_transform(count_matrix: List[List[int]]) -> List[List[float]]:
    """
    Преобразовать матрицу частот в матрицу TF

    Parameters
    ----------
    count_matrix : List[List[int]]
       матрица подсчетов входления i-го слова в j-том тексте

    Returns
    -------
    List[List[float]]
        матрица TF
    """
    result = []
    for vec in count_matrix:
        sum_vec = sum(vec)
        if sum_vec == 0:
            result.append([0.0] * len(vec))
        else:
            tf = [symb / sum_vec for symb in vec]
            result.append(tf)
    return result
