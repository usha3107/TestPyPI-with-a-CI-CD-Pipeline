"""TextCraft Utils - Modern text processing and manipulation utility library.

This library provides clean, robust string transformations, slugification,
word counting, truncation, and hashtag extraction.
"""

from .utils import (
    count_words,
    extract_hashtags,
    slugify,
    to_uppercase,
    truncate,
)

__version__ = "0.0.1"

__all__ = [
    "count_words",
    "extract_hashtags",
    "slugify",
    "to_uppercase",
    "truncate",
    "__version__",
]
