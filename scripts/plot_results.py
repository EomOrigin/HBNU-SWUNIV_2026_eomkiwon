#!/usr/bin/env python3
"""Draw the AP-latency chart from results/efficiency.csv (manuscript Table 6).

Requires matplotlib. Writes assets/charts/ap_latency_aitodv2.{png,svg}.
"""

import csv
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, NullLocator

ROOT = Path(__file__).resolve().parents[1]

INK = '#0b0b0b'
INK_2 = '#52514e'
MUTED = '#898781'
GRID = '#e1e0d9'
AXIS = '#c3c2b7'
SURFACE = '#fcfcfb'
ACCENT = '#2a78d6'

CNN = {'DNTR', 'ORFENet', 'LTDNet'}
# Label offsets in points, chosen so that no two labels overlap.
OFFSETS = {
    'DNTR': (-8, 9, 'right'),
    'ORFENet': (9, -4, 'left'),
    'LTDNet': (9, -4, 'left'),
    'DINO': (9, -4, 'left'),
    'RT-DETR': (-9, 6, 'right'),
    'RT-DETRv2': (9, -4, 'left'),
    'DQ-DETR': (9, 4, 'left'),
    'Dome-DETR': (9, -4, 'left'),
    'SMWG-DETR': (9, -12, 'left'),
}


def main():
    with (ROOT / 'results/efficiency.csv').open(encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f))

    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11,
                         'axes.edgecolor': AXIS, 'axes.labelcolor': INK_2,
                         'xtick.color': MUTED, 'ytick.color': MUTED})
    fig, ax = plt.subplots(figsize=(8.6, 5.2), layout='constrained')
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)

    ours = next(r for r in rows if r['model'] == 'SPOT-DETR')
    base = next(r for r in rows if r['model'] == 'SMWG-DETR')
    for row in rows:
        if row is ours:
            continue
        x, y = float(row['latency_ms']), float(row['AP'])
        marker = 's' if row['model'] in CNN else 'o'
        ax.scatter(x, y, s=58, marker=marker, color=MUTED,
                   edgecolors=SURFACE, linewidths=2, zorder=3)
        dx, dy, ha = OFFSETS[row['model']]
        name = row['model'] + (' (baseline)' if row is base else '')
        ax.annotate(name, (x, y), xytext=(dx, dy), textcoords='offset points',
                    ha=ha, va='center', fontsize=10, color=INK_2)

    x, y = float(ours['latency_ms']), float(ours['AP'])
    ax.scatter(x, y, s=420, marker='*', color=ACCENT, edgecolors=SURFACE,
               linewidths=2, zorder=5)
    ax.annotate('SPOT-DETR (ours)\n33.3 ± 0.3 AP', (x, y), xytext=(12, 2),
                textcoords='offset points', ha='left', va='center',
                fontsize=11, fontweight='bold', color=INK)
    ax.annotate('', xy=(x * 0.93, y - 0.35),
                xytext=(float(base['latency_ms']) * 1.06, float(base['AP']) + 0.2),
                arrowprops={'arrowstyle': '->', 'color': INK_2, 'lw': 1.2,
                            'connectionstyle': 'arc3,rad=-0.25'})
    ax.text(62, 31.5, '+3.5 AP', fontsize=10,
            color=INK_2, ha='right', va='center')

    ax.set_xscale('log')
    ax.set_xlim(20, 1600)
    ax.set_ylim(20, 35)
    ax.xaxis.set_major_locator(FixedLocator([30, 50, 100, 200, 500, 1000]))
    ax.xaxis.set_minor_locator(NullLocator())
    ax.set_xticklabels(['30', '50', '100', '200', '500', '1000'])
    ax.set_xlabel('Latency (ms, log scale)  ←  faster')
    ax.set_ylabel('AP (AI-TOD-v2 test)')
    ax.grid(color=GRID, linewidth=1)
    ax.set_axisbelow(True)
    for side in ('top', 'right'):
        ax.spines[side].set_visible(False)
    ax.tick_params(length=0)

    handles = [
        plt.Line2D([], [], marker='*', ls='', ms=14, color=ACCENT, label='SPOT-DETR'),
        plt.Line2D([], [], marker='o', ls='', ms=7, color=MUTED, label='DETR-based'),
        plt.Line2D([], [], marker='s', ls='', ms=7, color=MUTED, label='CNN-based'),
    ]
    ax.legend(handles=handles, loc='upper right', frameon=False,
              fontsize=10, labelcolor=INK_2)
    ax.set_title('Accuracy vs. latency · 800×800 input · RTX A6000 · batch 1 · FP32',
                 loc='left', fontsize=11, color=INK_2, pad=10)

    out = ROOT / 'assets/charts'
    out.mkdir(parents=True, exist_ok=True)
    fig.savefig(out / 'ap_latency_aitodv2.png', dpi=200, facecolor=SURFACE)
    fig.savefig(out / 'ap_latency_aitodv2.svg', facecolor=SURFACE,
                metadata={'Date': None})
    svg = out / 'ap_latency_aitodv2.svg'
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines()) + '\n')
    plt.close(fig)


if __name__ == '__main__':
    main()
