# 집 꾸미기 홀릭 블로그

Flask로 만든 미니멀 개인 블로그입니다.

## 폴더 구조

```
blog/
├── app.py              ← Flask 서버 (여기서 포스트 추가)
├── requirements.txt    ← 필요한 패키지 목록
├── vercel.json         ← Vercel 배포 설정
├── templates/
│   ├── base.html       ← 공통 레이아웃 (사이드바, 헤더)
│   ├── index.html      ← 메인 페이지 (포스트 목록)
│   └── post.html       ← 포스트 상세 페이지
└── static/
    ├── css/style.css   ← 전체 스타일
    └── js/main.js      ← 사이드바, 애니메이션
```

## 로컬에서 실행하기

```bash
# 1. 패키지 설치
pip install -r requirements.txt

# 2. 서버 실행
python app.py

# 3. 브라우저에서 열기
# http://localhost:5000
```

## GitHub에 올리기

```bash
git init
git add .
git commit -m "첫 번째 커밋"
git branch -M main
git remote add origin https://github.com/유저명/repo이름.git
git push -u origin main
```

## Vercel로 배포하기

1. https://vercel.com 에서 회원가입 (GitHub 계정으로)
2. "Add New Project" 클릭
3. 위에서 올린 GitHub 저장소 선택
4. 설정 건드리지 말고 "Deploy" 클릭
5. 끝! 자동으로 URL이 생성됩니다.

## 포스트 추가하기

`app.py` 파일의 `posts` 리스트에 항목을 추가하면 돼요:

```python
{
    "id": 7,                          ← 번호 (겹치면 안 됨)
    "category": "INTERIOR",          ← INTERIOR / DAILY / ETC
    "tag": "홈인테리어",
    "title": "포스트 제목",
    "date": "2025.07.01",
    "summary": "짧은 소개글",
    "image": "이미지 URL"             ← Unsplash 무료 이미지 추천
}
```
