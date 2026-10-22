#!/usr/bin/env python3
"""Summarize reported manuscript values; this does not evaluate a model."""

import csv
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_table(name):
    with (ROOT / 'results' / name).open(encoding='utf-8', newline='') as file:
        return list(csv.DictReader(file))


def model_row(rows, model):
    return next(row for row in rows if row['model'] == model)


def main():
    print('SPOT-DETR | provided manuscript values, not a new model evaluation')
    for name, label in [('benchmark_aitodv2.csv', 'AI-TOD-v2'),
                        ('benchmark_aitod.csv', 'AI-TOD')]:
        rows = read_table(name)
        base = model_row(rows, 'SMWG-DETR')
        ours = model_row(rows, 'SPOT-DETR')
        print(f'\n{label} (AP scale: 0–100)')
        for metric in ('AP', 'APvt', 'APt', 'APs'):
            delta = Decimal(ours[metric]) - Decimal(base[metric])
            std = ours[f'{metric}_std']
            print(f'  {metric}: {base[metric]} -> {ours[metric]} ± {std}'
                  f' | {delta:+.1f} AP points')
    rows = read_table('proposal_recall_aitodv2.csv')
    base = next(row for row in rows if row['configuration'] == 'baseline_grid')
    ours = next(row for row in rows if row['configuration'] == 'spot_all')
    delta = Decimal(ours['vt']) - Decimal(base['vt'])
    print(f'\nVery tiny proposal recall: {base["vt"]}% -> {ours["vt"]}%'
          f' | {delta:+.1f} percentage points')
    print('  top 900 initial candidates, IoU >= 0.5; analysis model')
    rows = read_table('efficiency.csv')
    base = model_row(rows, 'SMWG-DETR')
    ours = model_row(rows, 'SPOT-DETR')
    print('\nEfficiency (reported table values)')
    for metric in ('params_M', 'GFLOPs', 'FPS', 'latency_ms'):
        ratio = Decimal(ours[metric]) / Decimal(base[metric])
        print(f'  {metric}: {base[metric]} -> {ours[metric]} | ratio {ratio:.2f}x')
    print('\nSPOT benchmark statistics: mean ± std over 3 seeds.')
    print('Baseline variances are not reported. See docs/experiments.md for scope.')


if __name__ == '__main__':
    main()
