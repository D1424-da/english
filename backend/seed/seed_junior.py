"""
中学レベル基本文法問題シードスクリプト
既存データを消さずに追加のみ行う。

実行:
  cd backend && python -m seed.seed_junior
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal, engine, Base
from app.models import Category, Unit, Question, Choice

Base.metadata.create_all(bind=engine)

JUNIOR_CATEGORY = {"name": "基本文型", "layer_id": 2, "order_priority": -1}

JUNIOR_UNITS = [
    {"code": "JG-001", "name": "be動詞", "order_priority": 1,
     "description": "am, is, are の使い分けと基本文型"},
    {"code": "JG-002", "name": "一般動詞", "order_priority": 2,
     "description": "一般動詞の肯定文・否定文・疑問文"},
    {"code": "JG-003", "name": "疑問詞", "order_priority": 3,
     "description": "what, who, where, when, why, how の使い方"},
    {"code": "JG-004", "name": "代名詞", "order_priority": 4,
     "description": "人称代名詞の主格・目的格・所有格"},
    {"code": "JG-005", "name": "前置詞", "order_priority": 5,
     "description": "in, on, at, to, for などの基本前置詞"},
    {"code": "JG-006", "name": "接続詞", "order_priority": 6,
     "description": "and, but, or, because, when, if などの接続詞"},
]

# fmt: off
JUNIOR_QUESTIONS = {
    # =========================================================================
    # be動詞 (JG-001) — 中1レベル
    # =========================================================================
    "JG-001": [
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な語を選びなさい。\n\nI (    ) a student.",
         "explanation": "主語が I のとき、be動詞は am を使います。",
         "choices": [
             {"text": "am", "correct": True, "order": 1},
             {"text": "is", "correct": False, "order": 2},
             {"text": "are", "correct": False, "order": 3},
             {"text": "be", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な語を選びなさい。\n\nThey (    ) from Canada.",
         "explanation": "主語が They（複数）のとき、be動詞は are を使います。",
         "choices": [
             {"text": "are", "correct": True, "order": 1},
             {"text": "is", "correct": False, "order": 2},
             {"text": "am", "correct": False, "order": 3},
             {"text": "was", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の英文を否定文にしたとき、正しいものを選びなさい。\n\nShe is happy.",
         "explanation": "be動詞の否定文は be動詞の後に not を置きます。She is not happy. が正解です。",
         "choices": [
             {"text": "She is not happy.", "correct": True, "order": 1},
             {"text": "She not is happy.", "correct": False, "order": 2},
             {"text": "She does not happy.", "correct": False, "order": 3},
             {"text": "She not happy.", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な語を選びなさい。\n\n(    ) you a teacher? — Yes, I am.",
         "explanation": "be動詞の疑問文は be動詞を主語の前に出します。Are you ...? が正解です。",
         "choices": [
             {"text": "Are", "correct": True, "order": 1},
             {"text": "Do", "correct": False, "order": 2},
             {"text": "Is", "correct": False, "order": 3},
             {"text": "Am", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な語を選びなさい。\n\nThis (    ) my pen.",
         "explanation": "主語が This（単数）のとき、be動詞は is を使います。",
         "choices": [
             {"text": "is", "correct": True, "order": 1},
             {"text": "are", "correct": False, "order": 2},
             {"text": "am", "correct": False, "order": 3},
             {"text": "do", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な語を選びなさい。\n\nTom and I (    ) good friends.",
         "explanation": "主語が Tom and I（複数）のとき、be動詞は are を使います。",
         "choices": [
             {"text": "are", "correct": True, "order": 1},
             {"text": "is", "correct": False, "order": 2},
             {"text": "am", "correct": False, "order": 3},
             {"text": "was", "correct": False, "order": 4},
         ]},
    ],

    # =========================================================================
    # 一般動詞 (JG-002) — 中1レベル
    # =========================================================================
    "JG-002": [
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な語を選びなさい。\n\nShe (    ) English every day.",
         "explanation": "三人称単数（She）の現在形では動詞に -s をつけます。studies が正解です。",
         "choices": [
             {"text": "studies", "correct": True, "order": 1},
             {"text": "study", "correct": False, "order": 2},
             {"text": "studying", "correct": False, "order": 3},
             {"text": "studied", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の英文を否定文にしたとき、正しいものを選びなさい。\n\nI like cats.",
         "explanation": "一般動詞の否定文は do not（don't）+ 動詞原形です。",
         "choices": [
             {"text": "I don't like cats.", "correct": True, "order": 1},
             {"text": "I am not like cats.", "correct": False, "order": 2},
             {"text": "I not like cats.", "correct": False, "order": 3},
             {"text": "I don't likes cats.", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の英文を疑問文にしたとき、正しいものを選びなさい。\n\nHe plays soccer.",
         "explanation": "三人称単数の疑問文は Does + 主語 + 動詞原形 です。動詞は原形に戻ります。",
         "choices": [
             {"text": "Does he play soccer?", "correct": True, "order": 1},
             {"text": "Do he plays soccer?", "correct": False, "order": 2},
             {"text": "Is he play soccer?", "correct": False, "order": 3},
             {"text": "Does he plays soccer?", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な語を選びなさい。\n\nWe (    ) to school by bus.",
         "explanation": "主語が We（一人称複数）のとき、動詞は原形のままです。go が正解です。",
         "choices": [
             {"text": "go", "correct": True, "order": 1},
             {"text": "goes", "correct": False, "order": 2},
             {"text": "going", "correct": False, "order": 3},
             {"text": "gone", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な語を選びなさい。\n\nMy mother (    ) breakfast every morning.",
         "explanation": "三人称単数（My mother）の現在形では makes となります。make → makes",
         "choices": [
             {"text": "makes", "correct": True, "order": 1},
             {"text": "make", "correct": False, "order": 2},
             {"text": "making", "correct": False, "order": 3},
             {"text": "is make", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な語句を選びなさい。\n\n(    ) you have any brothers? — Yes, I do.",
         "explanation": "一般動詞 have の疑問文は Do you have ...? です。",
         "choices": [
             {"text": "Do", "correct": True, "order": 1},
             {"text": "Are", "correct": False, "order": 2},
             {"text": "Does", "correct": False, "order": 3},
             {"text": "Is", "correct": False, "order": 4},
         ]},
    ],

    # =========================================================================
    # 疑問詞 (JG-003) — 中1〜中2レベル
    # =========================================================================
    "JG-003": [
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な疑問詞を選びなさい。\n\n(    ) is your birthday? — It's March 5th.",
         "explanation": "日付を聞いているので When（いつ）が正解です。",
         "choices": [
             {"text": "When", "correct": True, "order": 1},
             {"text": "What", "correct": False, "order": 2},
             {"text": "Where", "correct": False, "order": 3},
             {"text": "Who", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な疑問詞を選びなさい。\n\n(    ) lives in that house? — Mr. Yamada does.",
         "explanation": "人を聞いているので Who（誰）が正解です。Who が主語のとき do/does は不要です。",
         "choices": [
             {"text": "Who", "correct": True, "order": 1},
             {"text": "What", "correct": False, "order": 2},
             {"text": "Where", "correct": False, "order": 3},
             {"text": "Which", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な疑問詞を選びなさい。\n\n(    ) do you go to school? — By bicycle.",
         "explanation": "交通手段を聞いているので How（どのように）が正解です。",
         "choices": [
             {"text": "How", "correct": True, "order": 1},
             {"text": "What", "correct": False, "order": 2},
             {"text": "Why", "correct": False, "order": 3},
             {"text": "Where", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な疑問詞を選びなさい。\n\n(    ) is your favorite subject? — I like science.",
         "explanation": "「あなたの好きな教科は何ですか」と聞いているので What が正解です。",
         "choices": [
             {"text": "What", "correct": True, "order": 1},
             {"text": "Who", "correct": False, "order": 2},
             {"text": "How", "correct": False, "order": 3},
             {"text": "Which", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な疑問詞を選びなさい。\n\n(    ) did you go yesterday? — I went to the park.",
         "explanation": "場所を聞いているので Where（どこ）が正解です。",
         "choices": [
             {"text": "Where", "correct": True, "order": 1},
             {"text": "When", "correct": False, "order": 2},
             {"text": "What", "correct": False, "order": 3},
             {"text": "Why", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な疑問詞を選びなさい。\n\n(    ) are you late? — Because I missed the bus.",
         "explanation": "理由を聞いているので Why（なぜ）が正解です。Because で答えています。",
         "choices": [
             {"text": "Why", "correct": True, "order": 1},
             {"text": "How", "correct": False, "order": 2},
             {"text": "When", "correct": False, "order": 3},
             {"text": "What", "correct": False, "order": 4},
         ]},
    ],

    # =========================================================================
    # 代名詞 (JG-004) — 中1〜中2レベル
    # =========================================================================
    "JG-004": [
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な語を選びなさい。\n\nI know that boy. (    ) name is Ken.",
         "explanation": "「彼の名前」なので所有格の His が正解です。",
         "choices": [
             {"text": "His", "correct": True, "order": 1},
             {"text": "He", "correct": False, "order": 2},
             {"text": "Him", "correct": False, "order": 3},
             {"text": "Her", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な語を選びなさい。\n\nPlease give this book to (    ).",
         "explanation": "前置詞 to の後は目的格を使います。「彼女に」なので her が正解です。",
         "choices": [
             {"text": "her", "correct": True, "order": 1},
             {"text": "she", "correct": False, "order": 2},
             {"text": "hers", "correct": False, "order": 3},
             {"text": "herself", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な語を選びなさい。\n\nThis pen is (    ). It's not yours.",
         "explanation": "「私のもの」という所有代名詞は mine です。",
         "choices": [
             {"text": "mine", "correct": True, "order": 1},
             {"text": "my", "correct": False, "order": 2},
             {"text": "me", "correct": False, "order": 3},
             {"text": "I", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な語を選びなさい。\n\n(    ) like playing tennis.",
         "explanation": "主語なので主格の They が正解です。",
         "choices": [
             {"text": "They", "correct": True, "order": 1},
             {"text": "Them", "correct": False, "order": 2},
             {"text": "Their", "correct": False, "order": 3},
             {"text": "Theirs", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な語を選びなさい。\n\nMy sister and I love (    ) parents.",
         "explanation": "「私たちの両親」なので所有格の our が正解です。",
         "choices": [
             {"text": "our", "correct": True, "order": 1},
             {"text": "us", "correct": False, "order": 2},
             {"text": "we", "correct": False, "order": 3},
             {"text": "ours", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な語を選びなさい。\n\nThe teacher told (    ) to be quiet.",
         "explanation": "動詞 told の目的語なので目的格の us が正解です。",
         "choices": [
             {"text": "us", "correct": True, "order": 1},
             {"text": "we", "correct": False, "order": 2},
             {"text": "our", "correct": False, "order": 3},
             {"text": "ours", "correct": False, "order": 4},
         ]},
    ],

    # =========================================================================
    # 前置詞 (JG-005) — 中2レベル
    # =========================================================================
    "JG-005": [
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な前置詞を選びなさい。\n\nI get up (    ) seven every morning.",
         "explanation": "時刻の前には at を使います。at seven = 7時に",
         "choices": [
             {"text": "at", "correct": True, "order": 1},
             {"text": "in", "correct": False, "order": 2},
             {"text": "on", "correct": False, "order": 3},
             {"text": "to", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な前置詞を選びなさい。\n\nMy birthday is (    ) May.",
         "explanation": "月の前には in を使います。in May = 5月に",
         "choices": [
             {"text": "in", "correct": True, "order": 1},
             {"text": "on", "correct": False, "order": 2},
             {"text": "at", "correct": False, "order": 3},
             {"text": "for", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な前置詞を選びなさい。\n\nWe have a test (    ) Monday.",
         "explanation": "曜日の前には on を使います。on Monday = 月曜日に",
         "choices": [
             {"text": "on", "correct": True, "order": 1},
             {"text": "in", "correct": False, "order": 2},
             {"text": "at", "correct": False, "order": 3},
             {"text": "for", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な前置詞を選びなさい。\n\nThis present is (    ) you.",
         "explanation": "「あなたのために」は for you です。",
         "choices": [
             {"text": "for", "correct": True, "order": 1},
             {"text": "to", "correct": False, "order": 2},
             {"text": "of", "correct": False, "order": 3},
             {"text": "with", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な前置詞を選びなさい。\n\nThere is a cat (    ) the table.",
         "explanation": "「テーブルの下に」は under the table です。",
         "choices": [
             {"text": "under", "correct": True, "order": 1},
             {"text": "on", "correct": False, "order": 2},
             {"text": "at", "correct": False, "order": 3},
             {"text": "to", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な前置詞を選びなさい。\n\nShe went to school (    ) her friend.",
         "explanation": "「友達と一緒に」は with her friend です。",
         "choices": [
             {"text": "with", "correct": True, "order": 1},
             {"text": "for", "correct": False, "order": 2},
             {"text": "by", "correct": False, "order": 3},
             {"text": "from", "correct": False, "order": 4},
         ]},
    ],

    # =========================================================================
    # 接続詞 (JG-006) — 中2〜中3レベル
    # =========================================================================
    "JG-006": [
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な接続詞を選びなさい。\n\nI was hungry, (    ) I ate lunch.",
         "explanation": "「おなかがすいていた、だから昼食を食べた」と因果関係を表すので so が正解です。",
         "choices": [
             {"text": "so", "correct": True, "order": 1},
             {"text": "but", "correct": False, "order": 2},
             {"text": "or", "correct": False, "order": 3},
             {"text": "if", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な接続詞を選びなさい。\n\nI like dogs, (    ) my sister likes cats.",
         "explanation": "「私は犬が好き、しかし姉は猫が好き」と対比しているので but が正解です。",
         "choices": [
             {"text": "but", "correct": True, "order": 1},
             {"text": "and", "correct": False, "order": 2},
             {"text": "so", "correct": False, "order": 3},
             {"text": "because", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な接続詞を選びなさい。\n\nI stayed home (    ) it was raining.",
         "explanation": "「雨が降っていたので家にいた」と理由を述べているので because が正解です。",
         "choices": [
             {"text": "because", "correct": True, "order": 1},
             {"text": "but", "correct": False, "order": 2},
             {"text": "or", "correct": False, "order": 3},
             {"text": "and", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な接続詞を選びなさい。\n\n(    ) you finish your homework, you can play games.",
         "explanation": "「宿題を終えたら（〜の時）」という条件・時を表すので When が正解です。",
         "choices": [
             {"text": "When", "correct": True, "order": 1},
             {"text": "But", "correct": False, "order": 2},
             {"text": "Or", "correct": False, "order": 3},
             {"text": "So", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の空所に入る最も適切な接続詞を選びなさい。\n\nWould you like tea (    ) coffee?",
         "explanation": "「紅茶かコーヒー」と選択肢を提示しているので or が正解です。",
         "choices": [
             {"text": "or", "correct": True, "order": 1},
             {"text": "and", "correct": False, "order": 2},
             {"text": "but", "correct": False, "order": 3},
             {"text": "so", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の空所に入る最も適切な接続詞を選びなさい。\n\n(    ) it rains tomorrow, the game will be canceled.",
         "explanation": "「もし明日雨が降ったら」という条件を表すので If が正解です。",
         "choices": [
             {"text": "If", "correct": True, "order": 1},
             {"text": "Because", "correct": False, "order": 2},
             {"text": "Though", "correct": False, "order": 3},
             {"text": "Until", "correct": False, "order": 4},
         ]},
    ],
}
# fmt: on


def seed_junior():
    db = SessionLocal()
    try:
        existing_cats = {row[0] for row in db.query(Category.name).all()}
        if JUNIOR_CATEGORY["name"] not in existing_cats:
            cat = Category(**JUNIOR_CATEGORY)
            db.add(cat)
            db.flush()
            cat_id = cat.id
            db.commit()
            print(f"Added category: {JUNIOR_CATEGORY['name']} (id={cat_id})")
        else:
            cat = db.query(Category).filter(Category.name == JUNIOR_CATEGORY["name"]).first()
            cat_id = cat.id
            print(f"Category '{JUNIOR_CATEGORY['name']}' already exists (id={cat_id})")

        existing_unit_codes = {row[0] for row in db.query(Unit.code).all()}
        unit_code_to_id = {}
        new_unit_count = 0

        for u_data in JUNIOR_UNITS:
            if u_data["code"] in existing_unit_codes:
                unit = db.query(Unit).filter(Unit.code == u_data["code"]).first()
                unit_code_to_id[u_data["code"]] = unit.id
                continue

            unit = Unit(
                code=u_data["code"],
                name=u_data["name"],
                category_id=cat_id,
                order_priority=u_data["order_priority"],
                description=u_data["description"],
            )
            db.add(unit)
            db.flush()
            unit_code_to_id[u_data["code"]] = unit.id
            new_unit_count += 1

        db.commit()
        if new_unit_count > 0:
            print(f"Added {new_unit_count} new junior grammar units")

        existing_texts = {row[0] for row in db.query(Question.question_text).all()}
        new_q_count = 0

        for unit_code, questions in JUNIOR_QUESTIONS.items():
            unit_id = unit_code_to_id.get(unit_code)
            if not unit_id:
                print(f"WARNING: Unit {unit_code} not found, skipping")
                continue

            for q_data in questions:
                if q_data["question_text"] in existing_texts:
                    continue

                question = Question(
                    unit_id=unit_id,
                    question_text=q_data["question_text"],
                    difficulty=q_data["difficulty"],
                    explanation=q_data["explanation"],
                )
                db.add(question)
                db.flush()

                for c_data in q_data["choices"]:
                    choice = Choice(
                        question_id=question.id,
                        choice_text=c_data["text"],
                        is_correct=c_data["correct"],
                        choice_order=c_data["order"],
                    )
                    db.add(choice)
                new_q_count += 1

        db.commit()
        if new_q_count > 0:
            print(f"Added {new_q_count} new junior grammar questions")
        else:
            print("No new junior grammar questions to add.")

        print(f"\nJunior seed status:")
        print(f"  Total Units: {db.query(Unit).count()}")
        print(f"  Total Questions: {db.query(Question).count()}")

    finally:
        db.close()


if __name__ == "__main__":
    seed_junior()
