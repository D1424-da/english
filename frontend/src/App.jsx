import React, { useState, useEffect } from 'react'
import Home from './pages/Home'
import Diagnosis from './pages/Diagnosis'
import Results from './pages/Results'
import Dashboard from './pages/Dashboard'
import Practice from './pages/Practice'
import { startDiagnosis, getUser } from './api'

export default function App() {
  const [page, setPage] = useState('home')
  const [userId, setUserId] = useState(null)
  const [diagnosisData, setDiagnosisData] = useState(null)
  const [resultData, setResultData] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const savedId = localStorage.getItem('userId')
    if (savedId) {
      getUser(Number(savedId))
        .then(() => setUserId(Number(savedId)))
        .catch(() => localStorage.removeItem('userId'))
        .finally(() => setLoading(false))
    } else {
      setLoading(false)
    }
  }, [])

  const handleSetUserId = (id) => {
    setUserId(id)
    localStorage.setItem('userId', String(id))
  }

  const goHome = () => {
    setPage('home')
    setDiagnosisData(null)
    setResultData(null)
  }

  const handleLogout = () => {
    setUserId(null)
    localStorage.removeItem('userId')
    setPage('home')
    setDiagnosisData(null)
    setResultData(null)
  }

  const handleStartDiagnosis = async () => {
    try {
      const res = await startDiagnosis(userId)
      setDiagnosisData(res.data)
      setPage('diagnosis')
    } catch {
      alert('診断の開始に失敗しました')
    }
  }

  if (loading) {
    return (
      <div className="container" style={{ textAlign: 'center', paddingTop: 100 }}>
        <p>読み込み中...</p>
      </div>
    )
  }

  return (
    <div className="container">
      {page === 'home' && (
        <Home
          userId={userId}
          setUserId={handleSetUserId}
          onLogout={handleLogout}
          onStartDiagnosis={(data) => {
            setDiagnosisData(data)
            setPage('diagnosis')
          }}
          onGoDashboard={() => setPage('dashboard')}
          onGoPractice={() => setPage('practice')}
        />
      )}
      {page === 'diagnosis' && diagnosisData && (
        <Diagnosis
          diagnosisData={diagnosisData}
          userId={userId}
          onComplete={(result) => {
            setResultData(result)
            setPage('results')
          }}
          onBack={goHome}
        />
      )}
      {page === 'results' && resultData && (
        <Results
          result={resultData}
          userId={userId}
          onBack={goHome}
          onDashboard={() => setPage('dashboard')}
          onStartPractice={(data) => {
            setDiagnosisData(data)
            setPage('diagnosis')
          }}
          onPractice={() => setPage('practice')}
        />
      )}
      {page === 'practice' && userId && (
        <Practice
          userId={userId}
          onStartPractice={(data) => {
            setDiagnosisData(data)
            setPage('diagnosis')
          }}
          onBack={goHome}
        />
      )}
      {page === 'dashboard' && userId && (
        <Dashboard
          userId={userId}
          onStartDiagnosis={handleStartDiagnosis}
          onBack={goHome}
        />
      )}
    </div>
  )
}
