# 효율 측정 조건

[결과 자료로 돌아가기](README.md) · [실험 설명](../docs/experiments.md)

원고 표 6과 로컬 연구 프로젝트의 `work_dirs/efficiency_20261011/EFFICIENCY_RESULTS_KR.md`, `logs/v2_Ours.log`를 교차 확인했습니다. 이 문서는 기존 측정의 조건을 정리한 것으로, 포트폴리오 작성 중 새로 벤치마크한 결과는 아닙니다.

| 항목 | 확인한 조건 |
|---|---|
| GPU | NVIDIA RTX A6000 1장 |
| 입력 / 배치 | 800×800 / 1 |
| 정밀도 | FP32, matmul·cuDNN TF32 비활성화, AMP 없음 |
| 반복 | warm-up 10회 제외 후 test 영상 500장 평균 |
| 동기화 | 매 반복 전후 `torch.cuda.synchronize()` |
| 시간에 포함 | host→device 복사, forward, 후처리 |
| 시간에서 제외 | 디스크 I/O, CPU 전처리 |
| 연산량 | fvcore, MAC 1회 = 1 FLOP 기준, 후처리 제외 |
| 커스텀 연산 | deformable sampling, SAPA, Haar DWT, rFFT/irFFT 등 계산 규칙 포함 |
| 최종 모델 | `SMWG_DETR_AITODv2_sgs_spatial_atom_x2_rank025_trainval_ep40` |

최종 모델의 원본 `[ROW]`에서 로컬 경로를 제외한 측정 필드를 [efficiency_spot_log_excerpt.json](efficiency_spot_log_excerpt.json)에 보존했습니다. 원본의 연산량 382.38944156, FPS 9.13913664, 평균 지연 109.41952609ms는 각각 표의 382.4, 9.14, 109.4로 반올림됩니다.

## 표 6 각주의 의미

1. **동적 쿼리 모델의 GFLOPs:** DQ-DETR과 Dome-DETR-S는 영상마다 쿼리 수가 달라 20장 평균으로 계산했습니다.
2. **Dome-DETR-S의 속도:** 공개 구현에서 반복적인 GPU→CPU 동기화와 CPU 위치 임베딩 계산이 지연에 큰 영향을 줍니다. 모델의 이론적 연산량만으로 처리 속도를 해석하면 안 됩니다.
3. **DNTR의 GFLOPs:** 1,000개 RoI 기준 계산이며, 실제 test에서는 RPN 제안이 최대 3,000개여서 실제 연산량을 낮게 추정할 수 있습니다. FPS는 실제 추론 경로로 측정했습니다.

비교 모델의 구현·측정 조건에 따른 결과이며 다른 하드웨어나 전체 서비스의 처리 시간을 의미하지 않습니다.
