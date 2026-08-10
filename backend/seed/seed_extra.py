"""
弱点克服用の追加問題シードスクリプト。
文法・文構造の各単元に演習問題を追加する（既存データは消さない）。

実行:
  cd backend && python -m seed.seed_extra
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal, engine, Base
from app.models import Unit, Question, Choice

Base.metadata.create_all(bind=engine)

# fmt: off
EXTRA_QUESTIONS = {
    # ===== 時制 =====
    "TS-001": [
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語を選びなさい。\n\n「My brother ___ to school by bus.」",
         "explanation": "主語 My brother は三人称単数なので、goes を使います。",
         "choices": [
             {"text": "go", "correct": False, "order": 1},
             {"text": "goes", "correct": True, "order": 2},
             {"text": "going", "correct": False, "order": 3},
             {"text": "gone", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語を選びなさい。\n\n「The store ___ at ten every morning.」",
         "explanation": "every morning（毎朝）という習慣を表すので現在形。主語 The store は三人称単数なので opens です。",
         "choices": [
             {"text": "open", "correct": False, "order": 1},
             {"text": "opens", "correct": True, "order": 2},
             {"text": "opening", "correct": False, "order": 3},
             {"text": "opened", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「My sister ___ math every day.」",
         "explanation": "study の三人称単数形は y を i に変えて es をつけ、studies になります。",
         "choices": [
             {"text": "study", "correct": False, "order": 1},
             {"text": "studys", "correct": False, "order": 2},
             {"text": "studies", "correct": True, "order": 3},
             {"text": "studying", "correct": False, "order": 4},
         ]},
    ],
    "TS-002": [
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語を選びなさい。\n\n「I ___ a letter to my friend yesterday.」",
         "explanation": "write の過去形は wrote です。不規則変化動詞です。",
         "choices": [
             {"text": "write", "correct": False, "order": 1},
             {"text": "writed", "correct": False, "order": 2},
             {"text": "wrote", "correct": True, "order": 3},
             {"text": "written", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "次の動詞の過去形として正しいものを選びなさい。\n\n「bring」",
         "explanation": "bring の過去形は brought です。think-thought, buy-bought と同じ -ought のパターンです。",
         "choices": [
             {"text": "bringed", "correct": False, "order": 1},
             {"text": "brought", "correct": True, "order": 2},
             {"text": "brang", "correct": False, "order": 3},
             {"text": "bringing", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「She ___ go to the party last night.」（彼女は昨夜パーティーに行かなかった）",
         "explanation": "一般動詞の過去の否定文は didn't + 動詞の原形で表します。",
         "choices": [
             {"text": "doesn't", "correct": False, "order": 1},
             {"text": "didn't", "correct": True, "order": 2},
             {"text": "wasn't", "correct": False, "order": 3},
             {"text": "not", "correct": False, "order": 4},
         ]},
    ],
    "TS-003": [
        {"difficulty": 2,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I have ___ in Tokyo for ten years.」（東京に10年間住んでいる）",
         "explanation": "「ずっと〜している」という継続は have + 過去分詞で表します。live の過去分詞は lived です。",
         "choices": [
             {"text": "live", "correct": False, "order": 1},
             {"text": "living", "correct": False, "order": 2},
             {"text": "lived", "correct": True, "order": 3},
             {"text": "to live", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "空所に入る最も適切な語を選びなさい。\n\n「He has been sick ___ last Friday.」",
         "explanation": "since は「〜以来」と起点を表し、現在完了の継続用法とともに使います。for は期間を表します。",
         "choices": [
             {"text": "for", "correct": False, "order": 1},
             {"text": "since", "correct": True, "order": 2},
             {"text": "from", "correct": False, "order": 3},
             {"text": "at", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I have never ___ such a beautiful sunset.」",
         "explanation": "never を使った経験の否定は have never + 過去分詞。see の過去分詞は seen です。",
         "choices": [
             {"text": "see", "correct": False, "order": 1},
             {"text": "saw", "correct": False, "order": 2},
             {"text": "seen", "correct": True, "order": 3},
             {"text": "seeing", "correct": False, "order": 4},
         ]},
    ],
    "TS-004": [
        {"difficulty": 2,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「When she called me, I ___ already gone to bed.」",
         "explanation": "「彼女が電話してきた」時点より前に「寝てしまっていた」ので過去完了形 had gone を使います。",
         "choices": [
             {"text": "has", "correct": False, "order": 1},
             {"text": "had", "correct": True, "order": 2},
             {"text": "have", "correct": False, "order": 3},
             {"text": "was", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「She said she ___ the movie before.」（彼女は以前その映画を見たことがあると言った）",
         "explanation": "「言った」時点より前の経験なので、過去完了形 had seen を使います。",
         "choices": [
             {"text": "sees", "correct": False, "order": 1},
             {"text": "has seen", "correct": False, "order": 2},
             {"text": "had seen", "correct": True, "order": 3},
             {"text": "seeing", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I had never eaten sushi ___ I came to Japan.」",
         "explanation": "「日本に来るまでは一度も寿司を食べたことがなかった」。before（〜する前は）が適切です。",
         "choices": [
             {"text": "before", "correct": True, "order": 1},
             {"text": "after", "correct": False, "order": 2},
             {"text": "since", "correct": False, "order": 3},
             {"text": "while", "correct": False, "order": 4},
         ]},
    ],
    "TS-005": [
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「Please be quiet. I ___ to music now.」（静かにして。今、音楽を聴いているの）",
         "explanation": "now（今）まさに進行中の動作なので、現在進行形 am listening を使います。",
         "choices": [
             {"text": "listen", "correct": False, "order": 1},
             {"text": "am listening", "correct": True, "order": 2},
             {"text": "listened", "correct": False, "order": 3},
             {"text": "have listened", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「What ___ you doing at 8 pm yesterday?」",
         "explanation": "過去のある時点で進行中だった動作を尋ねる過去進行形の疑問文。主語が you なので were を使います。",
         "choices": [
             {"text": "are", "correct": False, "order": 1},
             {"text": "was", "correct": False, "order": 2},
             {"text": "were", "correct": True, "order": 3},
             {"text": "did", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "run を進行形にするとき、正しい -ing 形はどれですか？",
         "explanation": "run は n を重ねて running になります。swim→swimming, sit→sitting も同じパターンです。",
         "choices": [
             {"text": "runing", "correct": False, "order": 1},
             {"text": "running", "correct": True, "order": 2},
             {"text": "ranning", "correct": False, "order": 3},
             {"text": "runned", "correct": False, "order": 4},
         ]},
    ],
    "TS-006": [
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「A: The phone is ringing. B: OK, I ___ answer it.」",
         "explanation": "その場で決めたことは will で表します。前から決めていた予定ではないので be going to は不自然です。",
         "choices": [
             {"text": "will", "correct": True, "order": 1},
             {"text": "am going to", "correct": False, "order": 2},
             {"text": "was going to", "correct": False, "order": 3},
             {"text": "would", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「We ___ a party next Saturday. We have already sent the invitations.」",
         "explanation": "招待状をすでに送っている＝前から決めていた予定なので、be going to で表します。主語 We には are going to を使います。",
         "choices": [
             {"text": "are going to have", "correct": True, "order": 1},
             {"text": "are go to have", "correct": False, "order": 2},
             {"text": "going to have", "correct": False, "order": 3},
             {"text": "are going have", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I'll call you when I ___ home.」",
         "explanation": "when や if で始まる時・条件の副詞節の中では、未来のことでも現在形で表します。",
         "choices": [
             {"text": "will get", "correct": False, "order": 1},
             {"text": "get", "correct": True, "order": 2},
             {"text": "got", "correct": False, "order": 3},
             {"text": "getting", "correct": False, "order": 4},
         ]},
    ],
    # ===== 態 =====
    "VO-001": [
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「Soccer ___ by children all over the world.」（サッカーは世界中の子どもたちにプレーされている）",
         "explanation": "「プレーされている」という受動態は be動詞 + 過去分詞で、is played となります。",
         "choices": [
             {"text": "plays", "correct": False, "order": 1},
             {"text": "is played", "correct": True, "order": 2},
             {"text": "is playing", "correct": False, "order": 3},
             {"text": "played", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「This picture ___ by my grandfather 50 years ago.」",
         "explanation": "50年前のことなので過去形の受動態 was taken を使います。take a picture（写真を撮る）の take です。",
         "choices": [
             {"text": "is taken", "correct": False, "order": 1},
             {"text": "was taken", "correct": True, "order": 2},
             {"text": "took", "correct": False, "order": 3},
             {"text": "has taken", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の文を受動態に変えた場合、正しいものはどれですか？\n\n「Many people love this song.」",
         "explanation": "目的語 this song を主語にして、This song is loved by many people. となります。",
         "choices": [
             {"text": "This song is loved by many people.", "correct": True, "order": 1},
             {"text": "This song loves many people.", "correct": False, "order": 2},
             {"text": "This song was loved by many people.", "correct": False, "order": 3},
             {"text": "Many people are loved by this song.", "correct": False, "order": 4},
         ]},
    ],
    "VO-002": [
        {"difficulty": 2,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I ___ a present by my friend.」（友達からプレゼントをもらった）",
         "explanation": "give 人 物 のSVOO文型で、人を主語にした受動態は was given となります。",
         "choices": [
             {"text": "gave", "correct": False, "order": 1},
             {"text": "was given", "correct": True, "order": 2},
             {"text": "was giving", "correct": False, "order": 3},
             {"text": "given", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "空所に入る最も適切な語を選びなさい。\n\n「Mt. Fuji is covered ___ snow in winter.」",
         "explanation": "be covered with で「〜で覆われている」。by ではなく with を使う点に注意しましょう。",
         "choices": [
             {"text": "by", "correct": False, "order": 1},
             {"text": "with", "correct": True, "order": 2},
             {"text": "at", "correct": False, "order": 3},
             {"text": "for", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "空所に入る最も適切な語を選びなさい。\n\n「He is known ___ everyone in this town.」（彼はこの町の誰にでも知られている）",
         "explanation": "be known to で「〜に知られている」。by ではなく to を使う慣用表現です。",
         "choices": [
             {"text": "by", "correct": False, "order": 1},
             {"text": "to", "correct": True, "order": 2},
             {"text": "with", "correct": False, "order": 3},
             {"text": "as", "correct": False, "order": 4},
         ]},
    ],
    # ===== 助動詞 =====
    "MD-001": [
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語を選びなさい。\n\n「He ___ speak three languages.」（彼は3か国語を話すことができる）",
         "explanation": "「〜できる」という能力は can で表します。may は「〜かもしれない・〜してもよい」です。",
         "choices": [
             {"text": "can", "correct": True, "order": 1},
             {"text": "must", "correct": False, "order": 2},
             {"text": "should", "correct": False, "order": 3},
             {"text": "may", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「You ___ eat too much candy. It's bad for your teeth.」",
         "explanation": "「〜してはいけない」という禁止は must not (mustn't) で表します。",
         "choices": [
             {"text": "must", "correct": False, "order": 1},
             {"text": "mustn't", "correct": True, "order": 2},
             {"text": "may", "correct": False, "order": 3},
             {"text": "can", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「You ___ see a dentist about that tooth.」（その歯は歯医者に診てもらった方がいいよ）",
         "explanation": "「〜した方がよい」という助言は should で表します。",
         "choices": [
             {"text": "should", "correct": True, "order": 1},
             {"text": "may", "correct": False, "order": 2},
             {"text": "can", "correct": False, "order": 3},
             {"text": "will", "correct": False, "order": 4},
         ]},
    ],
    "MD-002": [
        {"difficulty": 3,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「The ground is wet. It ___ have rained last night.」",
         "explanation": "「地面が濡れている」という証拠から「雨が降ったに違いない」と推量するので must have + 過去分詞です。",
         "choices": [
             {"text": "must", "correct": True, "order": 1},
             {"text": "can", "correct": False, "order": 2},
             {"text": "will", "correct": False, "order": 3},
             {"text": "shall", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I ___ have brought an umbrella. It's raining now.」（傘を持ってくればよかった）",
         "explanation": "「〜すればよかった（のにしなかった）」という後悔は should have + 過去分詞で表します。",
         "choices": [
             {"text": "should", "correct": True, "order": 1},
             {"text": "must", "correct": False, "order": 2},
             {"text": "can", "correct": False, "order": 3},
             {"text": "may", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「She ___ have taken your umbrella. She wasn't here today.」（彼女が傘を持っていったはずがない）",
         "explanation": "「〜したはずがない」という強い否定の推量は can't have + 過去分詞で表します。",
         "choices": [
             {"text": "can't", "correct": True, "order": 1},
             {"text": "must", "correct": False, "order": 2},
             {"text": "should", "correct": False, "order": 3},
             {"text": "would", "correct": False, "order": 4},
         ]},
    ],
    # ===== 不定詞・動名詞 =====
    "IF-001": [
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「She promised ___ me this evening.」（彼女は今晩私に電話すると約束した）",
         "explanation": "promise は to不定詞を目的語にとる動詞です。promise to call で「電話すると約束する」です。",
         "choices": [
             {"text": "call", "correct": False, "order": 1},
             {"text": "to call", "correct": True, "order": 2},
             {"text": "calling", "correct": False, "order": 3},
             {"text": "called", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「It is important ___ breakfast every morning.」",
         "explanation": "It is ... to do の形式主語構文です。「毎朝朝食を食べることは大切だ」となります。",
         "choices": [
             {"text": "eat", "correct": False, "order": 1},
             {"text": "to eat", "correct": True, "order": 2},
             {"text": "ate", "correct": False, "order": 3},
             {"text": "eaten", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「She decided ___ abroad next year.」",
         "explanation": "decide は to不定詞を目的語にとる動詞です。decide to study で「勉強することに決めた」です。",
         "choices": [
             {"text": "study", "correct": False, "order": 1},
             {"text": "to study", "correct": True, "order": 2},
             {"text": "studying", "correct": False, "order": 3},
             {"text": "studied", "correct": False, "order": 4},
         ]},
    ],
    "IF-002": [
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I'm thirsty. I want something ___.」",
         "explanation": "something を後ろから修飾する不定詞の形容詞的用法で、something to drink（何か飲むもの）となります。",
         "choices": [
             {"text": "drink", "correct": False, "order": 1},
             {"text": "to drink", "correct": True, "order": 2},
             {"text": "drinking", "correct": False, "order": 3},
             {"text": "drank", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I went to the library ___ some books.」（本を借りるために図書館へ行った）",
         "explanation": "目的（〜するために）を表す不定詞の副詞的用法です。to borrow で「借りるために」となります。",
         "choices": [
             {"text": "borrow", "correct": False, "order": 1},
             {"text": "to borrow", "correct": True, "order": 2},
             {"text": "borrowed", "correct": False, "order": 3},
             {"text": "borrows", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "次の文の to win は何用法ですか？\n\n「I'm happy to win the game.」",
         "explanation": "happy（感情）の原因を表す副詞的用法です。「試合に勝ってうれしい」の意味です。",
         "choices": [
             {"text": "名詞的用法", "correct": False, "order": 1},
             {"text": "形容詞的用法", "correct": False, "order": 2},
             {"text": "副詞的用法（感情の原因）", "correct": True, "order": 3},
             {"text": "どれでもない", "correct": False, "order": 4},
         ]},
    ],
    "IF-003": [
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I enjoyed ___ tennis with my friends.」",
         "explanation": "enjoy は動名詞（〜ing）を目的語にとる動詞です。enjoy playing で「するのを楽しんだ」です。",
         "choices": [
             {"text": "play", "correct": False, "order": 1},
             {"text": "to play", "correct": False, "order": 2},
             {"text": "playing", "correct": True, "order": 3},
             {"text": "played", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「He finished ___ his homework before dinner.」",
         "explanation": "finish は動名詞を目的語にとる動詞です。finish doing で「〜し終える」です。",
         "choices": [
             {"text": "do", "correct": False, "order": 1},
             {"text": "to do", "correct": False, "order": 2},
             {"text": "doing", "correct": True, "order": 3},
             {"text": "did", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「Don't forget ___ the door when you leave.」（出るときドアに鍵をかけるのを忘れないで）",
         "explanation": "forget to do は「（これから）〜するのを忘れる」、forget doing は「（過去に）〜したことを忘れる」。ここではこれからの動作なので to lock です。",
         "choices": [
             {"text": "lock", "correct": False, "order": 1},
             {"text": "to lock", "correct": True, "order": 2},
             {"text": "locking", "correct": False, "order": 3},
             {"text": "locked", "correct": False, "order": 4},
         ]},
    ],
    # ===== 関係詞 =====
    "RL-001": [
        {"difficulty": 2,
         "question_text": "空所に入る最も適切な関係代名詞を選びなさい。\n\n「I have a friend ___ lives in Canada.」",
         "explanation": "先行詞 a friend は人で、関係詞節内で lives の主語になるので who を使います。",
         "choices": [
             {"text": "who", "correct": True, "order": 1},
             {"text": "which", "correct": False, "order": 2},
             {"text": "whose", "correct": False, "order": 3},
             {"text": "whom", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "空所に入る最も適切な関係代名詞を選びなさい。\n\n「The book ___ I read last week was very interesting.」",
         "explanation": "先行詞 The book は物で、read の目的語の役割なので which（または that）です。目的格なので省略も可能です。",
         "choices": [
             {"text": "who", "correct": False, "order": 1},
             {"text": "which", "correct": True, "order": 2},
             {"text": "whose", "correct": False, "order": 3},
             {"text": "whom", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "空所に入る最も適切な関係代名詞を選びなさい。\n\n「Look at the house ___ roof is red.」（屋根が赤いあの家を見て）",
         "explanation": "「家の屋根」という所有の関係を表すので、所有格の関係代名詞 whose を使います。whose は物にも使えます。",
         "choices": [
             {"text": "who", "correct": False, "order": 1},
             {"text": "whose", "correct": True, "order": 2},
             {"text": "which", "correct": False, "order": 3},
             {"text": "that", "correct": False, "order": 4},
         ]},
    ],
    "RL-002": [
        {"difficulty": 2,
         "question_text": "空所に入る最も適切な関係副詞を選びなさい。\n\n「This is the hotel ___ we stayed last summer.」",
         "explanation": "場所を表す先行詞 the hotel の後ろで、後続の文が完全な文（stayed に目的語は不要）なので関係副詞 where を使います。",
         "choices": [
             {"text": "where", "correct": True, "order": 1},
             {"text": "which", "correct": False, "order": 2},
             {"text": "when", "correct": False, "order": 3},
             {"text": "why", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "空所に入る最も適切な関係副詞を選びなさい。\n\n「Summer is the season ___ many people go to the beach.」",
         "explanation": "時を表す先行詞 the season の後ろでは関係副詞 when を使います。",
         "choices": [
             {"text": "where", "correct": False, "order": 1},
             {"text": "when", "correct": True, "order": 2},
             {"text": "why", "correct": False, "order": 3},
             {"text": "which", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "空所に入る最も適切な語を選びなさい。\n\n「This is ___ I solved the problem.」（これが私がその問題を解いた方法です）",
         "explanation": "方法を表すときは how を使います。the way how とは言わず、how だけか the way だけを使います。",
         "choices": [
             {"text": "how", "correct": True, "order": 1},
             {"text": "the way how", "correct": False, "order": 2},
             {"text": "what", "correct": False, "order": 3},
             {"text": "which", "correct": False, "order": 4},
         ]},
    ],
    # ===== 比較 =====
    "CP-001": [
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「This question is ___ than that one.」",
         "explanation": "easy の比較級は y を i に変えて easier です。",
         "choices": [
             {"text": "easy", "correct": False, "order": 1},
             {"text": "easier", "correct": True, "order": 2},
             {"text": "easiest", "correct": False, "order": 3},
             {"text": "more easy", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「Tom can run as ___ as Ken.」（トムはケンと同じくらい速く走れる）",
         "explanation": "as ... as の間には原級（もとの形）が入ります。「同じくらい速く」なので fast のままです。",
         "choices": [
             {"text": "fast", "correct": True, "order": 1},
             {"text": "faster", "correct": False, "order": 2},
             {"text": "fastest", "correct": False, "order": 3},
             {"text": "more fast", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「Which do you like ___, summer or winter?」",
         "explanation": "2つのものを比べて「どちらが好き？」と聞くときは比較級 better を使います。",
         "choices": [
             {"text": "well", "correct": False, "order": 1},
             {"text": "better", "correct": True, "order": 2},
             {"text": "best", "correct": False, "order": 3},
             {"text": "good", "correct": False, "order": 4},
         ]},
    ],
    "CP-002": [
        {"difficulty": 2,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「It is getting ___ these days.」（最近ますます暖かくなってきている）",
         "explanation": "「比較級 and 比較級」で「ますます〜」を表します。warmer and warmer が正解です。",
         "choices": [
             {"text": "warm and warm", "correct": False, "order": 1},
             {"text": "warmer and warmer", "correct": True, "order": 2},
             {"text": "warmest and warmest", "correct": False, "order": 3},
             {"text": "more and more warm", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「Time is ___ important than money.」（時間はお金よりずっと大切だ）",
         "explanation": "比較級を強調する「ずっと」は much を使います。very は比較級には使えません。",
         "choices": [
             {"text": "very more", "correct": False, "order": 1},
             {"text": "much more", "correct": True, "order": 2},
             {"text": "very", "correct": False, "order": 3},
             {"text": "too more", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「No other student in the class is ___ than Aya.」（クラスでアヤより背の高い生徒はいない）",
         "explanation": "No other + 単数名詞 ... 比較級 than で最上級と同じ意味を表します。taller が正解です。",
         "choices": [
             {"text": "tall", "correct": False, "order": 1},
             {"text": "taller", "correct": True, "order": 2},
             {"text": "tallest", "correct": False, "order": 3},
             {"text": "as tall", "correct": False, "order": 4},
         ]},
    ],
    # ===== 仮定法 =====
    "SB-001": [
        {"difficulty": 3,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「If I ___ how to cook, I would make dinner for you.」（料理の仕方を知っていたら、夕食を作ってあげるのに）",
         "explanation": "現在の事実に反する仮定（実際は料理ができない）なので、仮定法過去。if節の動詞は過去形 knew です。",
         "choices": [
             {"text": "know", "correct": False, "order": 1},
             {"text": "knew", "correct": True, "order": 2},
             {"text": "have known", "correct": False, "order": 3},
             {"text": "will know", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「If I were a bird, I ___ fly to you.」",
         "explanation": "仮定法過去の帰結節は would/could + 動詞の原形です。「飛んでいけるのに」なので could が適切です。",
         "choices": [
             {"text": "can", "correct": False, "order": 1},
             {"text": "could", "correct": True, "order": 2},
             {"text": "will", "correct": False, "order": 3},
             {"text": "am able to", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「I wish it ___ sunny today.」（今日晴れていたらなあ）",
         "explanation": "I wish + 仮定法過去で現在の願望を表します。be動詞は were を使います。",
         "choices": [
             {"text": "is", "correct": False, "order": 1},
             {"text": "were", "correct": True, "order": 2},
             {"text": "will be", "correct": False, "order": 3},
             {"text": "be", "correct": False, "order": 4},
         ]},
    ],
    "SB-002": [
        {"difficulty": 3,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「If you ___ me earlier, I could have helped you.」",
         "explanation": "過去の事実に反する仮定（実際は早く言わなかった）なので、if節は had + 過去分詞です。",
         "choices": [
             {"text": "told", "correct": False, "order": 1},
             {"text": "had told", "correct": True, "order": 2},
             {"text": "tell", "correct": False, "order": 3},
             {"text": "have told", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「If I had known about the sale, I ___ bought the shoes.」",
         "explanation": "仮定法過去完了の帰結節は would have + 過去分詞です。「買っていたのに」という意味になります。",
         "choices": [
             {"text": "would", "correct": False, "order": 1},
             {"text": "would have", "correct": True, "order": 2},
             {"text": "will have", "correct": False, "order": 3},
             {"text": "had", "correct": False, "order": 4},
         ]},
        {"difficulty": 3,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「Without your help, I ___ have finished the project.」（あなたの助けがなかったら、完成できなかっただろう）",
         "explanation": "Without 〜 は if節の代わりに仮定を表します。「できなかっただろう」なので couldn't have + 過去分詞です。",
         "choices": [
             {"text": "couldn't", "correct": True, "order": 1},
             {"text": "can't", "correct": False, "order": 2},
             {"text": "don't", "correct": False, "order": 3},
             {"text": "didn't", "correct": False, "order": 4},
         ]},
    ],
    # ===== 基本文型（中学基礎） =====
    "JG-001": [
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語を選びなさい。\n\n「___ your parents at home now?」",
         "explanation": "主語 your parents は複数なので Are を使います。",
         "choices": [
             {"text": "Is", "correct": False, "order": 1},
             {"text": "Are", "correct": True, "order": 2},
             {"text": "Am", "correct": False, "order": 3},
             {"text": "Do", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「My father ___ a teacher. He works at a junior high school.」",
         "explanation": "主語 My father は三人称単数なので is を使います。",
         "choices": [
             {"text": "am", "correct": False, "order": 1},
             {"text": "is", "correct": True, "order": 2},
             {"text": "are", "correct": False, "order": 3},
             {"text": "be", "correct": False, "order": 4},
         ]},
    ],
    "JG-002": [
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語を選びなさい。\n\n「My sister ___ like carrots.」（妹はにんじんが好きではない）",
         "explanation": "三人称単数の否定文は doesn't + 動詞の原形です。",
         "choices": [
             {"text": "don't", "correct": False, "order": 1},
             {"text": "doesn't", "correct": True, "order": 2},
             {"text": "isn't", "correct": False, "order": 3},
             {"text": "not", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「Does he ___ soccer every day?」",
         "explanation": "Does を使った疑問文では、動詞は原形（play）に戻ります。",
         "choices": [
             {"text": "play", "correct": True, "order": 1},
             {"text": "plays", "correct": False, "order": 2},
             {"text": "playing", "correct": False, "order": 3},
             {"text": "played", "correct": False, "order": 4},
         ]},
    ],
    "JG-003": [
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語を選びなさい。\n\n「___ do you get up every morning? - At six thirty.」",
         "explanation": "「6時半に」と時刻を答えているので、時を尋ねる What time が適切です。",
         "choices": [
             {"text": "What time", "correct": True, "order": 1},
             {"text": "Where", "correct": False, "order": 2},
             {"text": "Who", "correct": False, "order": 3},
             {"text": "Why", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語句を選びなさい。\n\n「___ books do you have? - I have about fifty.」",
         "explanation": "「約50冊」と数を答えているので、数を尋ねる How many が適切です。",
         "choices": [
             {"text": "How many", "correct": True, "order": 1},
             {"text": "How much", "correct": False, "order": 2},
             {"text": "What", "correct": False, "order": 3},
             {"text": "Which", "correct": False, "order": 4},
         ]},
    ],
    "JG-004": [
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語を選びなさい。\n\n「This is my bike. That bike is ___ too.」（あの自転車も私のものです）",
         "explanation": "「私のもの」は mine で表します。my は後ろに名詞が必要です。",
         "choices": [
             {"text": "my", "correct": False, "order": 1},
             {"text": "mine", "correct": True, "order": 2},
             {"text": "me", "correct": False, "order": 3},
             {"text": "I", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語を選びなさい。\n\n「Do you know ___? He is our new teacher.」",
         "explanation": "know の目的語なので目的格 him を使います。",
         "choices": [
             {"text": "he", "correct": False, "order": 1},
             {"text": "his", "correct": False, "order": 2},
             {"text": "him", "correct": True, "order": 3},
             {"text": "himself", "correct": False, "order": 4},
         ]},
    ],
    "JG-005": [
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語を選びなさい。\n\n「My birthday is ___ May 5th.」",
         "explanation": "特定の日付には on を使います。月だけなら in May となります。",
         "choices": [
             {"text": "in", "correct": False, "order": 1},
             {"text": "on", "correct": True, "order": 2},
             {"text": "at", "correct": False, "order": 3},
             {"text": "to", "correct": False, "order": 4},
         ]},
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語を選びなさい。\n\n「The cat is sleeping ___ the table.」（ネコはテーブルの下で眠っている）",
         "explanation": "「〜の下に」は under を使います。",
         "choices": [
             {"text": "on", "correct": False, "order": 1},
             {"text": "under", "correct": True, "order": 2},
             {"text": "in", "correct": False, "order": 3},
             {"text": "at", "correct": False, "order": 4},
         ]},
    ],
    "JG-006": [
        {"difficulty": 1,
         "question_text": "空所に入る最も適切な語を選びなさい。\n\n「I was tired, ___ I went to bed early.」（疲れていたので早く寝た）",
         "explanation": "「だから」と結果を表す接続詞は so です。",
         "choices": [
             {"text": "but", "correct": False, "order": 1},
             {"text": "so", "correct": True, "order": 2},
             {"text": "or", "correct": False, "order": 3},
             {"text": "if", "correct": False, "order": 4},
         ]},
        {"difficulty": 2,
         "question_text": "空所に入る最も適切な語を選びなさい。\n\n「___ it is sunny tomorrow, let's go on a picnic.」",
         "explanation": "「もし明日晴れたら」という条件を表す接続詞は If です。",
         "choices": [
             {"text": "If", "correct": True, "order": 1},
             {"text": "But", "correct": False, "order": 2},
             {"text": "So", "correct": False, "order": 3},
             {"text": "Or", "correct": False, "order": 4},
         ]},
    ],
}
# fmt: on


def seed_extra():
    db = SessionLocal()
    try:
        unit_code_to_id = {}
        for unit_code in EXTRA_QUESTIONS.keys():
            unit = db.query(Unit).filter(Unit.code == unit_code).first()
            if unit:
                unit_code_to_id[unit_code] = unit.id

        existing_texts = {
            row[0] for row in db.query(Question.question_text).all()
        }
        new_q_count = 0
        for unit_code, questions in EXTRA_QUESTIONS.items():
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
            print(f"Added {new_q_count} new extra practice questions")
        else:
            print("No new extra practice questions to add.")

        print(f"\nExtra seed status:")
        print(f"  Total Questions: {db.query(Question).count()}")
        print(f"  Total Choices: {db.query(Choice).count()}")

    finally:
        db.close()


if __name__ == "__main__":
    seed_extra()
