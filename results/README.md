# 실험표 CSV

[포트폴리오로 돌아가기](../README.md) · [실험 설명](../docs/experiments.md)

출처는 `SPOT_DETR_final_20261022.zip` 안의 한국어 원고 `SPOT_DETR_Manuscript_KR.md`입니다. **원고 보고값을 전사한 자료**이며, 원시 학습 로그·평가 결과 파일은 아닙니다.

| 파일 | 원고 출처 | 단위 |
|---|---|---|
| [benchmark_aitodv2.csv](benchmark_aitodv2.csv) | 표 1 | AP 0–100 |
| [benchmark_aitod.csv](benchmark_aitod.csv) | 표 2 | AP 0–100 |
| [category_aitodv2.csv](category_aitodv2.csv) | 표 3 | 범주별 AP 0–100 |
| [ablation_aitodv2.csv](ablation_aitodv2.csv) | 표 4 | AP 0–100, 분석 모델 |
| [proposal_recall_aitodv2.csv](proposal_recall_aitodv2.csv) | 표 5 | 재현율 %, 상위 900개·IoU ≥ 0.5 |
| [efficiency.csv](efficiency.csv) | 표 6 | Params M, GFLOPs, FPS, latency ms, AP 0–100 |

`*_std`는 표준편차입니다. 빈 칸은 원고에 보고되지 않았다는 뜻이며 0이 아닙니다. `statistic`은 3개 시드 평균인지, 단일 분석 모델인지, 분산 미보고 값인지를 구분합니다. `source_table`은 원고 표 번호입니다.

효율 표의 `source_footnote`는 원고 표의 위첨자 1–3을 보존합니다. 별도 측정 기록에서 확인한 설명은 [효율 측정 조건](efficiency_measurement.md)에 정리했습니다.

```bash
python3 scripts/summarize_results.py
```

이 명령은 위 표에서 주요 차이와 계산량·속도 비를 계산합니다. GPU나 외부 패키지가 필요하지 않습니다.
