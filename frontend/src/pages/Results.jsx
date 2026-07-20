import React, { useState } from 'react'
import { startWeakPractice } from '../api'

export default function Results({ result, userId, onBack, onDashboard, onStartPractice, onPractice }) {
  const { overall_score, correct_count, total_questions, unit_scores, weak_units, recommendations } = result
  const [loading, setLoading] = useState(false)

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
      </div>

      {weak_units.length > 0 && (
        <div className="card">
          <h3 style={{ marginBottom: 16, color: 'var(--danger)' }}>
            弱点単元（正答率 60% 未満）
          </h3>
          {weak_units.map((unit, i) => (
            <div key={i} className="weak-item">
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
          ))}
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
              <div className="fill" style={{ width: `${unit.score}%`, background: barColor(unit.score) }} />
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
