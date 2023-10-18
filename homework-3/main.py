from typing import List
from count_vectorizer import CountVectorizer


if __name__ == '__main__':
    corpus: List[str] = []
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
