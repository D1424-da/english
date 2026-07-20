import React, { useState } from 'react'
import Home from './pages/Home'
import Diagnosis from './pages/Diagnosis'
import Results from './pages/Results'
import Dashboard from './pages/Dashboard'
import { startDiagnosis } from './api'

export default function App() {
  const [page, setPage] = useState('home')
  const [userId, setUserId] = useState(null)
  const [diagnosisData, setDiagnosisData] = useState(null)
  const [resultData, setResultData] = useState(null)

  const goHome = () => {
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

  return (
    <div className="container">
      {page === 'home' && (
        <Home
          userId={userId}
          setUserId={setUserId}
          onStartDiagnosis={(data) => {
            setDiagnosisData(data)
            setPage('diagnosis')
          }}
          onGoDashboard={() => setPage('dashboard')}
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
