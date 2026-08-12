import React, { useState } from 'react'
import { startWeakPractice } from '../api'

export default function Results({ result, userId, onBack, onDashboard, onStartPractice, onPractice }) {
  const { overall_score, correct_count, total_questions, unit_scores, weak_units, recommendations } = result
  const [loading, setLoading] = useState(false)
  const [showAllWeak, setShowAllWeak] = useState(false)

  const visibleWeak = showAllWeak ? weak_units : weak_units.slice(0, 3)

  const scoreClass = overall_score >= 80 ? 'high' : overall_score >= 50 ? 'mid' : 'low'

  const sortedUnits = [...unit_scores].sort((a, b) => a.score - b.score)

  const barColor = (score) => {
    if (score >= 80) return 'var(--success)'
    if (score >= 50) return 'var(--warning)'
    return 'var(--danger)'
  }

  const handleWeakPractice = async () => {
    const weakCodes = weak_units.map(u => u.unit_code)
    setLoading(true)
    try {
      const res = await startWeakPractice(userId, weakCodes)
      onStartPractice(res.data)
    } catch {
      alert('弱点克服モードの開始に失敗しました')
    } finally {
      setLoading(false)
    }
  }

  return (
    <>
      <div className="header">
        <h1>診断結果</h1>
        <p>あなたの英語力を分析しました</p>
      </div>

      <div className="card" style={{ textAlign: 'center' }}>
        <div className={`score-circle ${scoreClass}`}>
          {overall_score}%
          <span className="label">正答率</span>
        </div>
        <p style={{ fontSize: '1.1rem', color: 'var(--text-light)' }}>
          {total_questions}問中 {correct_count}問正解
        </p>
        <p style={{ fontSize: '1rem', fontWeight: 600, marginTop: 8 }}>
          {overall_score >= 80 ? '\u{1F389} すばらしい！この調子で続けよう！'
            : overall_score >= 50 ? '\u{1F4AA} よくがんばりました！弱点をつぶせばもっと伸びる！'
            : '\u{1F331} ここからが伸びるチャンス！下の勉強法から始めよう！'}
        </p>
      </div>

      {weak_units.length > 0 && (
        <div className="card">
          <h3 style={{ marginBottom: 16, color: 'var(--danger)' }}>
            弱点単元（正答率 60% 未満）
          </h3>
          {visibleWeak.map((unit, i) => (
            <div key={i} style={{ borderBottom: '1px solid var(--border)', paddingBottom: 12, marginBottom: 12 }}>
              <div className="weak-item" style={{ border: 'none', padding: 0, marginBottom: 8 }}>
                <div>
                  <strong>{unit.unit_name}</strong>
                  <br />
                  <span style={{ fontSize: '0.8rem', color: 'var(--text-light)' }}>
                    {unit.layer_name} &gt; {unit.category_name}
                  </span>
                </div>
                <span style={{ fontWeight: 700, color: 'var(--danger)', fontSize: '1.1rem' }}>
                  {unit.score}%
                </span>
              </div>
              {unit.study_points && unit.study_points.length > 0 && (
                <details open={i < 3} style={{
                  background: 'rgba(102,126,234,0.06)', borderRadius: 8,
                  padding: '10px 14px', fontSize: '0.88rem', lineHeight: 1.7,
                }}>
                  <summary style={{ fontWeight: 700, color: 'var(--primary)', cursor: 'pointer' }}>
                    克服のための勉強法
                  </summary>
                  <ul style={{ paddingLeft: 18, margin: '8px 0 0' }}>
                    {unit.study_points.map((point, j) => (
                      <li key={j} style={{ marginBottom: 2 }}>{point}</li>
                    ))}
                  </ul>
                </details>
              )}
            </div>
          ))}
          {weak_units.length > 3 && (
            <button
              onClick={() => setShowAllWeak(!showAllWeak)}
              style={{
                width: '100%', background: 'none', border: 'none',
                color: 'var(--primary)', fontWeight: 600, cursor: 'pointer',
                padding: '8px 0', fontSize: '0.95rem',
              }}
            >
              {showAllWeak ? '閉じる' : `他${weak_units.length - 3}件の弱点を見る`}
            </button>
          )}
          <button
            className="btn btn-primary"
            style={{ width: '100%', marginTop: 16, background: 'var(--danger)' }}
            onClick={handleWeakPractice}
            disabled={loading}
          >
            {loading ? '準備中...' : '弱点を克服する'}
          </button>
        </div>
      )}

      <div className="card">
        <h3 style={{ marginBottom: 16 }}>単元別スコア</h3>
        {sortedUnits.map((unit, i) => (
          <div key={i} className="unit-bar">
            <span className="name" title={unit.unit_name}>{unit.unit_name}</span>
            <div className="bar">
              <div className="fill" style={{ width: `${Math.max(unit.score, 3)}%`, background: barColor(unit.score) }} />
            </div>
            <span className="pct" style={{ color: barColor(unit.score) }}>{unit.score}%</span>
          </div>
        ))}
      </div>

      <div className="card">
        <h3 style={{ marginBottom: 16, color: 'var(--primary)' }}>学習アドバイス</h3>
        {recommendations.map((rec, i) => (
          <div key={i} className="recommendation">{rec}</div>
        ))}
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: 10, marginTop: 8, marginBottom: 40 }}>
        <button className="btn btn-primary" style={{ width: '100%', padding: 14 }} onClick={onPractice}>
          単元別練習へ
        </button>
        <div style={{ display: 'flex', gap: 12 }}>
          <button className="btn btn-secondary" style={{ flex: 1 }} onClick={onDashboard}>
            学習履歴を見る
          </button>
          <button className="btn btn-secondary" style={{ flex: 1 }} onClick={onBack}>
            ホームに戻る
          </button>
        </div>
      </div>
    </>
  )
}
