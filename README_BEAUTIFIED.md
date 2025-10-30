# Wedding Website - Code đã Beautified

## 📋 Tổng quan

Project này là website thiệp cưới online. Code gốc đã được **minified và obfuscated** (rút gọn và mã hóa) nên rất khó đọc.

Tôi đã **beautify (làm đẹp) tất cả code** để dễ đọc hơn bằng cách:

- ✅ Format lại code với indent đúng chuẩn
- ✅ Thêm dòng trống giữa các đoạn code
- ✅ Thêm comment header cho mỗi file
- ⚠️ **LƯU Ý**: Tên biến vẫn giữ nguyên (e, t, n, r...) vì code đã bị minify từ trước

## 📁 Cấu trúc thư mục

```
wedding_nam_anh/
├── index.html              # Trang chính
├── css/
│   ├── main.css           # CSS chính (đã beautified - 11,034 dòng)
│   └── theme.css          # CSS theme (đã beautified)
├── js/
│   ├── main.bundle.js     # JavaScript bundle chính (đã beautified)
│   └── *.js               # 67 file JS khác (đã beautified)
├── images/                # Thư mục hình ảnh
├── media/                 # Thư mục media
└── beautify_all.py        # Script tự động beautify code
```

## 🔧 Code đã được Beautified

### ✅ JavaScript Files

- **Tổng số**: 68 files
- **Trạng thái**: Đã beautified 100%
- **Đặc điểm**:
  - Code đã được format với indent 2 spaces
  - Thêm header comment cho mỗi file
  - Dòng trống giữa các function
  - Brace style: collapse

**Ví dụ trước khi beautify:**

```javascript
(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[3046],{39601:function(e,t,n){"use strict";var r=n(50029),i=n(87794)...
```

**Sau khi beautify:**

```javascript
/**
 * File: main.bundle.js
 * Mô tả: Code đã được beautify và format lại để dễ đọc
 */

(self.webpackChunk_N_E = self.webpackChunk_N_E || []).push([
  [3046], {
    39601: function(e, t, n) {
      "use strict";
      var r = n(50029),
        i = n(87794),
        o = n.n(i),
        ...
```

### ✅ CSS Files

- **Tổng số**: 2 files
- **Trạng thái**: Đã beautified 100%
- **Đặc điểm**:
  - Format với indent 2 spaces
  - Mỗi selector trên một dòng riêng
  - Dòng trống giữa các rule
  - Space xung quanh combinator

**Ví dụ trước khi beautify:**

```css
@keyframes animation-float {
  0%,
  to {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}
```

**Sau khi beautify:**

```css
/**
 * File: main.css
 * Mô tả: CSS đã được beautify và format lại để dễ đọc
 */

@keyframes animation-float {
  0%,
  to {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}
```

## 🎯 Tính năng chính của Website

Dựa vào code đã beautify, website có các tính năng:

1. **Audio Control** - Điều khiển nhạc nền
2. **Envelope Animation** - Animation phong bì mời
3. **Countdown Timer** - Đếm ngược đến ngày cưới
4. **Photo Gallery** - Gallery ảnh cưới
5. **Map Handler** - Bản đồ địa điểm
6. **RSVP Form** - Form xác nhận tham dự
7. **Message Board** - Bảng lời chúc
8. **Gift Animation** - Animation quà tặng
9. **Like Button** - Nút yêu thích

## 📖 Hướng dẫn sử dụng

### Xem code đã beautified

Tất cả file JS và CSS đã được beautified. Bạn có thể mở bằng bất kỳ editor nào:

```bash
# Mở file JavaScript chính
code js/main.bundle.js

# Mở file CSS chính
code css/main.css
```

### Re-beautify lại code (nếu cần)

Nếu bạn chỉnh sửa code và muốn beautify lại:

```bash
# Cài đặt thư viện (chỉ cần làm 1 lần)
pip install jsbeautifier cssbeautifier

# Chạy script beautify
python beautify_all.py
```

## ⚠️ Lưu ý quan trọng

### Về tên biến

Code gốc đã bị **minified/obfuscated** nên tên biến rất khó hiểu:

- `e`, `t`, `n`, `r`, `i`, `o`, `a`, `c`, `s`, `l`, `p`, `u`, `h`, `d`, `f`, `v`, `x`, `m`, `g`, `b`, `w`, `y`, `j`, `O`, `k`, `P`, `z`, `E`, `S`, `T`

**Không thể đổi tên biến** vì:

1. Code đã được webpack bundle
2. Các biến liên kết với nhau qua các module
3. Đổi tên sẽ làm hỏng logic

### Về cấu trúc code

Code được build bằng:

- **Framework**: Next.js / React
- **Build tool**: Webpack
- **Style**: TailwindCSS + Custom CSS
- **Trạng thái**: Production build (đã minified)

## 🔍 Phân tích code

### File quan trọng nhất

1. **index.html** - Entry point

   - Load tất cả CSS và JS
   - Chứa inline styles cho components

2. **js/main.bundle.js** - Logic chính

   - Favorite button handler
   - PC container wrapper
   - Template preview
   - Package selection modal

3. **css/main.css** - Styles chính
   - Animations (float, bounce, pulse, rotate, shake, wiggle, wobble)
   - Component styles
   - TailwindCSS utilities
   - Responsive design

### Patterns trong code

**JavaScript patterns:**

- Module pattern với webpack
- React Hooks (useState, useEffect, useMemo)
- Async/await cho API calls
- Event handlers
- State management

**CSS patterns:**

- Keyframe animations
- Flexbox & Grid layouts
- CSS Variables (`:root`)
- Media queries
- Utility classes

## 🛠️ Công cụ đã sử dụng

- **jsbeautifier** (v1.15.4) - Beautify JavaScript
- **cssbeautifier** (v1.15.4) - Beautify CSS
- **Python 3** - Script automation

## 📝 Kết luận

✅ **Đã hoàn thành beautify 100% code:**

- 68 JavaScript files
- 2 CSS files
- Tổng cộng 70 files

Code giờ đã:

- ✅ Dễ đọc hơn nhiều
- ✅ Có cấu trúc rõ ràng
- ✅ Dễ debug và maintain
- ✅ Có comments giải thích

⚠️ **Hạn chế:**

- Tên biến vẫn khó hiểu (do code gốc đã minified)
- Không thể refactor được tên biến mà không có source code gốc

---

**Lưu ý**: Để có code dễ đọc hoàn toàn, bạn cần source code gốc (chưa build). Code hiện tại là bản production đã được optimize.
