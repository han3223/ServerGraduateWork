import nltk
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import os
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import PyPDF2

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


# Функция для извлечения текста из PDF-файла
def extract_text_from_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text


# Функция для удаления специальных символов и нерелевантных слов
def remove_special_and_irrelevant_words(tokens):
    # Замена специальных символов на пробелы
    new_tokens = [re.sub(r'[^a-zA-Zа-яА-Я0-9]', ' ', token) for token in tokens]
    # Удаление нерелевантных слов
    new_tokens = [token for token in new_tokens if token.lower() not in stopwords.words('russian')]
    return new_tokens


# Функция для нормализации текста
def normalize_text(input_text):
    lemmatizer = WordNetLemmatizer()
    # Токенизация текста
    new_tokens = word_tokenize(input_text)
    # Удаление специальных символов и нерелевантных слов
    new_tokens = remove_special_and_irrelevant_words(new_tokens)
    # Нормализация слов
    normalized_new_tokens = [lemmatizer.lemmatize(token.lower()) for token in new_tokens]
    return normalized_new_tokens


# Путь к тренировочным PDF-файлам
train_data_path = "C:/Users/Ivan/Desktop/Android приложение по базе научных статей/Статьи"

# Подготовка тренировочных данных
train_documents = []
for filename in os.listdir(train_data_path):
    if filename.endswith(".pdf"):
        file_path = os.path.join(train_data_path, filename)
        # Извлекаем текст из PDF-файла
        my_text = extract_text_from_pdf(file_path)
        # Нормализация текста
        normalized_tokens = normalize_text(my_text)
        # Создаем объект TaggedDocument, где каждый документ имеет уникальный тег
        train_documents.append(TaggedDocument(words=normalized_tokens, tags=[filename]))

# Обучение модели Doc2Vec
model = Doc2Vec(train_documents, vector_size=800, window=15, min_count=2, workers=2, epochs=60)

# Пример применения обученной модели
test_document_path = "C:/Users/Ivan/Desktop/Android приложение по базе научных статей/Статьи/elibrary_12111300_37188088.pdf"
test_text = extract_text_from_pdf(test_document_path)
tokens = word_tokenize(test_text)

# Получение векторного представления тестового документа
test_vector = model.infer_vector(tokens)

# Поиск наиболее похожих документов в базе данных
similar_documents = model.docvecs.most_similar([test_vector])
for doc_name, similarity in similar_documents:
    print(f"Название документа: {doc_name}\nСтепень схожести: {similarity * 100}")
