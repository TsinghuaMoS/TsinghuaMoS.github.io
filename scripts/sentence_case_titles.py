#!/usr/bin/env python3
"""Compatibility entry point; canonical sentence-case titles now live in Excel."""
from sync_publications import main

if __name__ == '__main__':
    print('Titles are maintained in documents/papers.xlsx; regenerating all publication outputs.')
    main()
