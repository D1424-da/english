"""
シードデータ投入スクリプト
実行: cd backend && source venv/bin/activate && python -m seed.seed_data
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal, engine, Base
from app.models import Layer, Category, Unit, Question, Choice

Base.metadata.create_all(bind=engine)

LAYERS = [
    {"id": 1, "name": "知識", "description": "語彙・品詞・基本ルールの知識", "order_priority": 1},
    {"id": 2, "name": "文構造", "description": "時制・態・文型など英文の構造理解", "order_priority": 2},
    {"id": 3, "name": "読解基礎", "description": "短文読解・文脈理解の基礎", "order_priority": 3},
    {"id": 4, "name": "読解応用", "description": "長文読解・推論・要約", "order_priority": 4},
    {"id": 5, "name": "表現", "description": "英作文・表現力", "order_priority": 5},
]

CATEGORIES = [
    {"id": 1, "name": "語彙", "layer_id": 1, "order_priority": 1},
    {"id": 2, "name": "品詞", "layer_id": 1, "order_priority": 2},
    {"id": 3, "name": "時制", "layer_id": 2, "order_priority": 1},
    {"id": 4, "name": "態", "layer_id": 2, "order_priority": 2},
    {"id": 5, "name": "助動詞", "layer_id": 2, "order_priority": 3},
    {"id": 6, "name": "不定詞・動名詞", "layer_id": 2, "order_priority": 4},
    {"id": 7, "name": "関係詞", "layer_id": 2, "order_priority": 5},
    {"id": 8, "name": "比較", "layer_id": 2, "order_priority": 6},
    {"id": 9, "name": "仮定法", "layer_id": 2, "order_priority": 7},
    {"id": 10, "name": "短文読解", "layer_id": 3, "order_priority": 1},
    {"id": 11, "name": "長文読解", "layer_id": 4, "order_priority": 1},
    {"id": 12, "name": "英作文", "layer_id": 5, "order_priority": 1},
]

UNITS = [
    # 層1: 知識
    {"id": 1, "code": "KN-001", "name": "基本語彙（中学復習）", "category_id": 1, "order_priority": 1,
     "description": "中学レベルの基本英単語の意味と用法"},
    {"id": 2, "code": "KN-002", "name": "高校基礎語彙", "category_id": 1, "order_priority": 2,
     "description": "高校1年レベルの基礎単語"},
    {"id": 3, "code": "KN-003", "name": "品詞の識別", "category_id": 2, "order_priority": 1,
     "description": "名詞・動詞・形容詞・副詞の識別"},
    {"id": 4, "code": "KN-004", "name": "品詞の働き", "category_id": 2, "order_priority": 2,
     "description": "文中での品詞の役割を理解する"},
    # 層2: 文構造
    {"id": 5, "code": "TS-001", "name": "現在形", "category_id": 3, "order_priority": 1,
     "description": "現在形の用法と三人称単数"},
    {"id": 6, "code": "TS-002", "name": "過去形", "category_id": 3, "order_priority": 2,
     "description": "過去形（規則変化・不規則変化）"},
    {"id": 7, "code": "TS-003", "name": "現在完了形", "category_id": 3, "order_priority": 3,
     "description": "現在完了形の3用法（完了・経験・継続）"},
    {"id": 8, "code": "TS-004", "name": "過去完了形", "category_id": 3, "order_priority": 4,
     "description": "過去完了形の用法"},
    {"id": 9, "code": "TS-005", "name": "進行形", "category_id": 3, "order_priority": 5,
     "description": "現在進行形・過去進行形"},
    {"id": 10, "code": "TS-006", "name": "未来表現", "category_id": 3, "order_priority": 6,
     "description": "will / be going to の使い分け"},
    {"id": 11, "code": "VO-001", "name": "受動態の基本", "category_id": 4, "order_priority": 1,
     "description": "能動態から受動態への変換"},
    {"id": 12, "code": "VO-002", "name": "受動態の応用", "category_id": 4, "order_priority": 2,
     "description": "SVOO, SVOCの受動態"},
    {"id": 13, "code": "MD-001", "name": "助動詞の基本", "category_id": 5, "order_priority": 1,
     "description": "can, may, must, should の基本用法"},
    {"id": 14, "code": "MD-002", "name": "助動詞の応用", "category_id": 5, "order_priority": 2,
     "description": "助動詞 + have + 過去分詞"},
    {"id": 15, "code": "IF-001", "name": "不定詞の名詞的用法", "category_id": 6, "order_priority": 1,
     "description": "to不定詞の名詞的用法"},
    {"id": 16, "code": "IF-002", "name": "不定詞の形容詞的・副詞的用法", "category_id": 6, "order_priority": 2,
     "description": "to不定詞の形容詞的・副詞的用法"},
    {"id": 17, "code": "IF-003", "name": "動名詞", "category_id": 6, "order_priority": 3,
     "description": "動名詞の用法とto不定詞との使い分け"},
    {"id": 18, "code": "RL-001", "name": "関係代名詞", "category_id": 7, "order_priority": 1,
     "description": "who, which, that の使い分け"},
    {"id": 19, "code": "RL-002", "name": "関係副詞", "category_id": 7, "order_priority": 2,
     "description": "where, when, why, how の用法"},
    {"id": 20, "code": "CP-001", "name": "比較の基本", "category_id": 8, "order_priority": 1,
     "description": "原級・比較級・最上級の基本"},
    {"id": 21, "code": "CP-002", "name": "比較の応用表現", "category_id": 8, "order_priority": 2,
     "description": "no more than, as...as 等の慣用表現"},
    {"id": 22, "code": "SB-001", "name": "仮定法過去", "category_id": 9, "order_priority": 1,
     "description": "現在の事実に反する仮定"},
    {"id": 23, "code": "SB-002", "name": "仮定法過去完了", "category_id": 9, "order_priority": 2,
     "description": "過去の事実に反する仮定"},
]

QUESTIONS = [
    # --- 層1: 語彙 ---
    {
        "unit_id": 1, "difficulty": 1,
        "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「important」",
        "explanation": "important は「重要な」という意味の形容詞です。",
        "choices": [
            {"text": "重要な", "correct": True, "order": 1},
            {"text": "面白い", "correct": False, "order": 2},
            {"text": "難しい", "correct": False, "order": 3},
            {"text": "美しい", "correct": False, "order": 4},
        ],
    },
    {
        "unit_id": 1, "difficulty": 1,
        "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「necessary」",
        "explanation": "necessary は「必要な」という意味の形容詞です。",
        "choices": [
            {"text": "自然な", "correct": False, "order": 1},
            {"text": "必要な", "correct": True, "order": 2},
            {"text": "簡単な", "correct": False, "order": 3},
            {"text": "特別な", "correct": False, "order": 4},
        ],
    },
    {
        "unit_id": 2, "difficulty": 1,
        "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「attitude」",
        "explanation": "attitude は「態度、姿勢」という意味の名詞です。altitude（高度）と間違えやすいので注意。",
        "choices": [
            {"text": "高度", "correct": False, "order": 1},
            {"text": "感謝", "correct": False, "order": 2},
            {"text": "態度", "correct": True, "order": 3},
            {"text": "適性", "correct": False, "order": 4},
        ],
    },
    {
        "unit_id": 2, "difficulty": 2,
        "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「significant」",
        "explanation": "significant は「重要な、意味のある」という意味の形容詞です。名詞形は significance。",
        "choices": [
            {"text": "重要な", "correct": True, "order": 1},
            {"text": "信号の", "correct": False, "order": 2},
            {"text": "署名する", "correct": False, "order": 3},
            {"text": "静かな", "correct": False, "order": 4},
        ],
    },
    # --- 層1: 品詞 ---
    {
        "unit_id": 3, "difficulty": 1,
        "question_text": "次の文で下線部の品詞は何ですか？\n\n「She speaks English _fluently_.」",
        "explanation": "fluently は speak（動詞）を修飾する副詞です。-ly で終わる語は副詞であることが多いです。",
        "choices": [
            {"text": "名詞", "correct": False, "order": 1},
            {"text": "形容詞", "correct": False, "order": 2},
            {"text": "副詞", "correct": True, "order": 3},
            {"text": "動詞", "correct": False, "order": 4},
        ],
    },
    {
        "unit_id": 3, "difficulty": 1,
        "question_text": "次の語のうち、形容詞はどれですか？",
        "explanation": "beautiful は「美しい」という意味の形容詞です。beauty(名詞), beautify(動詞), beautifully(副詞)と区別しましょう。",
        "choices": [
            {"text": "beauty", "correct": False, "order": 1},
            {"text": "beautiful", "correct": True, "order": 2},
            {"text": "beautifully", "correct": False, "order": 3},
            {"text": "beautify", "correct": False, "order": 4},
        ],
    },
    # --- 層2: 時制 ---
    {
        "unit_id": 5, "difficulty": 1,
        "question_text": "空所に入る最も適切な語を選びなさい。\n\n「She ___ to school every day.」",
        "explanation": "主語が She（三人称単数）で、every day は習慣を表すため、現在形の goes が正解です。",
        "choices": [
            {"text": "go", "correct": False, "order": 1},
            {"text": "goes", "correct": True, "order": 2},
            {"text": "going", "correct": False, "order": 3},
            {"text": "went", "correct": False, "order": 4},
        ],
    },
    {
        "unit_id": 5, "difficulty": 1,
        "question_text": "空所に入る最も適切な語を選びなさい。\n\n「Water ___ at 100 degrees Celsius.」",
        "explanation": "科学的事実や一般的真理は現在形で表します。Water は三人称単数なので boils が正解。",
        "choices": [
            {"text": "boil", "correct": False, "order": 1},
            {"text": "boils", "correct": True, "order": 2},
            {"text": "is boiling", "correct": False, "order": 3},
            {"text": "boiled", "correct": False, "order": 4},
        ],
    },
    {
        "unit_id": 6, "difficulty": 1,
        "question_text": "空所に入る最も適切な語を選びなさい。\n\n「I ___ the movie last night.」",
        "explanation": "last night は過去の時点を示すので、過去形の watched が正解です。",
        "choices": [
            {"text": "watch", "correct": False, "order": 1},
            {"text": "watches", "correct": False, "order": 2},
            {"text": "watched", "correct": True, "order": 3},
            {"text": "have watched", "correct": False, "order": 4},
        ],
    },
    {
        "unit_id": 6, "difficulty": 2,
        "question_text": "空所に入る最も適切な語を選びなさい。\n\n「They ___ to Paris two years ago.」",
        "explanation": "two years ago は明確な過去の時点を示すので、過去形の went が正解です。have been は現在完了形で ago とは一緒に使えません。",
        "choices": [
            {"text": "go", "correct": False, "order": 1},
            {"text": "have been", "correct": False, "order": 2},
            {"text": "have gone", "correct": False, "order": 3},
            {"text": "went", "correct": True, "order": 4},
        ],
    },
    {
        "unit_id": 7, "difficulty": 2,
        "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I ___ in Tokyo for five years.」（今も住んでいる）",
        "explanation": "「5年間住んでいる（今も継続中）」は現在完了形の継続用法で表します。for five years は期間を表す語句です。",
        "choices": [
            {"text": "live", "correct": False, "order": 1},
            {"text": "lived", "correct": False, "order": 2},
            {"text": "have lived", "correct": True, "order": 3},
            {"text": "had lived", "correct": False, "order": 4},
        ],
    },
    {
        "unit_id": 7, "difficulty": 2,
        "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I ___ sushi before.」（寿司を食べたことがある）",
        "explanation": "「～したことがある」は現在完了形の経験用法です。before は経験用法でよく使われる語です。",
        "choices": [
            {"text": "eat", "correct": False, "order": 1},
            {"text": "ate", "correct": False, "order": 2},
            {"text": "have eaten", "correct": True, "order": 3},
            {"text": "had eaten", "correct": False, "order": 4},
        ],
    },
    {
        "unit_id": 7, "difficulty": 2,
        "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「He ___ just ___ his homework.」（宿題を終えたところだ）",
        "explanation": "「ちょうど～したところだ」は現在完了形の完了用法です。just は have と過去分詞の間に入ります。",
        "choices": [
            {"text": "is ... finishing", "correct": False, "order": 1},
            {"text": "has ... finished", "correct": True, "order": 2},
            {"text": "had ... finished", "correct": False, "order": 3},
            {"text": "was ... finishing", "correct": False, "order": 4},
        ],
    },
    # --- 層2: 受動態 ---
    {
        "unit_id": 11, "difficulty": 1,
        "question_text": "次の文を受動態に変えた場合、正しいものはどれですか？\n\n「Tom wrote this letter.」",
        "explanation": "能動態の目的語 this letter が受動態の主語になります。過去形の受動態は was/were + 過去分詞。",
        "choices": [
            {"text": "This letter is written by Tom.", "correct": False, "order": 1},
            {"text": "This letter was written by Tom.", "correct": True, "order": 2},
            {"text": "This letter has been written by Tom.", "correct": False, "order": 3},
            {"text": "This letter wrote by Tom.", "correct": False, "order": 4},
        ],
    },
    {
        "unit_id": 11, "difficulty": 2,
        "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「English ___ in many countries.」",
        "explanation": "「英語は多くの国で話されている」という一般的事実は、現在形の受動態で表します。",
        "choices": [
            {"text": "speaks", "correct": False, "order": 1},
            {"text": "is spoken", "correct": True, "order": 2},
            {"text": "spoke", "correct": False, "order": 3},
            {"text": "was spoken", "correct": False, "order": 4},
        ],
    },
    # --- 層2: 助動詞 ---
    {
        "unit_id": 13, "difficulty": 1,
        "question_text": "空所に入る最も適切な語を選びなさい。\n\n「You ___ not park here.」（ここに駐車してはいけない）",
        "explanation": "「～してはいけない」という禁止は must not で表します。",
        "choices": [
            {"text": "can", "correct": False, "order": 1},
            {"text": "must", "correct": True, "order": 2},
            {"text": "should", "correct": False, "order": 3},
            {"text": "may", "correct": False, "order": 4},
        ],
    },
    {
        "unit_id": 13, "difficulty": 1,
        "question_text": "空所に入る最も適切な語を選びなさい。\n\n「___ I use your phone?」（電話を使ってもいいですか？）",
        "explanation": "許可を求める丁寧な表現は May I ...? です。Can I ...? よりもフォーマルです。",
        "choices": [
            {"text": "Must", "correct": False, "order": 1},
            {"text": "Should", "correct": False, "order": 2},
            {"text": "May", "correct": True, "order": 3},
            {"text": "Will", "correct": False, "order": 4},
        ],
    },
    # --- 層2: 不定詞・動名詞 ---
    {
        "unit_id": 15, "difficulty": 1,
        "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I want ___ a doctor.」",
        "explanation": "want は不定詞（to + 動詞の原形）を目的語にとる動詞です。want + -ing の形はありません。",
        "choices": [
            {"text": "be", "correct": False, "order": 1},
            {"text": "to be", "correct": True, "order": 2},
            {"text": "being", "correct": False, "order": 3},
            {"text": "been", "correct": False, "order": 4},
        ],
    },
    {
        "unit_id": 17, "difficulty": 2,
        "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I enjoy ___ books.」",
        "explanation": "enjoy は動名詞（-ing形）を目的語にとる動詞です。enjoy to do の形は使えません。",
        "choices": [
            {"text": "read", "correct": False, "order": 1},
            {"text": "to read", "correct": False, "order": 2},
            {"text": "reading", "correct": True, "order": 3},
            {"text": "to reading", "correct": False, "order": 4},
        ],
    },
    # --- 層2: 関係詞 ---
    {
        "unit_id": 18, "difficulty": 2,
        "question_text": "空所に入る最も適切な関係代名詞を選びなさい。\n\n「The man ___ lives next door is a teacher.」",
        "explanation": "先行詞 The man は人で、関係詞節内で主語の役割を果たすので、who が正解です。",
        "choices": [
            {"text": "who", "correct": True, "order": 1},
            {"text": "which", "correct": False, "order": 2},
            {"text": "whom", "correct": False, "order": 3},
            {"text": "whose", "correct": False, "order": 4},
        ],
    },
    {
        "unit_id": 18, "difficulty": 2,
        "question_text": "空所に入る最も適切な関係代名詞を選びなさい。\n\n「This is the book ___ I bought yesterday.」",
        "explanation": "先行詞 the book は物で、関係詞節内で bought の目的語の役割です。物の場合は which か that を使います。",
        "choices": [
            {"text": "who", "correct": False, "order": 1},
            {"text": "which", "correct": True, "order": 2},
            {"text": "whose", "correct": False, "order": 3},
            {"text": "whom", "correct": False, "order": 4},
        ],
    },
    # --- 層2: 比較 ---
    {
        "unit_id": 20, "difficulty": 1,
        "question_text": "空所に入る最も適切な語を選びなさい。\n\n「Tom is ___ than his brother.」",
        "explanation": "than があるので比較級を使います。tall の比較級は taller です。",
        "choices": [
            {"text": "tall", "correct": False, "order": 1},
            {"text": "taller", "correct": True, "order": 2},
            {"text": "tallest", "correct": False, "order": 3},
            {"text": "more tall", "correct": False, "order": 4},
        ],
    },
    {
        "unit_id": 20, "difficulty": 2,
        "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「This problem is ___ difficult than that one.」",
        "explanation": "difficult は長い形容詞なので、比較級は more difficult です。difficulter とは言いません。",
        "choices": [
            {"text": "difficulter", "correct": False, "order": 1},
            {"text": "more", "correct": True, "order": 2},
            {"text": "most", "correct": False, "order": 3},
            {"text": "much", "correct": False, "order": 4},
        ],
    },
    # --- 層2: 仮定法 ---
    {
        "unit_id": 22, "difficulty": 3,
        "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「If I ___ rich, I would travel around the world.」",
        "explanation": "仮定法過去は、現在の事実に反する仮定を表します。be動詞は主語に関わらず were を使います。",
        "choices": [
            {"text": "am", "correct": False, "order": 1},
            {"text": "was", "correct": False, "order": 2},
            {"text": "were", "correct": True, "order": 3},
            {"text": "have been", "correct": False, "order": 4},
        ],
    },
    {
        "unit_id": 22, "difficulty": 3,
        "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「If I knew his phone number, I ___ him.」",
        "explanation": "仮定法過去の帰結節は would + 動詞の原形で表します。",
        "choices": [
            {"text": "call", "correct": False, "order": 1},
            {"text": "called", "correct": False, "order": 2},
            {"text": "would call", "correct": True, "order": 3},
            {"text": "will call", "correct": False, "order": 4},
        ],
    },
]


def seed():
    db = SessionLocal()
    try:
        if db.query(Layer).count() > 0:
            print("Data already exists. Skipping seed.")
            return

        for data in LAYERS:
            db.add(Layer(**data))
        db.commit()
        print(f"Inserted {len(LAYERS)} layers")

        for data in CATEGORIES:
            db.add(Category(**data))
        db.commit()
        print(f"Inserted {len(CATEGORIES)} categories")

        for data in UNITS:
            db.add(Unit(**data))
        db.commit()
        print(f"Inserted {len(UNITS)} units")

        for q_data in QUESTIONS:
            question = Question(
                unit_id=q_data["unit_id"],
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

        db.commit()
        print(f"Inserted {len(QUESTIONS)} questions with choices")

        print("\nSeed completed successfully!")
        print(f"  Layers: {db.query(Layer).count()}")
        print(f"  Categories: {db.query(Category).count()}")
        print(f"  Units: {db.query(Unit).count()}")
        print(f"  Questions: {db.query(Question).count()}")
        print(f"  Choices: {db.query(Choice).count()}")

    finally:
        db.close()


if __name__ == "__main__":
    seed()
