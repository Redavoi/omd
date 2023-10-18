import re
from copy import copy
from typing import List, Dict


class CountVectorizer:
    """
    Класс реализует токенизатор текстов
    """
    def __init__(self):
        """
        Инициализировать пустой шаблон признаков
        """
        self.__features_template: Dict[str, 0] = {}

    def fit_transform(self, corpus: List[str]) -> List[List[int]] | List:
        """
        Токенизирует тексты в корпусе и заполняет признаки

        Parameters:
            corpus (List[str]): Список текстов для токенизации

        Returns:
            List[List[int]]: Список токенизированных текстов
        """
        for word in ' '.join(corpus).split(' '):
            preprocessed_word = re.sub(r'[!@#$%^&*()=+{}|;:,.<>?~]',
                                       '',
                                       word.strip().lower())
            self.__features_template[preprocessed_word] = 0

        tokenized_corpus: List[List[int]] = list()
        for text in corpus:
            cur_tokenization = copy(self.__features_template)
            for word in text.split(' '):
                preprocessed_word = re.sub(r'[!@#$%^&*()=+{}|;:,.<>?~]',
                                           '',
                                           word.strip().lower())
                cur_tokenization.setdefault(preprocessed_word, 0)
                cur_tokenization[preprocessed_word] += 1
            tokenized_corpus.append(list(cur_tokenization.values()))

        return tokenized_corpus

    def get_feature_names(self) -> List[str]:
        """
        Получить список признаков

        Returns:
            List[str]: Список признаков
        """
        return list(self.__features_template.keys())
