import React, { useState, useEffect } from 'react'
import { createUser, loginUser, startDiagnosis, getMotivation, startReviewMistakes } from '../api'

export default function Home({ userId, setUserId, onLogout, onStartDiagnosis, onGoDashboard, onGoPractice }) {
  const [mode, setMode] = useState('login')
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [displayName, setDisplayName] = useState('')
  const [grade, setGrade] = useState('junior1')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [registered, setRegistered] = useState(!!userId)
  const [motivation, setMotivation] = useState(null)

  useEffect(() => {
    if (registered && userId) {
      getMotivation(userId)
        .then((res) => setMotivation(res.data))
        .catch(() => {})
    }
  }, [registered, userId])

  const gradeLabels = {
    junior1: '中学1年',
    junior2: '中学2年',
    junior3: '中学3年',
    high1: '高校1年',
    high2: '高校2年',
    high3: '高校3年',
  }

  const handleLogin = async (e) => {
    e.preventDefault()
    if (!username.trim() || !password) {
      setError('ユーザー名とパスワードを入力してください')
      return
    }
    setLoading(true)
    setError('')
    try {
      const res = await loginUser({ username: username.trim(), password })
      setUserId(res.data.id)
      setRegistered(true)
    } catch (err) {
      if (err.response?.status === 401) {
        setError(err.response.data.detail || 'ユーザー名またはパスワードが正しくありません')
      } else {
        setError('ログインに失敗しました')
      }
    } finally {
      setLoading(false)
    }
  }

  const handleRegister = async (e) => {
    e.preventDefault()
    if (!username.trim()) {
      setError('ユーザー名を入力してください')
      return
    }
    if (!password || password.length < 4) {
      setError('パスワードは4文字以上で入力してください')
      return
    }
    setLoading(true)
    setError('')
    try {
      const res = await createUser({
        username: username.trim(),
        password,
        display_name: displayName.trim() || username.trim(),
        grade: gradeLabels[grade],
      })
      setUserId(res.data.id)
      setRegistered(true)
    } catch (err) {
      if (err.response?.status === 400) {
        const detail = err.response.data.detail || ''
        if (detail.includes('Username')) {
          setError('このユーザー名は既に使われています')
        } else {
          setError(detail || '登録に失敗しました')
        }
      } else {
        setError('登録に失敗しました。もう一度お試しください')
      }
    } finally {
      setLoading(false)
    }
  }

  const handleStartDiagnosis = async () => {
    setLoading(true)
    setError('')
    try {
      const res = await startDiagnosis(userId)
      onStartDiagnosis(res.data)
    } catch (err) {
      setError('診断の開始に失敗しました')
    } finally {
      setLoading(false)
    }
  }

  const handleReviewMistakes = async () => {
    setLoading(true)
    setError('')
    try {
      const res = await startReviewMistakes(userId)
      onStartDiagnosis(res.data)
    } catch (err) {
      if (err.response?.status === 404) {
        setError(err.response.data.detail || '解き直す問題がありません')
      } else {
        setError('解き直しの開始に失敗しました')
      }
    } finally {
      setLoading(false)
    }
  }

  const switchMode = () => {
    setMode(mode === 'login' ? 'register' : 'login')
    setError('')
  }

  const inputStyle = {
    width: '100%', padding: '10px 14px', border: '2px solid var(--border)',
    borderRadius: 8, fontSize: '1rem',
  }

  return (
    <>
      <div className="header">
        <h1>English Diagnosis</h1>
        <p>あなたの英語の弱点を見つけるアプリ</p>
      </div>

      {!registered ? (
        <div className="card">
          {mode === 'login' ? (
            <>
              <h2 style={{ marginBottom: 20 }}>ログイン</h2>
              <form onSubmit={handleLogin}>
                <div style={{ marginBottom: 16 }}>
                  <label style={{ display: 'block', marginBottom: 6, fontWeight: 600 }}>
                    ユーザー名
                  </label>
                  <input type="text" value={username} onChange={(e) => setUsername(e.target.value)}
                    placeholder="ユーザー名を入力" style={inputStyle} />
                </div>
                <div style={{ marginBottom: 20 }}>
                  <label style={{ display: 'block', marginBottom: 6, fontWeight: 600 }}>
                    パスワード
                  </label>
                  <input type="password" value={password} onChange={(e) => setPassword(e.target.value)}
                    placeholder="パスワードを入力" style={inputStyle} />
                </div>
                {error && <p style={{ color: 'var(--danger)', marginBottom: 12 }}>{error}</p>}
                <button type="submit" className="btn btn-primary" style={{ width: '100%' }}
                  disabled={loading}>
                  {loading ? 'ログイン中...' : 'ログイン'}
                </button>
              </form>
              <p style={{ textAlign: 'center', marginTop: 16, color: 'var(--text-light)' }}>
                アカウントをお持ちでない方は
                <button onClick={switchMode} style={{
                  background: 'none', border: 'none', color: 'var(--primary)',
                  fontWeight: 600, cursor: 'pointer', padding: '0 4px', fontSize: 'inherit',
                }}>新規登録</button>
              </p>
            </>
          ) : (
            <>
              <h2 style={{ marginBottom: 20 }}>新規登録</h2>
              <form onSubmit={handleRegister}>
                <div style={{ marginBottom: 16 }}>
                  <label style={{ display: 'block', marginBottom: 6, fontWeight: 600 }}>
                    ユーザー名
                  </label>
                  <input type="text" value={username} onChange={(e) => setUsername(e.target.value)}
                    placeholder="英数字で入力" style={inputStyle} />
                </div>
                <div style={{ marginBottom: 16 }}>
                  <label style={{ display: 'block', marginBottom: 6, fontWeight: 600 }}>
                    パスワード
                  </label>
                  <input type="password" value={password} onChange={(e) => setPassword(e.target.value)}
                    placeholder="4文字以上" style={inputStyle} />
                </div>
                <div style={{ marginBottom: 16 }}>
                  <label style={{ display: 'block', marginBottom: 6, fontWeight: 600 }}>
                    表示名（任意）
                  </label>
                  <input type="text" value={displayName} onChange={(e) => setDisplayName(e.target.value)}
                    placeholder="ニックネームなど" style={inputStyle} />
                </div>
                <div style={{ marginBottom: 20 }}>
                  <label style={{ display: 'block', marginBottom: 6, fontWeight: 600 }}>
                    学年
                  </label>
                  <select value={grade} onChange={(e) => setGrade(e.target.value)}
                    style={{ ...inputStyle, background: 'white' }}>
                    <option value="junior1">中学1年</option>
                    <option value="junior2">中学2年</option>
                    <option value="junior3">中学3年</option>
                    <option value="high1">高校1年</option>
                    <option value="high2">高校2年</option>
                    <option value="high3">高校3年</option>
                  </select>
                </div>
                {error && <p style={{ color: 'var(--danger)', marginBottom: 12 }}>{error}</p>}
                <button type="submit" className="btn btn-primary" style={{ width: '100%' }}
                  disabled={loading}>
                  {loading ? '登録中...' : '登録する'}
                </button>
              </form>
              <p style={{ textAlign: 'center', marginTop: 16, color: 'var(--text-light)' }}>
                既にアカウントをお持ちの方は
                <button onClick={switchMode} style={{
                  background: 'none', border: 'none', color: 'var(--primary)',
                  fontWeight: 600, cursor: 'pointer', padding: '0 4px', fontSize: 'inherit',
                }}>ログイン</button>
              </p>
            </>
          )}
        </div>
      ) : (
        <>
          {motivation && (
            <div className="card">
              <div style={{ display: 'flex', justifyContent: 'space-around', textAlign: 'center', marginBottom: 16 }}>
                <div>
                  <div style={{ fontSize: '1.6rem', fontWeight: 700 }}>
                    {motivation.streak > 0 ? '\u{1F525}' : '\u{1F331}'} {motivation.streak}日
                  </div>
                  <div style={{ fontSize: '0.8rem', color: 'var(--text-light)' }}>連続学習</div>
                </div>
                <div>
                  <div style={{ fontSize: '1.6rem', fontWeight: 700, color: 'var(--primary)' }}>
                    Lv.{motivation.level}
                  </div>
                  <div style={{ fontSize: '0.8rem', color: 'var(--text-light)' }}>
                    {motivation.xp} XP
                  </div>
                </div>
                <div>
                  <div style={{ fontSize: '1.6rem', fontWeight: 700, color: motivation.today_count >= motivation.daily_goal ? 'var(--success)' : 'var(--text)' }}>
                    {motivation.today_count}/{motivation.daily_goal}問
                  </div>
                  <div style={{ fontSize: '0.8rem', color: 'var(--text-light)' }}>今日の目標</div>
                </div>
              </div>
              <div className="progress-bar" style={{ marginBottom: 6 }}>
                <div className="fill" style={{
                  width: `${Math.min(motivation.today_count / motivation.daily_goal * 100, 100)}%`,
                  background: motivation.today_count >= motivation.daily_goal ? 'var(--success)' : 'var(--primary)',
                }} />
              </div>
              <p style={{ fontSize: '0.85rem', color: 'var(--text-light)', textAlign: 'center' }}>
                {motivation.today_count >= motivation.daily_goal
                  ? '\u{1F389} 今日の目標達成！すばらしい！'
                  : `今日はあと${motivation.daily_goal - motivation.today_count}問で目標達成！`}
              </p>
            </div>
          )}

          <div className="card" style={{ textAlign: 'center' }}>
            <h2 style={{ marginBottom: 16 }}>診断を始めましょう</h2>
            <p style={{ marginBottom: 8, color: 'var(--text-light)' }}>
              20問の診断問題に答えて、あなたの英語の弱点を分析します。
            </p>
            <p style={{ marginBottom: 24, color: 'var(--text-light)', fontSize: '0.9rem' }}>
              所要時間：約10〜15分
            </p>
            {error && <p style={{ color: 'var(--danger)', marginBottom: 12 }}>{error}</p>}
            <button className="btn btn-primary" style={{ width: '100%', fontSize: '1.1rem', padding: '16px', marginBottom: 10 }}
              onClick={handleStartDiagnosis} disabled={loading}>
              {loading ? '準備中...' : '診断スタート'}
            </button>
            {motivation && motivation.mistake_count > 0 && (
              <button className="btn btn-secondary" style={{
                width: '100%', marginBottom: 10,
                borderColor: 'var(--warning)', color: 'var(--warning)',
              }} onClick={handleReviewMistakes} disabled={loading}>
                間違えた問題を解き直す（{motivation.mistake_count}問）
              </button>
            )}
            <button className="btn btn-secondary" style={{ width: '100%', marginBottom: 10 }}
              onClick={onGoPractice}>
              単元別練習
            </button>
            <button className="btn btn-secondary" style={{ width: '100%', marginBottom: 10 }}
              onClick={onGoDashboard}>
              学習履歴を見る
            </button>
            <button onClick={onLogout} style={{
              background: 'none', border: 'none', color: 'var(--text-light)',
              cursor: 'pointer', fontSize: '0.9rem', marginTop: 8,
            }}>
              ログアウト
            </button>
          </div>

          <div className="card">
            <h3 style={{ marginBottom: 12 }}>このアプリでできること</h3>
            <ul style={{ listStyle: 'none' }}>
              {[
                '自分の弱点を診断',
                '何を勉強すべきか提案',
                '成長をグラフで可視化',
                'AIによる分かりやすい解説',
              ].map((item, i) => (
                <li key={i} style={{
                  padding: '10px 0', borderBottom: i < 3 ? '1px solid var(--border)' : 'none',
                  display: 'flex', alignItems: 'center', gap: 10,
                }}>
                  <span style={{ color: 'var(--primary)', fontWeight: 'bold' }}>&#10003;</span>
                  {item}
                </li>
              ))}
            </ul>
          </div>
        </>
      )}
    </>
  )
}
