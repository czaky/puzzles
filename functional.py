"""Tools and utilities related to functional programming."""

from __future__ import annotations


def bit(x) -> int:
    """Turn an object to 1 or 0."""
    # Avoids attempts at parsing.
    return 1 if x else 0


def identity(a, *args):
    """Return the same thing back."""
    return (a, *args) if args else a
