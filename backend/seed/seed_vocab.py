"""
学年別語彙問題シードスクリプト（中1〜高3）
既存データを消さずに追加のみ行う。

実行:
  cd backend && python -m seed.seed_vocab
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal, engine, Base
from app.models import Layer, Category, Unit, Question, Choice

Base.metadata.create_all(bind=engine)

VOCAB_UNITS = [
    {"code": "VB-J1", "name": "中学1年 基本語彙", "category_id": 1, "order_priority": 10,
     "description": "中学1年で学ぶ基本英単語"},
    {"code": "VB-J2", "name": "中学2年 基本語彙", "category_id": 1, "order_priority": 11,
     "description": "中学2年で学ぶ英単語"},
    {"code": "VB-J3", "name": "中学3年 基本語彙", "category_id": 1, "order_priority": 12,
     "description": "中学3年・高校入試レベルの英単語"},
    {"code": "VB-H1", "name": "高校1年 語彙", "category_id": 1, "order_priority": 13,
     "description": "高校1年で学ぶ英単語"},
    {"code": "VB-H2", "name": "高校2年 語彙", "category_id": 1, "order_priority": 14,
     "description": "高校2年で学ぶ英単語"},
    {"code": "VB-H3", "name": "高校3年 語彙", "category_id": 1, "order_priority": 15,
     "description": "高校3年・大学入試レベルの英単語"},
]

# fmt: off
VOCAB_QUESTIONS = {
    # =========================================================================
    # 中学1年 基本語彙 (VB-J1)
    # =========================================================================
    "VB-J1": [
        {"difficulty": 1,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「apple」",
         "explanation": "apple は「りんご」という意味の名詞です。",
         "choices": [
             {"text": "りんご", "correct": True, "order": 1},
             {"text": "みかん", "correct": False, "order": 2},
             {"text": "ぶどう", "correct": False, "order": 3},
             {"text": "もも", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「brother」",
         "explanation": "brother は「兄弟」という意味の名詞です。",
         "choices": [
             {"text": "兄弟", "correct": True, "order": 1},
             {"text": "姉妹", "correct": False, "order": 2},
             {"text": "友達", "correct": False, "order": 3},
             {"text": "先生", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「morning」",
         "explanation": "morning は「朝」という意味の名詞です。",
         "choices": [
             {"text": "朝", "correct": True, "order": 1},
             {"text": "夜", "correct": False, "order": 2},
             {"text": "昼", "correct": False, "order": 3},
             {"text": "夕方", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「学校」",
         "explanation": "「学校」は英語で school です。",
         "choices": [
             {"text": "school", "correct": True, "order": 1},
             {"text": "store", "correct": False, "order": 2},
             {"text": "station", "correct": False, "order": 3},
             {"text": "street", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「eat」",
         "explanation": "eat は「食べる」という意味の動詞です。",
         "choices": [
             {"text": "食べる", "correct": True, "order": 1},
             {"text": "飲む", "correct": False, "order": 2},
             {"text": "走る", "correct": False, "order": 3},
             {"text": "歩く", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「大きい」",
         "explanation": "「大きい」は英語で big / large です。",
         "choices": [
             {"text": "big", "correct": True, "order": 1},
             {"text": "bad", "correct": False, "order": 2},
             {"text": "busy", "correct": False, "order": 3},
             {"text": "blue", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「happy」",
         "explanation": "happy は「幸せな、うれしい」という意味の形容詞です。",
         "choices": [
             {"text": "うれしい", "correct": True, "order": 1},
             {"text": "悲しい", "correct": False, "order": 2},
             {"text": "怒っている", "correct": False, "order": 3},
             {"text": "疲れた", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「水」",
         "explanation": "「水」は英語で water です。",
         "choices": [
             {"text": "water", "correct": True, "order": 1},
             {"text": "weather", "correct": False, "order": 2},
             {"text": "winter", "correct": False, "order": 3},
             {"text": "window", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「swim」",
         "explanation": "swim は「泳ぐ」という意味の動詞です。",
         "choices": [
             {"text": "泳ぐ", "correct": True, "order": 1},
             {"text": "走る", "correct": False, "order": 2},
             {"text": "飛ぶ", "correct": False, "order": 3},
             {"text": "踊る", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「本」",
         "explanation": "「本」は英語で book です。",
         "choices": [
             {"text": "book", "correct": True, "order": 1},
             {"text": "box", "correct": False, "order": 2},
             {"text": "bag", "correct": False, "order": 3},
             {"text": "ball", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「open」",
         "explanation": "open は「開ける、開く」という意味の動詞です。",
         "choices": [
             {"text": "開ける", "correct": True, "order": 1},
             {"text": "閉める", "correct": False, "order": 2},
             {"text": "壊す", "correct": False, "order": 3},
             {"text": "作る", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「友達」",
         "explanation": "「友達」は英語で friend です。",
         "choices": [
             {"text": "friend", "correct": True, "order": 1},
             {"text": "family", "correct": False, "order": 2},
             {"text": "father", "correct": False, "order": 3},
             {"text": "flower", "correct": False, "order": 4},
         ]},
    ],

    # =========================================================================
    # 中学2年 基本語彙 (VB-J2)
    # =========================================================================
    "VB-J2": [
        {"difficulty": 1,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「foreign」",
         "explanation": "foreign は「外国の」という意味の形容詞です。",
         "choices": [
             {"text": "外国の", "correct": True, "order": 1},
             {"text": "有名な", "correct": False, "order": 2},
             {"text": "自由な", "correct": False, "order": 3},
             {"text": "将来の", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「discover」",
         "explanation": "discover は「発見する」という意味の動詞です。",
         "choices": [
             {"text": "発見する", "correct": True, "order": 1},
             {"text": "議論する", "correct": False, "order": 2},
             {"text": "描写する", "correct": False, "order": 3},
             {"text": "破壊する", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「言語」",
         "explanation": "「言語」は英語で language です。",
         "choices": [
             {"text": "language", "correct": True, "order": 1},
             {"text": "luggage", "correct": False, "order": 2},
             {"text": "landscape", "correct": False, "order": 3},
             {"text": "laughter", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「across」",
         "explanation": "across は「〜を横切って」という意味の前置詞・副詞です。",
         "choices": [
             {"text": "〜を横切って", "correct": True, "order": 1},
             {"text": "〜の下に", "correct": False, "order": 2},
             {"text": "〜の上に", "correct": False, "order": 3},
             {"text": "〜の間に", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「決める」",
         "explanation": "「決める」は英語で decide です。",
         "choices": [
             {"text": "decide", "correct": True, "order": 1},
             {"text": "design", "correct": False, "order": 2},
             {"text": "deliver", "correct": False, "order": 3},
             {"text": "demand", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「communication」",
         "explanation": "communication は「コミュニケーション、伝達」という意味の名詞です。",
         "choices": [
             {"text": "伝達・意思疎通", "correct": True, "order": 1},
             {"text": "競争", "correct": False, "order": 2},
             {"text": "共同体", "correct": False, "order": 3},
             {"text": "祝賀", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「improve」",
         "explanation": "improve は「改善する、上達する」という意味の動詞です。",
         "choices": [
             {"text": "改善する", "correct": True, "order": 1},
             {"text": "輸入する", "correct": False, "order": 2},
             {"text": "印象づける", "correct": False, "order": 3},
             {"text": "含む", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「経験」",
         "explanation": "「経験」は英語で experience です。",
         "choices": [
             {"text": "experience", "correct": True, "order": 1},
             {"text": "experiment", "correct": False, "order": 2},
             {"text": "expression", "correct": False, "order": 3},
             {"text": "explanation", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「imagine」",
         "explanation": "imagine は「想像する」という意味の動詞です。",
         "choices": [
             {"text": "想像する", "correct": True, "order": 1},
             {"text": "管理する", "correct": False, "order": 2},
             {"text": "模倣する", "correct": False, "order": 3},
             {"text": "測定する", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「伝統」",
         "explanation": "「伝統」は英語で tradition です。",
         "choices": [
             {"text": "tradition", "correct": True, "order": 1},
             {"text": "translation", "correct": False, "order": 2},
             {"text": "transportation", "correct": False, "order": 3},
             {"text": "transaction", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「unfortunately」",
         "explanation": "unfortunately は「残念ながら」という意味の副詞です。",
         "choices": [
             {"text": "残念ながら", "correct": True, "order": 1},
             {"text": "幸運にも", "correct": False, "order": 2},
             {"text": "明らかに", "correct": False, "order": 3},
             {"text": "最終的に", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「環境」",
         "explanation": "「環境」は英語で environment です。",
         "choices": [
             {"text": "environment", "correct": True, "order": 1},
             {"text": "entertainment", "correct": False, "order": 2},
             {"text": "equipment", "correct": False, "order": 3},
             {"text": "employment", "correct": False, "order": 4},
         ]},
    ],

    # =========================================================================
    # 中学3年 基本語彙 (VB-J3)
    # =========================================================================
    "VB-J3": [
        {"difficulty": 2,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「opportunity」",
         "explanation": "opportunity は「機会」という意味の名詞です。",
         "choices": [
             {"text": "機会", "correct": True, "order": 1},
             {"text": "反対", "correct": False, "order": 2},
             {"text": "意見", "correct": False, "order": 3},
             {"text": "組織", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「society」",
         "explanation": "society は「社会」という意味の名詞です。",
         "choices": [
             {"text": "社会", "correct": True, "order": 1},
             {"text": "科学", "correct": False, "order": 2},
             {"text": "安全", "correct": False, "order": 3},
             {"text": "解決", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「影響」",
         "explanation": "「影響」は英語で influence です。affect も類義語です。",
         "choices": [
             {"text": "influence", "correct": True, "order": 1},
             {"text": "insurance", "correct": False, "order": 2},
             {"text": "intelligence", "correct": False, "order": 3},
             {"text": "independence", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「succeed」",
         "explanation": "succeed は「成功する」という意味の動詞です。名詞形は success です。",
         "choices": [
             {"text": "成功する", "correct": True, "order": 1},
             {"text": "提案する", "correct": False, "order": 2},
             {"text": "苦しむ", "correct": False, "order": 3},
             {"text": "支える", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「文化」",
         "explanation": "「文化」は英語で culture です。",
         "choices": [
             {"text": "culture", "correct": True, "order": 1},
             {"text": "creature", "correct": False, "order": 2},
             {"text": "courage", "correct": False, "order": 3},
             {"text": "capture", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「population」",
         "explanation": "population は「人口」という意味の名詞です。",
         "choices": [
             {"text": "人口", "correct": True, "order": 1},
             {"text": "汚染", "correct": False, "order": 2},
             {"text": "人気", "correct": False, "order": 3},
             {"text": "位置", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「refuse」",
         "explanation": "refuse は「断る、拒否する」という意味の動詞です。",
         "choices": [
             {"text": "断る", "correct": True, "order": 1},
             {"text": "参照する", "correct": False, "order": 2},
             {"text": "紹介する", "correct": False, "order": 3},
             {"text": "繰り返す", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「技術」",
         "explanation": "「技術」は英語で technology です。",
         "choices": [
             {"text": "technology", "correct": True, "order": 1},
             {"text": "technique", "correct": False, "order": 2},
             {"text": "territory", "correct": False, "order": 3},
             {"text": "telescope", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「government」",
         "explanation": "government は「政府」という意味の名詞です。",
         "choices": [
             {"text": "政府", "correct": True, "order": 1},
             {"text": "知事", "correct": False, "order": 2},
             {"text": "重力", "correct": False, "order": 3},
             {"text": "保証", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「増加する」",
         "explanation": "「増加する」は英語で increase です。反対語は decrease です。",
         "choices": [
             {"text": "increase", "correct": True, "order": 1},
             {"text": "include", "correct": False, "order": 2},
             {"text": "indicate", "correct": False, "order": 3},
             {"text": "involve", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「advantage」",
         "explanation": "advantage は「利点、有利」という意味の名詞です。反対語は disadvantage です。",
         "choices": [
             {"text": "利点", "correct": True, "order": 1},
             {"text": "冒険", "correct": False, "order": 2},
             {"text": "広告", "correct": False, "order": 3},
             {"text": "助言", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「発展する」",
         "explanation": "「発展する」は英語で develop です。名詞形は development です。",
         "choices": [
             {"text": "develop", "correct": True, "order": 1},
             {"text": "destroy", "correct": False, "order": 2},
             {"text": "deserve", "correct": False, "order": 3},
             {"text": "depart", "correct": False, "order": 4},
         ]},
    ],

    # =========================================================================
    # 高校1年 語彙 (VB-H1)
    # =========================================================================
    "VB-H1": [
        {"difficulty": 2,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「recognize」",
         "explanation": "recognize は「認識する、気づく」という意味の動詞です。",
         "choices": [
             {"text": "認識する", "correct": True, "order": 1},
             {"text": "推薦する", "correct": False, "order": 2},
             {"text": "記録する", "correct": False, "order": 3},
             {"text": "回復する", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「participate」",
         "explanation": "participate は「参加する」という意味の動詞です。participate in 〜 の形で使います。",
         "choices": [
             {"text": "参加する", "correct": True, "order": 1},
             {"text": "分割する", "correct": False, "order": 2},
             {"text": "準備する", "correct": False, "order": 3},
             {"text": "予測する", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「比較する」",
         "explanation": "「比較する」は英語で compare です。compare A with B の形で使います。",
         "choices": [
             {"text": "compare", "correct": True, "order": 1},
             {"text": "complete", "correct": False, "order": 2},
             {"text": "compete", "correct": False, "order": 3},
             {"text": "complain", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「appropriate」",
         "explanation": "appropriate は「適切な」という意味の形容詞です。",
         "choices": [
             {"text": "適切な", "correct": True, "order": 1},
             {"text": "おおよその", "correct": False, "order": 2},
             {"text": "感謝する", "correct": False, "order": 3},
             {"text": "明らかな", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「獲得する」",
         "explanation": "「獲得する」は英語で acquire です。",
         "choices": [
             {"text": "acquire", "correct": True, "order": 1},
             {"text": "admire", "correct": False, "order": 2},
             {"text": "achieve", "correct": False, "order": 3},
             {"text": "accuse", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「potential」",
         "explanation": "potential は「潜在的な、可能性のある」という意味の形容詞・名詞です。",
         "choices": [
             {"text": "潜在的な", "correct": True, "order": 1},
             {"text": "実用的な", "correct": False, "order": 2},
             {"text": "政治的な", "correct": False, "order": 3},
             {"text": "肯定的な", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「significant」",
         "explanation": "significant は「重要な、意味のある」という意味の形容詞です。",
         "choices": [
             {"text": "重要な", "correct": True, "order": 1},
             {"text": "単純な", "correct": False, "order": 2},
             {"text": "静かな", "correct": False, "order": 3},
             {"text": "厳格な", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「供給する」",
         "explanation": "「供給する」は英語で provide / supply です。",
         "choices": [
             {"text": "provide", "correct": True, "order": 1},
             {"text": "prevent", "correct": False, "order": 2},
             {"text": "predict", "correct": False, "order": 3},
             {"text": "pretend", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「consist」",
         "explanation": "consist は「成り立つ」という意味の動詞です。consist of 〜「〜から成る」の形でよく使います。",
         "choices": [
             {"text": "成り立つ", "correct": True, "order": 1},
             {"text": "含む", "correct": False, "order": 2},
             {"text": "同意する", "correct": False, "order": 3},
             {"text": "相談する", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「現象」",
         "explanation": "「現象」は英語で phenomenon です。複数形は phenomena です。",
         "choices": [
             {"text": "phenomenon", "correct": True, "order": 1},
             {"text": "philosophy", "correct": False, "order": 2},
             {"text": "photosynthesis", "correct": False, "order": 3},
             {"text": "philanthropy", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「consequence」",
         "explanation": "consequence は「結果、影響」という意味の名詞です。",
         "choices": [
             {"text": "結果", "correct": True, "order": 1},
             {"text": "意識", "correct": False, "order": 2},
             {"text": "合意", "correct": False, "order": 3},
             {"text": "矛盾", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「維持する」",
         "explanation": "「維持する」は英語で maintain です。",
         "choices": [
             {"text": "maintain", "correct": True, "order": 1},
             {"text": "manage", "correct": False, "order": 2},
             {"text": "manufacture", "correct": False, "order": 3},
             {"text": "modify", "correct": False, "order": 4},
         ]},
    ],

    # =========================================================================
    # 高校2年 語彙 (VB-H2)
    # =========================================================================
    "VB-H2": [
        {"difficulty": 3,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「demonstrate」",
         "explanation": "demonstrate は「証明する、実演する」という意味の動詞です。",
         "choices": [
             {"text": "証明する", "correct": True, "order": 1},
             {"text": "要求する", "correct": False, "order": 2},
             {"text": "破壊する", "correct": False, "order": 3},
             {"text": "延期する", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「perspective」",
         "explanation": "perspective は「見方、視点」という意味の名詞です。",
         "choices": [
             {"text": "見方・視点", "correct": True, "order": 1},
             {"text": "性格", "correct": False, "order": 2},
             {"text": "許可", "correct": False, "order": 3},
             {"text": "持続", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「調査する」",
         "explanation": "「調査する」は英語で investigate です。",
         "choices": [
             {"text": "investigate", "correct": True, "order": 1},
             {"text": "intimidate", "correct": False, "order": 2},
             {"text": "illuminate", "correct": False, "order": 3},
             {"text": "immigrate", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「controversy」",
         "explanation": "controversy は「論争」という意味の名詞です。controversial は形容詞形です。",
         "choices": [
             {"text": "論争", "correct": True, "order": 1},
             {"text": "便利さ", "correct": False, "order": 2},
             {"text": "会話", "correct": False, "order": 3},
             {"text": "変換", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「偏見」",
         "explanation": "「偏見」は英語で prejudice です。",
         "choices": [
             {"text": "prejudice", "correct": True, "order": 1},
             {"text": "privilege", "correct": False, "order": 2},
             {"text": "principle", "correct": False, "order": 3},
             {"text": "precedent", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「hypothesis」",
         "explanation": "hypothesis は「仮説」という意味の名詞です。複数形は hypotheses です。",
         "choices": [
             {"text": "仮説", "correct": True, "order": 1},
             {"text": "偽善", "correct": False, "order": 2},
             {"text": "催眠", "correct": False, "order": 3},
             {"text": "歴史", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「simultaneously」",
         "explanation": "simultaneously は「同時に」という意味の副詞です。",
         "choices": [
             {"text": "同時に", "correct": True, "order": 1},
             {"text": "単独で", "correct": False, "order": 2},
             {"text": "徐々に", "correct": False, "order": 3},
             {"text": "突然に", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「矛盾」",
         "explanation": "「矛盾」は英語で contradiction です。contradict は動詞形です。",
         "choices": [
             {"text": "contradiction", "correct": True, "order": 1},
             {"text": "contribution", "correct": False, "order": 2},
             {"text": "concentration", "correct": False, "order": 3},
             {"text": "constitution", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「reluctant」",
         "explanation": "reluctant は「気が進まない、しぶしぶの」という意味の形容詞です。",
         "choices": [
             {"text": "気が進まない", "correct": True, "order": 1},
             {"text": "関連した", "correct": False, "order": 2},
             {"text": "信頼できる", "correct": False, "order": 3},
             {"text": "注目すべき", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「把握する」",
         "explanation": "「把握する」は英語で grasp / comprehend です。",
         "choices": [
             {"text": "grasp", "correct": True, "order": 1},
             {"text": "grant", "correct": False, "order": 2},
             {"text": "grind", "correct": False, "order": 3},
             {"text": "groan", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「unprecedented」",
         "explanation": "unprecedented は「前例のない」という意味の形容詞です。",
         "choices": [
             {"text": "前例のない", "correct": True, "order": 1},
             {"text": "予期しない", "correct": False, "order": 2},
             {"text": "不必要な", "correct": False, "order": 3},
             {"text": "不確かな", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「妥協」",
         "explanation": "「妥協」は英語で compromise です。",
         "choices": [
             {"text": "compromise", "correct": True, "order": 1},
             {"text": "committee", "correct": False, "order": 2},
             {"text": "complement", "correct": False, "order": 3},
             {"text": "competence", "correct": False, "order": 4},
         ]},
    ],

    # =========================================================================
    # 高校3年 語彙 (VB-H3) — 大学入試レベル
    # =========================================================================
    "VB-H3": [
        {"difficulty": 3,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「accommodate」",
         "explanation": "accommodate は「収容する、対応する」という意味の動詞です。",
         "choices": [
             {"text": "収容する・対応する", "correct": True, "order": 1},
             {"text": "蓄積する", "correct": False, "order": 2},
             {"text": "同行する", "correct": False, "order": 3},
             {"text": "達成する", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「elaborate」",
         "explanation": "elaborate は「精巧な、詳細な」（形容詞）、「詳しく述べる」（動詞）という意味です。",
         "choices": [
             {"text": "精巧な・詳しく述べる", "correct": True, "order": 1},
             {"text": "優雅な", "correct": False, "order": 2},
             {"text": "弾力のある", "correct": False, "order": 3},
             {"text": "選挙の", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「必然的に」",
         "explanation": "「必然的に」は英語で inevitably です。形容詞形は inevitable です。",
         "choices": [
             {"text": "inevitably", "correct": True, "order": 1},
             {"text": "incredibly", "correct": False, "order": 2},
             {"text": "independently", "correct": False, "order": 3},
             {"text": "indefinitely", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「legitimate」",
         "explanation": "legitimate は「正当な、合法的な」という意味の形容詞です。",
         "choices": [
             {"text": "正当な", "correct": True, "order": 1},
             {"text": "文字通りの", "correct": False, "order": 2},
             {"text": "伝説的な", "correct": False, "order": 3},
             {"text": "立法の", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「普及させる」",
         "explanation": "「普及させる」は英語で disseminate / spread です。",
         "choices": [
             {"text": "disseminate", "correct": True, "order": 1},
             {"text": "discriminate", "correct": False, "order": 2},
             {"text": "discourage", "correct": False, "order": 3},
             {"text": "disintegrate", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「comprehensive」",
         "explanation": "comprehensive は「包括的な」という意味の形容詞です。",
         "choices": [
             {"text": "包括的な", "correct": True, "order": 1},
             {"text": "競争力のある", "correct": False, "order": 2},
             {"text": "補完的な", "correct": False, "order": 3},
             {"text": "強制的な", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「advocate」",
         "explanation": "advocate は「提唱する」（動詞）、「提唱者」（名詞）という意味です。",
         "choices": [
             {"text": "提唱する", "correct": True, "order": 1},
             {"text": "宣伝する", "correct": False, "order": 2},
             {"text": "適応する", "correct": False, "order": 3},
             {"text": "管理する", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「固有の」",
         "explanation": "「固有の」は英語で inherent です。inherent in 〜「〜に固有の」の形で使います。",
         "choices": [
             {"text": "inherent", "correct": True, "order": 1},
             {"text": "inferior", "correct": False, "order": 2},
             {"text": "infinite", "correct": False, "order": 3},
             {"text": "initial", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「ambiguous」",
         "explanation": "ambiguous は「あいまいな」という意味の形容詞です。名詞形は ambiguity です。",
         "choices": [
             {"text": "あいまいな", "correct": True, "order": 1},
             {"text": "野心的な", "correct": False, "order": 2},
             {"text": "豊富な", "correct": False, "order": 3},
             {"text": "匿名の", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「根絶する」",
         "explanation": "「根絶する」は英語で eradicate です。",
         "choices": [
             {"text": "eradicate", "correct": True, "order": 1},
             {"text": "elaborate", "correct": False, "order": 2},
             {"text": "evacuate", "correct": False, "order": 3},
             {"text": "evaporate", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「skeptical」",
         "explanation": "skeptical は「懐疑的な」という意味の形容詞です。skepticism は名詞形です。",
         "choices": [
             {"text": "懐疑的な", "correct": True, "order": 1},
             {"text": "熟練した", "correct": False, "order": 2},
             {"text": "壮大な", "correct": False, "order": 3},
             {"text": "特殊な", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の日本語に当たる英単語を選びなさい。\n\n「自律性」",
         "explanation": "「自律性」は英語で autonomy です。形容詞形は autonomous です。",
         "choices": [
             {"text": "autonomy", "correct": True, "order": 1},
             {"text": "authority", "correct": False, "order": 2},
             {"text": "autobiography", "correct": False, "order": 3},
             {"text": "automation", "correct": False, "order": 4},
         ]},
    ],
}
# fmt: on


def seed_vocab():
    db = SessionLocal()
    try:
        existing_unit_codes = {
            row[0] for row in db.query(Unit.code).all()
        }
        unit_code_to_id = {}

        new_unit_count = 0
        for u_data in VOCAB_UNITS:
            if u_data["code"] in existing_unit_codes:
                unit = db.query(Unit).filter(Unit.code == u_data["code"]).first()
                unit_code_to_id[u_data["code"]] = unit.id
                continue

            unit = Unit(
                code=u_data["code"],
                name=u_data["name"],
                category_id=u_data["category_id"],
                order_priority=u_data["order_priority"],
                description=u_data["description"],
            )
            db.add(unit)
            db.flush()
            unit_code_to_id[u_data["code"]] = unit.id
            new_unit_count += 1

        db.commit()
        if new_unit_count > 0:
            print(f"Added {new_unit_count} new vocabulary units")
        else:
            print("All vocabulary units already exist.")

        existing_texts = {
            row[0] for row in db.query(Question.question_text).all()
        }
        new_q_count = 0
        for unit_code, questions in VOCAB_QUESTIONS.items():
            unit_id = unit_code_to_id.get(unit_code)
            if not unit_id:
                print(f"WARNING: Unit {unit_code} not found, skipping questions")
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
            print(f"Added {new_q_count} new vocabulary questions")
        else:
            print("No new vocabulary questions to add.")

        print(f"\nVocab seed status:")
        print(f"  Total Units: {db.query(Unit).count()}")
        print(f"  Total Questions: {db.query(Question).count()}")
        print(f"  Total Choices: {db.query(Choice).count()}")

    finally:
        db.close()


if __name__ == "__main__":
    seed_vocab()
