import React, { useState, useEffect } from 'react'
import { getLayers, getCategories, getUnits, startWeakPractice } from '../api'

export default function Practice({ userId, onStartPractice, onBack }) {
  const [layers, setLayers] = useState([])
  const [categories, setCategories] = useState([])
  const [units, setUnits] = useState([])
  const [selectedLayer, setSelectedLayer] = useState(null)
  const [selectedCategory, setSelectedCategory] = useState(null)
  const [selectedUnits, setSelectedUnits] = useState([])
  const [loading, setLoading] = useState(true)
  const [starting, setStarting] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    getLayers()
      .then((res) => setLayers(res.data))
      .catch(() => setError('データの取得に失敗しました'))
      .finally(() => setLoading(false))
  }, [])

  useEffect(() => {
    if (!selectedLayer) {
      setCategories([])
      setSelectedCategory(null)
      return
    }
    getCategories(selectedLayer).then((res) => setCategories(res.data))
  }, [selectedLayer])

  useEffect(() => {
    if (!selectedCategory) {
      setUnits([])
      return
    }
    getUnits(selectedCategory).then((res) => setUnits(res.data))
  }, [selectedCategory])

  const toggleUnit = (code) => {
    setSelectedUnits((prev) =>
      prev.includes(code) ? prev.filter((c) => c !== code) : [...prev, code]
    )
  }

  const selectAllUnits = () => {
    if (selectedUnits.length === units.length) {
      setSelectedUnits([])
    } else {
      setSelectedUnits(units.map((u) => u.code))
    }
  }

  const handleStart = async () => {
    if (selectedUnits.length === 0) {
      setError('練習する単元を1つ以上選んでください')
      return
    }
    setStarting(true)
    setError('')
    try {
      const res = await startWeakPractice(userId, selectedUnits)
      if (res.data.questions.length === 0) {
        setError('選択した単元に問題がありません')
        setStarting(false)
        return
      }
      onStartPractice(res.data)
    } catch {
      setError('練習の開始に失敗しました')
    } finally {
      setStarting(false)
    }
  }

  if (loading) {
    return <div className="card" style={{ textAlign: 'center', padding: 40 }}>読み込み中...</div>
  }

  const chipStyle = (active) => ({
    display: 'inline-block',
    padding: '8px 16px',
    borderRadius: 20,
    border: `2px solid ${active ? 'var(--primary)' : 'var(--border)'}`,
    background: active ? 'rgba(102, 126, 234, 0.1)' : 'white',
    color: active ? 'var(--primary)' : 'var(--text)',
    fontWeight: active ? 600 : 400,
    cursor: 'pointer',
    fontSize: '0.9rem',
    transition: 'all 0.2s',
  })

  const unitCheckStyle = (active) => ({
    display: 'flex',
    alignItems: 'center',
    gap: 10,
    padding: '12px 16px',
    borderRadius: 10,
    border: `2px solid ${active ? 'var(--primary)' : 'var(--border)'}`,
    background: active ? 'rgba(102, 126, 234, 0.06)' : 'white',
    cursor: 'pointer',
    marginBottom: 8,
    transition: 'all 0.2s',
  })

  return (
    <>
      <div className="header">
        <h1>単元別練習</h1>
        <p>学びたい単元を選んで練習しましょう</p>
      </div>

      {/* Step 1: Layer */}
      <div className="card">
        <h3 style={{ marginBottom: 12 }}>1. 分野を選ぶ</h3>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8 }}>
          {layers.map((layer) => (
            <button
              key={layer.id}
              style={chipStyle(selectedLayer === layer.id)}
              onClick={() => {
                setSelectedLayer(selectedLayer === layer.id ? null : layer.id)
                setSelectedCategory(null)
                setSelectedUnits([])
              }}
            >
              {layer.name}
            </button>
          ))}
        </div>
      </div>

      {/* Step 2: Category */}
      {categories.length > 0 && (
        <div className="card">
          <h3 style={{ marginBottom: 12 }}>2. カテゴリを選ぶ</h3>
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8 }}>
            {categories.map((cat) => (
              <button
                key={cat.id}
                style={chipStyle(selectedCategory === cat.id)}
                onClick={() => {
                  setSelectedCategory(selectedCategory === cat.id ? null : cat.id)
                  setSelectedUnits([])
                }}
              >
                {cat.name}
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Step 3: Units */}
      {units.length > 0 && (
        <div className="card">
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 }}>
            <h3>3. 単元を選ぶ</h3>
            <button
              onClick={selectAllUnits}
              style={{
                background: 'none', border: 'none', color: 'var(--primary)',
                fontWeight: 600, cursor: 'pointer', fontSize: '0.85rem',
              }}
            >
              {selectedUnits.length === units.length ? '全解除' : '全選択'}
            </button>
          </div>
          {units.map((unit) => {
            const active = selectedUnits.includes(unit.code)
            return (
              <div
                key={unit.id}
                style={unitCheckStyle(active)}
                onClick={() => toggleUnit(unit.code)}
              >
                <span style={{
                  width: 22, height: 22, borderRadius: 6,
                  border: `2px solid ${active ? 'var(--primary)' : 'var(--border)'}`,
                  background: active ? 'var(--primary)' : 'white',
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  color: 'white', fontSize: '0.8rem', fontWeight: 700, flexShrink: 0,
                }}>
                  {active && '✓'}
                </span>
                <div>
                  <div style={{ fontWeight: 500 }}>{unit.name}</div>
                  {unit.description && (
                    <div style={{ fontSize: '0.8rem', color: 'var(--text-light)', marginTop: 2 }}>
                      {unit.description}
                    </div>
                  )}
                </div>
              </div>
            )
          })}
        </div>
      )}

      {error && (
        <p style={{ color: 'var(--danger)', textAlign: 'center', marginBottom: 12 }}>{error}</p>
      )}

      {/* Actions */}
      <div style={{ display: 'flex', gap: 12, marginBottom: 40 }}>
        {selectedUnits.length > 0 && (
          <button
            className="btn btn-primary"
            style={{ flex: 1, padding: 14, fontSize: '1.05rem' }}
            onClick={handleStart}
            disabled={starting}
          >
            {starting ? '準備中...' : `${selectedUnits.length}単元で練習スタート`}
          </button>
        )}
        <button
          className="btn btn-secondary"
          style={{ flex: selectedUnits.length > 0 ? 'none' : 1, padding: 14 }}
          onClick={onBack}
        >
          戻る
        </button>
      </div>
    </>
  )
}
