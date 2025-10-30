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

def beautify_js_file(file_path):
    """Beautify một file JavaScript"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Cấu hình beautifier
        opts = jsbeautifier.default_options()
        opts.indent_size = 2
        opts.indent_char = ' '
        opts.max_preserve_newlines = 2
        opts.preserve_newlines = True
        opts.keep_array_indentation = False
        opts.break_chained_methods = False
        opts.indent_scripts = 'normal'
        opts.brace_style = 'collapse'
        opts.space_before_conditional = True
        opts.unescape_strings = False
        opts.jslint_happy = False
        opts.end_with_newline = True
        opts.wrap_line_length = 0
        opts.indent_inner_html = False
        opts.comma_first = False
        opts.e4x = False
        opts.indent_empty_lines = False
        
        # Beautify code
        beautified = jsbeautifier.beautify(content, opts)
        
        # Thêm header comment
        header = f"""/**
 * File: {os.path.basename(file_path)}
 * Mô tả: Code đã được beautify và format lại để dễ đọc
 * Lưu ý: Code gốc đã được minified/obfuscated, 
 *        nên tên biến vẫn giữ nguyên (e, t, n, r, ...)
 */

"""
        beautified = header + beautified
        
        # Ghi file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(beautified)
        
        return True
    except Exception as e:
        print(f"Lỗi khi beautify {file_path}: {str(e)}")
        return False

def beautify_css_file(file_path):
    """Beautify một file CSS"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Cấu hình beautifier
        opts = cssbeautifier.default_options()
        opts.indent_size = 2
        opts.indent_char = ' '
        opts.selector_separator_newline = True
        opts.end_with_newline = True
        opts.newline_between_rules = True
        opts.space_around_combinator = True
        
        # Beautify code
        beautified = cssbeautifier.beautify(content, opts)
        
        # Thêm header comment
        header = f"""/**
 * File: {os.path.basename(file_path)}
 * Mô tả: CSS đã được beautify và format lại để dễ đọc
 */

"""
        beautified = header + beautified
        
        # Ghi file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(beautified)
        
        return True
    except Exception as e:
        print(f"Lỗi khi beautify {file_path}: {str(e)}")
        return False

def main():
    """Beautify tất cả file JS và CSS trong project"""
    
    # Đường dẫn gốc
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Beautify tất cả file JS
    js_dir = os.path.join(base_dir, 'js')
    if os.path.exists(js_dir):
        print("🔧 Beautifying JavaScript files...")
        js_files = [f for f in os.listdir(js_dir) if f.endswith('.js')]
        
        success_count = 0
        for js_file in js_files:
            file_path = os.path.join(js_dir, js_file)
            print(f"  Processing: {js_file}")
            if beautify_js_file(file_path):
                success_count += 1
        
        print(f"✅ Beautified {success_count}/{len(js_files)} JS files")
    
    # Beautify tất cả file CSS
    css_dir = os.path.join(base_dir, 'css')
    if os.path.exists(css_dir):
        print("\n🎨 Beautifying CSS files...")
        css_files = [f for f in os.listdir(css_dir) if f.endswith('.css')]
        
        success_count = 0
        for css_file in css_files:
            file_path = os.path.join(css_dir, css_file)
            print(f"  Processing: {css_file}")
            if beautify_css_file(file_path):
                success_count += 1
        
        print(f"✅ Beautified {success_count}/{len(css_files)} CSS files")
    
    print("\n🎉 Hoàn thành beautify tất cả files!")

if __name__ == "__main__":
    main()
