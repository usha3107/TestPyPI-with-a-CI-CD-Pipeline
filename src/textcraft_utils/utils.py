"""Core text utility functions for textcraft_utils.

This module provides essential string manipulation, transformation,
and analysis functions with robust edge-case handling.
"""

from __future__ import annotations

import re


def slugify(text: str, delimiter: str = "-") -> str:
    """Converts a string to a URL-friendly slug.

    Transforms input text by stripping leading/trailing whitespace,
    converting to lowercase, replacing whitespace, underscores, and hyphens
    with a chosen delimiter, and removing characters that are not alphanumeric
    or the delimiter.

    Args:
        text: The input string to convert.
        delimiter: The character used to separate words (default is '-').

    Returns:
        A sanitized, URL-friendly slug string.

    Examples:
        >>> slugify("Hello World!")
        'hello-world'
        >>> slugify(" leading and trailing spaces ")
        'leading-and-trailing-spaces'
        >>> slugify("Python & Packaging_CI-CD", delimiter="_")
        'python_packaging_ci_cd'
    """
    if not text:
        return ""

    # Convert to lowercase and strip whitespace
    cleaned = text.lower().strip()

    # Replace whitespace, hyphens, and underscores with the delimiter
    cleaned = re.sub(r"[\s_-]+", delimiter, cleaned)

    # Escape delimiter for regex safety
    escaped_delimiter = re.escape(delimiter)

    # Strip any characters that are not alphanumeric or the delimiter
    pattern = rf"[^a-z0-9{escaped_delimiter}]"
    cleaned = re.sub(pattern, "", cleaned)

    # Collapse multiple consecutive delimiters into a single delimiter
    cleaned = re.sub(rf"{escaped_delimiter}+", delimiter, cleaned)

    # Strip leading and trailing delimiters
    return cleaned.strip(delimiter)


def count_words(text: str) -> int:
    """Counts the number of words in a string.

    Words are defined as whitespace-separated character sequences.
    Empty strings or strings containing only whitespace return 0.

    Args:
        text: The string to count words in.

    Returns:
        The total count of words in the string.

    Examples:
        >>> count_words("one two three")
        3
        >>> count_words("")
        0
        >>> count_words("   hello   world   ")
        2
    """
    if not text or not text.strip():
        return 0
    return len(text.split())


def to_uppercase(text: str) -> str:
    """Converts a string to uppercase.

    Args:
        text: The string to convert.

    Returns:
        The uppercase representation of the input string.

    Examples:
        >>> to_uppercase("hello world")
        'HELLO WORLD'
        >>> to_uppercase("")
        ''
    """
    return text.upper()


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncates a string to a specified maximum length and appends a suffix.

    If the text is shorter than or equal to max_length, it is returned unchanged.
    If truncated, the resulting string length including suffix will equal max_length
    (or suffix length if max_length is less than suffix length).

    Args:
        text: The input string to truncate.
        max_length: The maximum allowed length of the output string.
        suffix: The string to append if truncated (default: '...').

    Returns:
        The truncated string with suffix appended if truncated.

    Raises:
        ValueError: If max_length is negative.

    Examples:
        >>> truncate("Hello World", 8)
        'Hello...'
        >>> truncate("Short", 10)
        'Short'
    """
    if max_length < 0:
        raise ValueError("max_length must be non-negative")

    if len(text) <= max_length:
        return text

    if max_length <= len(suffix):
        return suffix[:max_length]

    cutoff = max_length - len(suffix)
    return text[:cutoff] + suffix


def extract_hashtags(text: str) -> list[str]:
    """Extracts all unique hashtags from a given text.

    Finds words prefixed with '#', strips punctuation, and returns a list
    of lowercase hashtag strings in the order of first appearance.

    Args:
        text: The text containing hashtags.

    Returns:
        A list of extracted hashtag names without the '#' symbol.

    Examples:
        >>> extract_hashtags("Loving the new #python release! #coding #Python")
        ['python', 'coding']
        >>> extract_hashtags("No hashtags here.")
        []
    """
    if not text:
        return []

    # Match # followed by word characters (letters, numbers, underscores)
    matches = re.findall(r"#([A-Za-z0-9_]+)", text)

    # Preserve order while deduplicating in lowercase
    seen = set()
    result = []
    for tag in matches:
        lowered = tag.lower()
        if lowered not in seen:
            seen.add(lowered)
            result.append(lowered)

    return result
