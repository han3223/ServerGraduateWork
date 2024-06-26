import openai
import pdfplumber
import re


def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text


def summarize_text(text):
    openai.api_key = 'sk-proj-dZzWiJZE8knLUCw22OlkT3BlbkFJimk4C3y59YdvwhvPuRxZ'

    max_chunk_size = 10000  # Максимальное количество символов в одном запросе
    chunks = [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]

    messages = []
    for i, chunk in enumerate(chunks):
        role = "system" if i == 0 else "assistant"
        messages.append({"role": role, "content": chunk})

    pattern = "Ты должен составить на русском языке связанное по смыслу краткое описание текста (600 - 700 символов) на основе предоставленного материала. " \
              "Описание должно быть представлено на русском языке, другие языки не принимаются." \
              "Отформатировать содержание, выделив абзацы для python кода. " \
              "Текст должен содержать только текстовую информацию. " \
              "Текст для описания: " \
              f"[{messages}]"

    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "system",
                "content": pattern,
            },
        ],
    )

    return completion.choices[0].message.content


def test(text):
    # Удаляем лишние пробелы, переводы строк и знаки пунктуации
    cleaned_text = re.sub(r'\s+', ' ', text)
    cleaned_text = re.sub(r'[^a-zA-Zа-яА-Я0-9.,;:!?\'" ]', '', cleaned_text)

    # Пересказываем текст
    summarized_text = summarize_text(cleaned_text)

    return summarized_text


def main(pdf_file_path):
    # Извлекаем текст из PDF файла
    pdf_text = extract_text_from_pdf(pdf_file_path)


if __name__ == "__main__":
    pass
