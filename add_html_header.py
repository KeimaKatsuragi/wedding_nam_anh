#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script để thêm header comment cho HTML
KHÔNG format HTML vì HTML quá phức tạp với inline styles
"""

import os

def add_html_header(file_path):
    """Chỉ thêm header comment vào HTML, không format"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Kiểm tra xem đã có header chưa
        if '<!-- File:' in content or 'Mô tả: HTML đã được beautify' in content:
            print(f"  Skipped (already has header): {os.path.basename(file_path)}")
            return True
        
        # Thêm header comment
        header = f"""<!--
  File: {os.path.basename(file_path)}
  Mô tả: File HTML gốc - KHÔNG được beautify do code quá phức tạp
  Lưu ý: HTML này có nhiều inline styles và attributes phức tạp
        Beautify HTML có thể làm hỏng code, nên giữ nguyên
-->

"""
        beautified = header + content
        
        # Ghi file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(beautified)
        
        print(f"  ✅ Added header: {os.path.basename(file_path)}")
        return True
    except Exception as e:
        print(f"  ❌ Error: {file_path}: {str(e)}")
        return False

def main():
    """Thêm header cho file HTML"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("📄 Adding header to HTML files...")
    html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]
    
    for html_file in html_files:
        file_path = os.path.join(base_dir, html_file)
        add_html_header(file_path)
    
    print(f"\n✅ Done! Processed {len(html_files)} HTML file(s)")

if __name__ == "__main__":
    main()
