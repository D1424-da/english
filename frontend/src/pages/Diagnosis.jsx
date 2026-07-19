import React, { useState } from 'react'
import { submitAnswer, getDiagnosisResult } from '../api'

export default function Diagnosis({ diagnosisData, userId, onComplete, onBack }) {
  const { session_id, questions } = diagnosisData
  const [current, setCurrent] = useState(0)
  const [selectedId, setSelectedId] = useState(null)
  const [answered, setAnswered] = useState(false)
  const [answerResult, setAnswerResult] = useState(null)
  const [loading, setLoading] = useState(false)

  const question = questions[current]
  const progress = ((current + (answered ? 1 : 0)) / questions.length) * 100

  const handleSelect = async (choiceId) => {
    if (answered || loading) return
    setSelectedId(choiceId)
    setLoading(true)

    try {
      const res = await submitAnswer(session_id, userId, question.id, choiceId)
      setAnswerResult(res.data)
      setAnswered(true)
    } catch {
      alert('回答の送信に失敗しました')
    } finally {
      setLoading(false)
    }
  }

  const handleNext = async () => {
    if (current < questions.length - 1) {
      setCurrent(current + 1)
      setSelectedId(null)
      setAnswered(false)
      setAnswerResult(null)
    } else {
      setLoading(true)
      try {
        const res = await getDiagnosisResult(session_id, userId)
        onComplete(res.data)
      } catch {
        alert('結果の取得に失敗しました')
      } finally {
        setLoading(false)
      }
    }
  }

  const getChoiceClass = (choice) => {
    if (!answered) return selectedId === choice.id ? 'selected' : ''
    if (choice.id === answerResult?.correct_choice_id) return 'correct'
    if (choice.id === selectedId && !answerResult?.is_correct) return 'incorrect'
    return ''
  }

  return (
    <>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 }}>
        <button className="btn btn-secondary" onClick={onBack}
          style={{ padding: '6px 16px', fontSize: '0.85rem' }}>
          戻る
        </button>
        <span style={{ color: 'var(--text-light)', fontSize: '0.9rem' }}>
          {current + 1} / {questions.length}
        </span>
      </div>

      <div className="progress-bar">
        <div className="fill" style={{ width: `${progress}%` }} />
      </div>

      <div className="card">
        {question.unit_name && (
          <span style={{
            display: 'inline-block', background: 'rgba(102,126,234,0.1)', color: 'var(--primary)',
            padding: '4px 12px', borderRadius: 20, fontSize: '0.8rem', marginBottom: 12,
          }}>
            {question.unit_name}
          </span>
        )}
        <h3 style={{ marginBottom: 20, lineHeight: 1.8, whiteSpace: 'pre-line' }}>
          {question.question_text}
        </h3>

        {question.choices.map((choice) => (
          <button
            key={choice.id}
            className={`btn-choice ${getChoiceClass(choice)}`}
            onClick={() => handleSelect(choice.id)}
            disabled={answered}
          >
            {choice.choice_text}
          </button>
        ))}

        {answered && answerResult && (
          <div style={{
            marginTop: 16, padding: 16, borderRadius: 10,
            background: answerResult.is_correct ? 'rgba(72,187,120,0.1)' : 'rgba(245,101,101,0.1)',
            border: `2px solid ${answerResult.is_correct ? 'var(--success)' : 'var(--danger)'}`,
          }}>
            <p style={{
              fontWeight: 700, marginBottom: 8,
              color: answerResult.is_correct ? 'var(--success)' : 'var(--danger)',
            }}>
              {answerResult.is_correct ? '正解！' : '不正解'}
            </p>
            {answerResult.explanation && (
              <p style={{ fontSize: '0.95rem', lineHeight: 1.7 }}>
                {answerResult.explanation}
              </p>
            )}
          </div>
        )}

        {answered && (
          <button
            className="btn btn-primary"
            style={{ width: '100%', marginTop: 16 }}
            onClick={handleNext}
            disabled={loading}
          >
            {loading
              ? '結果を計算中...'
              : current < questions.length - 1
              ? '次の問題へ'
              : '結果を見る'}
          </button>
        )}
      </div>
    </>
  )
}
