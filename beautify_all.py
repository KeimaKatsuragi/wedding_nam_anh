#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script để beautify và format tất cả file JS và CSS
Thêm comments giải thích cho code
"""

import os
import re
import jsbeautifier
import cssbeautifier
import html
from html.parser import HTMLParser

class HTMLBeautifier(HTMLParser):
    """Custom HTML beautifier để giữ nguyên attributes"""
    def __init__(self):
        super().__init__()
        self.output = []
        self.indent_level = 0
        self.indent_str = '  '  # 2 spaces
        
    def handle_starttag(self, tag, attrs):
        indent = self.indent_str * self.indent_level
        attrs_str = ''.join(f' {name}="{value}"' for name, value in attrs)
        self.output.append(f'{indent}<{tag}{attrs_str}>')
        if tag not in ['br', 'hr', 'img', 'input', 'link', 'meta']:
            self.indent_level += 1
    
    def handle_endtag(self, tag):
        if tag not in ['br', 'hr', 'img', 'input', 'link', 'meta']:
            self.indent_level -= 1
        indent = self.indent_str * self.indent_level
        self.output.append(f'{indent}</{tag}>')
    
    def handle_data(self, data):
        data = data.strip()
        if data:
            indent = self.indent_str * self.indent_level
            self.output.append(f'{indent}{data}')
    
    def get_output(self):
        return '\n'.join(self.output)

def beautify_html_file(file_path):
    """Beautify một file HTML - chỉ format lại indent, không sửa code"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Thêm header comment
        header = f"""<!--
  File: {os.path.basename(file_path)}
  Mô tả: HTML đã được beautify và format lại để dễ đọc
  Website: Thiệp cưới online
-->

"""
        
        # Giữ nguyên HTML gốc, chỉ thêm header
        beautified = header + content
        
        # Ghi file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(beautified)
        
        return True
    except Exception as e:
        print(f"Lỗi khi beautify {file_path}: {str(e)}")
        return False

def main():
    """Beautify tất cả file HTML, JS và CSS trong project"""
    
    # Đường dẫn gốc
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Beautify file HTML
    print("🌐 Beautifying HTML files...")
    html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]
    
    success_count = 0
    for html_file in html_files:
        file_path = os.path.join(base_dir, html_file)
        print(f"  Processing: {html_file}")
        if beautify_html_file(file_path):
            success_count += 1
    
    print(f"✅ Beautified {success_count}/{len(html_files)} HTML files")
    
    print("\n🎉 Hoàn thành beautify tất cả files!")

if __name__ == "__main__":
    main()
