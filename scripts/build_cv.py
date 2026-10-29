#!/usr/bin/env python3
"""Build CV.md, CV_EN.md and their PDFs from cv/cv_ko.json and cv/cv_en.json.

Requires PyMuPDF (fitz >= 1.23) and NanumGothic Regular/Bold TTFs in cv/fonts/,
which are not tracked in git. Edit the JSON files, then run this script.
"""

import html
import json
import re
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
FONTS = ROOT / 'cv' / 'fonts'
OUTPUTS = {
    'ko': ('CV.md', 'CV_EN.md', 'cv/KiwonEom_CV_KR.pdf', '**한국어** | [English](CV_EN.md)',
           'PDF로 받기', '포트폴리오 홈', 'README_KO.md'),
    'en': ('CV_EN.md', 'CV.md', 'cv/KiwonEom_CV_EN.pdf', '[한국어](CV.md) | **English**',
           'Download PDF', 'Portfolio home', 'README.md'),
}

CSS = """
@font-face { font-family: nanum; src: url(NanumGothic-Regular.ttf); }
@font-face { font-family: nanum; font-weight: bold; src: url(NanumGothic-Bold.ttf); }
body { font-family: nanum; font-size: 9.0pt; line-height: 1.28; color: #1b1b1b; }
h1 { font-size: 19pt; margin: 0 0 1pt 0; }
h1 span { font-size: 11pt; font-weight: normal; color: #52514e; }
p.headline { color: #52514e; margin: 0 0 2pt 0; }
p.contact { font-size: 8.6pt; margin: 0 0 4pt 0; }
h2 { font-size: 10.6pt; color: #1c5cab; margin: 6pt 0 2.5pt 0; padding-bottom: 1pt;
     border-bottom: 0.6pt solid #c3c2b7; }
p { margin: 0; }
p.what { margin-top: 2pt; }
span.meta { color: #52514e; font-size: 8.6pt; font-weight: normal; }
ul { margin: 1pt 0 0 0; padding-left: 12pt; }
li { margin: 0 0 1pt 0; }
p.pub { margin: 2pt 0 0 0; }
p.note { color: #52514e; font-size: 8.6pt; margin-bottom: 1pt; }
a { color: #1c5cab; text-decoration: none; }
"""


def md_inline(text):
    """Markdown keeps **bold**; nothing else to convert."""
    return text


def html_inline(text):
    text = html.escape(text, quote=False)
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)


def plain(text):
    return text.replace('**', '')


def to_markdown(cv, lang):
    md_name, other, pdf, toggle, pdf_label, home_label, home = OUTPUTS[lang]
    contacts = ' &nbsp;/&nbsp; '.join(f'[{label}]({url})' for label, _, url in cv['contacts'])
    out = ['<div align="center">', '', f"# {cv['name']} &nbsp;<sub>{cv['name_alt']}</sub>", '',
           cv['headline'], '', contacts, '',
           f'{toggle} &nbsp;·&nbsp; [{pdf_label}]({pdf}) &nbsp;·&nbsp; [{home_label}]({home})',
           '', '</div>', '']
    for sec in cv['sections']:
        out += [f"## {sec['title']}", '']
        kind = sec['type']
        if kind == 'text':
            out += [md_inline(sec['text']), '']
        elif kind == 'kv':
            out += [f'- **{k}**: {v}' for k, v in sec['items']] + ['']
        elif kind == 'pubs':
            out += [sec['note'], '']
            for p in sec['items']:
                link = ' [{}]({})'.format(*p['link']) if p.get('link') else ''
                out += [f"- {md_inline(p['authors'])}. **{p['title']}.** *{p['venue']}*.{link}"]
            out += ['']
        elif kind == 'entries':
            for e in sec['items']:
                meta = ' · '.join(x for x in (e.get('sub'), e['when']) if x)
                out += [f"**{e['what']}** &nbsp;·&nbsp; {meta}"]
                if e.get('bullets'):
                    out += [''] + [f'- {md_inline(b)}' for b in e['bullets']]
                out += ['']
    return '\n'.join(out).rstrip() + '\n'


def to_html(cv):
    contacts = '  ·  '.join(
        f'<a href="{html.escape(url)}">{html.escape(shown)}</a>' for _, shown, url in cv['contacts'])
    parts = [f"<h1>{html.escape(cv['name'])} <span>{html.escape(cv['name_alt'])}</span></h1>",
             f"<p class='headline'>{html.escape(cv['headline'])}</p>",
             f"<p class='contact'>{contacts}</p>"]
    for sec in cv['sections']:
        parts.append(f"<h2>{html.escape(sec['title'])}</h2>")
        kind = sec['type']
        if kind == 'text':
            parts.append(f"<p>{html_inline(sec['text'])}</p>")
        elif kind == 'kv':
            parts += [f'<p><b>{html.escape(k)}</b>  {html.escape(v)}</p>' for k, v in sec['items']]
        elif kind == 'pubs':
            parts.append(f"<p class='note'>{html.escape(sec['note'])}</p>")
            for p in sec['items']:
                link = ''
                if p.get('link'):
                    label, url = p['link']
                    link = f" <a href='{html.escape(url)}'>{html.escape(label)}</a>"
                parts.append(f"<p class='pub'>{html_inline(p['authors'])}. <b>{html.escape(p['title'])}.</b> "
                             f"<i>{html.escape(p['venue'])}</i>.{link}</p>")
        elif kind == 'entries':
            for e in sec['items']:
                meta = ' · '.join(html.escape(x) for x in (e.get('sub'), e['when']) if x)
                parts.append(f"<p class='what'><b>{html.escape(e['what'])}</b>"
                             f"<span class='meta'>  ·  {meta}</span></p>")
                if e.get('bullets'):
                    parts.append('<ul>' + ''.join(f'<li>{html_inline(b)}</li>' for b in e['bullets']) + '</ul>')
    return '<html><body>' + '\n'.join(parts) + '</body></html>'


def to_pdf(cv, path):
    archive = fitz.Archive(str(FONTS))
    story = fitz.Story(html=to_html(cv), user_css=CSS, archive=archive)
    page = fitz.paper_rect('a4')
    body = page + (46, 30, -46, -22)

    def rectfn(rect_num, filled):
        return page, body, None

    doc = story.write_with_links(rectfn)
    doc.set_metadata({'title': f"{plain(cv['name'])} CV", 'author': cv['name_alt'] if cv['lang'] == 'ko'
                      else cv['name']})
    doc.subset_fonts()
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    doc.save(out, garbage=4, deflate=True, no_new_id=True)
    return doc.page_count


def main():
    for name in ('Regular', 'Bold'):
        if not (FONTS / f'NanumGothic-{name}.ttf').exists():
            raise SystemExit(f'Missing cv/fonts/NanumGothic-{name}.ttf (not tracked in git).')
    for lang in ('ko', 'en'):
        cv = json.loads((ROOT / 'cv' / f'cv_{lang}.json').read_text(encoding='utf-8'))
        md_name, _, pdf, *_ = OUTPUTS[lang]
        (ROOT / md_name).write_text(to_markdown(cv, lang), encoding='utf-8')
        pages = to_pdf(cv, pdf)
        print(f'{md_name}, {pdf} ({pages} page{"s" if pages > 1 else ""})')


if __name__ == '__main__':
    main()
