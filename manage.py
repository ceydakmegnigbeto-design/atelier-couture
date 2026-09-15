#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, BASE_DIR)


def main():
    """Run administrative tasks."""
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "config.settings"
    )

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django n'est pas installé ou n'est pas accessible."
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()