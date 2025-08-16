#!/usr/bin/env python3
"""
MyST-specific BibTeX cleanup script

This script handles MyST's strict BibTeX requirements.
"""

import re

def clean_for_myst(input_file, output_file):
    """Clean BibTeX specifically for MyST compatibility."""
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Fix the specific problematic pattern that's causing issues
    # Replace Musician{\'}s with Musician's (simple apostrophe)
    content = re.sub(r"Musician\{\\'\}s", "Musician's", content)
    
    # Fix specific problematic pattern: Da{\" }{\i}s -> Daïs
    content = re.sub(r'Da\{\\" \}\{\\i\}s', 'Daïs', content)
    content = re.sub(r'da\{\\" \}\{\\i\}s', 'daïs', content)
    
    # More general fixes for LaTeX accents to simple characters
    content = re.sub(r"\{\\'a\}", "á", content)
    content = re.sub(r"\{\\'e\}", "é", content)
    content = re.sub(r"\{\\'i\}", "í", content)
    content = re.sub(r"\{\\'o\}", "ó", content)
    content = re.sub(r"\{\\'u\}", "ú", content)
    content = re.sub(r"\{\\'y\}", "ý", content)
    content = re.sub(r"\{\\'A\}", "Á", content)
    content = re.sub(r"\{\\'E\}", "É", content)
    content = re.sub(r"\{\\'I\}", "Í", content)
    content = re.sub(r"\{\\'O\}", "Ó", content)
    content = re.sub(r"\{\\'U\}", "Ú", content)
    content = re.sub(r"\{\\'Y\}", "Ý", content)
    
    # Handle other common accents
    content = re.sub(r"\{\\`a\}", "à", content)
    content = re.sub(r"\{\\`e\}", "è", content)
    content = re.sub(r"\{\\`i\}", "ì", content)
    content = re.sub(r"\{\\`o\}", "ò", content)
    content = re.sub(r"\{\\`u\}", "ù", content)
    
    content = re.sub(r'\{\\"a\}', "ä", content)
    content = re.sub(r'\{\\"e\}', "ë", content)
    content = re.sub(r'\{\\"i\}', "ï", content)
    content = re.sub(r'\{\\"o\}', "ö", content)
    content = re.sub(r'\{\\"u\}', "ü", content)
    content = re.sub(r'\{\\"A\}', "Ä", content)
    content = re.sub(r'\{\\"E\}', "Ë", content)
    content = re.sub(r'\{\\"I\}', "Ï", content)
    content = re.sub(r'\{\\"O\}', "Ö", content)
    content = re.sub(r'\{\\"U\}', "Ü", content)
    
    # Handle circumflex
    content = re.sub(r"\{\^a\}", "â", content)
    content = re.sub(r"\{\^e\}", "ê", content)
    content = re.sub(r"\{\^i\}", "î", content)
    content = re.sub(r"\{\^o\}", "ô", content)
    content = re.sub(r"\{\^u\}", "û", content)
    
    # Handle tilde
    content = re.sub(r"\{~a\}", "ã", content)
    content = re.sub(r"\{~n\}", "ñ", content)
    content = re.sub(r"\{~o\}", "õ", content)
    content = re.sub(r"\{~N\}", "Ñ", content)
    
    # Handle cedilla
    content = re.sub(r"\{\\c\{c\}\}", "ç", content)
    content = re.sub(r"\{\\c\{C\}\}", "Ç", content)
    
    # Handle slash
    content = re.sub(r"\{\\o\}", "ø", content)
    content = re.sub(r"\{\\O\}", "Ø", content)
    
    # Handle Nordic characters
    content = re.sub(r"\{\\aa\}", "å", content)
    content = re.sub(r"\{\\AA\}", "Å", content)
    content = re.sub(r"\{\\ae\}", "æ", content)
    content = re.sub(r"\{\\AE\}", "Æ", content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"MyST-specific cleanup complete: {output_file}")

if __name__ == '__main__':
    clean_for_myst('book/references_cleaned.bib', 'book/references_myst.bib')
