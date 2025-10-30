#!/usr/bin/env node
/**
 * Lightly format the <head> section of index.html for readability:
 * - Puts each common tag (<meta>, <link>, <title>, <script>, <style>, <noscript>, <base>) on its own line
 * - Adds two-space indentation inside <head>
 * - Keeps inline script/style content as-is (no reflow)
 *
 * Usage:
 *   node tools/format_head.js [path/to/index.html]
 */
const fs = require('fs');
const path = require('path');

const filePath = process.argv[2] || path.join(__dirname, '..', 'index.html');
let html = fs.readFileSync(filePath, 'utf8');

const openHeadIdx = html.indexOf('<head>');
const closeHeadIdx = html.indexOf('</head>');
if (openHeadIdx === -1 || closeHeadIdx === -1 || closeHeadIdx < openHeadIdx) {
  console.error('Could not locate <head>...</head> in', filePath);
  process.exit(1);
}

const before = html.slice(0, openHeadIdx);
const headOpen = '<head>';
const headContent = html.slice(openHeadIdx + headOpen.length, closeHeadIdx);
const after = html.slice(closeHeadIdx);

// Normalize: ensure no leading/trailing spaces
let content = headContent.trim();

// Insert newlines before tags we want on separate lines
const tags = ['meta', 'link', 'title', 'script', 'style', 'noscript', 'base'];
// Add newline before each target tag if not already at line start
for (const tag of tags) {
  const re = new RegExp(`<${tag}\\b`, 'gi');
  content = content.replace(re, (m) => `\n${m}`);
}
// Also newline after closing </script> or </style> blocks
content = content.replace(/<\/script>/gi, '</script>\n');
content = content.replace(/<\/style>/gi, '</style>\n');

// Split into lines, indent each non-empty line by two spaces
const lines = content.split('\n').map((l) => l.trim()).filter((l, i, arr) => !(l === '' && (i === 0 || i === arr.length - 1)));
const indented = lines.map((l) => (l.length ? `  ${l}` : l)).join('\n');

const formatted = `${before}${headOpen}\n${indented}\n</head>${after}`;

fs.writeFileSync(filePath, formatted, 'utf8');
console.log(`Formatted <head> in ${filePath}`);
