# 📑 Danh Mục Code Đã Beautified

## 🎯 Mục đích

File này giúp bạn dễ dàng tìm kiếm và hiểu chức năng của từng file trong project.

---

## 📄 HTML Files

### index.html

**Chức năng**: Trang chính của website thiệp cưới

**Nội dung chính**:

- Meta tags (SEO, Open Graph, Twitter Card)
- Google Analytics tracking
- Load CSS files (main.css, theme.css)
- Load 68 JavaScript modules
- Inline styles cho components:
  - `#audio-control-wrapper` - Nút điều khiển nhạc
  - `.envelope-shadow` - Bóng phong bì
  - `.envelope-container` - Container phong bì
  - `.animated-envelope-component` - Animation phong bì
  - `.text-box-component` - Component text box
  - `.photo-component` - Component ảnh
  - `.material-component` - Component material
  - `.countdown` - Đếm ngược
  - `.simple-map-container` - Container bản đồ
  - `.rsvp-form-container` - Container form RSVP
  - `.toolbar-toggle-button` - Nút toggle toolbar
  - `.watermark` - Watermark CineLove

**Độ dài**: ~250 dòng

---

## 🎨 CSS Files (2 files - Đã beautified 100%)

### 1. css/main.css

**Chức năng**: CSS chính cho toàn bộ website

**Kích thước**: 13,291 dòng (sau khi beautify)

**Nội dung chính**:

#### Animations (Dòng 1-100)

```css
@keyframes animation-float     // Animation lơ lửng
@keyframes animation-bounce    // Animation nhảy
@keyframes animation-pulse     // Animation nhấp nháy
@keyframes animation-rotate    // Animation xoay
@keyframes animation-shake     // Animation rung
@keyframes animation-wiggle    // Animation lắc
@keyframes animation-wobble    // Animation đung đưa;
```

#### Component Classes (Dòng 100-500)

```css
.component-hovered          // Style khi hover component
.component-selected         // Style khi select component
.transition                 // Transition mặc định
#root-page-container        // Container trang gốc
.ant-message                // Message notification;
```

#### Calendar Component (Dòng 500-800)

```css
.calendar .template-one     // Template lịch 1
.calendar .template-two     // Template lịch 2
.calendar .template-three   // Template lịch 3
.body-week                  // Tuần trong lịch
.body-year                  // Năm trong lịch
img.heart-date              // Icon trái tim ngày;
```

#### Map Component (Dòng 800-1200)

```css
.advanced-marker-wrapper    // Wrapper cho marker
.real-estate-marker         // Marker địa điểm
.custom-pin                 // Pin custom
.photo-gallery              // Gallery ảnh
.listing-content            // Nội dung listing;
```

#### Sidebar Menu (Dòng 1200-1600)

```css
.menu-sidebar               // Sidebar menu
.miniicons                  // Icons nhỏ
.sidebar-nav                // Navigation sidebar
.sidebar-dropdown           // Dropdown menu
.brand-logo                 // Logo;
```

#### Tailwind CSS Reset & Base (Dòng 1600-3000)

```css
*::before, *::after         // Box-sizing reset
html, body                  // HTML reset
form elements               // Input, select, textarea styles
```

#### CSS Variables (Dòng 3000-3100)

```css
:root {
  --color-primary           // Màu chính
  --color-secondary         // Màu phụ
  --color-info             // Màu info
  --color-success          // Màu thành công
  --color-warning          // Màu cảnh báo
  --color-error            // Màu lỗi
  --color-pink-cinelove    // Màu hồng brand
}
```

#### Utility Classes (Dòng 3100-13291)

```css
.sr-only                    // Screen reader only
.pointer-events-none        // Disable pointer events
.visible, .invisible        // Visibility
.fixed, .absolute, .relative // Position
.z-{number}                 // Z-index utilities
.top-*, .bottom-*, .left-*, .right-* // Position utilities
... hàng nghìn utility classes khác
```

### 2. css/theme.css

**Chức năng**: Theme styles bổ sung

**Kích thước**: ~50-100 dòng (sau khi beautify)

**Nội dung**: Custom theme colors và overrides

---

## ⚙️ JavaScript Files (68 files - Đã beautified 100%)

### Core Files

#### js/main.bundle.js

**Chức năng**: JavaScript bundle chính

**Kích thước**: 545 dòng (sau khi beautify)

**Modules chính**:

1. **Module 39601** - Favorite Button Component

   ```javascript
   // Xử lý nút yêu thích
   // Functions: toggleFavorite, initializeFavorites
   // State: isAuthenticated, isFavorite
   ```

2. **Module 76292** - PC Container Wrapper

   ```javascript
   // Wrapper cho PC view
   // Style: background, border, shadow
   ```

3. **Module 57066** - Template Preview Component
   ```javascript
   // Preview template thiệp cưới
   // Features: resize, zoom, animation
   // State management với React hooks
   ```

**Dependencies**:

- React (67294)
- Next.js Router (11163)
- Session management (33299)

### Module Files (67 files khác)

Tất cả đều đã được beautified. Tên file dạng hash (do webpack):

#### Animation Related

- `1kiISAeTvc3a.js` - Animation utilities
- `2Y35zuM5iwri.js` - Animation effects
- `3tGnvso2EpgS.js` - Transition handlers

#### Component Related

- `4qQLwiD523Ch.js` - Component registry
- `5INlo313Ur5s.js` - Component lifecycle
- `6ctGqlsvuRJ3.js` - Component props

#### UI Elements

- `8eTk3xZPZFRb.js` - Button components
- `8jaxHZ6DGogP.js` - Form elements
- `8UpAZ4T6Y1TM.js` - Input handlers

#### State Management

- `aLm4dSTQ1ZnK.js` - State store
- `AMemM9NOTkFJ.js` - State actions
- `BkA4hpJBD0KM.js` - State reducers

#### API & Data

- `bp8Q2rmfXxKH.js` - API calls
- `bPekwsPArrL0.js` - Data fetching
- `cZme8bnnLBkC.js` - Data parsing

#### Utilities

- `DjVklmWpv1W6.js` - String utilities
- `eEi0DFA5zidD.js` - Date utilities
- `ErEyk5D8GlEA.js` - Math utilities

_(Còn 50+ files khác với tên hash tương tự)_

---

## 🔍 Cách Đọc Code

### 1. Bắt đầu từ đâu?

**Recommend order**:

1. `index.html` - Hiểu cấu trúc trang
2. `css/main.css` - Hiểu styles và animations
3. `js/main.bundle.js` - Hiểu logic chính
4. Các module JS khác theo nhu cầu

### 2. Tìm kiếm chức năng cụ thể

**Audio control**:

- HTML: Inline style `#audio-control-wrapper`
- CSS: `.audio-toggle`, `.music-icon`
- JS: Tìm trong các module có `audio`, `music`

**Countdown timer**:

- HTML: Inline style `.countdown`
- CSS: `.countdown`, `.vertical`, `>div`
- JS: Tìm module có `timer`, `countdown`

**Envelope animation**:

- HTML: Inline style `.envelope-container`
- CSS: `.envelope-shadow`, `.flap`, `.letter`
- JS: Tìm module có `envelope`, `animation`

**Photo gallery**:

- HTML: Inline style `.photo-component`
- CSS: `.photo-gallery`, `.photo-bg-wrap`
- JS: Tìm module có `gallery`, `photo`

**Map**:

- HTML: Inline style `.simple-map-container`
- CSS: `.advanced-marker-wrapper`, `.real-estate-marker`
- JS: Tìm module có `map`, `marker`

**RSVP Form**:

- HTML: Inline style `.rsvp-form-container`
- CSS: Form styles trong main.css
- JS: Tìm module có `rsvp`, `form`

### 3. Hiểu cấu trúc Webpack Module

Mỗi file JS có cấu trúc:

```javascript
/**
 * File: [tên file].js
 * Mô tả: Code đã được beautify
 */

// Webpack chunk definition
(self.webpackChunk_N_E = self.webpackChunk_N_E || []).push([
  [chunkId],
  {
    moduleId: function (e, t, n) {
      // Module dependencies
      var r = n(dep1),
        i = n(dep2);

      // Module exports
      t.Z = function (e) {
        // Module logic
      };
    },
  },
]);
```

**Giải thích**:

- `e` = exports object
- `t` = module object
- `n` = require function
- `r, i, o, a, c, s, l, p, u, h, d, f...` = imported dependencies

### 4. Debug Tips

**Tìm text trong code**:

```bash
# Tìm trong JS
findstr /s /i "countdown" js\*.js

# Tìm trong CSS
findstr /s /i "animation" css\*.css
```

**Tìm function/variable**:

```bash
# Tìm function definition
findstr /s "function.*toggleFavorite" js\*.js

# Tìm class definition
findstr /s "\.countdown" css\*.css
```

---

## 📊 Thống kê Code

### JavaScript

- **Tổng files**: 68 files
- **Tổng dòng code**: ~15,000+ dòng (ước tính)
- **Minified variables**: e, t, n, r, i, o, a, c, s, l, p, u, h, d, f, v, x, m, g, b, w, y, j, O, k, P, z, E, S, T, Z, N, C, R, L, D, I, B, M, V, F, W, X, H, q, G

### CSS

- **Tổng files**: 2 files
- **Tổng dòng code**: ~13,500 dòng
- **Animations**: 7 keyframes
- **Components**: 50+ component classes
- **Utilities**: 1000+ utility classes

### HTML

- **Tổng files**: 1 file
- **Tổng dòng code**: ~250 dòng
- **Inline styles**: 15+ component styles
- **Script tags**: 68 JS files loaded

---

## 🎓 Kiến thức cần thiết

Để hiểu và chỉnh sửa code này, bạn cần biết:

### Frontend

- ✅ HTML5, CSS3
- ✅ JavaScript ES6+
- ✅ React (hooks, components, state)
- ✅ Next.js (routing, SSR)
- ✅ TailwindCSS (utility classes)

### Build Tools

- ✅ Webpack (module bundling)
- ✅ NPM/Yarn (package management)
- ✅ Babel (transpiling)

### Concepts

- ✅ Component-based architecture
- ✅ State management
- ✅ Event handling
- ✅ Async/await, Promises
- ✅ CSS animations & transitions
- ✅ Responsive design

---

## ⚡ Quick Reference

### Màu sắc chính

```css
--color-primary: #3a9bff           /* Xanh dương */
--color-secondary: #14e9e2         /* Xanh ngọc */
--color-pink-cinelove: #ff8fa3     /* Hồng brand */
--color-error: #ff6692             /* Đỏ lỗi */
--color-success: #36c76c           /* Xanh success */
```

### Breakpoints

```css
@media (min-width: 640px) /* sm */ @media (min-width: 768px) /* md */ @media (min-width: 1024px) /* lg */ @media (min-width: 1280px) /* xl */ @media (min-width: 1536px); /* 2xl */
```

### Z-index layers

```css
z-0     /* Base layer */
z-10    /* Content layer */
z-20    /* Dropdown layer */
z-40    /* Modal layer */
z-50    /* Toast layer */
z-9999  /* Tooltip layer */
```

---

**Ghi chú**: File này sẽ được cập nhật khi có thêm thông tin về các module.
