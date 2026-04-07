from __future__ import annotations

from pathlib import Path
import re


def load_text(path: str) -> str:
    """Load and return the full text from a UTF-8 file."""
    return Path(path).read_text(encoding="utf-8")


def normalize_text(text: str) -> str:
    """Return a normalized version of the text."""
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def tokenize(text: str) -> list[str]:
    """Split normalized text into a list of words."""
    if not text:
        return []
    return text.split()


def count_words(words: list[str]) -> dict[str, int]:
    """Count how many times each word appears."""
    counts: dict[str, int] = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts


def top_n_words(counts: dict[str, int], n: int) -> list[tuple[str, int]]:
    """Return the top N words."""
    if n <= 0:
        return []

    sorted_items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]


def extra_insight(words: list[str], counts: dict[str, int]) -> object:
    """Return words that appear only once."""
    return [word for word, count in counts.items() if count == 1]


def run_demo(path: str, n: int = 10) -> dict[str, object]:
    """Run full pipeline."""
    text = load_text(path)
    normalized = normalize_text(text)
    words = tokenize(normalized)
    counts = count_words(words)

    return {
        "total_words": len(words),
        "unique_words": len(counts),
        "top_words": top_n_words(counts, n),
        "extra_insight": extra_insight(words, counts),
    }


if __name__ == "__main__":
    demo_path = Path("data/sample.txt")
    if demo_path.exists():
        results = run_demo(str(demo_path), n=10)
        for key, value in results.items():
            print(f"{key}: {value}")
    else:
        print("No demo file found at data/sample.txt")