# DALLA (나는 다른 카오스크랑 다르고, 음료를 달라!)
![58B22EA2-B5A4-4A05-89A0-E05245B40810 PNG](https://github.com/jiyoungzero/GAMUL_Django/assets/79441145/33b5f965-e47e-40e3-8b9b-a48b214946ad)
## 📍 서비스 소개
> **고령층을 위한 키오스크 서비스, 달라**
- 2023년 데이터사이언스 캡스톤디자인 2팀
- 웹, 앱 기반 서비스
- 프로젝트기간 : 2023.04 ~ 2023.6 (3개월)

## 🧠 서비스 배경 / 문제상황
 - 현재의 키오스크는 주무절차가 너무 복잡하니, 4단계로 최소화하자!(시작 - 주문메뉴 - 주문상세화 - 결제)
 -  서비스 흐름이 잘 보이고 가독성 좋도록 UI/UX를 개선하자!
 -  불필요한 영어의 사용은 지양했으면 좋겠다!

- 사용한 API : 구글 CLOUD STT서비스
---
## 📚 기술 스택 및 개발 환경

### ✔ Back-end
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">

### ✔ Front-end
<img src="https://img.shields.io/badge/react-61DAFB?style=for-the-badge&logo=react&logoColor=black"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> 

### ✔ Machine Learning
<img src="https://img.shields.io/badge/Google Cloud STT-4285F4?style=flat-square&logo=Google Cloud&logoColor=white"/>

### ✔IDE 
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/>

---
## 🔍 사용 방법
> 이미지로 보는 서비스 FLOW

![Untitled](https://github.com/jiyoungzero/GAMUL_Django/assets/79441145/1e4fb3ab-5bcb-4cea-9827-1f82929abf7b)
 
> 영상으로 간단히 둘러보기
(영상 삽입 예정)



> 핵심기능

- STT(Speech-to-Text) : 음성으로 주문받기 위해 메뉴, 주문 상세화 부분에 해당 기능 추가. 버튼을 터치하는 과정을 최소화하는 효과 기대
- 화면 전환시 요구사항이 음성으로 나옴 : 글을 읽으시는 게 힘든 고령층을 위해 음성으로 해당 페이지에서 요구하는 것을 안내하는 기능
- UI/UX 개선 : 논문을 기반하여 고령층에게 효과적인 디자인으로 개선 🔎 [논문참고](https://file.notion.so/f/s/5619cad2-1a38-47d1-bf3d-6deb86fc3c29/%E1%84%80%E1%85%A9%E1%84%85%E1%85%A7%E1%86%BC%E1%84%8E%E1%85%B3%E1%86%BC%E1%84%8B%E1%85%B3%E1%86%AF_%E1%84%8B%E1%85%B1%E1%84%92%E1%85%A1%E1%86%AB_%E1%84%91%E1%85%A2%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%E1%84%91%E1%85%AE%E1%84%83%E1%85%B3%E1%84%8C%E1%85%A5%E1%86%B7_AI_%E1%84%8B%E1%85%B3%E1%86%B7%E1%84%89%E1%85%A5%E1%86%BC%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8_%E1%84%8F%E1%85%B5%E1%84%8B%E1%85%A9%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3_%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%90%E1%85%A5%E1%84%91%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%B3%E1%84%8B%E1%85%B4_%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%89%E1%85%A5%E1%86%BC_%E1%84%87%E1%85%B5%E1%84%80%E1%85%AD_%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1.pdf?id=ac795870-bbe5-4229-9dee-b10418ea9256&table=block&spaceId=cfc890e7-0159-495f-af8d-c21dea9983d4&expirationTimestamp=1690509600000&signature=QjmBm5GCRJl3oZWmE_gOIIBL2B9kVsR6W4MJxrqr3rQ&downloadName=%E1%84%80%E1%85%A9%E1%84%85%E1%85%A7%E1%86%BC%E1%84%8E%E1%85%B3%E1%86%BC%E1%84%8B%E1%85%B3%E1%86%AF+%E1%84%8B%E1%85%B1%E1%84%92%E1%85%A1%E1%86%AB+%E1%84%91%E1%85%A2%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%E1%84%91%E1%85%AE%E1%84%83%E1%85%B3%E1%84%8C%E1%85%A5%E1%86%B7+AI+%E1%84%8B%E1%85%B3%E1%86%B7%E1%84%89%E1%85%A5%E1%86%BC%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8+%E1%84%8F%E1%85%B5%E1%84%8B%E1%85%A9%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3+%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%90%E1%85%A5%E1%84%91%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%B3%E1%84%8B%E1%85%B4+%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%89%E1%85%A5%E1%86%BC+%E1%84%87%E1%85%B5%E1%84%80%E1%85%AD+%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1.pdf)


---
## 👥 멤버
| 이지영 | 추예진 | 
|:---:|:---------:|
| <img src="https://user-images.githubusercontent.com/65756225/208081475-0b5e5188-bef9-4ace-9b02-48360988f57f.png" width="200px" /> |(이미지준비중) |
|  *백엔드, 머신러닝(STT)* |*프론트엔드*|

