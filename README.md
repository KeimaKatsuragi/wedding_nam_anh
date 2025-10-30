# Wedding Invitation – Maintenance Guide

This repository contains a static export of a template-based wedding invitation. The assets here are build artifacts (minified HTML/CSS/JS) from a framework bundle. As such, variable, function, and class names inside the JS files are minified and should not be manually renamed (it will break the runtime).

## What was improved

- Human-friendly CSS filenames: `css/main.css`, `css/theme.css`
- Human-friendly main JS filename: `js/main.bundle.js`
- Fixed a critical malformed inline style for the wax-seal image
- Repaired the two top text blocks’ inline styles

## Limitations on renaming variables

The JavaScript files under `js/` (many hashed files) are minified bundles. Renaming variables inside them is unsafe without the original source and a proper build pipeline. If you need meaningful variable names, consider recovering or recreating the project source and rebuilding.

## Auto-fix inline styles (font-family)

The exported HTML has many broken inline style attributes where `font-family` got split. Use the helper script to repair most cases automatically:

```bash
node tools/fix_inline_styles.js
```

Optionally specify a path:

```bash
node tools/fix_inline_styles.js /absolute/path/to/index.html
```

The script handles common broken patterns and normalizes them. Review diffs after running.

## Suggested next steps

- Source recovery: Rebuild from original project to get readable source code for safe variable/function renaming.
- Progressive cleanup: Move repeated inline styles into CSS classes in `css/main.css` to reduce inline complexity.
- Encoding fixes: Replace misencoded Vietnamese characters (�) with correct UTF-8 text.

## File map (high-level)

- `index.html` – Main page; contains inline styled-jsx blocks and many inline styles
- `css/main.css` – General styles bundle (from original 8DpcXvvCsyrH.css)
- `css/theme.css` – Theme/UI and variables (from original otxhCtjiN1JO.css)
- `js/main.bundle.js` – Main page bundle (replaces `[templateSlug]-*.js` in `index.html` for readability)
- `tools/fix_inline_styles.js` – Script to fix broken inline styles in `index.html`

## Caution

- Do not rename styled-jsx scoped class names (e.g., `jsx-<id>`) or CSS module hashes; they are tied to the inline CSS blocks.
- Avoid renaming JS variables inside minified files. Do so only with source + build step.
