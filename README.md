# 📺 TV 프로그램 장르 분류
> **시놉시스 기반 TV 프로그램 장르 분류 프로젝트**

<div align="center">

![Python](https://img.shields.io/badge/python-v3.9+-blue.svg)
![Keras](https://img.shields.io/badge/Keras-TensorFlow-red.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange.svg)
![Konlpy](https://img.shields.io/badge/KoNLPy-0.6+-blueviolet.svg)
![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)
![Gemini](https://img.shields.io/badge/Gemini_API-google--generativeai-red.svg)

</div>

---

## 📌 개요 (Overview)

본 프로젝트는 TV 프로그램의 시놉시스(줄거리) 텍스트를 분석하여 해당 프로그램의 장르를 예측하고 분류하는 것을 목표로 합니다.

**주요 기능:**
- **데이터 파이프라인**: 웹 크롤링, 텍스트 전처리(Konlpy), 모델 학습(Keras)의 전체 과정을 포함합니다.
- **두 가지 예측 방식**: 학습된 모델을 커맨드 라인(CLI) 또는 GUI 환경에서 사용할 수 있습니다.
- **데이터 생성**: Google Gemini API를 활용하여 테스트용 시놉시스를 동적으로 생성하는 기능을 제공합니다.

---

## 📁 프로젝트 구조 (Project Structure)

```
TV_program_genre_classification-1/
│
├── genre_predictor_gui.py      # GUI 예측 애플리케이션
├── README.md                   # 프로젝트 설명 파일
├── requirements.txt            # 의존성 패키지 목록
│
├── 1_crawl_data.py             # 1. 데이터 수집
├── 2_preprocess_data.py        # 2. 데이터 전처리
├── 3_train_model.py            # 3. ML 모델 학습
├── 4_predict_example.py        # 4. CLI 기반 장르 예측 예제
│
├── crawling_data/              # (생성됨) 크롤링된 원본 데이터 (.csv)
└── models/                     # (생성됨) 학습된 모델 (.h5, .pickle)
```

---

## 💻 사용 방법 (Usage)

### 1단계: 모델 학습

예측 애플리케이션을 실행하기 전에, 먼저 스크립트들을 순서대로 실행하여 ML 모델을 생성해야 합니다.

```bash
# 1. 데이터 수집
python 1_crawl_data.py

# 2. 데이터 전처리
python 2_preprocess_data.py

# 3. 모델 학습
python 3_train_model.py
```
- 위 과정이 정상적으로 완료되면 `models` 폴더에 `multilabel_classification_model_*.h5` 파일과 `token_*.pickle`, `encoder_*.pickle` 파일이 생성됩니다.

---

### 2단계: 장르 예측

모델 학습이 완료되면, 다음 두 가지 방법으로 장르를 예측할 수 있습니다.

#### A) 커맨드 라인(CLI)에서 예측하기

`4_predict_example.py`는 학습된 모델을 사용해 예측을 수행하는 간단한 예제 스크립트입니다.
```bash
python 4_predict_example.py
```
- 스크립트 내부의 샘플 시놉시스에 대한 예측 결과가 터미널에 출력됩니다.

#### B) GUI 애플리케이션으로 예측하기

`genre_predictor_gui.py`를 실행하여 그래픽 인터페이스를 갖춘 예측 프로그램을 사용할 수 있습니다.
```bash
python genre_predictor_gui.py
```

**GUI 기능 설명:**
1.  **시놉시스 직접 입력 및 예측**:
    - `📝 예측할 시놉시스:` 란에 원하는 줄거리를 직접 입력합니다.
    - `🎯 장르 예측하기` 버튼을 클릭하면, 하단에 해당 시놉시스의 장르별 확률이 상위 5개까지 표시됩니다.
2.  **Gemini로 시놉시스 생성 및 테스트**:
    - `🌟 Gemini로 시놉시스 생성` 버튼을 클릭합니다.
    - Gemini API가 새로운 시놉시스와 해당 장르를 생성하여 각 텍스트 박스에 자동으로 입력해줍니다.
    - `🎯 장르 예측하기` 버튼을 눌러, 생성된 시놉시스에 대해 우리 모델이 얼마나 잘 예측하는지 테스트해볼 수 있습니다.

---

## 👥 팀 구성 (Team)

| 이름 | 역할 | 주요 담당 |
|:---:|:---:|:---:|
| **조해찬** | **Team Leader** | • 프로젝트 총괄 및 데이터 파이프라인 설계<br>• 분담 데이터 수집/전처리<br>• 개별 모델 학습 및 최종 모델 선정 기여<br>• GUI 예측 애플리케이션 개발 |
| **김현빈** | **Team Member** | • 프로젝트 코드 총괄 및 버전 관리<br>• 분담 데이터 수집/전처리<br>• 개별 모델 학습 및 최종 모델 선정 기여 |
| **이은서** | **Team Member** | • 발표 자료 기획 및 제작<br>• 분담 데이터 수집/전처리<br>• 개별 모델 학습 및 최종 모델 선정 기여 |

---

## 📜 라이선스 (License)

This project is licensed under the MIT License.
