from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import re

TEAM = [('Alung Destantio Cahya Utama Putra', '434241001'), ('Daffa Eka Sujianto', '434241004'),
        ('Nabil Hakim Alfikri', '434241055'), ('Muhammad Javier Rakha Abhista', '434241021'),
        ('Muhammad Reyhan Ammar', '434241061'), ('Alfiyan Rasyid El-Fahmi', '434241047')]


class Doc:
    def __init__(self):
        d = self.d = Document()
        s = d.sections[0]
        s.page_width, s.page_height = Cm(21), Cm(29.7)
        s.top_margin = s.bottom_margin = s.left_margin = s.right_margin = Cm(3)
        st = d.styles['Normal']
        st.font.name = 'Times New Roman'; st.font.size = Pt(12)
        st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
        pf = st.paragraph_format
        pf.line_spacing = 1.5; pf.space_after = Pt(0); pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        for n, sz in (('Heading 1', 14), ('Heading 2', 12), ('Heading 3', 12)):
            h = d.styles[n]
            h.font.name = 'Times New Roman'; h.font.size = Pt(sz); h.font.bold = True
            h.font.color.rgb = RGBColor(0, 0, 0)
            h.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
            h.element.rPr.rFonts.set(qn('w:ascii'), 'Times New Roman')
            h.element.rPr.rFonts.set(qn('w:hAnsi'), 'Times New Roman')
            h.paragraph_format.space_before = Pt(12); h.paragraph_format.space_after = Pt(6)
            h.paragraph_format.keep_with_next = True
        d.styles['Heading 1'].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        d.styles['Heading 2'].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        d.styles['Heading 3'].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        self.fig = 0; self.tab = 0

    # ---- teks
    def _runs(self, p, text, size=None, bold=None):
        for part in re.split(r'(\*\*.+?\*\*)', text):
            if not part: continue
            b = part.startswith('**') and part.endswith('**')
            r = p.add_run(part[2:-2] if b else part)
            r.bold = True if (b or bold) else None
            if size: r.font.size = Pt(size)

    def p(self, text, indent=True, align=None, size=None, bold=None, after=6):
        p = self.d.add_paragraph()
        if indent: p.paragraph_format.first_line_indent = Cm(1.27)
        if align == 'c': p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(after)
        self._runs(p, text, size, bold)
        return p

    def h1(self, t, newpage=True):
        if newpage: self.d.add_page_break()
        return self.d.add_heading(t.upper(), 1)

    def h2(self, t): return self.d.add_heading(t, 2)
    def h3(self, t): return self.d.add_heading(t, 3)

    def bullets(self, items, numbered=False):
        for it in items:
            p = self.d.add_paragraph(style='List Number' if numbered else 'List Bullet')
            p.paragraph_format.space_after = Pt(2)
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            self._runs(p, it)
        self.d.add_paragraph().paragraph_format.space_after = Pt(0)

    def note(self, text):
        t = self.d.add_table(rows=1, cols=1); t.style = 'Table Grid'
        c = t.rows[0].cells[0]; self._shade(c, 'FFF4D6')
        c.paragraphs[0].paragraph_format.line_spacing = 1.15
        c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
        self._runs(c.paragraphs[0], text, 11)
        self.d.add_paragraph().paragraph_format.space_after = Pt(0)

    # ---- tabel dan gambar
    def _shade(self, cell, color):
        tcPr = cell._tc.get_or_add_tcPr(); sh = OxmlElement('w:shd')
        sh.set(qn('w:val'), 'clear'); sh.set(qn('w:color'), 'auto'); sh.set(qn('w:fill'), color); tcPr.append(sh)

    def caption(self, text, kind):
        p = self.d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.15; p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = (kind == 'Tabel')
        r = p.add_run(text); r.italic = True; r.font.size = Pt(11)

    def table(self, caption, header, rows, widths=None, size=9.5, right_cols=(), bold_last=False):
        self.tab += 1
        self.caption(f'Tabel {self.tab}. {caption}', 'Tabel')
        t = self.d.add_table(rows=1, cols=len(header)); t.style = 'Table Grid'
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        for i, h in enumerate(header):
            c = t.rows[0].cells[i]; c.text = ''; self._shade(c, 'D9D9D9')
            pp = c.paragraphs[0]; pp.alignment = WD_ALIGN_PARAGRAPH.CENTER
            pp.paragraph_format.line_spacing = 1.0
            r = pp.add_run(h); r.bold = True; r.font.size = Pt(size)
        tr = t.rows[0]._tr.get_or_add_trPr(); th = OxmlElement('w:tblHeader'); th.set(qn('w:val'), 'true'); tr.append(th)
        for ri, row in enumerate(rows):
            cells = t.add_row().cells
            for i, v in enumerate(row):
                cells[i].text = ''
                pp = cells[i].paragraphs[0]; pp.paragraph_format.line_spacing = 1.0
                pp.alignment = WD_ALIGN_PARAGRAPH.RIGHT if i in right_cols else WD_ALIGN_PARAGRAPH.LEFT
                self._runs(pp, str(v), size, bold=(bold_last and ri == len(rows) - 1))
        if widths:
            tot = sum(widths)
            for row in t.rows:
                for i, w in enumerate(widths):
                    row.cells[i].width = Cm(15 * w / tot)
        self.d.add_paragraph().paragraph_format.space_after = Pt(0)
        return t

    def image(self, path, caption, width=14):
        self.fig += 1
        p = self.d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.keep_with_next = True; p.paragraph_format.line_spacing = 1.0
        p.add_run().add_picture(path, width=Cm(width))
        self.caption(f'Gambar {self.fig}. {caption}', 'Gambar')

    # ---- cover, toc, nomor halaman
    def _field(self, p, instr):
        r = p.add_run()
        for t, v in (('begin', None), ('instr', instr), ('separate', None), ('end', None)):
            if t == 'instr':
                e = OxmlElement('w:instrText'); e.set(qn('xml:space'), 'preserve'); e.text = v
            else:
                e = OxmlElement('w:fldChar'); e.set(qn('w:fldCharType'), t)
            r._r.append(e)

    def cover(self, jenis, judul, logo):
        d = self.d
        for t, sz, b in ((jenis.upper(), 14, True), ('KEWIRAUSAHAAN BIDANG TI (FVK25612002)', 12, True)):
            p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_after = Pt(4); r = p.add_run(t); r.bold = b; r.font.size = Pt(sz)
        p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(logo, width=Cm(4.5))
        p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(judul); r.bold = True; r.font.size = Pt(16)
        for t in ('Dosen Pengampu:', 'Nambi Sembilu, S.Kom., M.Kom.', '', 'Disusun oleh Kelompok 1:'):
            p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.line_spacing = 1.15; r = p.add_run(t); r.bold = t.endswith(':')
        for n, nim in TEAM:
            p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.line_spacing = 1.15; p.add_run(f'{n} ({nim})')
        for t in ('', 'PROGRAM STUDI D4 TEKNIK INFORMATIKA', 'FAKULTAS VOKASI', 'UNIVERSITAS AIRLANGGA',
                  'SURABAYA', 'GASAL 2026/2027'):
            p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.line_spacing = 1.15; r = p.add_run(t); r.bold = True

    def toc(self):
        self.d.add_page_break()
        p = self.d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run('DAFTAR ISI'); r.bold = True; r.font.size = Pt(14)
        self._field(self.d.add_paragraph(), 'TOC \\o "1-3" \\h \\z \\u')
        p = self.d.add_paragraph(); p.paragraph_format.line_spacing = 1.0
        r = p.add_run('(Daftar isi terisi saat file dibuka di Word: pilih Yes pada pertanyaan pembaruan, atau klik kanan lalu Update Field.)')
        r.italic = True; r.font.size = Pt(9)

    def footer_numbers(self):
        s = self.d.sections[0]
        p = s.footer.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        self._field(p, 'PAGE')

    def save(self, path):
        self.footer_numbers(); self.d.save(path)
