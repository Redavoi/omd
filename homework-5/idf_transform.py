import numpy as np
from typing import List


def idf_transform(count_matrx: List[List[int]]) -> List[List[float]]:
    """
    Преобразовывает матрицу вхождений i-го слова в j-том тексте в матрицу IDF

    Parameters
    ----------
    count_matrx : List[List[int]]
        матрица подсчетов входления i-го слова в j-том тексте

    Returns
    -------
    List[List[float]]
        матрица IDF
    """
    doc_num = len(count_matrx)
    doc_freq = [sum(1 for doc in count_matrx if doc[i] > 0)
                for i in range(len(count_matrx[0]))]
    idf_matrix = [np.around((np.log((doc_num + 1) / (num + 1)) + 1), 3)
                  for num in doc_freq]
    return idf_matrix
