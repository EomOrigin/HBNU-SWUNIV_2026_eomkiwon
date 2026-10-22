#!/usr/bin/env python3
"""Render manuscript table 1 from the checked-in CSV; requires matplotlib."""

import csv
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]


def main():
    with (ROOT / 'results/benchmark_aitodv2.csv').open(encoding='utf-8', newline='') as f:
        rows = {row['model']: row for row in csv.DictReader(f)}
    labels = ['SMWG-DETR', 'SPOT-DETR']
    colors = ['#8b9bad', '#176b75']
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12,
                         'axes.spines.top': False, 'axes.spines.right': False,
                         'axes.spines.left': False, 'axes.titleweight': 'bold'})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.8), layout='constrained')
    for ax, metric, title, ceiling in zip(axes, ['AP', 'APvt'],
                                        ['Overall AP', 'Very tiny AP'], [40, 26]):
        values = [float(rows[label][metric]) for label in labels]
        errors = [float(rows[label][f'{metric}_std'] or 0) for label in labels]
        bars = ax.bar(labels, values, width=0.53, color=colors)
        ax.errorbar([1], [values[1]], yerr=[errors[1]], fmt='none',
                    capsize=6, lw=1.6, ecolor='#163344')
        ax.set_ylim(0, ceiling)
        ax.set_ylabel('AP (0–100)')
        ax.set_title(title, loc='left', pad=20)
        ax.grid(axis='y', color='#e5eaf0', linewidth=0.8)
        ax.set_axisbelow(True)
        ax.tick_params(axis='both', length=0)
        for bar, val, err in zip(bars, values, errors):
            label = f'{val:.1f}' + (f' ± {err:.1f}' if err else '')
            ax.text(bar.get_x()+bar.get_width()/2, val+err+0.8, label,
                    ha='center', va='bottom', weight='bold', color='#163344')
        ax.text(0.98, 0.96, f'+{values[1]-values[0]:.1f} AP points', transform=ax.transAxes,
                ha='right', va='top', color=colors[1], fontsize=12, weight='bold')
    fig.suptitle('AI-TOD-v2 · Reported manuscript results', x=0.012, ha='left',
                 fontsize=17, weight='bold', color='#163344')
    fig.supxlabel('SPOT-DETR: mean ± std over 3 seeds; baseline variance not reported. Source: Table 1.',
                  fontsize=9, color='#566474')
    out = ROOT / 'assets/charts'
    out.mkdir(parents=True, exist_ok=True)
    for extension in ['png', 'svg']:
        fig.savefig(out / f'accuracy_comparison.{extension}', dpi=180, facecolor='white')
    svg = out / 'accuracy_comparison.svg'
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines()) + '\n')
    plt.close(fig)


if __name__ == '__main__':
    main()
