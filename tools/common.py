import json, os, re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = r'D:\08_CodeKuliah\project-uas-kwu'
OUT = ROOT + r'\output'
IMG = OUT + r'\img'
V = json.load(open(os.environ['KIROCREW_SCRATCH'] + r'\vals.json', encoding='utf8'))


def g(sheet, cell):
    return V[sheet.upper()][cell]


def rp(x, neg_paren=False):
    x = round(float(x))
    s = f'{abs(x):,}'.replace(',', '.')
    if x < 0:
        return f'({s})' if neg_paren else f'-Rp{s}'
    return f'Rp{s}'


def num(x):
    return f'{round(float(x)):,}'.replace(',', '.')


def pct(x, d=0):
    return f'{x*100:.{d}f}%'.replace('.', ',')


COLS = 'BCDEFGHIJKLM'
months = list(range(1, 13))
cust_end = [g('Proyeksi_Bulanan', f'{c}9') for c in COLS]
rev_m = [g('Proyeksi_Bulanan', f'{c}12') for c in COLS]
cash_end = [g('Arus_Kas', f'{c}17') for c in COLS]
net_m = [g('Proyeksi_Bulanan', f'{c}26') for c in COLS]

# angka kunci
PRICE = 24000
VAR = g('Unit_Economics', 'B4')
CM = g('Unit_Economics', 'B5')
BEP_D = g('Unit_Economics', 'B7')
BEP = int(g('Unit_Economics', 'B8'))
BEP_RP = g('Unit_Economics', 'B9')
LTV = g('Unit_Economics', 'B10')
LTVCAC = g('Unit_Economics', 'B11')
PAYBACK = g('Unit_Economics', 'B12')
M_BEP = g('Unit_Economics', 'B13')
M_PROFIT = g('Unit_Economics', 'B14')
FIX_H = 171000
FIX_P = 663000
import math
BEP_P = math.ceil(FIX_P / CM)
BEP_P_D = FIX_P / CM
# alt 2 (per pemakaian) dihitung di luar model xlsx
A2_REV = 22000
A2_VAR = 6900 + 0.007 * A2_REV
A2_CM = A2_REV - A2_VAR
A2_H = math.ceil(FIX_H / A2_CM)
A2_P = math.ceil(FIX_P / A2_CM)
SENS = {}
for p in (19000, 24000, 29000):
    cm = p - 6900 - 0.007 * p
    SENS[p] = (cm, math.ceil(FIX_H / cm), math.ceil(FIX_P / cm), math.ceil(994000 / cm))

NAVY = '#1F3A5F'
GREEN = '#2E8B57'
ORANGE = '#E8892B'
GREY = '#6B7280'


def chart_growth():
    fig, ax = plt.subplots(figsize=(7, 3.4), dpi=170)
    ax.bar(months, cust_end, color=GREEN, label='Warung berbayar (akhir bulan)')
    ax.axhline(BEP, color=ORANGE, ls='--', lw=1.5)
    ax.text(12.4, BEP + 0.4, f'BEP {BEP} warung', color=ORANGE, ha='right', fontsize=8)
    ax.set_xlabel('Bulan ke-'); ax.set_ylabel('Warung'); ax.set_xticks(months)
    ax.set_title('Pertumbuhan warung berbayar, tahun 1 (skenario moderat)', fontsize=10)
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    fig.tight_layout(); p = IMG + r'\c_growth.png'; fig.savefig(p); plt.close(fig); return p


def chart_cash():
    fig, ax = plt.subplots(figsize=(7, 3.4), dpi=170)
    ax.plot(months, [c / 1e6 for c in cash_end], color=NAVY, marker='o')
    ax.plot(months, [n / 1e3 / 1e3 for n in net_m], color=ORANGE, marker='s', ls='--', label='Laba bersih bulanan')
    ax.axhline(0, color=GREY, lw=.8)
    ax.set_xlabel('Bulan ke-'); ax.set_ylabel('Juta Rupiah'); ax.set_xticks(months)
    ax.legend(['Saldo kas akhir', 'Laba bersih bulanan'], fontsize=8, frameon=False)
    ax.set_title('Saldo kas dan laba bersih bulanan, tahun 1', fontsize=10)
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    fig.tight_layout(); p = IMG + r'\c_cash.png'; fig.savefig(p); plt.close(fig); return p


def chart_bep():
    fig, ax = plt.subplots(figsize=(7, 3.4), dpi=170)
    labels = ['Alt 1 hemat', 'Alt 1 penuh', 'Alt 2 hemat', 'Alt 2 penuh']
    vals = [BEP, BEP_P, A2_H, A2_P]
    ax.bar(labels, vals, color=[GREEN, NAVY, GREEN, NAVY])
    for y, c, t in ((25, ORANGE, 'Segmen awal 25'), (58, 'crimson', 'Batas atas 58')):
        ax.axhline(y, color=c, ls='--', lw=1.3); ax.text(3.45, y + 1, t, color=c, ha='right', fontsize=8)
    for i, v in enumerate(vals): ax.text(i, v + 1, str(v), ha='center', fontsize=9)
    ax.set_ylabel('Warung untuk impas')
    ax.set_title('Titik impas dibanding ukuran segmen', fontsize=10)
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    fig.tight_layout(); p = IMG + r'\c_bep.png'; fig.savefig(p); plt.close(fig); return p


def chart_scen():
    names = ['Pesimis', 'Moderat', 'Optimis']
    lab = [g('Sensitivitas', f'F{r}') for r in (4, 5, 6)]
    fig, ax = plt.subplots(figsize=(7, 3.2), dpi=170)
    ax.bar(names, [x / 1e3 for x in lab], color=[ORANGE, NAVY, GREEN])
    for i, v in enumerate(lab): ax.text(i, v / 1e3 + (20 if v >= 0 else -70), rp(v), ha='center', fontsize=8)
    ax.axhline(0, color=GREY, lw=.8); ax.set_ylabel('Ribu Rupiah')
    ax.set_title('Laba bersih tahun 1 per skenario', fontsize=10)
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    fig.tight_layout(); p = IMG + r'\c_scen.png'; fig.savefig(p); plt.close(fig); return p


def chart_cost():
    fig, ax = plt.subplots(figsize=(7, 3.2), dpi=170)
    items = ['Panggilan AI', 'Penagihan QRIS', 'Margin (CM)']
    vals = [6900, 168, CM]
    ax.barh(['Harga Rp24.000'], [6900], color=ORANGE, label='Panggilan AI')
    ax.barh(['Harga Rp24.000'], [168], left=[6900], color='crimson', label='Penagihan QRIS')
    ax.barh(['Harga Rp24.000'], [CM], left=[7068], color=GREEN, label='Margin kontribusi')
    ax.legend(fontsize=8, frameon=False, ncol=3, loc='upper center', bbox_to_anchor=(.5, -.2))
    ax.set_xlabel('Rupiah per warung per bulan'); ax.set_title('Uraian harga per warung', fontsize=10)
    ax.text(3450, 0, '6.900', ha='center', va='center', color='white', fontsize=8)
    ax.text(7068 + CM / 2, 0, num(CM), ha='center', va='center', color='white', fontsize=9)
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    fig.tight_layout(); p = IMG + r'\c_cost.png'; fig.savefig(p); plt.close(fig); return p


def make_charts():
    return dict(growth=chart_growth(), cash=chart_cash(), bep=chart_bep(), scen=chart_scen(), cost=chart_cost())


if __name__ == '__main__':
    print(make_charts())
    print(BEP, BEP_P, A2_H, A2_P, SENS)
