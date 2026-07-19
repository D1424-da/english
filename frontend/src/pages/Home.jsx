import React, { useState } from 'react'
import { createUser, startDiagnosis } from '../api'

export default function Home({ userId, setUserId, onStartDiagnosis }) {
  const [username, setUsername] = useState('')
  const [displayName, setDisplayName] = useState('')
  const [grade, setGrade] = useState('high2')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [registered, setRegistered] = useState(!!userId)

  const gradeLabels = {
    high1: '高校1年',
    high2: '高校2年',
    high3: '高校3年',
  }

  const handleRegister = async (e) => {
    e.preventDefault()
    if (!username.trim()) {
      setError('ユーザー名を入力してください')
      return
    }
    setLoading(true)
    setError('')
    try {
      const res = await createUser({
        username: username.trim(),
        display_name: displayName.trim() || username.trim(),
        grade: gradeLabels[grade],
      })
      setUserId(res.data.id)
      setRegistered(true)
    } catch (err) {
      if (err.response?.status === 400) {
        setError('このユーザー名は既に使われています')
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

  return (
    <>
      <div className="header">
        <h1>English Diagnosis</h1>
        <p>あなたの英語の弱点を見つけるアプリ</p>
      </div>

      {!registered ? (
        <div className="card">
          <h2 style={{ marginBottom: 20 }}>はじめに</h2>
          <p style={{ marginBottom: 20, color: 'var(--text-light)' }}>
            ユーザー登録をして診断を始めましょう
          </p>
          <form onSubmit={handleRegister}>
            <div style={{ marginBottom: 16 }}>
              <label style={{ display: 'block', marginBottom: 6, fontWeight: 600 }}>
                ユーザー名
              </label>
              <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="英数字で入力"
                style={{
                  width: '100%', padding: '10px 14px', border: '2px solid var(--border)',
                  borderRadius: 8, fontSize: '1rem',
                }}
              />
            </div>
            <div style={{ marginBottom: 16 }}>
              <label style={{ display: 'block', marginBottom: 6, fontWeight: 600 }}>
                表示名（任意）
              </label>
              <input
                type="text"
                value={displayName}
                onChange={(e) => setDisplayName(e.target.value)}
                placeholder="ニックネームなど"
                style={{
                  width: '100%', padding: '10px 14px', border: '2px solid var(--border)',
                  borderRadius: 8, fontSize: '1rem',
                }}
              />
            </div>
            <div style={{ marginBottom: 20 }}>
              <label style={{ display: 'block', marginBottom: 6, fontWeight: 600 }}>
                学年
              </label>
              <select
                value={grade}
                onChange={(e) => setGrade(e.target.value)}
                style={{
                  width: '100%', padding: '10px 14px', border: '2px solid var(--border)',
                  borderRadius: 8, fontSize: '1rem', background: 'white',
                }}
              >
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
        </div>
      ) : (
        <>
          <div className="card" style={{ textAlign: 'center' }}>
            <h2 style={{ marginBottom: 16 }}>診断を始めましょう</h2>
            <p style={{ marginBottom: 8, color: 'var(--text-light)' }}>
              20問の診断問題に答えて、あなたの英語の弱点を分析します。
            </p>
            <p style={{ marginBottom: 24, color: 'var(--text-light)', fontSize: '0.9rem' }}>
              所要時間：約10〜15分
            </p>
            {error && <p style={{ color: 'var(--danger)', marginBottom: 12 }}>{error}</p>}
            <button className="btn btn-primary" style={{ width: '100%', fontSize: '1.1rem', padding: '16px' }}
              onClick={handleStartDiagnosis} disabled={loading}>
              {loading ? '準備中...' : '診断スタート'}
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
