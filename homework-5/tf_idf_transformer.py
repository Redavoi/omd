from tf_transform import tf_transform
from idf_transform import idf_transform


class TfidfTransformer():
    """
    Класс реализует трансформер tf-idf
    """
    def fit_transform(self, count_matrix):
        tf = tf_transform(count_matrix)
        idf = idf_transform(count_matrix)
        res = []
        for doc in tf:
            res.append([t * i for t, i in zip(doc, idf)])
        return res
