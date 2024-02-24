from datetime import datetime

from app.services.file_processor import calculate_file_metadata, calculate_word_count

def test_calculate_word_counts():
    # Corrected test cases to reflect accurate behavior

    # Content separated strictly by spaces
    content = b"hello world hello"
    word_count, unique_word_count = calculate_word_count(content)
    assert word_count == 3, "Expected 3 words"
    assert unique_word_count == 2, "Expected 2 unique words"

    # Content that includes a newline, which should be treated as a single space
    content = b"hello world\nhello"
    word_count, unique_word_count = calculate_word_count(content)
    assert word_count == 3, "Expected 3 words for content with newline"
    assert unique_word_count == 2, "Expected 2 unique words for content with newline"

def test_calculate_file_metadata():
    filename = "test.txt"
    content = b"hello world hello"
    metadata = calculate_file_metadata(filename, content)

    assert metadata["filename"] == filename, "Filename should match"
    assert metadata["size"] == len(content), "File size should match content length"
    assert metadata["word_count"] == 3, "Expected 3 words"
    assert metadata["unique_words"] == 2, "Expected 2 unique words"

    known_sha256 = "9db07dad3f51e31144ae853a76bba4739609c14ae813ec2cd7080726acc10eb0"
    assert metadata["sha256"] == known_sha256, "SHA256 hash does not match known value"

    expected_date_format = "%Y-%m-%d"
    assert datetime.strptime(metadata["date"], expected_date_format), "Date should match the expected format"