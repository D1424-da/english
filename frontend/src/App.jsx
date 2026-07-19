import React, { useState } from 'react'
import Home from './pages/Home'
import Diagnosis from './pages/Diagnosis'
import Results from './pages/Results'

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
        <Results result={resultData} onBack={goHome} />
      )}
    </div>
  )
}
