#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to fix broken style attributes in HTML file
"""

import re

def fix_html_styles(input_file, output_file):
    """Fix broken style attributes in HTML"""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern 1: Fix broken font-family attributes
    # font-family:"'fontname' -> font-family:'fontname'
    # The pattern captures incomplete font-family declarations and looks for the closing part
    
    # First, let's read line by line to fix multi-line style attributes
    lines = content.split('\n')
    fixed_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if line has broken font-family
        if 'font-family:"' in line and not line.strip().endswith('">'):
            # This line is broken, need to merge with next line
            current = line
            i += 1
            
            # Find the continuation
            while i < len(lines):
                next_line = lines[i]
                # Look for the pattern that ends the style attribute
                if '";color:rgb(102,102,102)' in next_line or next_line.strip().endswith('">'):
                    # Found the end
                    current += ' ' + next_line.strip()
                    i += 1
                    break
                elif next_line.strip():
                    current += ' ' + next_line.strip()
                    i += 1
                else:
                    i += 1
                    break
            
            fixed_lines.append(current)
        else:
            fixed_lines.append(line)
            i += 1
    
    content = '\n'.join(fixed_lines)
    
    # Now fix the font-family format: font-family:"'arial' -> font-family:'arial'
    # Pattern: font-family:"'([^']+)'[^"]*"
    content = re.sub(
        r'''font-family:"'([^']+)'[^"]*";color:rgb\(([^)]+)\)''',
        r"font-family:'\1'",
        content
    )
    
    # Alternative simpler pattern for incomplete font-family
    content = re.sub(
        r'''font-family:"'([^']+)'[^>]*>''',
        r"font-family:'\1'>",
        content
    )
    
    # Fix empty font-family
    content = re.sub(
        r'''font-family:"[^>]*">''',
        r'">',
        content
    )
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed HTML saved to: {output_file}")

if __name__ == '__main__':
    fix_html_styles('index.html', 'index_fixed.html')
    print("Done! Please check index_fixed.html")
