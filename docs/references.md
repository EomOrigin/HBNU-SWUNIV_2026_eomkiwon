# 참고 자료

[SPOT-DETR 프로젝트 페이지](../SPOT-DETR.md) · [홈](../README.md)

## 대표 연구

엄기원, 박천음, 김은경, 장한얼. **SPOT-DETR: 고해상도 특징 정제와 off-grid 후보 메모리를 이용한 항공 영상 극소 객체 탐지.** 2026.10.22 투고 전 원고. 엄기원·박천음 공동 제1저자, 김은경·장한얼 공동 교신저자.

[제공 원고 PDF](../paper/SPOT_DETR_manuscript_20261022.pdf) · [원본과 변환본 정보](../paper/SOURCE.md)

## 데이터와 기반 기술

| 자료 | 포트폴리오에서의 역할 |
|---|---|
| [AI-TOD 공식 저장소](https://github.com/jwwangchn/AI-TOD) | 항공 영상 극소 객체 탐지 데이터셋 |
| [AI-TOD-v2 프로젝트](https://chasel-tsui.github.io/AI-TOD-v2/) | 같은 영상에 대해 수정된 주석을 제공하는 데이터셋 |
| [MMDetection](https://github.com/open-mmlab/mmdetection) | 객체 탐지 구현 프레임워크 |
| SMWG-DETR, “DETR Enhanced by Fourier Spectral Modulation and Wavelet-Guided Fusion for Tiny Object Detection” | 기반 탐지기; 기존 스펙트럼 변조·웨이블릿 융합·잡음 제거 학습 |

비교 모델과 방법론의 전체 참고문헌은 연구 원고의 참고문헌 절에 있습니다. 표의 비교값은 원 논문의 최고 성능을 모아 놓은 값이 아니라, SPOT-DETR 원고가 공통 프로토콜에서 수행했다고 보고한 실험값입니다.
