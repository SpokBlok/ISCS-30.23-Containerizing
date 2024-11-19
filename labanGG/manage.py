#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management import execute_from_command_line

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "labanGG.settings")
    port = os.getenv("$PORT", "8080")
    execute_from_command_line(["manage.py", "runserver", f"0.0.0.0:{port}"])


if __name__ == '__main__':
    main()
