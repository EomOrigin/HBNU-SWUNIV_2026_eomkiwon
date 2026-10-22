<div align="center">

# 엄기원 &nbsp;<sub>Ki-won Eom</sub>

국립한밭대학교 컴퓨터공학과 학부생 · AIM Lab 학부연구생

[Email](mailto:eomkiwon1528@gmail.com) &nbsp;/&nbsp; [GitHub](https://github.com/EomOrigin) &nbsp;/&nbsp; [Kaggle](https://www.kaggle.com/kiwoneom) &nbsp;/&nbsp; [DACON](https://dacon.io/myprofile/497780/home)

**한국어** | [English](README_EN.md)

</div>

국립한밭대학교 컴퓨터공학과 학부생이고, 2024년 2월부터 AIM Lab에서 학부연구생으로 연구하고 있습니다. 위성·항공 영상에서 몇 픽셀 크기의 객체를 찾아내는 문제를 연구하며, 광학 영상과 SAR 영상을 함께 다룹니다. 지금까지 KCI 등재지에 제1저자 논문 2편을 게재했고, 공동 제1저자로 쓴 SPOT-DETR 원고는 투고를 준비하고 있습니다.

<sub>2026학년도 국립한밭대학교 컴퓨터공학과 포트폴리오경진대회 출품작</sub>

## 소식

- **2026.10** &nbsp; SPOT-DETR 원고 완성, 투고 준비 중
- **2026.03** &nbsp; YOLO-Dos, 전기전자학회논문지 게재
- **2025** &nbsp; ViT 기반 딥페이크 탐지 논문, 디지털포렌식연구 게재
- **2025** &nbsp; SW중심대학 공동 AI 경진대회 본선 16위 / 271팀
- **2024** &nbsp; 제6회 연구개발특구 AI SPARK 챌린지 대상
- **2024.02** &nbsp; AIM Lab 학부연구생 시작

## 대표 연구

<a href="SPOT-DETR.md"><img src="assets/figures/Fig1_concept.png" alt="기존 DETR과 SPOT-DETR의 파이프라인 비교"></a>

**[SPOT-DETR: 고해상도 특징 정제와 off-grid 후보 메모리를 이용한 항공 영상 극소 객체 탐지](SPOT-DETR.md)**

항공 영상의 차량이나 사람은 한 변이 몇 픽셀이라, DETR 계열 검출기를 거치면 특징 맵의 한두 셀로 줄어들고 셀 중심에서 출발한 후보와도 잘 맞지 않습니다. SPOT-DETR은 stride 4 특징에서 시작하는 고해상도 경로 하나에서 특징 정제(SGS)와 off-grid 후보 생성(ATOM)을 함께 수행해 이 두 문제를 다룹니다.

| | AI-TOD AP | AI-TOD-v2 AP | AP<sub>vt</sub> (v2) | very tiny 후보 재현율 |
|---|:---:|:---:|:---:|:---:|
| 기준 모델 (SMWG-DETR) | 32.1 | 29.8 | 15.7 | 38.5% |
| **SPOT-DETR** | **37.6** | **33.3** | **20.8** | **67.1%** |

같은 프로토콜로 다시 학습한 비교 검출기 가운데 두 데이터셋 모두에서 가장 높은 AP입니다. 공동 제1저자로서 문제 정의, 구현, 비교 실험, 원고 작성을 맡았습니다. 방법, 전체 결과, 분석과 한계는 [프로젝트 페이지](SPOT-DETR.md)에 정리했습니다.

## 논문

원격탐사 영상의 객체 탐지와 분할을 주로 연구합니다. <sup>†</sup>는 공동 제1저자입니다.

<table>
<tr>
<td width="34%" valign="top"><a href="SPOT-DETR.md"><img src="assets/thumbs/spot_detr.png" width="260" alt="SPOT-DETR"></a></td>
<td valign="top">
<a href="SPOT-DETR.md"><b>SPOT-DETR: Tiny object detection in aerial images using high-resolution feature refinement and off-grid candidate memory</b></a><br>
<b>Ki-won Eom</b><sup>†</sup>, Cheoneum Park<sup>†</sup>, Eunkyung Kim, Haneol Jang<br>
<i>Manuscript in preparation</i>, 2026<br>
<a href="SPOT-DETR.md">프로젝트 페이지</a> / <a href="paper/SPOT_DETR_manuscript_20261022.pdf">원고</a>
<p>stride 4 특징 경로 하나에서 특징 정제와 off-grid 후보 생성을 함께 수행해, 다시 학습한 비교 검출기 가운데 AI-TOD와 AI-TOD-v2에서 가장 높은 AP를 얻었습니다.</p>
</td>
</tr>
<tr>
<td width="34%" valign="top"><a href="https://doi.org/10.7471/ikeee.2026.30.1.171"><img src="assets/thumbs/yolo_dos.png" width="260" alt="YOLO-Dos"></a></td>
<td valign="top">
<a href="https://doi.org/10.7471/ikeee.2026.30.1.171"><b>YOLO-Dos: Improving YOLO-Based SAR Object Detection Performance via a Speckle Suppression Module</b></a><br>
<b>Ki-won Eom</b>, Eunkyung Kim, Haneol Jang<br>
<i>Journal of IKEEE (전기전자학회논문지)</i>, 30(1):171–181, 2026 · KCI 등재<br>
<a href="https://doi.org/10.7471/ikeee.2026.30.1.171">DOI</a> / <a href="https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003322680">KCI</a>
<p>YOLOv8의 입력 스템을 스펙클 억제 모듈(로그 변환, 웨이블릿 분해, 고주파 어텐션)로 바꿔, HRSID에서 YOLOv8보다 mAP@50:95를 5.75%p, F1을 3.21%p 높였습니다.</p>
</td>
</tr>
<tr>
<td width="34%" valign="top"><a href="https://doi.org/10.22798/KDFS.2025.19.4.116"><img src="assets/thumbs/rwm_deepfake.png" width="260" alt="Region Weight Module"></a></td>
<td valign="top">
<a href="https://doi.org/10.22798/KDFS.2025.19.4.116"><b>ViT-based Deepfake Detection via Regional Emphasis Weights on Eyes, Nose, and Mouth</b></a><br>
<b>Ki-won Eom</b>, Dong-Su Kim, Tae-Woo Oh, Haneol Jang<br>
<i>Journal of Digital Forensics (디지털포렌식연구)</i>, 19(4):116–131, 2025 · KCI 등재<br>
<a href="https://doi.org/10.22798/KDFS.2025.19.4.116">DOI</a> / <a href="https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003243484">KCI</a> / <a href="https://github.com/EomOrigin/HBNU-SWUNIV_2025_eomkiwon">2025 포트폴리오</a>
<p>ViT의 패치 임베딩 단계에서 눈·코·입 영역에 학습 가능한 가중치를 주는 Region Weight Module을 제안했고, FaceForensics++에서 ViT 대비 ACER는 7.94%, AUC는 약 3% 개선되었습니다.</p>
</td>
</tr>
</table>

## 수상

- **대상**, 제6회 연구개발특구 AI SPARK 챌린지 (위성 다분광 영상 기반 산불 탐지), 2024 · [대회](https://aifactory.space/task/2723/overview)
- **본선 16위 / 271팀**, SW중심대학 공동 AI 경진대회, 2025 · [대회](https://dacon.io/competitions/official/236473/overview/description)
- **예선 2위 / 13팀** (2024), **예선 5위 / 17팀** (2025), SW중심대학 공동 AI 경진대회
- **2위**, 위성 영상 구름 분할 Kaggle 챌린지 (국립한밭대학교 AI 교과), 2025 · [대회](https://www.kaggle.com/competitions/clouds-segmentation-2025/overview)

## 이력

- **2024.02 – 현재** &nbsp; 학부연구생, AIM Lab, 국립한밭대학교
- **2023.03 – 현재** &nbsp; 학사과정, 국립한밭대학교 컴퓨터공학과

---

<sub>페이지 구성은 [Jon Barron](https://jonbarron.info/)의 학술 홈페이지 형식을 참고했습니다.</sub>
