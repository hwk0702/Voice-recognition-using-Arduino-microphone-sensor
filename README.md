# Voice recognition using Arduino microphone sensor

### 1. 소개
#### 1.1 목표

<img src='/img/target.PNG' width='400'>

#### 1.2 방법

1) 아두이노 마이크 모듈 이용 음성 데이터 수집

2) 데이터 수정 및 확보

3) 데이터 전처리

4) Tensorflow 사용, 데이터 학습

5) 음성인식

6) 결과를 아두이노 스피커 모듈로 출력

#### 1.3 데이터

- 6명의 데이터 사용
- 세 번 정도 녹음
- 데이터 개수를 늘리기 위하여 시간, 높낮이 조정

#### 1.4 Hardware & software

<img src='/img/hwsw.PNG' width='400'>

#### 1.5 사용 부품

<img src='/img/hw.PNG' width='400'>

#### 1.6 브레드보드 뷰

<img src='/img/breadboard.PNG' width='400'>

#### 1.7 사용 기술

<img src='/img/tec.PNG' width='400'>

<img src='/img/tec2.PNG' width='400'>

---

### 2. 프로젝트 과정
#### 2.1 Tensorflow 과정

1) 아두이노 데이터 모듈 이용 음성 데이터 수집

<img src='/img/voicedata1.png' width='400'>
<img src='/img/voicedata3.png' width='400'>
<img src='/img/voicedata2.png' width='400'>
<img src='/img/voicedata4.png' width='400'>

- 샘플링 속도는 ADC Free running mode일때 대략 100kHz로, 이를 FFT하게되면 이론적으로 샘플링 속도의 반, 50kHz까지 읽을 수 있다. FFT후 샘플 개수는 128개로, 대략 막대기 하나 하나 간격이 약390Hz


2) 데이터 수정 및 확보

<img src='/img/voicedata7.png' width='400'>

<img src='/img/voicedata5.png' width='300'>

- 시간, 높낮이 조정하여 데이터 개수 확보

3) 데이터 전처리

<img src='/img/voicedata6.png' width='300'>

<img src='/img/voicedata8.png' width='200'>

4) Tensorflow 사용, 데이터 학습

<img src='/img/voicedata9.png' width='400'>

<img src='/img/voicedata10.png' width='400'>

<img src='/img/voicedata11.png' width='400'>

<img src='/img/voicedata12.png' width='400'>

5) 테스트

<img src='/img/voicedata13.png' width='400'>

#### 2.2 출력 파일(오디오)

1) Google TTS 이용하여 출력 파일 생성

2) 오디오 파일 16비트, 8000Hz로 설정

2) gain 변환

- WaveGain 프로그램 이용

3) bit data 출력

- FreeMat 프로그램 이용 txt 파일로 저장

4) bit datafmf byte data로 변환

- bits2byte 프로그램 이용

---

### 3. 결과

[![Video Label](https://i.ytimg.com/vi/RTp90wNrhfQ/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLAfarc71ZBysdtC_uD6IS_RtDqUuQ)](https://www.youtube.com/watch?v=RTp90wNrhfQ&feature=youtu.be)
