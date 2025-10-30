#!/usr/bin/env node
/**
 * Fix broken inline style attributes in index.html caused by split font-family tokens.
 *
 * Patterns handled:
 * 1) style="...;font-family:"<FONT>";<REST>""  ->  style="...;font-family:'<FONT>'; <REST>"
 * 2) style="...;font-family:'<FONT>\; <REST>"   ->  style="...;font-family:'<FONT>'; <REST>"
 *
 * Usage:
 *   node tools/fix_inline_styles.js [path/to/index.html]
 */
const fs = require('fs');
const path = require('path');

const filePath = process.argv[2] || path.join(__dirname, '..', 'index.html');

let html = fs.readFileSync(filePath, 'utf8');

// Case 1: font-family:"FONT";REST"" -> font-family:'FONT';REST"
// This captures:
// group 1: before style content up to font-family:
// group 2: font name
// group 3: rest of style props up to the next closing quote before the accidental ""
const reSplit = /(style=\"[^\"]*?font-family:\")(\s*[-_a-zA-Z0-9\s]+)\"\s*;\s*([^\"]*?)\"\"/g;
html = html.replace(reSplit, (m, before, font, rest) => {
  const cleanFont = font.trim().replace(/\s+/g, ' ');
  return `${before}'${cleanFont}';${rest}\"`;
});

// Case 2: font-family:'FONT\;REST'  ->  font-family:'FONT';REST
// This happens when a semicolon was escaped into the font-family value.
const reEscaped = /(style=\"[^\"]*?font-family:\')([^'\\]+)\\;\s*([^\"]*?)\"/g;
html = html.replace(reEscaped, (m, before, font, rest) => {
  const cleanFont = font.trim();
  return `${before}${cleanFont}'; ${rest}\"`;
});

// Also normalize any font-family:" (dangling) into a safe default to prevent CSS parse errors
html = html.replace(/font-family:\"(?=\")/g, "font-family: Arial, sans-serif;");

// Case 3: style is prematurely closed around font-family value:
// style="...font-family:" FONT";rest"=""  ->  style="...font-family:'FONT';rest"
const reBrokenAttr = /(style=\"[^\"]*?font-family:\")[\s\n\r]*([A-Za-z0-9 _-]+)\"\s*;([^\"]*?)\"\s*=\s*\"\"/g;
html = html.replace(reBrokenAttr, (m, before, font, rest) => {
  const cleanFont = font.trim().replace(/\s+/g, ' ');
  const cleanRest = rest.trim();
  return `${before}'${cleanFont}';${cleanRest}\"`;
});

// Case 4: simpler dangling pattern font-family:" NAME"; -> font-family:'NAME';
const reSimpleDangling = /(font-family:\")[\s\n\r]*([A-Za-z0-9 _-]+)\"\s*;/g;
html = html.replace(reSimpleDangling, (m, before, font) => {
  const cleanFont = font.trim().replace(/\s+/g, ' ');
  return `${before}'${cleanFont}';`;
});

// Normalize whitespace inside style attributes (conservative collapse)
html = html.replace(/style=\"([\s\S]*?)\"/g, (m, content) => {
  const collapsed = content.replace(/\s{2,}/g, ' ').trim();
  return `style=\"${collapsed}\"`;
});

fs.writeFileSync(filePath, html, 'utf8');
console.log(`Rewrote inline styles in ${filePath}`);
