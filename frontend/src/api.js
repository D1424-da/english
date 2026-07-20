import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
})

export const healthCheck = () => api.get('/health')

export const createUser = (data) => api.post('/users/', data)
export const loginUser = (data) => api.post('/users/login', data)
export const getUser = (id) => api.get(`/users/${id}`)

export const getLayers = () => api.get('/questions/layers')
export const getCategories = (layerId) => api.get('/questions/categories', { params: { layer_id: layerId } })
export const getUnits = (categoryId) => api.get('/questions/units', { params: { category_id: categoryId } })

export const startDiagnosis = (userId) => api.post('/diagnosis/start', { user_id: userId })
export const startWeakPractice = (userId, unitCodes) =>
  api.post('/diagnosis/weak-practice', { user_id: userId, unit_codes: unitCodes })
export const submitAnswer = (sessionId, userId, questionId, choiceId) =>
  api.post(`/diagnosis/answer?session_id=${sessionId}&user_id=${userId}`, {
    question_id: questionId,
    selected_choice_id: choiceId,
  })
export const getDiagnosisResult = (sessionId, userId) =>
  api.post(`/diagnosis/result?session_id=${sessionId}&user_id=${userId}`)

export const getSessionHistory = (userId) => api.get(`/history/${userId}/sessions`)
export const getUserStats = (userId) => api.get(`/history/${userId}/stats`)
export const getUnitProgress = (userId) => api.get(`/history/${userId}/unit-progress`)

export default api
