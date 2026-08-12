import React, { useState, useEffect } from 'react'
import { getUserStats, getUnitProgress, getMotivation } from '../api'

export default function Dashboard({ userId, onStartDiagnosis, onBack }) {
  const [stats, setStats] = useState(null)
  const [progress, setProgress] = useState([])
  const [motivation, setMotivation] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    const load = async () => {
      try {
        const [statsRes, progRes, motRes] = await Promise.all([
          getUserStats(userId),
          getUnitProgress(userId),
          getMotivation(userId),
        ])
        setStats(statsRes.data)
        setProgress(progRes.data)
        setMotivation(motRes.data)
      } catch (err) {
        console.error(err)
        setError('データの読み込みに失敗しました')
      } finally {
        setLoading(false)
      }
    }
    load()
  }, [userId])

  if (loading) return <div className="card" style={{ textAlign: 'center', padding: 40 }}>読み込み中...</div>

  if (error) return (
    <div className="card" style={{ textAlign: 'center', padding: 40 }}>
      <p style={{ color: 'var(--danger)', marginBottom: 16 }}>{error}</p>
      <button className="btn btn-secondary" onClick={onBack}>ホームに戻る</button>
    </div>
  )

  const barColor = (score) => {
    if (score >= 80) return 'var(--success)'
    if (score >= 50) return 'var(--warning)'
    return 'var(--danger)'
  }

  return (
    <>
      <div className="header">
        <h1>ダッシュボード</h1>
        <p>{stats?.user?.display_name || stats?.user?.username} さんの学習状況</p>
      </div>

      {/* Motivation cards */}
      {motivation && (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))', gap: 12, marginBottom: 16 }}>
          <div className="card" style={{ textAlign: 'center', marginBottom: 0 }}>
            <div style={{ fontSize: '2rem', fontWeight: 700 }}>
              {'\u{1F525}'} {motivation.streak}日
            </div>
            <div style={{ fontSize: '0.85rem', color: 'var(--text-light)' }}>連続学習</div>
          </div>
          <div className="card" style={{ textAlign: 'center', marginBottom: 0 }}>
            <div style={{ fontSize: '2rem', fontWeight: 700, color: 'var(--primary)' }}>
              Lv.{motivation.level}
            </div>
            <div style={{ fontSize: '0.85rem', color: 'var(--text-light)' }}>
              次のレベルまで {motivation.xp_per_level - motivation.xp_in_level} XP
            </div>
            <div className="progress-bar" style={{ height: 6, marginTop: 6, marginBottom: 0 }}>
              <div className="fill" style={{ width: `${motivation.xp_in_level / motivation.xp_per_level * 100}%` }} />
            </div>
          </div>
        </div>
      )}

      {/* Learning calendar heatmap */}
      {motivation && (
        <div className="card">
          <h3 style={{ marginBottom: 12 }}>学習カレンダー（直近10週間）</h3>
          {motivation.activity.every((d) => d.count === 0) ? (
            <p style={{ color: 'var(--text-light)', textAlign: 'center', padding: '16px 0' }}>
              {'\u{1F331}'} 今日から学習の記録が始まります！<br />
              問題を解くと、この場所に学習した日が色づいていきます。
            </p>
          ) : (
            <>
              <div style={{ display: 'flex', gap: 6 }}>
                <div style={{
                  display: 'grid', gridTemplateRows: 'repeat(7, 1fr)', gap: 3,
                  fontSize: '0.65rem', color: 'var(--text-light)', textAlign: 'center',
                }}>
                  {(() => {
                    const dayNames = ['日', '月', '火', '水', '木', '金', '土']
                    const first = new Date(motivation.activity[0].date + 'T00:00:00')
                    return Array.from({ length: 7 }, (_, r) => (
                      <span key={r} style={{ display: 'flex', alignItems: 'center' }}>
                        {r % 2 === 1 ? dayNames[(first.getDay() + r) % 7] : ''}
                      </span>
                    ))
                  })()}
                </div>
                <div style={{ flex: 1, display: 'grid', gridTemplateColumns: 'repeat(10, 1fr)', gridAutoFlow: 'column', gridTemplateRows: 'repeat(7, 1fr)', gap: 3 }}>
                  {motivation.activity.map((day, i) => {
                    const c = day.count
                    const bg = c === 0 ? 'var(--border)'
                      : c < 5 ? 'rgba(102,126,234,0.35)'
                      : c < 10 ? 'rgba(102,126,234,0.65)'
                      : 'var(--primary)'
                    return (
                      <div key={i} title={`${day.date}: ${c}問`} style={{
                        aspectRatio: '1', borderRadius: 3, background: bg,
                      }} />
                    )
                  })}
                </div>
              </div>
              <p style={{ fontSize: '0.75rem', color: 'var(--text-light)', marginTop: 8, textAlign: 'right' }}>
                色が濃いほどたくさん学習した日
              </p>
            </>
          )}
        </div>
      )}

      {/* Stats cards */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))', gap: 12, marginBottom: 16 }}>
        <div className="card" style={{ textAlign: 'center' }}>
          <div style={{ fontSize: '2rem', fontWeight: 700, color: 'var(--primary)' }}>
            {stats?.total_sessions || 0}
          </div>
          <div style={{ fontSize: '0.85rem', color: 'var(--text-light)' }}>診断回数</div>
        </div>
        <div className="card" style={{ textAlign: 'center' }}>
          <div style={{ fontSize: '2rem', fontWeight: 700, color: 'var(--primary)' }}>
            {stats?.overall_accuracy || 0}%
          </div>
          <div style={{ fontSize: '0.85rem', color: 'var(--text-light)' }}>総合正答率</div>
        </div>
        <div className="card" style={{ textAlign: 'center' }}>
          <div style={{ fontSize: '2rem', fontWeight: 700, color: 'var(--success)' }}>
            {stats?.best_score ?? '-'}%
          </div>
          <div style={{ fontSize: '0.85rem', color: 'var(--text-light)' }}>最高スコア</div>
        </div>
        <div className="card" style={{ textAlign: 'center' }}>
          <div style={{ fontSize: '2rem', fontWeight: 700, color: 'var(--warning)' }}>
            {stats?.latest_score ?? '-'}%
          </div>
          <div style={{ fontSize: '0.85rem', color: 'var(--text-light)' }}>最新スコア</div>
        </div>
      </div>

      {/* Score trend */}
      {stats?.score_history?.length > 1 && (
        <div className="card">
          <h3 style={{ marginBottom: 16 }}>スコア推移</h3>
          <div style={{ display: 'flex', alignItems: 'end', gap: 4, height: 120 }}>
            {stats.score_history.map((h, i) => {
              const height = Math.max(h.score, 5)
              return (
                <div key={i} style={{
                  flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 4,
                }}>
                  <span style={{ fontSize: '0.7rem', color: 'var(--text-light)' }}>{h.score}%</span>
                  <div style={{
                    width: '100%', maxWidth: 40,
                    height: `${height}%`,
                    background: barColor(h.score),
                    borderRadius: '4px 4px 0 0',
                    minHeight: 4,
                  }} />
                  <span style={{ fontSize: '0.65rem', color: 'var(--text-light)' }}>
                    {i + 1}回目
                  </span>
                </div>
              )
            })}
          </div>
        </div>
      )}

      {/* Unit progress */}
      {progress.length > 0 && (
        <div className="card">
          <h3 style={{ marginBottom: 16 }}>単元別習熟度</h3>
          {progress.map((unit, i) => (
            <div key={i} className="unit-bar">
              <span className="name" title={unit.unit_name}>{unit.unit_name}</span>
              <div className="bar">
                <div className="fill" style={{ width: `${Math.max(unit.score, 3)}%`, background: barColor(unit.score) }} />
              </div>
              <span className="pct" style={{ color: barColor(unit.score) }}>{unit.score}%</span>
            </div>
          ))}
        </div>
      )}

      {/* Actions */}
      <div style={{ display: 'flex', gap: 12, marginTop: 8, marginBottom: 40 }}>
        <button className="btn btn-primary" style={{ flex: 1, padding: 14 }} onClick={onStartDiagnosis}>
          もう一度診断する
        </button>
        <button className="btn btn-secondary" style={{ flex: 1, padding: 14 }} onClick={onBack}>
          ホームに戻る
        </button>
      </div>
    </>
  )
}
