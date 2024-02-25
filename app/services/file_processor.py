import hashlib
from datetime import datetime

def calculate_file_metadata(filename: str, content: bytes) -> dict:
    """
    Calculates metadata for a given file, including SHA256 hash, file size in bytes, word count,
    number of unique words, and the current date.

    Args:
        filename (str): The name of the file.
        content (bytes): The content of the file.

    Returns:
        dict: A dictionary containing the file's metadata.
    """
    sha256_hash = hashlib.sha256(content).hexdigest()
    file_size = len(content)  # File size in bytes
    word_count, unique_word_count = calculate_word_count(content)

    return {
        "filename": filename,
        "sha256": sha256_hash,
        "size": file_size,  # Adjusted to include file size
        "word_count": word_count,
        "unique_words": unique_word_count,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

def calculate_word_count(content: bytes) -> tuple:
    """
    Calculates the total number of words and the number of unique words in the file content,
    assuming words are separated by spaces.

    Args:
        content (bytes): The content of the file.

    Returns:
        tuple: A tuple containing the total word count and the unique word count.
    """
    words = content.decode('utf-8').split()
    word_count = len(words)
    unique_word_count = len(set(words))

    return word_count, unique_word_count