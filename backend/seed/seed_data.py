"""
シードデータ投入スクリプト
実行:
  Linux/Mac: cd backend && source venv/bin/activate && python -m seed.seed_data
  Windows:   cd backend && .\venv\Scripts\Activate.ps1 && python -m seed.seed_data
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

# fmt: off
QUESTIONS = [
    # =====================================================================
    # 層1: 知識 > 語彙
    # =====================================================================
    # --- unit 1: 基本語彙（中学復習） ---
    {"unit_id": 1, "difficulty": 1,
     "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「important」",
     "explanation": "important は「重要な」という意味の形容詞です。",
     "choices": [
         {"text": "重要な", "correct": True, "order": 1},
         {"text": "面白い", "correct": False, "order": 2},
         {"text": "難しい", "correct": False, "order": 3},
         {"text": "美しい", "correct": False, "order": 4},
     ]},
    {"unit_id": 1, "difficulty": 1,
     "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「necessary」",
     "explanation": "necessary は「必要な」という意味の形容詞です。",
     "choices": [
         {"text": "自然な", "correct": False, "order": 1},
         {"text": "必要な", "correct": True, "order": 2},
         {"text": "簡単な", "correct": False, "order": 3},
         {"text": "特別な", "correct": False, "order": 4},
     ]},
    {"unit_id": 1, "difficulty": 1,
     "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「experience」",
     "explanation": "experience は「経験」という意味の名詞（「経験する」という動詞にもなる）です。",
     "choices": [
         {"text": "実験", "correct": False, "order": 1},
         {"text": "費用", "correct": False, "order": 2},
         {"text": "経験", "correct": True, "order": 3},
         {"text": "説明", "correct": False, "order": 4},
     ]},
    {"unit_id": 1, "difficulty": 1,
     "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「improve」",
     "explanation": "improve は「改善する、上達する」という意味の動詞です。",
     "choices": [
         {"text": "証明する", "correct": False, "order": 1},
         {"text": "改善する", "correct": True, "order": 2},
         {"text": "輸入する", "correct": False, "order": 3},
         {"text": "印象づける", "correct": False, "order": 4},
     ]},
    # --- unit 2: 高校基礎語彙 ---
    {"unit_id": 2, "difficulty": 1,
     "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「attitude」",
     "explanation": "attitude は「態度、姿勢」という意味の名詞です。altitude（高度）と間違えやすいので注意。",
     "choices": [
         {"text": "高度", "correct": False, "order": 1},
         {"text": "感謝", "correct": False, "order": 2},
         {"text": "態度", "correct": True, "order": 3},
         {"text": "適性", "correct": False, "order": 4},
     ]},
    {"unit_id": 2, "difficulty": 2,
     "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「significant」",
     "explanation": "significant は「重要な、意味のある」という意味の形容詞です。名詞形は significance。",
     "choices": [
         {"text": "重要な", "correct": True, "order": 1},
         {"text": "信号の", "correct": False, "order": 2},
         {"text": "署名する", "correct": False, "order": 3},
         {"text": "静かな", "correct": False, "order": 4},
     ]},
    {"unit_id": 2, "difficulty": 2,
     "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「opportunity」",
     "explanation": "opportunity は「機会」という意味の名詞です。chance より少しフォーマルな語です。",
     "choices": [
         {"text": "反対", "correct": False, "order": 1},
         {"text": "操作", "correct": False, "order": 2},
         {"text": "機会", "correct": True, "order": 3},
         {"text": "意見", "correct": False, "order": 4},
     ]},
    {"unit_id": 2, "difficulty": 2,
     "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「overcome」",
     "explanation": "overcome は「克服する、打ち勝つ」という意味の動詞です。over（上に）+ come（来る）で「乗り越える」イメージ。",
     "choices": [
         {"text": "見落とす", "correct": False, "order": 1},
         {"text": "克服する", "correct": True, "order": 2},
         {"text": "過ぎ去る", "correct": False, "order": 3},
         {"text": "覆す", "correct": False, "order": 4},
     ]},
    # =====================================================================
    # 層1: 知識 > 品詞
    # =====================================================================
    # --- unit 3: 品詞の識別 ---
    {"unit_id": 3, "difficulty": 1,
     "question_text": "次の文で下線部の品詞は何ですか？\n\n「She speaks English _fluently_.」",
     "explanation": "fluently は speak（動詞）を修飾する副詞です。-ly で終わる語は副詞であることが多いです。",
     "choices": [
         {"text": "名詞", "correct": False, "order": 1},
         {"text": "形容詞", "correct": False, "order": 2},
         {"text": "副詞", "correct": True, "order": 3},
         {"text": "動詞", "correct": False, "order": 4},
     ]},
    {"unit_id": 3, "difficulty": 1,
     "question_text": "次の語のうち、形容詞はどれですか？",
     "explanation": "beautiful は「美しい」という意味の形容詞です。beauty(名詞), beautify(動詞), beautifully(副詞)と区別しましょう。",
     "choices": [
         {"text": "beauty", "correct": False, "order": 1},
         {"text": "beautiful", "correct": True, "order": 2},
         {"text": "beautifully", "correct": False, "order": 3},
         {"text": "beautify", "correct": False, "order": 4},
     ]},
    {"unit_id": 3, "difficulty": 1,
     "question_text": "次の文で下線部の品詞は何ですか？\n\n「He made a _careful_ decision.」",
     "explanation": "careful は decision（名詞）を修飾する形容詞です。名詞の前に置かれて修飾するのが形容詞の基本的な働きです。",
     "choices": [
         {"text": "名詞", "correct": False, "order": 1},
         {"text": "形容詞", "correct": True, "order": 2},
         {"text": "副詞", "correct": False, "order": 3},
         {"text": "動詞", "correct": False, "order": 4},
     ]},
    # --- unit 4: 品詞の働き ---
    {"unit_id": 4, "difficulty": 1,
     "question_text": "次の文で「quickly」はどの語を修飾していますか？\n\n「He quickly finished his homework.」",
     "explanation": "quickly は副詞で、動詞 finished を修飾しています。「速く終えた」という意味になります。",
     "choices": [
         {"text": "He", "correct": False, "order": 1},
         {"text": "finished", "correct": True, "order": 2},
         {"text": "his", "correct": False, "order": 3},
         {"text": "homework", "correct": False, "order": 4},
     ]},
    {"unit_id": 4, "difficulty": 2,
     "question_text": "次の文で「very」はどの語を修飾していますか？\n\n「She is a very kind person.」",
     "explanation": "very は副詞で、形容詞 kind を修飾しています。副詞は形容詞や他の副詞も修飾できます。",
     "choices": [
         {"text": "She", "correct": False, "order": 1},
         {"text": "is", "correct": False, "order": 2},
         {"text": "kind", "correct": True, "order": 3},
         {"text": "person", "correct": False, "order": 4},
     ]},
    {"unit_id": 4, "difficulty": 2,
     "question_text": "次の文で下線部の語は何の働きをしていますか？\n\n「_Swimming_ is good exercise.」",
     "explanation": "Swimming は動名詞で、この文では主語として名詞の働きをしています。",
     "choices": [
         {"text": "主語（名詞の働き）", "correct": True, "order": 1},
         {"text": "動詞", "correct": False, "order": 2},
         {"text": "形容詞の働き", "correct": False, "order": 3},
         {"text": "副詞の働き", "correct": False, "order": 4},
     ]},
    # =====================================================================
    # 層2: 文構造 > 時制
    # =====================================================================
    # --- unit 5: 現在形 ---
    {"unit_id": 5, "difficulty": 1,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「She ___ to school every day.」",
     "explanation": "主語が She（三人称単数）で、every day は習慣を表すため、現在形の goes が正解です。",
     "choices": [
         {"text": "go", "correct": False, "order": 1},
         {"text": "goes", "correct": True, "order": 2},
         {"text": "going", "correct": False, "order": 3},
         {"text": "went", "correct": False, "order": 4},
     ]},
    {"unit_id": 5, "difficulty": 1,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「Water ___ at 100 degrees Celsius.」",
     "explanation": "科学的事実や一般的真理は現在形で表します。Water は三人称単数なので boils が正解。",
     "choices": [
         {"text": "boil", "correct": False, "order": 1},
         {"text": "boils", "correct": True, "order": 2},
         {"text": "is boiling", "correct": False, "order": 3},
         {"text": "boiled", "correct": False, "order": 4},
     ]},
    {"unit_id": 5, "difficulty": 1,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「He ___ not like coffee.」",
     "explanation": "三人称単数の否定文は does not (doesn't) + 動詞の原形です。",
     "choices": [
         {"text": "do", "correct": False, "order": 1},
         {"text": "does", "correct": True, "order": 2},
         {"text": "is", "correct": False, "order": 3},
         {"text": "has", "correct": False, "order": 4},
     ]},
    # --- unit 6: 過去形 ---
    {"unit_id": 6, "difficulty": 1,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「I ___ the movie last night.」",
     "explanation": "last night は過去の時点を示すので、過去形の watched が正解です。",
     "choices": [
         {"text": "watch", "correct": False, "order": 1},
         {"text": "watches", "correct": False, "order": 2},
         {"text": "watched", "correct": True, "order": 3},
         {"text": "have watched", "correct": False, "order": 4},
     ]},
    {"unit_id": 6, "difficulty": 2,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「They ___ to Paris two years ago.」",
     "explanation": "two years ago は明確な過去の時点を示すので、過去形の went が正解です。have been は現在完了形で ago とは一緒に使えません。",
     "choices": [
         {"text": "go", "correct": False, "order": 1},
         {"text": "have been", "correct": False, "order": 2},
         {"text": "have gone", "correct": False, "order": 3},
         {"text": "went", "correct": True, "order": 4},
     ]},
    {"unit_id": 6, "difficulty": 1,
     "question_text": "次の動詞の過去形として正しいものを選びなさい。\n\n「teach」",
     "explanation": "teach の過去形は taught です。不規則変化動詞なので注意しましょう。",
     "choices": [
         {"text": "teached", "correct": False, "order": 1},
         {"text": "taught", "correct": True, "order": 2},
         {"text": "teaching", "correct": False, "order": 3},
         {"text": "tought", "correct": False, "order": 4},
     ]},
    {"unit_id": 6, "difficulty": 2,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「She ___ her keys yesterday.」",
     "explanation": "yesterday は過去の時点を示します。lose の過去形は lost です。",
     "choices": [
         {"text": "loses", "correct": False, "order": 1},
         {"text": "lost", "correct": True, "order": 2},
         {"text": "has lost", "correct": False, "order": 3},
         {"text": "losed", "correct": False, "order": 4},
     ]},
    # --- unit 7: 現在完了形 ---
    {"unit_id": 7, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I ___ in Tokyo for five years.」（今も住んでいる）",
     "explanation": "「5年間住んでいる（今も継続中）」は現在完了形の継続用法で表します。for five years は期間を表す語句です。",
     "choices": [
         {"text": "live", "correct": False, "order": 1},
         {"text": "lived", "correct": False, "order": 2},
         {"text": "have lived", "correct": True, "order": 3},
         {"text": "had lived", "correct": False, "order": 4},
     ]},
    {"unit_id": 7, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I ___ sushi before.」（寿司を食べたことがある）",
     "explanation": "「～したことがある」は現在完了形の経験用法です。before は経験用法でよく使われる語です。",
     "choices": [
         {"text": "eat", "correct": False, "order": 1},
         {"text": "ate", "correct": False, "order": 2},
         {"text": "have eaten", "correct": True, "order": 3},
         {"text": "had eaten", "correct": False, "order": 4},
     ]},
    {"unit_id": 7, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「He ___ just ___ his homework.」（宿題を終えたところだ）",
     "explanation": "「ちょうど～したところだ」は現在完了形の完了用法です。just は have と過去分詞の間に入ります。",
     "choices": [
         {"text": "is ... finishing", "correct": False, "order": 1},
         {"text": "has ... finished", "correct": True, "order": 2},
         {"text": "had ... finished", "correct": False, "order": 3},
         {"text": "was ... finishing", "correct": False, "order": 4},
     ]},
    {"unit_id": 7, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「She ___ never ___ abroad.」（海外に行ったことがない）",
     "explanation": "never を使った経験の否定は現在完了形で表します。has never + 過去分詞の語順です。",
     "choices": [
         {"text": "has ... been", "correct": True, "order": 1},
         {"text": "is ... being", "correct": False, "order": 2},
         {"text": "was ... been", "correct": False, "order": 3},
         {"text": "did ... be", "correct": False, "order": 4},
     ]},
    # --- unit 8: 過去完了形 ---
    {"unit_id": 8, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「When I arrived at the station, the train ___ already ___.」",
     "explanation": "「駅に着いたとき、電車はすでに出発していた」過去のある時点より前の出来事は過去完了形(had + 過去分詞)で表します。",
     "choices": [
         {"text": "has ... left", "correct": False, "order": 1},
         {"text": "had ... left", "correct": True, "order": 2},
         {"text": "was ... leaving", "correct": False, "order": 3},
         {"text": "is ... leaving", "correct": False, "order": 4},
     ]},
    {"unit_id": 8, "difficulty": 3,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「She told me that she ___ the book the day before.」",
     "explanation": "時制の一致により、主節が過去形(told)の場合、従属節内の過去の出来事は過去完了形になります。",
     "choices": [
         {"text": "reads", "correct": False, "order": 1},
         {"text": "read", "correct": False, "order": 2},
         {"text": "has read", "correct": False, "order": 3},
         {"text": "had read", "correct": True, "order": 4},
     ]},
    {"unit_id": 8, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I ___ never ___ such a beautiful sunset before that day.」",
     "explanation": "that day（その日）より前の経験を表すので、過去完了形 had never seen を使います。",
     "choices": [
         {"text": "have ... seen", "correct": False, "order": 1},
         {"text": "had ... seen", "correct": True, "order": 2},
         {"text": "was ... seeing", "correct": False, "order": 3},
         {"text": "did ... see", "correct": False, "order": 4},
     ]},
    # --- unit 9: 進行形 ---
    {"unit_id": 9, "difficulty": 1,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「Look! It ___ outside.」",
     "explanation": "Look!（見て!）は今まさに起きていることを指すので、現在進行形 is raining を使います。",
     "choices": [
         {"text": "rains", "correct": False, "order": 1},
         {"text": "is raining", "correct": True, "order": 2},
         {"text": "rained", "correct": False, "order": 3},
         {"text": "was raining", "correct": False, "order": 4},
     ]},
    {"unit_id": 9, "difficulty": 1,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I ___ dinner when the phone rang.」",
     "explanation": "電話が鳴った（過去の一時点）とき、夕食を食べている最中だったので、過去進行形 was cooking を使います。",
     "choices": [
         {"text": "cook", "correct": False, "order": 1},
         {"text": "cooked", "correct": False, "order": 2},
         {"text": "was cooking", "correct": True, "order": 3},
         {"text": "have cooked", "correct": False, "order": 4},
     ]},
    {"unit_id": 9, "difficulty": 2,
     "question_text": "次の文のうち、進行形にできない動詞を含むものはどれですか？",
     "explanation": "know は状態動詞なので、通常は進行形にできません。I am knowing... とは言いません。",
     "choices": [
         {"text": "I am studying English.", "correct": False, "order": 1},
         {"text": "She is running in the park.", "correct": False, "order": 2},
         {"text": "I am knowing the answer.", "correct": True, "order": 3},
         {"text": "They are playing soccer.", "correct": False, "order": 4},
     ]},
    # --- unit 10: 未来表現 ---
    {"unit_id": 10, "difficulty": 1,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I ___ help you with your homework.」（手伝ってあげるよ）",
     "explanation": "その場での意志・申し出を表すときは will を使います。",
     "choices": [
         {"text": "will", "correct": True, "order": 1},
         {"text": "am going to", "correct": False, "order": 2},
         {"text": "would", "correct": False, "order": 3},
         {"text": "shall", "correct": False, "order": 4},
     ]},
    {"unit_id": 10, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「Look at those clouds. It ___ rain.」（雨が降りそうだ）",
     "explanation": "根拠に基づく予測（雲が出ている）には be going to を使います。will は根拠なしの予測に使います。",
     "choices": [
         {"text": "will", "correct": False, "order": 1},
         {"text": "is going to", "correct": True, "order": 2},
         {"text": "would", "correct": False, "order": 3},
         {"text": "was going to", "correct": False, "order": 4},
     ]},
    {"unit_id": 10, "difficulty": 1,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「The train ___ at 9:00 tomorrow.」（電車は明日9時に出発する）",
     "explanation": "時刻表やスケジュールなど確定した未来の予定は現在形で表せます。",
     "choices": [
         {"text": "leaves", "correct": True, "order": 1},
         {"text": "will leave", "correct": False, "order": 2},
         {"text": "is going to leave", "correct": False, "order": 3},
         {"text": "left", "correct": False, "order": 4},
     ]},
    # =====================================================================
    # 層2: 文構造 > 態
    # =====================================================================
    # --- unit 11: 受動態の基本 ---
    {"unit_id": 11, "difficulty": 1,
     "question_text": "次の文を受動態に変えた場合、正しいものはどれですか？\n\n「Tom wrote this letter.」",
     "explanation": "能動態の目的語 this letter が受動態の主語になります。過去形の受動態は was/were + 過去分詞。",
     "choices": [
         {"text": "This letter is written by Tom.", "correct": False, "order": 1},
         {"text": "This letter was written by Tom.", "correct": True, "order": 2},
         {"text": "This letter has been written by Tom.", "correct": False, "order": 3},
         {"text": "This letter wrote by Tom.", "correct": False, "order": 4},
     ]},
    {"unit_id": 11, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「English ___ in many countries.」",
     "explanation": "「英語は多くの国で話されている」という一般的事実は、現在形の受動態で表します。",
     "choices": [
         {"text": "speaks", "correct": False, "order": 1},
         {"text": "is spoken", "correct": True, "order": 2},
         {"text": "spoke", "correct": False, "order": 3},
         {"text": "was spoken", "correct": False, "order": 4},
     ]},
    {"unit_id": 11, "difficulty": 1,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「This castle ___ 500 years ago.」",
     "explanation": "500 years ago は過去の時点なので、過去形の受動態 was built を使います。",
     "choices": [
         {"text": "built", "correct": False, "order": 1},
         {"text": "was built", "correct": True, "order": 2},
         {"text": "is built", "correct": False, "order": 3},
         {"text": "has been built", "correct": False, "order": 4},
     ]},
    # --- unit 12: 受動態の応用 ---
    {"unit_id": 12, "difficulty": 2,
     "question_text": "次の文を受動態に変えた場合、正しいものはどれですか？\n\n「She gave me a present.」",
     "explanation": "SVOO（第4文型）の受動態では、間接目的語 me を主語にすると I was given a present (by her). になります。",
     "choices": [
         {"text": "A present was given me by her.", "correct": False, "order": 1},
         {"text": "I was given a present by her.", "correct": True, "order": 2},
         {"text": "Me was given a present by her.", "correct": False, "order": 3},
         {"text": "I was gave a present by her.", "correct": False, "order": 4},
     ]},
    {"unit_id": 12, "difficulty": 3,
     "question_text": "次の文を受動態に変えた場合、正しいものはどれですか？\n\n「They call him Ken.」",
     "explanation": "SVOC（第5文型）の受動態は、目的語が主語になり、補語はそのまま残ります。He is called Ken.",
     "choices": [
         {"text": "Ken is called him by them.", "correct": False, "order": 1},
         {"text": "He is called Ken.", "correct": True, "order": 2},
         {"text": "Him is called Ken by them.", "correct": False, "order": 3},
         {"text": "He is call Ken.", "correct": False, "order": 4},
     ]},
    {"unit_id": 12, "difficulty": 3,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「He is ___ in Japanese history.」（日本史に興味がある）",
     "explanation": "be interested in は「～に興味がある」という受動態の慣用表現です。",
     "choices": [
         {"text": "interesting", "correct": False, "order": 1},
         {"text": "interested", "correct": True, "order": 2},
         {"text": "interest", "correct": False, "order": 3},
         {"text": "interests", "correct": False, "order": 4},
     ]},
    # =====================================================================
    # 層2: 文構造 > 助動詞
    # =====================================================================
    # --- unit 13: 助動詞の基本 ---
    {"unit_id": 13, "difficulty": 1,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「You ___ not park here.」（ここに駐車してはいけない）",
     "explanation": "「～してはいけない」という禁止は must not で表します。",
     "choices": [
         {"text": "can", "correct": False, "order": 1},
         {"text": "must", "correct": True, "order": 2},
         {"text": "should", "correct": False, "order": 3},
         {"text": "may", "correct": False, "order": 4},
     ]},
    {"unit_id": 13, "difficulty": 1,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「___ I use your phone?」（電話を使ってもいいですか？）",
     "explanation": "許可を求める丁寧な表現は May I ...? です。Can I ...? よりもフォーマルです。",
     "choices": [
         {"text": "Must", "correct": False, "order": 1},
         {"text": "Should", "correct": False, "order": 2},
         {"text": "May", "correct": True, "order": 3},
         {"text": "Will", "correct": False, "order": 4},
     ]},
    {"unit_id": 13, "difficulty": 1,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「You ___ see a doctor.」（医者に診てもらうべきだ）",
     "explanation": "「～すべきだ」という助言は should で表します。must は義務（～しなければならない）です。",
     "choices": [
         {"text": "should", "correct": True, "order": 1},
         {"text": "can", "correct": False, "order": 2},
         {"text": "would", "correct": False, "order": 3},
         {"text": "might", "correct": False, "order": 4},
     ]},
    # --- unit 14: 助動詞の応用 ---
    {"unit_id": 14, "difficulty": 3,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「She ___ have been tired. She went to bed early.」",
     "explanation": "「～だったに違いない」は must have + 過去分詞で表します。過去の推量を表す表現です。",
     "choices": [
         {"text": "must", "correct": True, "order": 1},
         {"text": "can", "correct": False, "order": 2},
         {"text": "should", "correct": False, "order": 3},
         {"text": "would", "correct": False, "order": 4},
     ]},
    {"unit_id": 14, "difficulty": 3,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「He ___ have studied harder for the exam.」（もっと勉強すべきだった）",
     "explanation": "「～すべきだったのに（しなかった）」は should have + 過去分詞で表します。過去の後悔を表す表現です。",
     "choices": [
         {"text": "must", "correct": False, "order": 1},
         {"text": "can", "correct": False, "order": 2},
         {"text": "should", "correct": True, "order": 3},
         {"text": "will", "correct": False, "order": 4},
     ]},
    {"unit_id": 14, "difficulty": 3,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「He ___ not have done such a thing.」（そんなことをしたはずがない）",
     "explanation": "「～したはずがない」は cannot have + 過去分詞で表します。過去の行為に対する強い否定の推量です。",
     "choices": [
         {"text": "must", "correct": False, "order": 1},
         {"text": "could", "correct": False, "order": 2},
         {"text": "can", "correct": True, "order": 3},
         {"text": "would", "correct": False, "order": 4},
     ]},
    # =====================================================================
    # 層2: 文構造 > 不定詞・動名詞
    # =====================================================================
    # --- unit 15: 不定詞の名詞的用法 ---
    {"unit_id": 15, "difficulty": 1,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I want ___ a doctor.」",
     "explanation": "want は不定詞（to + 動詞の原形）を目的語にとる動詞です。want + -ing の形はありません。",
     "choices": [
         {"text": "be", "correct": False, "order": 1},
         {"text": "to be", "correct": True, "order": 2},
         {"text": "being", "correct": False, "order": 3},
         {"text": "been", "correct": False, "order": 4},
     ]},
    {"unit_id": 15, "difficulty": 1,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「He decided ___ abroad.」",
     "explanation": "decide は不定詞を目的語にとる動詞です。decide + -ing の形は使えません。",
     "choices": [
         {"text": "study", "correct": False, "order": 1},
         {"text": "to study", "correct": True, "order": 2},
         {"text": "studying", "correct": False, "order": 3},
         {"text": "studied", "correct": False, "order": 4},
     ]},
    # --- unit 16: 不定詞の形容詞的・副詞的用法 ---
    {"unit_id": 16, "difficulty": 2,
     "question_text": "次の文の to read は何用法ですか？\n\n「I have a book to read.」",
     "explanation": "to read は book（名詞）を修飾しているので形容詞的用法です。「読むべき本」の意味。",
     "choices": [
         {"text": "名詞的用法", "correct": False, "order": 1},
         {"text": "形容詞的用法", "correct": True, "order": 2},
         {"text": "副詞的用法", "correct": False, "order": 3},
         {"text": "どれでもない", "correct": False, "order": 4},
     ]},
    {"unit_id": 16, "difficulty": 2,
     "question_text": "次の文の to buy は何用法ですか？\n\n「She went to the store to buy some milk.」",
     "explanation": "to buy は went（動詞）の目的・理由を表しているので副詞的用法です。「牛乳を買うために行った」の意味。",
     "choices": [
         {"text": "名詞的用法", "correct": False, "order": 1},
         {"text": "形容詞的用法", "correct": False, "order": 2},
         {"text": "副詞的用法", "correct": True, "order": 3},
         {"text": "どれでもない", "correct": False, "order": 4},
     ]},
    {"unit_id": 16, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I need something ___.」（何か飲むもの）",
     "explanation": "something を修飾する不定詞は後ろから修飾します。something to drink で「飲むための何か」。",
     "choices": [
         {"text": "drink", "correct": False, "order": 1},
         {"text": "to drink", "correct": True, "order": 2},
         {"text": "drinking", "correct": False, "order": 3},
         {"text": "drunk", "correct": False, "order": 4},
     ]},
    # --- unit 17: 動名詞 ---
    {"unit_id": 17, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I enjoy ___ books.」",
     "explanation": "enjoy は動名詞（-ing形）を目的語にとる動詞です。enjoy to do の形は使えません。",
     "choices": [
         {"text": "read", "correct": False, "order": 1},
         {"text": "to read", "correct": False, "order": 2},
         {"text": "reading", "correct": True, "order": 3},
         {"text": "to reading", "correct": False, "order": 4},
     ]},
    {"unit_id": 17, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「She stopped ___ when I entered the room.」（彼女は私が入ってきたとき話すのをやめた）",
     "explanation": "stop + -ing は「～するのをやめる」、stop + to do は「～するために立ち止まる」です。文脈から -ing が正解。",
     "choices": [
         {"text": "talk", "correct": False, "order": 1},
         {"text": "to talk", "correct": False, "order": 2},
         {"text": "talking", "correct": True, "order": 3},
         {"text": "talked", "correct": False, "order": 4},
     ]},
    {"unit_id": 17, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「Would you mind ___ the window?」（窓を開けていただけますか）",
     "explanation": "mind は動名詞を目的語にとります。Would you mind -ing? は丁寧な依頼表現です。",
     "choices": [
         {"text": "open", "correct": False, "order": 1},
         {"text": "to open", "correct": False, "order": 2},
         {"text": "opening", "correct": True, "order": 3},
         {"text": "opened", "correct": False, "order": 4},
     ]},
    # =====================================================================
    # 層2: 文構造 > 関係詞
    # =====================================================================
    # --- unit 18: 関係代名詞 ---
    {"unit_id": 18, "difficulty": 2,
     "question_text": "空所に入る最も適切な関係代名詞を選びなさい。\n\n「The man ___ lives next door is a teacher.」",
     "explanation": "先行詞 The man は人で、関係詞節内で主語の役割を果たすので、who が正解です。",
     "choices": [
         {"text": "who", "correct": True, "order": 1},
         {"text": "which", "correct": False, "order": 2},
         {"text": "whom", "correct": False, "order": 3},
         {"text": "whose", "correct": False, "order": 4},
     ]},
    {"unit_id": 18, "difficulty": 2,
     "question_text": "空所に入る最も適切な関係代名詞を選びなさい。\n\n「This is the book ___ I bought yesterday.」",
     "explanation": "先行詞 the book は物で、関係詞節内で bought の目的語の役割です。物の場合は which か that を使います。",
     "choices": [
         {"text": "who", "correct": False, "order": 1},
         {"text": "which", "correct": True, "order": 2},
         {"text": "whose", "correct": False, "order": 3},
         {"text": "whom", "correct": False, "order": 4},
     ]},
    {"unit_id": 18, "difficulty": 2,
     "question_text": "空所に入る最も適切な関係代名詞を選びなさい。\n\n「I have a friend ___ father is a doctor.」",
     "explanation": "所有の関係を表すときは whose を使います。「父親が医者である友人」の意味。",
     "choices": [
         {"text": "who", "correct": False, "order": 1},
         {"text": "which", "correct": False, "order": 2},
         {"text": "whose", "correct": True, "order": 3},
         {"text": "whom", "correct": False, "order": 4},
     ]},
    # --- unit 19: 関係副詞 ---
    {"unit_id": 19, "difficulty": 2,
     "question_text": "空所に入る最も適切な関係副詞を選びなさい。\n\n「This is the city ___ I was born.」",
     "explanation": "場所を表す先行詞 the city の後ろで、関係詞節内で副詞の働きをするので where を使います。",
     "choices": [
         {"text": "where", "correct": True, "order": 1},
         {"text": "when", "correct": False, "order": 2},
         {"text": "which", "correct": False, "order": 3},
         {"text": "why", "correct": False, "order": 4},
     ]},
    {"unit_id": 19, "difficulty": 2,
     "question_text": "空所に入る最も適切な関係副詞を選びなさい。\n\n「I remember the day ___ we first met.」",
     "explanation": "時を表す先行詞 the day の後ろでは when を使います。",
     "choices": [
         {"text": "where", "correct": False, "order": 1},
         {"text": "when", "correct": True, "order": 2},
         {"text": "which", "correct": False, "order": 3},
         {"text": "why", "correct": False, "order": 4},
     ]},
    {"unit_id": 19, "difficulty": 2,
     "question_text": "空所に入る最も適切な関係副詞を選びなさい。\n\n「Tell me the reason ___ you were late.」",
     "explanation": "理由を表す先行詞 the reason の後ろでは why を使います。",
     "choices": [
         {"text": "where", "correct": False, "order": 1},
         {"text": "when", "correct": False, "order": 2},
         {"text": "which", "correct": False, "order": 3},
         {"text": "why", "correct": True, "order": 4},
     ]},
    # =====================================================================
    # 層2: 文構造 > 比較
    # =====================================================================
    # --- unit 20: 比較の基本 ---
    {"unit_id": 20, "difficulty": 1,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「Tom is ___ than his brother.」",
     "explanation": "than があるので比較級を使います。tall の比較級は taller です。",
     "choices": [
         {"text": "tall", "correct": False, "order": 1},
         {"text": "taller", "correct": True, "order": 2},
         {"text": "tallest", "correct": False, "order": 3},
         {"text": "more tall", "correct": False, "order": 4},
     ]},
    {"unit_id": 20, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「This problem is ___ difficult than that one.」",
     "explanation": "difficult は長い形容詞なので、比較級は more difficult です。",
     "choices": [
         {"text": "difficulter", "correct": False, "order": 1},
         {"text": "more", "correct": True, "order": 2},
         {"text": "most", "correct": False, "order": 3},
         {"text": "much", "correct": False, "order": 4},
     ]},
    {"unit_id": 20, "difficulty": 1,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「She is the ___ student in our class.」",
     "explanation": "the + 最上級 + in ~「～の中で最も…」の構文です。tall の最上級は tallest。",
     "choices": [
         {"text": "tall", "correct": False, "order": 1},
         {"text": "taller", "correct": False, "order": 2},
         {"text": "tallest", "correct": True, "order": 3},
         {"text": "most tall", "correct": False, "order": 4},
     ]},
    # --- unit 21: 比較の応用表現 ---
    {"unit_id": 21, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「He is ___ tall ___ his father.」（彼は父と同じくらい背が高い）",
     "explanation": "「AはBと同じくらい～」は as ~ as の原級比較で表します。",
     "choices": [
         {"text": "as ... as", "correct": True, "order": 1},
         {"text": "so ... as", "correct": False, "order": 2},
         {"text": "more ... than", "correct": False, "order": 3},
         {"text": "the ... of", "correct": False, "order": 4},
     ]},
    {"unit_id": 21, "difficulty": 3,
     "question_text": "次の文の意味として正しいものを選びなさい。\n\n「No other mountain in Japan is as high as Mt. Fuji.」",
     "explanation": "No other A is as ~ as B は「BはAの中で最も～だ」を原級比較で表す構文です。",
     "choices": [
         {"text": "富士山は日本で最も高い山ではない", "correct": False, "order": 1},
         {"text": "日本で富士山ほど高い山はない（＝富士山が最も高い）", "correct": True, "order": 2},
         {"text": "富士山は他の山と同じ高さだ", "correct": False, "order": 3},
         {"text": "富士山より高い山が日本にある", "correct": False, "order": 4},
     ]},
    {"unit_id": 21, "difficulty": 3,
     "question_text": "次の文の意味として正しいものを選びなさい。\n\n「The sooner, the better.」",
     "explanation": "the + 比較級, the + 比較級 は「～すればするほど…」を表す構文です。",
     "choices": [
         {"text": "早い方が良い", "correct": True, "order": 1},
         {"text": "遅い方が良い", "correct": False, "order": 2},
         {"text": "早すぎる", "correct": False, "order": 3},
         {"text": "良くも悪くもない", "correct": False, "order": 4},
     ]},
    # =====================================================================
    # 層2: 文構造 > 仮定法
    # =====================================================================
    # --- unit 22: 仮定法過去 ---
    {"unit_id": 22, "difficulty": 3,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「If I ___ rich, I would travel around the world.」",
     "explanation": "仮定法過去は、現在の事実に反する仮定を表します。be動詞は主語に関わらず were を使います。",
     "choices": [
         {"text": "am", "correct": False, "order": 1},
         {"text": "was", "correct": False, "order": 2},
         {"text": "were", "correct": True, "order": 3},
         {"text": "have been", "correct": False, "order": 4},
     ]},
    {"unit_id": 22, "difficulty": 3,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「If I knew his phone number, I ___ him.」",
     "explanation": "仮定法過去の帰結節は would + 動詞の原形で表します。",
     "choices": [
         {"text": "call", "correct": False, "order": 1},
         {"text": "called", "correct": False, "order": 2},
         {"text": "would call", "correct": True, "order": 3},
         {"text": "will call", "correct": False, "order": 4},
     ]},
    {"unit_id": 22, "difficulty": 3,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I wish I ___ a bird.」（鳥だったらなあ）",
     "explanation": "wish + 仮定法過去で「～であればなあ」と現在の願望を表します。be動詞は were を使います。",
     "choices": [
         {"text": "am", "correct": False, "order": 1},
         {"text": "were", "correct": True, "order": 2},
         {"text": "was", "correct": False, "order": 3},
         {"text": "be", "correct": False, "order": 4},
     ]},
    # --- unit 23: 仮定法過去完了 ---
    {"unit_id": 23, "difficulty": 3,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「If I had known the truth, I ___ differently.」",
     "explanation": "仮定法過去完了の帰結節は would have + 過去分詞で表します。過去の事実に反する仮定です。",
     "choices": [
         {"text": "will act", "correct": False, "order": 1},
         {"text": "would act", "correct": False, "order": 2},
         {"text": "would have acted", "correct": True, "order": 3},
         {"text": "had acted", "correct": False, "order": 4},
     ]},
    {"unit_id": 23, "difficulty": 3,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「If she ___ earlier, she would have caught the train.」",
     "explanation": "仮定法過去完了の条件節は if + had + 過去分詞です。「もっと早く出発していたら」の意味。",
     "choices": [
         {"text": "left", "correct": False, "order": 1},
         {"text": "has left", "correct": False, "order": 2},
         {"text": "would leave", "correct": False, "order": 3},
         {"text": "had left", "correct": True, "order": 4},
     ]},
    {"unit_id": 23, "difficulty": 3,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I wish I ___ harder when I was young.」（若いとき、もっと勉強しておけばよかった）",
     "explanation": "wish + 仮定法過去完了で「～していればよかったのに」と過去の後悔を表します。",
     "choices": [
         {"text": "study", "correct": False, "order": 1},
         {"text": "studied", "correct": False, "order": 2},
         {"text": "had studied", "correct": True, "order": 3},
         {"text": "have studied", "correct": False, "order": 4},
     ]},
    # =====================================================================
    # 層3: 読解基礎 > 短文読解
    # =====================================================================
    {"unit_id": 1, "difficulty": 2, "question_text":
     "次の英文の意味として最も適切なものを選びなさい。\n\n「Despite the heavy rain, she decided to go out.」",
     "explanation": "despite は「～にもかかわらず」という意味の前置詞です。後ろには名詞（句）が続きます。",
     "choices": [
         {"text": "大雨のせいで、彼女は外出を決めた", "correct": False, "order": 1},
         {"text": "大雨にもかかわらず、彼女は外出を決めた", "correct": True, "order": 2},
         {"text": "大雨が降る前に、彼女は外出を決めた", "correct": False, "order": 3},
         {"text": "大雨が降ったので、彼女は外出をやめた", "correct": False, "order": 4},
     ]},
    {"unit_id": 1, "difficulty": 2, "question_text":
     "次の英文の意味として最も適切なものを選びなさい。\n\n「He is not only smart but also kind.」",
     "explanation": "not only A but also B は「AだけでなくBも」という意味の相関接続詞です。",
     "choices": [
         {"text": "彼は賢いが優しくない", "correct": False, "order": 1},
         {"text": "彼は賢くないが優しい", "correct": False, "order": 2},
         {"text": "彼は賢いだけでなく優しくもある", "correct": True, "order": 3},
         {"text": "彼は賢くも優しくもない", "correct": False, "order": 4},
     ]},
    {"unit_id": 2, "difficulty": 2, "question_text":
     "次の英文の意味として最も適切なものを選びなさい。\n\n「The more you practice, the better you become.」",
     "explanation": "the + 比較級, the + 比較級 で「～すればするほど…になる」の意味です。",
     "choices": [
         {"text": "もっと練習すれば、すぐに上手になる", "correct": False, "order": 1},
         {"text": "練習すればするほど、上手になる", "correct": True, "order": 2},
         {"text": "練習しても、上手にならない", "correct": False, "order": 3},
         {"text": "一番練習した人が一番上手だ", "correct": False, "order": 4},
     ]},
    {"unit_id": 2, "difficulty": 3, "question_text":
     "次の英文の空所に入る最も適切な語を選びなさい。\n\n「It is important for students to develop critical thinking skills. ___, they should read various kinds of books.」",
     "explanation": "前文で「批判的思考力を身につけることが重要」と述べ、その方法として「様々な本を読むべき」と続けるので、Therefore（したがって）が適切です。",
     "choices": [
         {"text": "However", "correct": False, "order": 1},
         {"text": "Therefore", "correct": True, "order": 2},
         {"text": "Meanwhile", "correct": False, "order": 3},
         {"text": "Otherwise", "correct": False, "order": 4},
     ]},
    # =====================================================================
    # 追加問題（各単元3問ずつ）
    # =====================================================================
    # --- unit 1: 基本語彙（中学復習） ---
    {"unit_id": 1, "difficulty": 1,
     "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「decide」",
     "explanation": "decide は「決める、決心する」という意味の動詞です。",
     "choices": [
         {"text": "決める", "correct": True, "order": 1},
         {"text": "分ける", "correct": False, "order": 2},
         {"text": "下がる", "correct": False, "order": 3},
         {"text": "宣言する", "correct": False, "order": 4},
     ]},
    {"unit_id": 1, "difficulty": 1,
     "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「borrow」",
     "explanation": "borrow は「借りる」という意味の動詞です。「貸す」は lend で、方向が逆になるので注意しましょう。",
     "choices": [
         {"text": "貸す", "correct": False, "order": 1},
         {"text": "借りる", "correct": True, "order": 2},
         {"text": "買う", "correct": False, "order": 3},
         {"text": "返す", "correct": False, "order": 4},
     ]},
    {"unit_id": 1, "difficulty": 1,
     "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「arrive」",
     "explanation": "arrive は「到着する」という意味の動詞です。arrive at/in の形でよく使われます。",
     "choices": [
         {"text": "出発する", "correct": False, "order": 1},
         {"text": "到着する", "correct": True, "order": 2},
         {"text": "遅れる", "correct": False, "order": 3},
         {"text": "急ぐ", "correct": False, "order": 4},
     ]},
    # --- unit 2: 高校基礎語彙 ---
    {"unit_id": 2, "difficulty": 2,
     "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「essential」",
     "explanation": "essential は「不可欠な、必須の」という意味の形容詞です。名詞形は essence（本質）。",
     "choices": [
         {"text": "本質的な、不可欠な", "correct": True, "order": 1},
         {"text": "本質的でない", "correct": False, "order": 2},
         {"text": "季節の", "correct": False, "order": 3},
         {"text": "感情的な", "correct": False, "order": 4},
     ]},
    {"unit_id": 2, "difficulty": 2,
     "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「achieve」",
     "explanation": "achieve は「達成する」という意味の動詞です。名詞形は achievement（業績、達成）。",
     "choices": [
         {"text": "達成する", "correct": True, "order": 1},
         {"text": "到達を試みる", "correct": False, "order": 2},
         {"text": "獲得を諦める", "correct": False, "order": 3},
         {"text": "調整する", "correct": False, "order": 4},
     ]},
    {"unit_id": 2, "difficulty": 2,
     "question_text": "次の英単語の意味として正しいものを選びなさい。\n\n「consequence」",
     "explanation": "consequence は「結果、影響」という意味の名詞です。as a consequence（その結果として）の形もよく使われます。",
     "choices": [
         {"text": "原因", "correct": False, "order": 1},
         {"text": "結果", "correct": True, "order": 2},
         {"text": "自信", "correct": False, "order": 3},
         {"text": "続き", "correct": False, "order": 4},
     ]},
    # --- unit 3: 品詞の識別 ---
    {"unit_id": 3, "difficulty": 1,
     "question_text": "次の文で下線部の品詞は何ですか？\n\n「_Happiness_ is important to everyone.」",
     "explanation": "Happiness は「幸福」という意味の名詞で、この文の主語になっています。",
     "choices": [
         {"text": "名詞", "correct": True, "order": 1},
         {"text": "形容詞", "correct": False, "order": 2},
         {"text": "副詞", "correct": False, "order": 3},
         {"text": "動詞", "correct": False, "order": 4},
     ]},
    {"unit_id": 3, "difficulty": 1,
     "question_text": "次の文で下線部の品詞は何ですか？\n\n「The children _played_ in the park.」",
     "explanation": "played は「遊んだ」という意味の動詞（play の過去形）です。",
     "choices": [
         {"text": "名詞", "correct": False, "order": 1},
         {"text": "副詞", "correct": False, "order": 2},
         {"text": "動詞", "correct": True, "order": 3},
         {"text": "形容詞", "correct": False, "order": 4},
     ]},
    {"unit_id": 3, "difficulty": 1,
     "question_text": "次の文で下線部の品詞は何ですか？\n\n「He answered the question _correctly_.」",
     "explanation": "correctly は動詞 answered を修飾する副詞です。「正しく答えた」という意味になります。",
     "choices": [
         {"text": "名詞", "correct": False, "order": 1},
         {"text": "形容詞", "correct": False, "order": 2},
         {"text": "副詞", "correct": True, "order": 3},
         {"text": "動詞", "correct": False, "order": 4},
     ]},
    # --- unit 4: 品詞の働き ---
    {"unit_id": 4, "difficulty": 1,
     "question_text": "次の文で「hard」はどの語を修飾していますか？\n\n「He works hard every day.」",
     "explanation": "hard はここでは副詞で、動詞 works を修飾しています。「熱心に働く」という意味です。",
     "choices": [
         {"text": "He", "correct": False, "order": 1},
         {"text": "works", "correct": True, "order": 2},
         {"text": "every", "correct": False, "order": 3},
         {"text": "day", "correct": False, "order": 4},
     ]},
    {"unit_id": 4, "difficulty": 2,
     "question_text": "次の文で下線部の語は何の働きをしていますか？\n\n「_Reading_ books is fun.」",
     "explanation": "Reading は動名詞で、この文では主語として名詞の働きをしています。",
     "choices": [
         {"text": "主語（名詞の働き）", "correct": True, "order": 1},
         {"text": "動詞", "correct": False, "order": 2},
         {"text": "形容詞の働き", "correct": False, "order": 3},
         {"text": "副詞の働き", "correct": False, "order": 4},
     ]},
    {"unit_id": 4, "difficulty": 1,
     "question_text": "次の文で「red」はどの語を修飾していますか？\n\n「She has a red car.」",
     "explanation": "red は形容詞で、名詞 car を修飾しています。",
     "choices": [
         {"text": "She", "correct": False, "order": 1},
         {"text": "has", "correct": False, "order": 2},
         {"text": "car", "correct": True, "order": 3},
         {"text": "a", "correct": False, "order": 4},
     ]},
    # --- unit 5: 現在形 ---
    {"unit_id": 5, "difficulty": 1,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「I ___ two dogs.」",
     "explanation": "主語が I なので、have を使います（三人称単数の場合のみ has になります）。",
     "choices": [
         {"text": "have", "correct": True, "order": 1},
         {"text": "has", "correct": False, "order": 2},
         {"text": "having", "correct": False, "order": 3},
         {"text": "had", "correct": False, "order": 4},
     ]},
    {"unit_id": 5, "difficulty": 1,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「The sun ___ in the east.」",
     "explanation": "普遍的な真理・自然現象は現在形で表します。sun は三人称単数なので rises が正解です。",
     "choices": [
         {"text": "rise", "correct": False, "order": 1},
         {"text": "rises", "correct": True, "order": 2},
         {"text": "rose", "correct": False, "order": 3},
         {"text": "is rising", "correct": False, "order": 4},
     ]},
    {"unit_id": 5, "difficulty": 1,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「___ she like tea?」",
     "explanation": "三人称単数の疑問文は Does + 主語 + 動詞の原形の形になります。",
     "choices": [
         {"text": "Do", "correct": False, "order": 1},
         {"text": "Does", "correct": True, "order": 2},
         {"text": "Is", "correct": False, "order": 3},
         {"text": "Has", "correct": False, "order": 4},
     ]},
    # --- unit 6: 過去形 ---
    {"unit_id": 6, "difficulty": 1,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「We ___ our grandparents last weekend.」",
     "explanation": "last weekend は過去の時点を示すので、visit の過去形 visited が正解です。",
     "choices": [
         {"text": "visit", "correct": False, "order": 1},
         {"text": "visits", "correct": False, "order": 2},
         {"text": "visited", "correct": True, "order": 3},
         {"text": "have visited", "correct": False, "order": 4},
     ]},
    {"unit_id": 6, "difficulty": 1,
     "question_text": "次の動詞の過去形として正しいものを選びなさい。\n\n「buy」",
     "explanation": "buy の過去形は bought です。不規則変化動詞なので注意しましょう。",
     "choices": [
         {"text": "buyed", "correct": False, "order": 1},
         {"text": "bought", "correct": True, "order": 2},
         {"text": "buying", "correct": False, "order": 3},
         {"text": "boughted", "correct": False, "order": 4},
     ]},
    {"unit_id": 6, "difficulty": 2,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「Did you ___ the movie last night?」",
     "explanation": "Did を使った疑問文では、動詞は原形を使います。過去の意味はすでに Did に含まれています。",
     "choices": [
         {"text": "see", "correct": True, "order": 1},
         {"text": "saw", "correct": False, "order": 2},
         {"text": "seen", "correct": False, "order": 3},
         {"text": "seeing", "correct": False, "order": 4},
     ]},
    # --- unit 7: 現在完了形 ---
    {"unit_id": 7, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I have ___ finished my homework.」（すでに宿題を終えた）",
     "explanation": "already は「すでに」という意味で、完了用法の現在完了形とともによく使われ、have と過去分詞の間に置かれます。",
     "choices": [
         {"text": "yet", "correct": False, "order": 1},
         {"text": "already", "correct": True, "order": 2},
         {"text": "ever", "correct": False, "order": 3},
         {"text": "since", "correct": False, "order": 4},
     ]},
    {"unit_id": 7, "difficulty": 2,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「___ you ever been to Okinawa?」",
     "explanation": "経験を尋ねる現在完了形の疑問文は Have you ever + 過去分詞 ...? の形になります。",
     "choices": [
         {"text": "Do", "correct": False, "order": 1},
         {"text": "Did", "correct": False, "order": 2},
         {"text": "Have", "correct": True, "order": 3},
         {"text": "Are", "correct": False, "order": 4},
     ]},
    {"unit_id": 7, "difficulty": 2,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「She hasn't arrived ___.」（彼女はまだ到着していない）",
     "explanation": "否定文で「まだ」を表すときは yet を文末に置きます。",
     "choices": [
         {"text": "already", "correct": False, "order": 1},
         {"text": "yet", "correct": True, "order": 2},
         {"text": "just", "correct": False, "order": 3},
         {"text": "ever", "correct": False, "order": 4},
     ]},
    # --- unit 8: 過去完了形 ---
    {"unit_id": 8, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「By the time we got there, the movie ___ already ___.」",
     "explanation": "「私たちが着いた時にはすでに」という過去のある時点よりさらに前の出来事は過去完了形で表します。",
     "choices": [
         {"text": "has ... started", "correct": False, "order": 1},
         {"text": "had ... started", "correct": True, "order": 2},
         {"text": "was ... starting", "correct": False, "order": 3},
         {"text": "did ... start", "correct": False, "order": 4},
     ]},
    {"unit_id": 8, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I realized I ___ my wallet at home.」（財布を家に忘れてきたことに気づいた）",
     "explanation": "「気づいた」より前に「忘れてきた」という出来事があるため、過去完了形 had left を使います。",
     "choices": [
         {"text": "leave", "correct": False, "order": 1},
         {"text": "left", "correct": False, "order": 2},
         {"text": "had left", "correct": True, "order": 3},
         {"text": "have left", "correct": False, "order": 4},
     ]},
    {"unit_id": 8, "difficulty": 3,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「She was tired because she ___ all night for the exam.」",
     "explanation": "「疲れていた」原因が、それより前の時点から続いていた行為であるため、過去完了形 had studied を使います。",
     "choices": [
         {"text": "studies", "correct": False, "order": 1},
         {"text": "studied", "correct": False, "order": 2},
         {"text": "had studied", "correct": True, "order": 3},
         {"text": "has studied", "correct": False, "order": 4},
     ]},
    # --- unit 9: 進行形 ---
    {"unit_id": 9, "difficulty": 1,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「Be quiet! The baby ___.」",
     "explanation": "今まさに起きていることを表すので、現在進行形 is sleeping を使います。",
     "choices": [
         {"text": "sleeps", "correct": False, "order": 1},
         {"text": "is sleeping", "correct": True, "order": 2},
         {"text": "slept", "correct": False, "order": 3},
         {"text": "has slept", "correct": False, "order": 4},
     ]},
    {"unit_id": 9, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「While I ___ TV, my sister was doing her homework.」",
     "explanation": "過去のある時間帯に進行中だった動作は過去進行形で表します。while は「～している間」という意味です。",
     "choices": [
         {"text": "watch", "correct": False, "order": 1},
         {"text": "watched", "correct": False, "order": 2},
         {"text": "was watching", "correct": True, "order": 3},
         {"text": "have watched", "correct": False, "order": 4},
     ]},
    {"unit_id": 9, "difficulty": 2,
     "question_text": "次の文のうち、進行形にできない動詞を含むものはどれですか？\n\n（状態動詞 own を含む文を選びなさい）",
     "explanation": "own（所有する）は状態動詞なので、通常は進行形にできません。I am owning... とは言いません。",
     "choices": [
         {"text": "He is reading a book.", "correct": False, "order": 1},
         {"text": "I am owning a car.", "correct": True, "order": 2},
         {"text": "They are eating lunch.", "correct": False, "order": 3},
         {"text": "She is writing a letter.", "correct": False, "order": 4},
     ]},
    # --- unit 10: 未来表現 ---
    {"unit_id": 10, "difficulty": 1,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I ___ visit my grandmother next weekend. I've already planned it.」",
     "explanation": "すでに決まっている予定を表すときは be going to を使います。",
     "choices": [
         {"text": "will", "correct": False, "order": 1},
         {"text": "am going to", "correct": True, "order": 2},
         {"text": "would", "correct": False, "order": 3},
         {"text": "might", "correct": False, "order": 4},
     ]},
    {"unit_id": 10, "difficulty": 1,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「___ you help me carry this box?」（この箱を運ぶのを手伝ってくれますか）",
     "explanation": "その場での依頼は Will you ...? で表せます。",
     "choices": [
         {"text": "Will", "correct": True, "order": 1},
         {"text": "Do", "correct": False, "order": 2},
         {"text": "Are", "correct": False, "order": 3},
         {"text": "Did", "correct": False, "order": 4},
     ]},
    {"unit_id": 10, "difficulty": 1,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「The concert ___ at 7 pm tomorrow.」（コンサートは明日午後7時に始まる）",
     "explanation": "確定したスケジュールを表す未来の予定は現在形で表せます。",
     "choices": [
         {"text": "starts", "correct": True, "order": 1},
         {"text": "started", "correct": False, "order": 2},
         {"text": "is start", "correct": False, "order": 3},
         {"text": "starting", "correct": False, "order": 4},
     ]},
    # --- unit 11: 受動態の基本 ---
    {"unit_id": 11, "difficulty": 1,
     "question_text": "次の文を受動態に変えた場合、正しいものはどれですか？\n\n「Someone stole my bike.」",
     "explanation": "能動態の目的語 my bike が受動態の主語になります。My bike was stolen (by someone). となります。",
     "choices": [
         {"text": "My bike stole someone.", "correct": False, "order": 1},
         {"text": "My bike was stolen.", "correct": True, "order": 2},
         {"text": "My bike is stolen.", "correct": False, "order": 3},
         {"text": "My bike has stolen.", "correct": False, "order": 4},
     ]},
    {"unit_id": 11, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「This song ___ by a famous singer.」",
     "explanation": "「この歌はある有名な歌手によって書かれた」という過去の事実は、過去形の受動態 was written で表します。",
     "choices": [
         {"text": "wrote", "correct": False, "order": 1},
         {"text": "was written", "correct": True, "order": 2},
         {"text": "is written", "correct": False, "order": 3},
         {"text": "writes", "correct": False, "order": 4},
     ]},
    {"unit_id": 11, "difficulty": 1,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「These cookies ___ every day at the bakery.」",
     "explanation": "「毎日作られている」という習慣的な事実は現在形の受動態 are made で表します。",
     "choices": [
         {"text": "make", "correct": False, "order": 1},
         {"text": "are made", "correct": True, "order": 2},
         {"text": "made", "correct": False, "order": 3},
         {"text": "were made", "correct": False, "order": 4},
     ]},
    # --- unit 12: 受動態の応用 ---
    {"unit_id": 12, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「The news ___ to everyone by email.」（そのニュースはメールで全員に送られた）",
     "explanation": "SVOO文型の受動態で、直接目的語（news）を主語にした形です。過去のことなので was sent が正解です。",
     "choices": [
         {"text": "sent", "correct": False, "order": 1},
         {"text": "was sent", "correct": True, "order": 2},
         {"text": "is sent", "correct": False, "order": 3},
         {"text": "has sent", "correct": False, "order": 4},
     ]},
    {"unit_id": 12, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「This room ___ clean by the staff every morning.」（この部屋は毎朝スタッフによってきれいに保たれる）",
     "explanation": "keep O C（OをCに保つ）のSVOC文型の受動態です。補語 clean はそのまま残ります。",
     "choices": [
         {"text": "keeps", "correct": False, "order": 1},
         {"text": "is kept", "correct": True, "order": 2},
         {"text": "is keeping", "correct": False, "order": 3},
         {"text": "kept", "correct": False, "order": 4},
     ]},
    {"unit_id": 12, "difficulty": 3,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「He was made ___ his room by his mother.」（彼は母親に部屋を掃除させられた）",
     "explanation": "使役動詞 make の受動態では、原形不定詞ではなく to不定詞を使います。make O do → O is made to do。",
     "choices": [
         {"text": "clean", "correct": False, "order": 1},
         {"text": "to clean", "correct": True, "order": 2},
         {"text": "cleaning", "correct": False, "order": 3},
         {"text": "cleaned", "correct": False, "order": 4},
     ]},
    # --- unit 13: 助動詞の基本 ---
    {"unit_id": 13, "difficulty": 1,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「___ you swim?」（あなたは泳げますか）",
     "explanation": "能力を尋ねる表現は Can you ...? です。",
     "choices": [
         {"text": "Can", "correct": True, "order": 1},
         {"text": "Should", "correct": False, "order": 2},
         {"text": "Must", "correct": False, "order": 3},
         {"text": "Would", "correct": False, "order": 4},
     ]},
    {"unit_id": 13, "difficulty": 1,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「You ___ wear a seatbelt in the car.」（車ではシートベルトを着用しなければならない）",
     "explanation": "「～しなければならない」という義務・強制は must で表します。",
     "choices": [
         {"text": "may", "correct": False, "order": 1},
         {"text": "must", "correct": True, "order": 2},
         {"text": "would", "correct": False, "order": 3},
         {"text": "could", "correct": False, "order": 4},
     ]},
    {"unit_id": 13, "difficulty": 2,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「___ you pass the salt, please?」（塩を取っていただけますか）",
     "explanation": "Would you ...? は Will you ...? よりも丁寧な依頼表現です。",
     "choices": [
         {"text": "Would", "correct": True, "order": 1},
         {"text": "Must", "correct": False, "order": 2},
         {"text": "Should", "correct": False, "order": 3},
         {"text": "Do", "correct": False, "order": 4},
     ]},
    # --- unit 14: 助動詞の応用 ---
    {"unit_id": 14, "difficulty": 3,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「He ___ have missed the bus. He's not here yet.」（バスに乗り遅れたに違いない）",
     "explanation": "現在の状況からの過去の出来事に対する強い推量は must have + 過去分詞で表します。",
     "choices": [
         {"text": "must", "correct": True, "order": 1},
         {"text": "may", "correct": False, "order": 2},
         {"text": "should", "correct": False, "order": 3},
         {"text": "will", "correct": False, "order": 4},
     ]},
    {"unit_id": 14, "difficulty": 3,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「You ___ have called me. I was so worried about you.」（電話してくれればよかったのに）",
     "explanation": "「～すればよかったのに（しなかった）」という過去への非難・後悔は should have + 過去分詞です。",
     "choices": [
         {"text": "must", "correct": False, "order": 1},
         {"text": "should", "correct": True, "order": 2},
         {"text": "can", "correct": False, "order": 3},
         {"text": "will", "correct": False, "order": 4},
     ]},
    {"unit_id": 14, "difficulty": 3,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「She ___ have known about the surprise party; she looked so shocked.」（彼女がそのサプライズパーティーを知っていたはずがない）",
     "explanation": "「～だったはずがない」という過去に対する強い否定の推量は can't (cannot) have + 過去分詞で表します。",
     "choices": [
         {"text": "must", "correct": False, "order": 1},
         {"text": "should", "correct": False, "order": 2},
         {"text": "can't", "correct": True, "order": 3},
         {"text": "may", "correct": False, "order": 4},
     ]},
    # --- unit 15: 不定詞の名詞的用法 ---
    {"unit_id": 15, "difficulty": 1,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I hope ___ you again soon.」",
     "explanation": "hope は不定詞を目的語にとる動詞です。「またすぐに会えることを望む」という意味になります。",
     "choices": [
         {"text": "see", "correct": False, "order": 1},
         {"text": "to see", "correct": True, "order": 2},
         {"text": "seeing", "correct": False, "order": 3},
         {"text": "seen", "correct": False, "order": 4},
     ]},
    {"unit_id": 15, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「___ a new language takes time and effort.」（新しい言語を学ぶことは時間と努力を要する）",
     "explanation": "不定詞の名詞的用法は文の主語にもなれます。To learn ... で「～することは」という意味です。",
     "choices": [
         {"text": "Learn", "correct": False, "order": 1},
         {"text": "To learn", "correct": True, "order": 2},
         {"text": "Learned", "correct": False, "order": 3},
         {"text": "Learns", "correct": False, "order": 4},
     ]},
    {"unit_id": 15, "difficulty": 1,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「My dream is ___ a doctor in the future.」",
     "explanation": "不定詞の名詞的用法は be動詞の補語にもなれます。「私の夢は医者になることだ」という意味です。",
     "choices": [
         {"text": "become", "correct": False, "order": 1},
         {"text": "to become", "correct": True, "order": 2},
         {"text": "becoming", "correct": False, "order": 3},
         {"text": "became", "correct": False, "order": 4},
     ]},
    # --- unit 16: 不定詞の形容詞的・副詞的用法 ---
    {"unit_id": 16, "difficulty": 2,
     "question_text": "次の文の to hear は何用法ですか？\n\n「I was surprised to hear the news.」",
     "explanation": "to hear は surprised（感情）の原因を表しているので副詞的用法です。「その知らせを聞いて驚いた」の意味。",
     "choices": [
         {"text": "名詞的用法", "correct": False, "order": 1},
         {"text": "形容詞的用法", "correct": False, "order": 2},
         {"text": "副詞的用法", "correct": True, "order": 3},
         {"text": "どれでもない", "correct": False, "order": 4},
     ]},
    {"unit_id": 16, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「She has no time ___ TV these days.」（最近テレビを見る時間がない）",
     "explanation": "time を後ろから修飾する不定詞の形容詞的用法です。「テレビを見るための時間」という意味になります。",
     "choices": [
         {"text": "watch", "correct": False, "order": 1},
         {"text": "to watch", "correct": True, "order": 2},
         {"text": "watching", "correct": False, "order": 3},
         {"text": "watched", "correct": False, "order": 4},
     ]},
    {"unit_id": 16, "difficulty": 3,
     "question_text": "次の文の to become は何用法ですか？\n\n「He grew up to become a famous scientist.」",
     "explanation": "grew up to become は「成長して～になった」という結果を表す副詞的用法です。",
     "choices": [
         {"text": "名詞的用法", "correct": False, "order": 1},
         {"text": "形容詞的用法", "correct": False, "order": 2},
         {"text": "副詞的用法（結果）", "correct": True, "order": 3},
         {"text": "どれでもない", "correct": False, "order": 4},
     ]},
    # --- unit 17: 動名詞 ---
    {"unit_id": 17, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「___ the piano is my favorite hobby.」（ピアノを弾くことが私の一番好きな趣味だ）",
     "explanation": "動名詞は文の主語にもなれます。Playing で「弾くこと」という意味になります。",
     "choices": [
         {"text": "Play", "correct": False, "order": 1},
         {"text": "Played", "correct": False, "order": 2},
         {"text": "Playing", "correct": True, "order": 3},
         {"text": "To playing", "correct": False, "order": 4},
     ]},
    {"unit_id": 17, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I'm looking forward to ___ you at the party.」（パーティーであなたに会えるのを楽しみにしています）",
     "explanation": "look forward to は「～を楽しみに待つ」という意味の熟語で、to の後ろには動名詞が続きます（不定詞ではありません）。",
     "choices": [
         {"text": "see", "correct": False, "order": 1},
         {"text": "seeing", "correct": True, "order": 2},
         {"text": "seen", "correct": False, "order": 3},
         {"text": "saw", "correct": False, "order": 4},
     ]},
    {"unit_id": 17, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「He is good at ___ foreign languages.」（彼は外国語を学ぶのが得意だ）",
     "explanation": "be good at は「～が得意だ」という意味の熟語で、at の後ろには動名詞が続きます。",
     "choices": [
         {"text": "learn", "correct": False, "order": 1},
         {"text": "to learn", "correct": False, "order": 2},
         {"text": "learning", "correct": True, "order": 3},
         {"text": "learned", "correct": False, "order": 4},
     ]},
    # --- unit 18: 関係代名詞 ---
    {"unit_id": 18, "difficulty": 2,
     "question_text": "空所に入る最も適切な関係代名詞を選びなさい。\n\n「The woman ___ I met yesterday is a doctor.」",
     "explanation": "先行詞 The woman は人で、関係詞節内で met の目的語の役割です。目的格の who(m) を使います（口語では who も可）。",
     "choices": [
         {"text": "whom", "correct": True, "order": 1},
         {"text": "which", "correct": False, "order": 2},
         {"text": "whose", "correct": False, "order": 3},
         {"text": "what", "correct": False, "order": 4},
     ]},
    {"unit_id": 18, "difficulty": 2,
     "question_text": "空所に入る最も適切な関係代名詞を選びなさい。\n\n「This is the house ___ was built in 1990.」",
     "explanation": "先行詞 the house は物で、関係詞節内で was built の主語の役割を果たすので which が正解です。",
     "choices": [
         {"text": "who", "correct": False, "order": 1},
         {"text": "which", "correct": True, "order": 2},
         {"text": "whom", "correct": False, "order": 3},
         {"text": "whose", "correct": False, "order": 4},
     ]},
    {"unit_id": 18, "difficulty": 3,
     "question_text": "空所に入る最も適切な関係代名詞を選びなさい。\n\n「Everything ___ he said was true.」",
     "explanation": "先行詞に everything, anything, all などが来る場合は、関係代名詞は which ではなく that を使うのが一般的です。",
     "choices": [
         {"text": "what", "correct": False, "order": 1},
         {"text": "who", "correct": False, "order": 2},
         {"text": "that", "correct": True, "order": 3},
         {"text": "whose", "correct": False, "order": 4},
     ]},
    # --- unit 19: 関係副詞 ---
    {"unit_id": 19, "difficulty": 2,
     "question_text": "空所に入る最も適切な関係副詞を選びなさい。\n\n「Do you know the reason ___ he was absent yesterday?」",
     "explanation": "理由を表す先行詞 the reason の後ろでは why を使います。",
     "choices": [
         {"text": "where", "correct": False, "order": 1},
         {"text": "when", "correct": False, "order": 2},
         {"text": "why", "correct": True, "order": 3},
         {"text": "how", "correct": False, "order": 4},
     ]},
    {"unit_id": 19, "difficulty": 2,
     "question_text": "空所に入る最も適切な関係副詞を選びなさい。\n\n「That's the restaurant ___ we had dinner last night.」",
     "explanation": "場所を表す先行詞 the restaurant の後ろでは where を使います。",
     "choices": [
         {"text": "where", "correct": True, "order": 1},
         {"text": "when", "correct": False, "order": 2},
         {"text": "why", "correct": False, "order": 3},
         {"text": "which", "correct": False, "order": 4},
     ]},
    {"unit_id": 19, "difficulty": 2,
     "question_text": "空所に入る最も適切な関係副詞を選びなさい。\n\n「I still remember the day ___ I met her for the first time.」",
     "explanation": "時を表す先行詞 the day の後ろでは when を使います。",
     "choices": [
         {"text": "where", "correct": False, "order": 1},
         {"text": "when", "correct": True, "order": 2},
         {"text": "why", "correct": False, "order": 3},
         {"text": "which", "correct": False, "order": 4},
     ]},
    # --- unit 20: 比較の基本 ---
    {"unit_id": 20, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「This is the ___ book I have ever read.」（今まで読んだ中で最も面白い本だ）",
     "explanation": "interesting は長い形容詞なので、最上級は most interesting になります。",
     "choices": [
         {"text": "interestingest", "correct": False, "order": 1},
         {"text": "more interesting", "correct": False, "order": 2},
         {"text": "most interesting", "correct": True, "order": 3},
         {"text": "much interesting", "correct": False, "order": 4},
     ]},
    {"unit_id": 20, "difficulty": 1,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「My bag is ___ than yours.」",
     "explanation": "than があるので比較級を使います。heavy の比較級は y を i に変えて heavier です。",
     "choices": [
         {"text": "heavy", "correct": False, "order": 1},
         {"text": "heavier", "correct": True, "order": 2},
         {"text": "heaviest", "correct": False, "order": 3},
         {"text": "more heavy", "correct": False, "order": 4},
     ]},
    {"unit_id": 20, "difficulty": 1,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「He is the ___ runner in his class.」",
     "explanation": "the + 最上級 + in ~ の構文です。fast の最上級は fastest。",
     "choices": [
         {"text": "fast", "correct": False, "order": 1},
         {"text": "faster", "correct": False, "order": 2},
         {"text": "fastest", "correct": True, "order": 3},
         {"text": "most fast", "correct": False, "order": 4},
     ]},
    # --- unit 21: 比較の応用表現 ---
    {"unit_id": 21, "difficulty": 2,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「This is by far the ___ hotel in town.」（この町で断然一番良いホテルだ）",
     "explanation": "good の最上級は good - better - best と不規則変化します。by far は最上級を強調する表現です。",
     "choices": [
         {"text": "goodest", "correct": False, "order": 1},
         {"text": "better", "correct": False, "order": 2},
         {"text": "best", "correct": True, "order": 3},
         {"text": "most good", "correct": False, "order": 4},
     ]},
    {"unit_id": 21, "difficulty": 2,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「She has ___ books than I do.」（彼女は私より本の数が少ない）",
     "explanation": "数えられる名詞（books）の少なさを比較するときは fewer を使います。less は数えられない名詞に使います。",
     "choices": [
         {"text": "less", "correct": False, "order": 1},
         {"text": "fewer", "correct": True, "order": 2},
         {"text": "few", "correct": False, "order": 3},
         {"text": "little", "correct": False, "order": 4},
     ]},
    {"unit_id": 21, "difficulty": 2,
     "question_text": "空所に入る最も適切な語を選びなさい。\n\n「He is not as tall ___ his brother.」（彼は兄ほど背が高くない）",
     "explanation": "not as ~ as ... は「…ほど～ではない」という否定の原級比較です。",
     "choices": [
         {"text": "as", "correct": True, "order": 1},
         {"text": "than", "correct": False, "order": 2},
         {"text": "so", "correct": False, "order": 3},
         {"text": "like", "correct": False, "order": 4},
     ]},
    # --- unit 22: 仮定法過去 ---
    {"unit_id": 22, "difficulty": 3,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「If I ___ you, I would apologize to her.」（もし私があなたなら、彼女に謝るだろう）",
     "explanation": "仮定法過去では、be動詞は主語に関わらず were を使うのが原則です。",
     "choices": [
         {"text": "am", "correct": False, "order": 1},
         {"text": "was", "correct": False, "order": 2},
         {"text": "were", "correct": True, "order": 3},
         {"text": "be", "correct": False, "order": 4},
     ]},
    {"unit_id": 22, "difficulty": 3,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「If she had more time, she ___ join us.」",
     "explanation": "仮定法過去の帰結節は would + 動詞の原形で表します。",
     "choices": [
         {"text": "will", "correct": False, "order": 1},
         {"text": "would", "correct": True, "order": 2},
         {"text": "has", "correct": False, "order": 3},
         {"text": "had", "correct": False, "order": 4},
     ]},
    {"unit_id": 22, "difficulty": 2,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I wish I ___ speak French fluently.」（フランス語を流暢に話せたらなあ）",
     "explanation": "wish + 仮定法過去（could + 動詞の原形）で「～できたらなあ」という現在の願望を表します。",
     "choices": [
         {"text": "can", "correct": False, "order": 1},
         {"text": "could", "correct": True, "order": 2},
         {"text": "will", "correct": False, "order": 3},
         {"text": "may", "correct": False, "order": 4},
     ]},
    # --- unit 23: 仮定法過去完了 ---
    {"unit_id": 23, "difficulty": 3,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「If he had studied harder, he ___ passed the exam.」",
     "explanation": "仮定法過去完了の帰結節は would have + 過去分詞で表します。過去の事実に反する仮定です。",
     "choices": [
         {"text": "will have", "correct": False, "order": 1},
         {"text": "would have", "correct": True, "order": 2},
         {"text": "would", "correct": False, "order": 3},
         {"text": "had", "correct": False, "order": 4},
     ]},
    {"unit_id": 23, "difficulty": 3,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「If it ___ rained, we would have had a picnic.」",
     "explanation": "仮定法過去完了の条件節は if + had not + 過去分詞（否定形は had not / hadn't）で表します。",
     "choices": [
         {"text": "didn't", "correct": False, "order": 1},
         {"text": "hadn't", "correct": True, "order": 2},
         {"text": "wouldn't have", "correct": False, "order": 3},
         {"text": "hasn't", "correct": False, "order": 4},
     ]},
    {"unit_id": 23, "difficulty": 3,
     "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I wish I ___ him the truth back then.」（あの時、彼に本当のことを話していればよかった）",
     "explanation": "wish + 仮定法過去完了（had + 過去分詞）で「～していればよかったのに」という過去の後悔を表します。",
     "choices": [
         {"text": "tell", "correct": False, "order": 1},
         {"text": "told", "correct": False, "order": 2},
         {"text": "had told", "correct": True, "order": 3},
         {"text": "have told", "correct": False, "order": 4},
     ]},
]
# fmt: on


def seed():
    db = SessionLocal()
    try:
        existing_layers = db.query(Layer).count()
        if existing_layers == 0:
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
        else:
            print("Layers/Categories/Units already exist. Skipping.")

        existing_texts = {
            row[0] for row in db.query(Question.question_text).all()
        }
        new_count = 0
        for q_data in QUESTIONS:
            if q_data["question_text"] in existing_texts:
                continue

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
            new_count += 1

        db.commit()
        if new_count > 0:
            print(f"Inserted {new_count} new questions with choices")
        else:
            print("No new questions to add.")

        print(f"\nSeed status:")
        print(f"  Layers: {db.query(Layer).count()}")
        print(f"  Categories: {db.query(Category).count()}")
        print(f"  Units: {db.query(Unit).count()}")
        print(f"  Questions: {db.query(Question).count()}")
        print(f"  Choices: {db.query(Choice).count()}")

    finally:
        db.close()


if __name__ == "__main__":
    seed()
