"""Unit tests for textcraft_utils package."""

import pytest
from textcraft_utils import (
    __version__,
    count_words,
    extract_hashtags,
    slugify,
    to_uppercase,
    truncate,
)


def test_package_metadata():
    """Verify package version and exported members."""
    assert __version__ == "0.0.1"


class TestSlugify:
    """Test suite for slugify function."""

    def test_basic_slugify(self):
        assert slugify("Hello World!") == "hello-world"

    def test_leading_and_trailing_spaces(self):
        assert slugify(" leading and trailing spaces ") == "leading-and-trailing-spaces"

    def test_special_characters_and_symbols(self):
        assert slugify("Python & Packaging_CI-CD") == "python-packaging-ci-cd"

    def test_custom_delimiter(self):
        assert slugify("Custom Delimiter Test", delimiter="_") == "custom_delimiter_test"

    def test_empty_string(self):
        assert slugify("") == ""

    def test_symbols_only(self):
        assert slugify("!@#$%^&*()_+") == ""

    def test_repeated_delimiters_collapsed(self):
        assert slugify("a   ---   b") == "a-b"


class TestCountWords:
    """Test suite for count_words function."""

    def test_multiple_words(self):
        assert count_words("one two three") == 3

    def test_empty_string(self):
        assert count_words("") == 0

    def test_whitespace_only(self):
        assert count_words("   \t  \n  ") == 0

    def test_single_word(self):
        assert count_words("antigravity") == 1

    def test_irregular_spacing(self):
        assert count_words("  hello   world  from \n python \t ") == 4


class TestToUppercase:
    """Test suite for to_uppercase function."""

    def test_lowercase_conversion(self):
        assert to_uppercase("hello world") == "HELLO WORLD"

    def test_mixed_case(self):
        assert to_uppercase("PyThOn 3.11") == "PYTHON 3.11"

    def test_empty_string(self):
        assert to_uppercase("") == ""


class TestTruncate:
    """Test suite for truncate function."""

    def test_shorter_than_limit(self):
        assert truncate("Short", 10) == "Short"

    def test_exact_limit(self):
        assert truncate("Exact", 5) == "Exact"

    def test_truncation_with_default_suffix(self):
        assert truncate("Hello World", 8) == "Hello..."

    def test_max_length_less_than_suffix(self):
        assert truncate("Hello World", 2, suffix="...") == ".."

    def test_max_length_zero(self):
        assert truncate("Hello World", 0) == ""

    def test_custom_suffix(self):
        assert truncate("Testing custom suffix", 12, suffix="~") == "Testing cus~"

    def test_negative_length_raises_error(self):
        with pytest.raises(ValueError, match="max_length must be non-negative"):
            truncate("Sample", -1)


class TestExtractHashtags:
    """Test suite for extract_hashtags function."""

    def test_multiple_hashtags_deduplication(self):
        text = "Loving the new #python release! #coding #Python #dev"
        assert extract_hashtags(text) == ["python", "coding", "dev"]

    def test_no_hashtags(self):
        assert extract_hashtags("Plain text without tags") == []

    def test_empty_string(self):
        assert extract_hashtags("") == []

    def test_alphanumeric_and_underscore_tags(self):
        text = "Join #100DaysOfCode and follow #ai_tools!"
        assert extract_hashtags(text) == ["100daysofcode", "ai_tools"]
