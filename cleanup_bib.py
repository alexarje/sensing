#!/usr/bin/env python3
"""
BibTeX Cleanup Script

This script cleans up common BibTeX syntax errors and formatting issues.
It handles:
- Malformed escape sequences
- Missing braces around special characters
- Inconsistent field formatting
- Empty fields
- Duplicate entries (basic detection)
- File path fields that may cause issues

Usage:
    python cleanup_bib.py input.bib output.bib
"""

import re
import sys
import argparse
from collections import defaultdict
from pathlib import Path


def fix_escape_sequences(text):
    """Fix common escape sequence problems in BibTeX."""
    # Fix malformed apostrophes like {\' } -> {\'}  and {\'}s -> {\'s}
    text = re.sub(r"\{\\'\s*\}", r"{\\'}", text)
    text = re.sub(r"\{\\'\\}", r"{\\'}", text)  # Remove double backslashes
    text = re.sub(r"\{\\'\}s", r"{\'s}", text)  # Fix possessive forms
    
    # Fix double braces around accented characters like {{\'c}} -> {\'c}
    text = re.sub(r"\{\{\\(.)\}\}", r"{\\1}", text)
    
    # Fix malformed umlauts like {\"o} (should be already correct but ensure consistency)
    text = re.sub(r"\{\\\"([a-zA-Z])\}", r'{\\"\1}', text)
    
    # Fix other common accent patterns
    text = re.sub(r"\{\\`([a-zA-Z])\}", r'{\\`\1}', text)  # grave
    text = re.sub(r"\{\\'([a-zA-Z])\}", r"{\\'\\1}", text)  # acute
    text = re.sub(r"\{\\^([a-zA-Z])\}", r'{\\^\1}', text)  # circumflex
    text = re.sub(r"\{\\~([a-zA-Z])\}", r'{\\~\1}', text)  # tilde
    text = re.sub(r"\{\\=([a-zA-Z])\}", r'{\\=\1}', text)  # macron
    text = re.sub(r"\{\\\.([a-zA-Z])\}", r'{\\\.\1}', text)  # dot above
    
    return text


def clean_field_value(value):
    """Clean a BibTeX field value."""
    if not value:
        return value
    
    # Remove leading/trailing whitespace
    value = value.strip()
    
    # Fix escape sequences
    value = fix_escape_sequences(value)
    
    # Remove file paths that might cause issues (optional - uncomment if needed)
    # if value.startswith('/') or value.startswith('C:'):
    #     return ''
    
    return value


def parse_bib_entry(entry_text):
    """Parse a single BibTeX entry and return cleaned version."""
    lines = entry_text.strip().split('\n')
    if not lines:
        return None
    
    # Extract entry type and key
    first_line = lines[0].strip()
    if not first_line.startswith('@'):
        return None
    
    try:
        entry_match = re.match(r'@(\w+)\{([^,]+),?', first_line)
        if not entry_match:
            return None
        
        entry_type = entry_match.group(1)
        entry_key = entry_match.group(2)
        
        # Parse fields
        fields = {}
        current_field = None
        current_value = []
        
        for line in lines[1:]:
            line = line.strip()
            if not line or line == '}':
                continue
            
            # Check if this starts a new field
            field_match = re.match(r'(\w+)\s*=\s*(.+)', line)
            if field_match:
                # Save previous field if exists
                if current_field:
                    field_value = ' '.join(current_value).rstrip(',')
                    fields[current_field] = clean_field_value(field_value)
                
                # Start new field
                current_field = field_match.group(1)
                current_value = [field_match.group(2)]
            else:
                # Continuation of current field
                if current_field:
                    current_value.append(line)
        
        # Save last field
        if current_field:
            field_value = ' '.join(current_value).rstrip(',')
            fields[current_field] = clean_field_value(field_value)
        
        # Remove empty fields
        fields = {k: v for k, v in fields.items() if v and v.strip()}
        
        # Format the cleaned entry
        result = f"@{entry_type}{{{entry_key}"
        if fields:
            result += ",\n"
            field_lines = []
            for field, value in fields.items():
                # Skip problematic file fields (optional)
                if field == 'file' and (value.startswith('/') or 'Dropbox' in value):
                    continue
                field_lines.append(f"  {field} = {value}")
            result += ",\n".join(field_lines)
        result += "\n}\n"
        
        return result
        
    except Exception as e:
        print(f"Error parsing entry starting with: {first_line[:50]}...")
        print(f"Error: {e}")
        return None


def clean_bib_file(input_path, output_path, remove_file_paths=True):
    """Clean a BibTeX file."""
    try:
        with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except UnicodeDecodeError:
        print("Trying with latin-1 encoding...")
        with open(input_path, 'r', encoding='latin-1') as f:
            content = f.read()
    
    # Split into entries
    entries = re.split(r'\n@', content)
    
    cleaned_entries = []
    entry_keys = set()
    duplicate_count = 0
    error_count = 0
    
    for i, entry in enumerate(entries):
        if not entry.strip():
            continue
        
        # Add @ back if it was removed by split
        if not entry.startswith('@'):
            entry = '@' + entry
        
        # Parse and clean the entry
        cleaned = parse_bib_entry(entry)
        if cleaned:
            # Basic duplicate detection
            key_match = re.search(r'@\w+\{([^,\n]+)', cleaned)
            if key_match:
                key = key_match.group(1)
                if key in entry_keys:
                    print(f"Duplicate entry found: {key}")
                    duplicate_count += 1
                    continue
                entry_keys.add(key)
            
            cleaned_entries.append(cleaned)
        else:
            error_count += 1
            print(f"Failed to parse entry {i+1}")
    
    # Write cleaned file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(cleaned_entries))
    
    print(f"Cleanup complete!")
    print(f"  Processed: {len(entries)} entries")
    print(f"  Cleaned: {len(cleaned_entries)} entries")
    print(f"  Errors: {error_count} entries")
    print(f"  Duplicates removed: {duplicate_count} entries")
    print(f"  Output written to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description='Clean up BibTeX files')
    parser.add_argument('input', help='Input BibTeX file')
    parser.add_argument('output', help='Output BibTeX file')
    parser.add_argument('--keep-file-paths', action='store_true', 
                       help='Keep file path fields (default: remove them)')
    
    args = parser.parse_args()
    
    if not Path(args.input).exists():
        print(f"Error: Input file '{args.input}' not found")
        sys.exit(1)
    
    remove_paths = not args.keep_file_paths
    clean_bib_file(args.input, args.output, remove_paths)


if __name__ == '__main__':
    main()
