<div align="center">

# 엄기원 &nbsp;<sub>Ki-won Eom</sub>

국립한밭대학교 컴퓨터공학과 학부생 · AIM Lab 학부연구생

[Email](mailto:eomkiwon1528@gmail.com) &nbsp;/&nbsp; [CV](CV.md) &nbsp;/&nbsp; [GitHub](https://github.com/EomOrigin) &nbsp;/&nbsp; [Kaggle](https://www.kaggle.com/kiwoneom) &nbsp;/&nbsp; [DACON](https://dacon.io/myprofile/497780/home)

**한국어** | [English](README_EN.md)

</div>

국립한밭대학교 컴퓨터공학과 학부생이고, 2024년 2월부터 장한얼 교수님의 AIM Lab에서 학부연구생으로 연구하고 있습니다. **컴퓨터 비전**, 그중에서도 광학·항공·SAR **위성 영상의 객체 탐지**를 주로 연구합니다. 지금까지 **KCI 등재지에 제1저자 논문 2편**을 게재했고, 공동 제1저자 원고 1편을 투고 준비하고 있습니다. 대회도 꾸준히 나가 최근에는 **LG Aimers 9기 결선(3,393명 중 96명)** 에 진출했습니다.

## 소식

- **2026.10** &nbsp; SPOT-DETR 원고 완성, 투고 준비 중
- **2026.10** &nbsp; 2026 국립공원 위성 모니터링 AI 챌린지 **6위 / 138팀**
- **2026.09** &nbsp; **LG Aimers 9기 결선 진출**(3,393명 중 96명), 결선 15위 · 온라인 예선 29위 / 1,090팀
- **2026.03** &nbsp; YOLO-Dos, 전기전자학회논문지 게재
- **2025** &nbsp; ViT 기반 딥페이크 탐지 논문, 디지털포렌식연구 게재
- **2025** &nbsp; 2025 SW중심대학 디지털 경진대회 AI부문 16위 / 271팀
- **2024** &nbsp; 제6회 연구개발특구 AI SPARK 챌린지 **대상**
- **2024.02** &nbsp; AIM Lab 학부연구생 시작

## 연구 분야

- **위성·항공 영상 객체 탐지**: 작고 빽빽한 객체(SPOT-DETR), 스펙클이 심한 SAR 영상(YOLO-Dos)
- **위성 영상 분석**: 산불 탐지, 구름 분할, 해안 쓰레기 탐지
- **영상 포렌식**: Vision Transformer 기반 딥페이크 탐지

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/research-line-ko-dark.png">
  <img alt="2024 산불 탐지, 2025 딥페이크 탐지, 2026 YOLO-Dos, 2026 SPOT-DETR" src="assets/research-line-ko-light.png" width="100%">
</picture>

검출기가 어떤 영상에서 왜 틀리는지를 특징 해상도, 후보 위치, 센서 잡음처럼 측정할 수 있는 원인으로 나누고, 그 원인을 직접 겨냥하는 구조를 설계하는 데 관심이 있습니다.

## 논문

<sup>†</sup>는 공동 제1저자입니다.

<table>
<tr>
<td width="34%" valign="top"><a href="https://doi.org/10.7471/ikeee.2026.30.1.171"><img src="assets/thumbs/yolo_dos.png" width="260" alt="YOLO-Dos"></a></td>
<td valign="top">
<a href="https://doi.org/10.7471/ikeee.2026.30.1.171"><b>YOLO-Dos: 스펙클 억제 모듈을 통한 YOLO 기반 SAR 객체 탐지 성능 개선</b></a><br>
<b>엄기원</b>, 김은경, 장한얼<br>
<i>전기전자학회논문지</i>, 30(1), 171–181, 2026 · KCI 등재<br>
<a href="https://doi.org/10.7471/ikeee.2026.30.1.171">DOI</a> / <a href="https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003322680">KCI</a>
<p>YOLOv8의 입력 스템을 스펙클 억제 모듈(로그 변환, 웨이블릿 분해, 고주파 어텐션)로 바꿔, HRSID에서 YOLOv8보다 <b>mAP@50:95를 5.75%p</b>, F1을 3.21%p 높였습니다.</p>
</td>
</tr>
<tr>
<td width="34%" valign="top"><a href="https://doi.org/10.22798/KDFS.2025.19.4.116"><img src="assets/thumbs/rwm_deepfake.png" width="260" alt="Region Weight Module"></a></td>
<td valign="top">
<a href="https://doi.org/10.22798/KDFS.2025.19.4.116"><b>눈·코·입 영역 강조 가중치를 활용한 ViT 기반 딥페이크 탐지 기법 연구</b></a><br>
<b>엄기원</b>, 김동수, 오태우, 장한얼<br>
<i>디지털포렌식연구</i>, 19(4), 116–131, 2025 · KCI 등재<br>
<a href="https://doi.org/10.22798/KDFS.2025.19.4.116">DOI</a> / <a href="https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003243484">KCI</a> / <a href="https://github.com/EomOrigin/HBNU-SWUNIV_2025_eomkiwon">2025 포트폴리오</a>
<p>ViT의 패치 임베딩 단계에서 눈·코·입 영역에 학습 가능한 가중치를 주는 Region Weight Module을 제안했고, FaceForensics++에서 ViT 대비 <b>ACER가 7.94%</b>, AUC가 약 3% 개선되었습니다.</p>
</td>
</tr>
<tr>
<td width="34%" valign="top"><a href="SPOT-DETR.md"><img src="assets/thumbs/spot_detr.png" width="260" alt="SPOT-DETR"></a></td>
<td valign="top">
<a href="SPOT-DETR.md"><b>SPOT-DETR: Tiny object detection in aerial images using high-resolution feature refinement and off-grid candidate memory</b></a><br>
<b>엄기원</b><sup>†</sup>, 박천음<sup>†</sup>, 김은경, 장한얼<br>
<i>투고 준비 중</i>, 2026<br>
<a href="SPOT-DETR.md">프로젝트 페이지</a> / <a href="paper/SPOT_DETR_manuscript_20261022.pdf">원고</a>
<p>stride 4 특징 경로 하나에서 특징 정제와 off-grid 후보 생성을 함께 수행해, 같은 조건으로 다시 학습한 비교 모델 가운데 <b>AI-TOD 37.6 AP, AI-TOD-v2 33.3 AP</b>로 가장 높았습니다.</p>
</td>
</tr>
</table>

## 프로젝트

**SPOT-DETR 웹 데모** · 캡스톤디자인(졸업작품), 2026

<a href="SPOT-DETR.md"><img src="assets/spot-detr-demo.gif" alt="밀집 주차장 장면에서 SPOT-DETR과 SMWG-DETR을 비교하는 웹 데모" width="100%"></a>

위성·항공 영상을 올리면 SPOT-DETR과 기준 모델(SMWG-DETR)의 탐지 결과를 나란히 보여 줍니다. 큰 영상은 원래 해상도 그대로 타일로 나눠 처리하고, 점수 임계값과 클래스 필터는 다시 돌리지 않아도 바로 반영됩니다. 위 주차장 장면에서 임계값 0.5 기준으로 SPOT-DETR은 차량 203대를, 기준 모델은 146대를 찾았습니다.

- **불법 축사 탐지 모델 개발** (진행 중, 2026)
- **위성 영상 구름 분할** (팀장, 2025) · 두꺼운 구름, 얇은 구름, 구름 그림자 3종을 분할해 교과 Kaggle 챌린지 **2위**(0.8555)
- **얼굴 위조 판별 분류** (팀장, 2025) · 실제 얼굴과 위조 얼굴을 정확도 98.33%로 구분
- **얼굴 인식 스마트 도어락** (팀장, 2024) · Raspberry Pi 4에서 얼굴을 인식해 잠금장치를 제어하고 출입 기록을 남기는 장치 · Python, OpenCV, SQLite, MQTT

## 수상·대회

| 결과 | 대회 | 연도 |
|---|---|:---:|
| **대상** | [제6회 연구개발특구 AI SPARK 챌린지](https://aifactory.space/task/2723/overview) · 위성 다분광 영상 기반 산불 탐지 | 2024 |
| **결선 진출**(3,393명 중 96명) · 결선 **15위** | **LG Aimers 9기 해커톤** · 투구 제구 성공 확률 예측 · [온라인 예선](https://dacon.io/competitions/official/236743/overview/description) 1,090팀 중 29위(상위 3%) · [오프라인 결선](https://dacon.io/competitions/official/236767/overview/description) | 2026 |
| **6위 / 138팀**(상위 5%) | [2026 국립공원 위성 모니터링 AI 챌린지](https://aifactory.space/ko/competitions/9307) · 주제 4: 해안 쓰레기 탐지 및 규모 추정 | 2026 |
| **16위 / 271팀**(상위 6%) | [2025 SW중심대학 디지털 경진대회](https://dacon.io/competitions/official/236473/overview/description) · AI부문 | 2025 |
| **85위 / 985팀**(상위 9%) | [제3회 풍력발전량 예측 AI 경진대회](https://dacon.io/competitions/official/236727/overview/description) (BARAM 2026) | 2026 |
| **28위 / 219팀**(상위 13%) | [SW중심대학 디지털 경진대회](https://dacon.io/competitions/official/236253/overview/description) · SW와 생성 AI의 만남, AI부문 | 2024 |
| **2위** | [위성 영상 구름 분할 Kaggle 챌린지](https://www.kaggle.com/competitions/clouds-segmentation-2025/overview) · 국립한밭대학교 AI 교과 | 2025 |

## 이력

- **2024.02 – 현재** &nbsp; 학부연구생, AIM Lab, 국립한밭대학교 (지도교수: 장한얼)
  - 참여 과제: 국방기술진흥연구소 우주계층 지능통신망 특화연구실 5세부 *퍼즐형 초광역 공간 위성영상 지능형 처리 연구*(경희대학교·국립한밭대학교). SPOT-DETR은 이 과제와 연계한 연구입니다.
- **2023.03 – 현재** &nbsp; 학사과정, 국립한밭대학교 컴퓨터공학과

자세한 내용은 [CV](CV.md)에 있고, [PDF](cv/KiwonEom_CV_KR.pdf)로도 받을 수 있습니다.

## 기술

- **언어** &nbsp; Python, C, Java
- **딥러닝·비전** &nbsp; PyTorch, MMDetection, Ultralytics YOLO, timm, OpenCV, MediaPipe, scikit-learn
- **실험 환경** &nbsp; Linux 다중 GPU 서버, Docker, Git, Weights & Biases

---

<sub>2026학년도 국립한밭대학교 컴퓨터공학과 포트폴리오경진대회 출품작 · 페이지 구성은 [Jon Barron](https://jonbarron.info/)의 학술 홈페이지 형식을 참고했습니다.</sub>
