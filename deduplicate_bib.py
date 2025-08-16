#!/usr/bin/env python3
"""
Remove duplicate entries from BibTeX file
"""

import re

def remove_duplicates(input_file, output_file):
    """Remove duplicate BibTeX entries by ID."""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into entries
    entries = re.split(r'\n@', content)
    
    seen_ids = set()
    unique_entries = []
    
    for i, entry in enumerate(entries):
        if not entry.strip():
            continue
        
        # Add @ back if it was removed by split
        if not entry.startswith('@'):
            entry = '@' + entry
        
        # Extract ID
        id_match = re.match(r'@\w+\{([^,\n]+)', entry)
        if id_match:
            entry_id = id_match.group(1)
            if entry_id not in seen_ids:
                seen_ids.add(entry_id)
                unique_entries.append(entry)
            else:
                print(f"Removing duplicate: {entry_id}")
        else:
            # Keep entries we can't parse
            unique_entries.append(entry)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(unique_entries))
    
    print(f"Deduplication complete: {len(entries)} -> {len(unique_entries)} entries")

if __name__ == '__main__':
    remove_duplicates('book/references_myst.bib', 'book/references_final.bib')
