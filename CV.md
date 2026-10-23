<div align="center">

# 엄기원 &nbsp;<sub>Ki-won Eom</sub>

국립한밭대학교 컴퓨터공학과 학부생 · AIM Lab 학부연구생

[Email](mailto:eomkiwon1528@gmail.com) &nbsp;/&nbsp; [GitHub](https://github.com/EomOrigin) &nbsp;/&nbsp; [포트폴리오](https://github.com/EomOrigin/HBNU-SWUNIV_2026_eomkiwon)

**한국어** | [English](CV_EN.md) &nbsp;·&nbsp; [PDF로 받기](cv/KiwonEom_CV_KR.pdf) &nbsp;·&nbsp; [포트폴리오 홈](README.md)

</div>

## 연구 관심

원격탐사 영상(광학·SAR)의 객체 탐지와 분할, 극소 객체 탐지, Detection Transformer

## 학력

**국립한밭대학교 컴퓨터공학과 학사과정** &nbsp;·&nbsp; 2023.03 – 현재

## 연구 경력

**학부연구생, AIM Lab, 국립한밭대학교** &nbsp;·&nbsp; 지도교수: 장한얼 교수 · 2024.02 – 현재

- 항공 영상 극소 객체 탐지 모델 SPOT-DETR을 설계·구현했습니다(공동 제1저자). 같은 조건으로 다시 학습한 모든 비교 검출기보다 AP가 높았습니다(AI-TOD 37.6, AI-TOD-v2 33.3).
- SAR 선박 탐지를 위한 스펙클 억제 모듈 YOLO-Dos를 제안했습니다(제1저자). HRSID에서 YOLOv8보다 mAP@50:95가 5.75%p 높았습니다.
- 눈·코·입 영역 가중치를 쓰는 ViT 딥페이크 탐지를 제안했습니다(제1저자). FaceForensics++에서 ViT 대비 ACER 7.94%, AUC 약 3%가 개선되었습니다.

## 논문

† 공동 제1저자

- **엄기원**†, 박천음†, 김은경, 장한얼. **SPOT-DETR: Tiny object detection in aerial images using high-resolution feature refinement and off-grid candidate memory.** *투고 준비 중, 2026*. [프로젝트 페이지](https://github.com/EomOrigin/HBNU-SWUNIV_2026_eomkiwon/blob/main/SPOT-DETR.md)
- **엄기원**, 김은경, 장한얼. **YOLO-Dos: 스펙클 억제 모듈을 통한 YOLO 기반 SAR 객체 탐지 성능 개선.** *전기전자학회논문지, 30(1), 171–181, 2026 · KCI 등재*. [DOI](https://doi.org/10.7471/ikeee.2026.30.1.171)
- **엄기원**, 김동수, 오태우, 장한얼. **눈·코·입 영역 강조 가중치를 활용한 ViT 기반 딥페이크 탐지 기법 연구.** *디지털포렌식연구, 19(4), 116–131, 2025 · KCI 등재*. [DOI](https://doi.org/10.22798/KDFS.2025.19.4.116)

## 수상·대회

**대상, 제6회 연구개발특구 AI SPARK 챌린지** &nbsp;·&nbsp; 위성 다분광 영상 기반 산불 탐지 · 2024

**온라인 29위 / 1,090팀(상위 3%), 오프라인 본선 15위, LG Aimers 9기 해커톤** &nbsp;·&nbsp; 투구 제구 성공 확률 예측 · 2026

**6위 / 138팀(상위 5%), 2026 국립공원 위성 모니터링 AI 챌린지** &nbsp;·&nbsp; 해안 쓰레기 탐지 및 규모 추정 · 2026

**16위 / 271팀(상위 6%), 2025 SW중심대학 디지털 경진대회 AI부문** &nbsp;·&nbsp; 2025

**85위 / 985팀(상위 9%), 제3회 풍력발전량 예측 AI 경진대회(BARAM 2026)** &nbsp;·&nbsp; 2026

**28위 / 219팀(상위 13%), SW중심대학 디지털 경진대회 AI부문** &nbsp;·&nbsp; SW와 생성 AI의 만남 · 2024

**2위, 위성 영상 구름 분할 Kaggle 챌린지** &nbsp;·&nbsp; 국립한밭대학교 AI 교과 · 2025

## 프로젝트

**불법 축사 탐지 모델 개발** &nbsp;·&nbsp; 2026 – 진행 중

**위성 영상 구름 분할 (팀장)** &nbsp;·&nbsp; 2025.09 – 2025.12

- 두꺼운 구름, 얇은 구름, 구름 그림자 3종을 분할하는 모델을 학습해 0.8555로 2위를 했습니다. PyTorch.

**얼굴 위조 판별 이미지 분류 (팀장)** &nbsp;·&nbsp; 2025.03 – 2025.06

- 실제 얼굴과 위조 얼굴을 구분하는 분류 모델로 정확도 98.33%를 얻었습니다. PyTorch.

**얼굴 인식 스마트 도어락 (팀장)** &nbsp;·&nbsp; 2024.09 – 2024.12

- 기존 도어락에 붙이는 장치로, Raspberry Pi 4에서 얼굴을 인식해 GPIO로 잠금장치를 제어하고 출입 기록과 사진을 남깁니다. Python, OpenCV, SQLite, MQTT.

## 기술

- **언어**: Python, C, Java
- **딥러닝**: PyTorch, MMDetection, Ultralytics YOLO, timm, OpenCV, MediaPipe, scikit-learn
- **실험 환경**: Linux 다중 GPU 서버, Docker, Git, Weights & Biases
