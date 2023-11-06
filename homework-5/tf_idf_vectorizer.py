from count_vectorizer import CountVectorizer
from tf_idf_transformer import TfidfTransformer
from typing import List


class TfidfVectorizer(CountVectorizer):
    """
    Класс реализует векторизатор tf-idf
    """
    def __init__(self):
        super().__init__()
        self.tfidf_ = TfidfTransformer()

    def fit_transform(self, corpus: List[str]) -> List[List[float]]:
        """
        Метод преобразует текстовый корпус в матрицу tf-idf

        Parameters
        ----------
        corpus : List[str]
            Список текстов для векторизации

        Returns
        -------
        List[List[float]]
            Матрица tf-idf
        """
        count_matrix = super().fit_transform(corpus)
        return self.tfidf_.fit_transform(count_matrix)
