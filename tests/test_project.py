from src.project import (
    load_text,
    normalize_text,
    tokenize,
    count_words,
    top_n_words,
    extra_insight,
)


def test_normalize_text_lowercases_text() -> None:
    assert normalize_text("Hello WORLD") == "hello world"


def test_normalize_text_removes_punctuation() -> None:
    assert normalize_text("Hello, world!") == "hello world"


def test_tokenize_splits_words() -> None:
    assert tokenize("one two three") == ["one", "two", "three"]


def test_tokenize_empty() -> None:
    assert tokenize("") == []


def test_count_words_counts_repeated_words() -> None:
    words = ["red", "blue", "red"]
    assert count_words(words) == {"red": 2, "blue": 1}


def test_count_words_empty() -> None:
    assert count_words([]) == {}


def test_top_n_words_returns_most_common_items() -> None:
    counts = {"apple": 3, "banana": 1, "carrot": 2}
    assert top_n_words(counts, 2) == [("apple", 3), ("carrot", 2)]


def test_top_n_words_tie_break() -> None:
    counts = {"apple": 2, "banana": 2}
    assert top_n_words(counts, 2) == [("apple", 2), ("banana", 2)]


def test_top_n_words_invalid_n() -> None:
    assert top_n_words({"a": 1}, 0) == []


def test_extra_insight_words_once() -> None:
    words = ["a", "b", "a", "c"]
    counts = {"a": 2, "b": 1, "c": 1}
    result = extra_insight(words, counts)
    assert sorted(result) == ["b", "c"]


def test_load_text(tmp_path) -> None:
    file = tmp_path / "file.txt"
    file.write_text("hello world", encoding="utf-8")

    assert load_text(str(file)) == "hello world"