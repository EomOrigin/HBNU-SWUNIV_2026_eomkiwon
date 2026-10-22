# 구현 환경과 재현 범위

[SPOT-DETR 프로젝트 페이지](../SPOT-DETR.md) · [홈](../README.md)

## 이 저장소에서 확인할 수 있는 것

이 저장소는 포트폴리오 문서, 투고 전 원고 PDF, 원고 그림의 PNG 변환본, 표 1–6을 옮긴 CSV, 결과 요약·차트 생성 스크립트를 제공합니다. CSV는 원고의 보고값을 구조화한 것으로, 개별 실행의 원시 로그가 아닙니다.

모델 학습·추론 코드, 데이터셋, 학습 가중치는 포함하지 않습니다. 따라서 이 저장소만으로 원고의 모델을 학습하거나 탐지 AP를 다시 계산할 수는 없습니다.

## 원고의 구현 환경

| 항목 | 설정 |
|---|---|
| 프레임워크 | PyTorch, MMDetection |
| 백본 | ImageNet 사전학습 ResNet-50, stem·BN 매개변수 고정 |
| 입력 / 증강 | 800×800, 데이터 증강 없음 |
| 특징 차원 | 256 |
| 디코더 | 6층, 8 attention heads, FFN 1,024 |
| 초기 쿼리 | 900 |
| 학습 | 40에포크, 배치 4, AdamW |
| 학습률 / weight decay | 각 1e-4, 백본 학습률은 0.1배 |
| warm-up / gradient clipping | 2,000 iteration 선형 warm-up, norm 0.1 |
| 평가 | EMA 가중치, NMS 없이 최종 디코더 출력 사용 |
| 원고가 기재한 실험 하드웨어 | 단일 NVIDIA RTX A6000, FP32 |

근거: 원고 4.1.3절. CUDA·PyTorch·MMCV의 정확한 버전과 환경 잠금 파일은 제공된 원고 ZIP에 포함되어 있지 않습니다.

## 문서 결과 확인

Python 3의 표준 라이브러리만으로 CSV의 주요 결과와 차이를 출력할 수 있습니다.

```bash
python3 scripts/summarize_results.py
```

차트는 Matplotlib이 설치된 환경에서 다시 생성할 수 있습니다.

```bash
python3 -m pip install matplotlib
python3 scripts/plot_results.py
```

출력은 원고 표 6을 그린 `assets/charts/ap_latency_aitodv2.png`와 `ap_latency_aitodv2.svg`입니다. 이 명령은 원고 표를 다시 그릴 뿐이며, 모델 학습이나 평가를 수행하지 않습니다.

## 모델 실험 전체를 재현하려면 필요한 자료

1. 최종 SPOT-DETR 구현과 해당 커밋, 의존성 버전
2. AI-TOD·AI-TOD-v2 원본 영상과 원고의 train+validation/test 주석
3. SGS·ATOM·손실·후보 선택·EMA를 포함한 최종 학습 설정
4. 3개 시드 목록, 마지막 체크포인트, 실행 명령 및 평가 로그
5. AP의 객체 크기 구간·maxDets 설정과 효율 측정 스크립트

데이터는 [AI-TOD](https://github.com/jwwangchn/AI-TOD)와 [AI-TOD-v2](https://chasel-tsui.github.io/AI-TOD-v2/)의 원 배포처에서 확인할 수 있습니다. 기반 프레임워크는 [MMDetection](https://github.com/open-mmlab/mmdetection)입니다.

## 읽을 때 구분할 사항

- 연구명은 SPOT-DETR이고, 구현 개발 과정의 파일명에는 기반 모델명 SMWG-DETR과 SGS/ATOM 조합이 남아 있을 수 있습니다.
- 최종 SGS의 X₂ 경로는 라플라시안 공간 게이트를 사용합니다. FFT 채널 게이트를 사용하는 실험 변형과 구분합니다.
- 최종 원고는 기준 모델의 L₁–GIoU 상자 회귀·매칭을 유지합니다. 별도의 Gaussian/KLD 등 손실 변형을 최종 성능의 설정으로 간주하지 않습니다.
- 이 포트폴리오의 성능은 제공된 원고의 보고값입니다. 포트폴리오 작성 과정에서 GPU 학습·평가를 재실행하지 않았습니다.
