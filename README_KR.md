# SecondBrain

- [English README](README_EM.md)
- [日本語のREADME](README_JP.md)
- [한국어 README](README_KR.md)
- [中文 README](README.md)

## 소개
SecondBrain은 사용자의 개인 사무 및 자원을 우선 순위에 따라 정렬하고 효과적으로 관리하는 데 도움을 주기 위해 설계된 효율적인 인생 계획 및 관리 도구입니다. 이 도구는 Notion 데이터베이스 관리, OpenAI GPT 지원, 지능형 시간 스케줄링, 날씨 조회 기능, 개인 현금 흐름 조회, 이메일 상호 작용 등 다양한 기능을 통합하여 개인 생활의 효율성을 향상시킵니다.

## 로드맵
- [ ] WeChat의 결제 내역을 모니터링하고 수입 및 지출 명세서를 작성합니다.
- [ ] ms to-do와 outlook을 통해 자동으로 일정 및 일상 작업을 추가하고 삭제합니다.
- [X] Openweather에서 제공하는 정확한 일일 날씨 데이터를 사용하여 여행 제안을 제공합니다.
- [X] Notion 데이터베이스에서 동적으로 작업 정보를 가져옵니다.
- [X] OpenAI GPT를 사용하여 작업 실행의 우선 순위와 제안을 생성합니다.
- [X] 이메일을 통해 매일 작업 및 제안을 자동으로 보냅니다.

## 설치 안내

### 환경 요구 사항
- Python 3.8 또는 그 이상 버전
- Notion 계정 및 관련 API 접근 권한
- OpenAI API 키

### 단계
1. 저장소를 클론합니다:
   ```
   git clone https://github.com/Zippland/SecondBrain.git
   ```
2. 프로젝트 디렉토리로 이동합니다:
   ```
   cd TaskPilot
   ```
3. 의존성을 설치합니다:
   ```
   pip install -r requirements.txt
   ```

## 사용 설명서
프로젝트를 시작하려면 다음 명령을 실행하세요:
```
python main.py
```
`config.py` 파일에 Notion의 토큰, 데이터베이스 ID, SMTP 서버 정보 및 OpenAI의 API 키를 포함하여 모든 필요한 구성 정보가 올바르게 설정되어 있는지 확인하세요.

## 기여 가이드
우리는 버그 보고, 기능 요청 및 코드 제출을 포함한 모든 형태의 기여를 환영합니다. 기여하려면 다음 단계를 따르세요:
1. 저장소를 포크하고 자신의 브랜치를 만듭니다.
2. 기능을 추가한 경우 테스트를 추가하세요.
3. 코드가 기존 코드 스타일을 준수하는지 확인하세요.
4. 병합 요청을 제출하세요.

## 라이센스
이 프로젝트는 [Apache 라이센스](LICENSE)를 채택합니다.

## 연락처
질문이 있으시면 [이메일](mailto:zihan.jian@outlook.com)을 통해 문의하세요.