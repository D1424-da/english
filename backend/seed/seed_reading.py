"""
読解・表現問題シードスクリプト（読解基礎・読解応用・表現）
既存データを消さずに追加のみ行う。

実行:
  cd backend && python -m seed.seed_reading
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal, engine, Base
from app.models import Unit, Question, Choice

Base.metadata.create_all(bind=engine)

READING_UNITS = [
    # 読解基礎 (category_id=10)
    {"code": "RD-001", "name": "短文の内容把握", "category_id": 10, "order_priority": 1,
     "description": "短い英文を読んで内容を正しく理解する"},
    {"code": "RD-002", "name": "指示語・代名詞の特定", "category_id": 10, "order_priority": 2,
     "description": "it, they, this などが何を指すか特定する"},
    # 読解応用 (category_id=11)
    {"code": "RD-003", "name": "段落の要旨把握", "category_id": 11, "order_priority": 1,
     "description": "パラグラフの主題・要旨を把握する"},
    {"code": "RD-004", "name": "推論・行間を読む", "category_id": 11, "order_priority": 2,
     "description": "明示されていない情報を文脈から推論する"},
    # 表現 (category_id=12)
    {"code": "EX-001", "name": "語句整序", "category_id": 12, "order_priority": 1,
     "description": "与えられた語句を正しい語順に並べる"},
    {"code": "EX-002", "name": "適語補充", "category_id": 12, "order_priority": 2,
     "description": "文脈に合う適切な語句を選ぶ"},
]

# fmt: off
READING_QUESTIONS = {
    # =========================================================================
    # 読解基礎: 短文の内容把握 (RD-001)
    # =========================================================================
    "RD-001": [
        {"difficulty": 2,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nTom usually gets up at seven, but yesterday he got up at six because he had to catch an early train.\n\n質問: なぜトムは昨日6時に起きたのですか？",
         "explanation": "because he had to catch an early train（早い電車に乗らなければならなかったから）が理由です。",
         "choices": [
             {"text": "早い電車に乗る必要があったから", "correct": True, "order": 1},
             {"text": "いつも6時に起きるから", "correct": False, "order": 2},
             {"text": "学校に遅刻しそうだったから", "correct": False, "order": 3},
             {"text": "目覚まし時計が鳴ったから", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nMy sister loves reading books. She goes to the library every Saturday and borrows three or four books each time.\n\n質問: 姉（妹）は毎週土曜日に何をしますか？",
         "explanation": "She goes to the library every Saturday（毎週土曜日に図書館に行く）が答えです。",
         "choices": [
             {"text": "図書館に行って本を借りる", "correct": True, "order": 1},
             {"text": "本屋で本を買う", "correct": False, "order": 2},
             {"text": "友達と映画を見る", "correct": False, "order": 3},
             {"text": "家で勉強する", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nThe weather was so bad that the soccer game was canceled. The players were very disappointed.\n\n質問: サッカーの試合はどうなりましたか？",
         "explanation": "the soccer game was canceled（試合は中止になった）とあります。天気が悪かったことが原因です。",
         "choices": [
             {"text": "中止になった", "correct": True, "order": 1},
             {"text": "延長された", "correct": False, "order": 2},
             {"text": "予定通り行われた", "correct": False, "order": 3},
             {"text": "別の場所で行われた", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nJapan is an island country surrounded by the sea. It has four main islands: Hokkaido, Honshu, Shikoku, and Kyushu.\n\n質問: この文によると、日本の主要な島はいくつですか？",
         "explanation": "four main islands（4つの主要な島）と明記されています。",
         "choices": [
             {"text": "4つ", "correct": True, "order": 1},
             {"text": "3つ", "correct": False, "order": 2},
             {"text": "5つ", "correct": False, "order": 3},
             {"text": "6つ", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nEmma wanted to buy a new dress for the party, but she didn't have enough money. So she decided to wear her mother's dress instead.\n\n質問: エマはパーティーで何を着ることにしましたか？",
         "explanation": "she decided to wear her mother's dress instead（代わりに母のドレスを着ることにした）が答えです。",
         "choices": [
             {"text": "母のドレス", "correct": True, "order": 1},
             {"text": "新しいドレス", "correct": False, "order": 2},
             {"text": "友達から借りたドレス", "correct": False, "order": 3},
             {"text": "古い自分のドレス", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nMore and more people are working from home these days. They can save time because they don't have to commute to the office.\n\n質問: 在宅勤務の利点として述べられていることは何ですか？",
         "explanation": "save time because they don't have to commute（通勤しなくてよいので時間を節約できる）が利点として述べられています。",
         "choices": [
             {"text": "通勤時間を節約できる", "correct": True, "order": 1},
             {"text": "給料が上がる", "correct": False, "order": 2},
             {"text": "同僚と会える", "correct": False, "order": 3},
             {"text": "運動ができる", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英文の意味として最も適切なものを選びなさい。\n\n「Despite the heavy rain, she decided to go out.」",
         "explanation": "despite は「～にもかかわらず」という意味の前置詞です。後ろには名詞（句）が続きます。",
         "choices": [
             {"text": "大雨のせいで、彼女は外出を決めた", "correct": False, "order": 1},
             {"text": "大雨にもかかわらず、彼女は外出を決めた", "correct": True, "order": 2},
             {"text": "大雨が降る前に、彼女は外出を決めた", "correct": False, "order": 3},
             {"text": "大雨が降ったので、彼女は外出をやめた", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英文の意味として最も適切なものを選びなさい。\n\n「He is not only smart but also kind.」",
         "explanation": "not only A but also B は「AだけでなくBも」という意味の相関接続詞です。",
         "choices": [
             {"text": "彼は賢いが優しくない", "correct": False, "order": 1},
             {"text": "彼は賢くないが優しい", "correct": False, "order": 2},
             {"text": "彼は賢いだけでなく優しくもある", "correct": True, "order": 3},
             {"text": "彼は賢くも優しくもない", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英文の意味として最も適切なものを選びなさい。\n\n「The more you practice, the better you become.」",
         "explanation": "the + 比較級, the + 比較級 で「～すればするほど…になる」の意味です。",
         "choices": [
             {"text": "もっと練習すれば、すぐに上手になる", "correct": False, "order": 1},
             {"text": "練習すればするほど、上手になる", "correct": True, "order": 2},
             {"text": "練習しても、上手にならない", "correct": False, "order": 3},
             {"text": "一番練習した人が一番上手だ", "correct": False, "order": 4},
         ]},
    ],

    # =========================================================================
    # 読解基礎: 指示語・代名詞の特定 (RD-002)
    # =========================================================================
    "RD-002": [
        {"difficulty": 2,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nKen bought a new bicycle last week. He rides it to school every day.\n\n質問: 下線部 it は何を指しますか？",
         "explanation": "it は前文の a new bicycle（新しい自転車）を指しています。",
         "choices": [
             {"text": "新しい自転車", "correct": True, "order": 1},
             {"text": "学校", "correct": False, "order": 2},
             {"text": "先週", "correct": False, "order": 3},
             {"text": "毎日", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nSakura and Yuki are classmates. They have been friends since elementary school.\n\n質問: 下線部 They は誰を指しますか？",
         "explanation": "They は前文の Sakura and Yuki（さくらとゆき）を指しています。",
         "choices": [
             {"text": "さくらとゆき", "correct": True, "order": 1},
             {"text": "クラスメイト全員", "correct": False, "order": 2},
             {"text": "小学校の先生たち", "correct": False, "order": 3},
             {"text": "さくらの友達", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nI tried to call my friend, but she didn't answer. This made me worried.\n\n質問: 下線部 This は何を指しますか？",
         "explanation": "This は「友達に電話したが出なかったこと」を指しています。",
         "choices": [
             {"text": "友達が電話に出なかったこと", "correct": True, "order": 1},
             {"text": "電話をかけたこと", "correct": False, "order": 2},
             {"text": "心配していること", "correct": False, "order": 3},
             {"text": "友達がいること", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nThe students visited the museum. There, they learned about the history of their city.\n\n質問: 下線部 There はどこを指しますか？",
         "explanation": "There は前文の the museum（博物館）を指しています。",
         "choices": [
             {"text": "博物館", "correct": True, "order": 1},
             {"text": "学校", "correct": False, "order": 2},
             {"text": "市役所", "correct": False, "order": 3},
             {"text": "図書館", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nSome people think that reading paper books is better than reading e-books. Others disagree with this opinion.\n\n質問: 下線部 this opinion とは何ですか？",
         "explanation": "this opinion は「紙の本を読む方が電子書籍より良いという考え」を指しています。",
         "choices": [
             {"text": "紙の本の方が電子書籍より良いという考え", "correct": True, "order": 1},
             {"text": "電子書籍の方が良いという考え", "correct": False, "order": 2},
             {"text": "本を読むべきだという考え", "correct": False, "order": 3},
             {"text": "多くの人が賛成しているという考え", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nThe teacher gave each student a piece of paper and asked them to write their names on it.\n\n質問: 下線部 it は何を指しますか？",
         "explanation": "it は a piece of paper（紙）を指しています。each student に1枚ずつ配られた紙のことです。",
         "choices": [
             {"text": "紙", "correct": True, "order": 1},
             {"text": "名前", "correct": False, "order": 2},
             {"text": "教室", "correct": False, "order": 3},
             {"text": "黒板", "correct": False, "order": 4},
         ]},
    ],

    # =========================================================================
    # 読解応用: 段落の要旨把握 (RD-003)
    # =========================================================================
    "RD-003": [
        {"difficulty": 3,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nSleep is very important for our health. When we sleep, our body repairs itself and our brain organizes the information we learned during the day. Without enough sleep, we cannot concentrate well and may get sick more easily.\n\n質問: この文章の主題は何ですか？",
         "explanation": "文章全体が睡眠の重要性について述べており、体の修復・脳の整理・集中力への影響を挙げています。",
         "choices": [
             {"text": "睡眠が健康にとって重要であること", "correct": True, "order": 1},
             {"text": "脳の仕組み", "correct": False, "order": 2},
             {"text": "病気の予防法", "correct": False, "order": 3},
             {"text": "集中力を高める方法", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nPlastic pollution has become a serious problem around the world. Millions of tons of plastic waste end up in the ocean every year, harming sea animals and polluting the water. Many countries are now trying to reduce plastic use by banning single-use plastic bags.\n\n質問: この文章で筆者が最も伝えたいことは何ですか？",
         "explanation": "プラスチック汚染が深刻な問題であり、各国が対策を取り始めていることが主旨です。",
         "choices": [
             {"text": "プラスチック汚染は深刻な世界的問題である", "correct": True, "order": 1},
             {"text": "海の動物は絶滅の危機にある", "correct": False, "order": 2},
             {"text": "プラスチック袋を使うべきではない", "correct": False, "order": 3},
             {"text": "海の水は汚れている", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nVolunteering can benefit both the community and the volunteer. By helping others, volunteers can develop new skills, make friends, and feel a sense of purpose. At the same time, communities receive much-needed support.\n\n質問: この文章の要旨として最も適切なものはどれですか？",
         "explanation": "ボランティアは地域社会とボランティアの双方に利益があるという点が主旨です。",
         "choices": [
             {"text": "ボランティアは双方に利益をもたらす", "correct": True, "order": 1},
             {"text": "ボランティアはスキルを身につけられる", "correct": False, "order": 2},
             {"text": "地域社会は支援を必要としている", "correct": False, "order": 3},
             {"text": "友達を作ることが大切である", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nLearning a second language has many advantages. Research shows that bilingual people are better at solving problems and can switch between tasks more easily. Moreover, knowing another language opens doors to different cultures and career opportunities.\n\n質問: この文章の主な内容は何ですか？",
         "explanation": "第二言語を学ぶことの利点（問題解決能力・文化理解・キャリア）について述べています。",
         "choices": [
             {"text": "第二言語を学ぶことの利点", "correct": True, "order": 1},
             {"text": "バイリンガルの脳の仕組み", "correct": False, "order": 2},
             {"text": "キャリアアップの方法", "correct": False, "order": 3},
             {"text": "異文化交流の大切さ", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nArtificial intelligence is changing the way we live and work. AI can analyze large amounts of data quickly and help doctors diagnose diseases more accurately. However, some people worry that AI may replace human jobs in the future.\n\n質問: この文章で述べられていることとして正しいものはどれですか？",
         "explanation": "AIの利点（データ分析・医療支援）と懸念（雇用への影響）の両面が述べられています。",
         "choices": [
             {"text": "AIには利点と懸念の両方がある", "correct": True, "order": 1},
             {"text": "AIは必ず人間の仕事を奪う", "correct": False, "order": 2},
             {"text": "AIは医療分野だけで使われている", "correct": False, "order": 3},
             {"text": "AIに反対する人が多数派である", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nTraditional Japanese gardens are designed to represent nature in a small space. They often include rocks, water, and carefully chosen plants. Every element is placed with great thought to create a feeling of peace and harmony.\n\n質問: この文章によると、日本庭園の特徴は何ですか？",
         "explanation": "自然を小さな空間に表現し、平和と調和の感覚を作り出すことが特徴として述べられています。",
         "choices": [
             {"text": "小さな空間に自然を表現し調和を生み出す", "correct": True, "order": 1},
             {"text": "できるだけ多くの植物を植える", "correct": False, "order": 2},
             {"text": "西洋庭園を模倣している", "correct": False, "order": 3},
             {"text": "大きな池を必ず含む", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英文の空所に入る最も適切な語を選びなさい。\n\n「It is important for students to develop critical thinking skills. ___, they should read various kinds of books.」",
         "explanation": "前文で「批判的思考力を身につけることが重要」と述べ、その方法として「様々な本を読むべき」と続けるので、Therefore（したがって）が適切です。",
         "choices": [
             {"text": "However", "correct": False, "order": 1},
             {"text": "Therefore", "correct": True, "order": 2},
             {"text": "Meanwhile", "correct": False, "order": 3},
             {"text": "Otherwise", "correct": False, "order": 4},
         ]},
    ],

    # =========================================================================
    # 読解応用: 推論・行間を読む (RD-004)
    # =========================================================================
    "RD-004": [
        {"difficulty": 3,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nWhen Lisa came home, she found the front door open and muddy footprints on the floor. Her dog Max was hiding under the table with a guilty look on his face.\n\n質問: この場面から推測できることは何ですか？",
         "explanation": "ドアが開いていて泥の足跡があり、犬が罪悪感のある表情で隠れていることから、犬が外に出て泥だらけで戻ったと推測できます。",
         "choices": [
             {"text": "犬が外に出て泥だらけで戻ってきた", "correct": True, "order": 1},
             {"text": "泥棒が家に入った", "correct": False, "order": 2},
             {"text": "リサが泥を持ち込んだ", "correct": False, "order": 3},
             {"text": "犬が病気になった", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nMr. Tanaka looked at his watch for the third time and sighed. The meeting was supposed to start at 2:00, and it was already 2:30. He tapped his fingers on the table impatiently.\n\n質問: 田中さんの気持ちとして最も適切なものはどれですか？",
         "explanation": "何度も時計を見てため息をつき、イライラして指でテーブルを叩いていることから、待たされていら立っていると推測できます。",
         "choices": [
             {"text": "待たされていら立っている", "correct": True, "order": 1},
             {"text": "会議が楽しみでわくわくしている", "correct": False, "order": 2},
             {"text": "疲れて眠そうにしている", "correct": False, "order": 3},
             {"text": "会議の準備をしている", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nAfter the exam, Yuki walked out of the classroom with a big smile. She called her mother right away and said, \"I think I did really well!\"\n\n質問: ユキの試験の結果について推測できることは何ですか？",
         "explanation": "大きな笑顔で出てきて、お母さんにすぐ電話して「うまくいったと思う」と言っていることから、手応えがあったと推測できます。",
         "choices": [
             {"text": "試験がうまくいったと感じている", "correct": True, "order": 1},
             {"text": "試験が難しすぎて困っている", "correct": False, "order": 2},
             {"text": "試験を受けられなかった", "correct": False, "order": 3},
             {"text": "結果にがっかりしている", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nThe small café on the corner used to be full of customers every weekend. But since the new shopping mall opened nearby, the café has had very few visitors. The owner is now thinking about closing the business.\n\n質問: このカフェの客が減った原因は何だと考えられますか？",
         "explanation": "近くにショッピングモールが開店して以来、客が激減したと書かれているので、モール開業が原因と推測できます。",
         "choices": [
             {"text": "近くにショッピングモールができたから", "correct": True, "order": 1},
             {"text": "料理の質が下がったから", "correct": False, "order": 2},
             {"text": "値段が上がったから", "correct": False, "order": 3},
             {"text": "道路工事が始まったから", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nDavid has been practicing the piano for three hours every day for the past six months. His teacher says he has improved a lot, but David still feels he is not good enough. He wants to win the national competition next year.\n\n質問: デイビッドについて推測できることは何ですか？",
         "explanation": "毎日3時間・6ヶ月練習し、全国大会で優勝したいと思っていることから、非常に向上心が強い人物だと推測できます。",
         "choices": [
             {"text": "とても向上心が強い", "correct": True, "order": 1},
             {"text": "ピアノが嫌いになりかけている", "correct": False, "order": 2},
             {"text": "先生の指導に不満がある", "correct": False, "order": 3},
             {"text": "すでに大会で優勝した", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英文を読んで、質問に答えなさい。\n\nThe line at the new ramen shop stretched around the block. People were waiting for over an hour just to get a seat. One customer said, \"It's totally worth the wait.\"\n\n質問: このラーメン店について推測できることは何ですか？",
         "explanation": "行列がブロックの周りまで伸び、1時間以上待っても「待つ価値がある」と言われていることから、非常に人気があると推測できます。",
         "choices": [
             {"text": "非常に人気がある", "correct": True, "order": 1},
             {"text": "店員が足りない", "correct": False, "order": 2},
             {"text": "値段が安い", "correct": False, "order": 3},
             {"text": "まもなく閉店する", "correct": False, "order": 4},
         ]},
    ],

    # =========================================================================
    # 表現: 語句整序 (EX-001)
    # =========================================================================
    "EX-001": [
        {"difficulty": 2,
         "question_text": "次の日本文の意味になるように、語句を正しく並べかえたものを選びなさい。\n\n「私は昨日公園でテニスをしました。」\n\n語句: [ tennis / I / in the park / played / yesterday ]",
         "explanation": "SVO＋場所＋時の語順で I played tennis in the park yesterday が正しい語順です。",
         "choices": [
             {"text": "I played tennis in the park yesterday.", "correct": True, "order": 1},
             {"text": "I tennis played in the park yesterday.", "correct": False, "order": 2},
             {"text": "Yesterday I in the park played tennis.", "correct": False, "order": 3},
             {"text": "I played yesterday tennis in the park.", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の日本文の意味になるように、語句を正しく並べかえたものを選びなさい。\n\n「彼女は英語を話すのが上手です。」\n\n語句: [ speaking / she / at / good / English / is ]",
         "explanation": "be good at ~ing で「〜するのが得意である」。She is good at speaking English が正解です。",
         "choices": [
             {"text": "She is good at speaking English.", "correct": True, "order": 1},
             {"text": "She is speaking good at English.", "correct": False, "order": 2},
             {"text": "She good is at speaking English.", "correct": False, "order": 3},
             {"text": "She is at good speaking English.", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の日本文の意味になるように、語句を正しく並べかえたものを選びなさい。\n\n「この本は私にとって難しすぎる。」\n\n語句: [ too / this book / for / is / difficult / me ]",
         "explanation": "too ... for ~ の構文で This book is too difficult for me が正解です。",
         "choices": [
             {"text": "This book is too difficult for me.", "correct": True, "order": 1},
             {"text": "This book is difficult too for me.", "correct": False, "order": 2},
             {"text": "This book for me is too difficult.", "correct": False, "order": 3},
             {"text": "Too difficult this book is for me.", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の日本文の意味になるように、語句を正しく並べかえたものを選びなさい。\n\n「あなたは何回日本に来たことがありますか？」\n\n語句: [ have / how many times / to Japan / you / come ]",
         "explanation": "現在完了の疑問文で How many times have you come to Japan? が正解です。",
         "choices": [
             {"text": "How many times have you come to Japan?", "correct": True, "order": 1},
             {"text": "How many times you have come to Japan?", "correct": False, "order": 2},
             {"text": "Have you how many times come to Japan?", "correct": False, "order": 3},
             {"text": "How many times have come you to Japan?", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の日本文の意味になるように、語句を正しく並べかえたものを選びなさい。\n\n「もし明日雨が降ったら、私は家にいます。」\n\n語句: [ rains / I / it / if / will / home / tomorrow / stay ]",
         "explanation": "if節（条件）は現在形、主節は will + 動詞原形。If it rains tomorrow, I will stay home. が正解です。",
         "choices": [
             {"text": "If it rains tomorrow, I will stay home.", "correct": True, "order": 1},
             {"text": "If it will rain tomorrow, I stay home.", "correct": False, "order": 2},
             {"text": "I will stay home if it will rains tomorrow.", "correct": False, "order": 3},
             {"text": "If tomorrow it rains, I will home stay.", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の日本文の意味になるように、語句を正しく並べかえたものを選びなさい。\n\n「私が昨日会った女性は医者です。」\n\n語句: [ the woman / met / I / yesterday / a doctor / is / whom ]",
         "explanation": "関係代名詞 whom を使った文。The woman whom I met yesterday is a doctor. が正解です。",
         "choices": [
             {"text": "The woman whom I met yesterday is a doctor.", "correct": True, "order": 1},
             {"text": "The woman I whom met yesterday is a doctor.", "correct": False, "order": 2},
             {"text": "The woman whom met I yesterday is a doctor.", "correct": False, "order": 3},
             {"text": "Whom the woman I met yesterday is a doctor.", "correct": False, "order": 4},
         ]},
    ],

    # =========================================================================
    # 表現: 適語補充 (EX-002)
    # =========================================================================
    "EX-002": [
        {"difficulty": 2,
         "question_text": "次の英文の空所に入る最も適切な語を選びなさい。\n\nI'm looking forward (    ) seeing you again.",
         "explanation": "look forward to ~ing で「〜を楽しみにしている」。to が正解です。",
         "choices": [
             {"text": "to", "correct": True, "order": 1},
             {"text": "for", "correct": False, "order": 2},
             {"text": "of", "correct": False, "order": 3},
             {"text": "at", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英文の空所に入る最も適切な語を選びなさい。\n\nShe is interested (    ) learning Japanese culture.",
         "explanation": "be interested in で「〜に興味がある」。in が正解です。",
         "choices": [
             {"text": "in", "correct": True, "order": 1},
             {"text": "on", "correct": False, "order": 2},
             {"text": "at", "correct": False, "order": 3},
             {"text": "to", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英文の空所に入る最も適切な語を選びなさい。\n\nThe movie was so boring (    ) I fell asleep.",
         "explanation": "so ... that ~ で「あまりに〜なので…」。that が正解です。",
         "choices": [
             {"text": "that", "correct": True, "order": 1},
             {"text": "than", "correct": False, "order": 2},
             {"text": "which", "correct": False, "order": 3},
             {"text": "because", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の英文の空所に入る最も適切な語を選びなさい。\n\nYou had better (    ) a doctor as soon as possible.",
         "explanation": "had better + 動詞原形 で「〜した方がよい」。see が正解です。",
         "choices": [
             {"text": "see", "correct": True, "order": 1},
             {"text": "seeing", "correct": False, "order": 2},
             {"text": "to see", "correct": False, "order": 3},
             {"text": "seen", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英文の空所に入る最も適切な語句を選びなさい。\n\nNot only (    ) speak English, but she can also speak French.",
         "explanation": "Not only の後は倒置になり can she speak の語順になります。",
         "choices": [
             {"text": "can she", "correct": True, "order": 1},
             {"text": "she can", "correct": False, "order": 2},
             {"text": "does she", "correct": False, "order": 3},
             {"text": "she does", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "次の英文の空所に入る最も適切な語句を選びなさい。\n\nThe city (    ) I was born has changed a lot.",
         "explanation": "場所を先行詞とする関係副詞 where が正解。The city where I was born で「私が生まれた街」。",
         "choices": [
             {"text": "where", "correct": True, "order": 1},
             {"text": "which", "correct": False, "order": 2},
             {"text": "what", "correct": False, "order": 3},
             {"text": "when", "correct": False, "order": 4},
         ]},
    ],
}
# fmt: on


def seed_reading():
    db = SessionLocal()
    try:
        existing_unit_codes = {
            row[0] for row in db.query(Unit.code).all()
        }
        unit_code_to_id = {}

        new_unit_count = 0
        for u_data in READING_UNITS:
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
            print(f"Added {new_unit_count} new reading/expression units")
        else:
            print("All reading/expression units already exist.")

        existing_texts = {
            row[0] for row in db.query(Question.question_text).all()
        }
        new_q_count = 0
        for unit_code, questions in READING_QUESTIONS.items():
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
            print(f"Added {new_q_count} new reading/expression questions")
        else:
            print("No new reading/expression questions to add.")

        print(f"\nReading seed status:")
        print(f"  Total Units: {db.query(Unit).count()}")
        print(f"  Total Questions: {db.query(Question).count()}")

    finally:
        db.close()


if __name__ == "__main__":
    seed_reading()
