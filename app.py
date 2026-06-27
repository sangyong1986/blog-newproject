from flask import Flask, render_template
import os

app = Flask(__name__, template_folder="templates")

posts = [
    {"id": 1, "category": "INTERIOR", "tag": "홈인테리어", "title": "작은 공간을 넓게 쓰는 인테리어 꿀팁", "date": "2025.06.20", "summary": "화이트 톤과 미니멀한 가구 배치로 좁은 방도 넓어 보이게 만드는 방법을 소개해요.", "image": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=600&q=80"},
    {"id": 2, "category": "INTERIOR", "tag": "룸/DIY", "title": "주말에 뚝딱! 셀프 선반 만들기 도전기", "date": "2025.06.15", "summary": "5만원도 안 되는 재료비로 거실 벽을 가득 채운 책장을 직접 만들었어요.", "image": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=600&q=80"},
    {"id": 3, "category": "DAILY", "tag": "일상", "title": "요즘 내 아침 루틴 — 커피 한 잔과 함께", "date": "2025.06.10", "summary": "바쁜 하루를 시작하기 전, 조용한 아침 시간이 얼마나 소중한지 새삼 느끼고 있어요.", "image": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=600&q=80"},
    {"id": 4, "category": "INTERIOR", "tag": "인테리어 아이템", "title": "올해 가장 잘 산 소품 TOP 5", "date": "2025.06.05", "summary": "집 분위기를 확 바꿔준 소품들을 솔직하게 리뷰해봤어요.", "image": "https://images.unsplash.com/photo-1416339442236-8ceb164046f8?w=600&q=80"},
    {"id": 5, "category": "ETC", "tag": "생활정보/리뷰", "title": "이케아 vs 다이소 수납용품 비교 리뷰", "date": "2025.05.28", "summary": "가격 차이만큼 퀄리티 차이가 날까요? 직접 써보고 솔직하게 비교해봤어요.", "image": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600&q=80"},
    {"id": 6, "category": "DAILY", "tag": "일상", "title": "새 식물 들였어요 — 몬스테라 키우기 시작", "date": "2025.05.20", "summary": "드디어 몬스테라를 집에 들였어요! 공간이 확 살아나는 느낌이 들더라고요.", "image": "https://images.unsplash.com/photo-1463936575829-25148e1db1b8?w=600&q=80"},
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts, active_category=None)

@app.route("/post/<int:post_id>")
def post(post_id):
    found = next((p for p in posts if p["id"] == post_id), None)
    if not found:
        return "포스트를 찾을 수 없어요", 404
    return render_template("post.html", post=found)

@app.route("/category/<name>")
def category(name):
    filtered = [p for p in posts if p["category"] == name.upper()]
    return render_template("index.html", posts=filtered, active_category=name.upper())

if __name__ == "__main__":
    app.run(debug=True)
