import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 90000, // 90s for multi-model processing
});

export const checkHealth = async () => {
  const response = await api.get('/health');
  return response.data;
};

export const getConfig = async () => {
  const response = await api.get('/config');
  return response.data;
};

export const generateContent = async (payload) => {
  const response = await api.post('/generate', payload);
  return response.data;
};

export const regeneratePlatformContent = async (payload) => {
  const response = await api.post('/regenerate', payload);
  return response.data;
};

export const rewriteContent = async (payload) => {
  const response = await api.post('/rewrite', payload);
  return response.data;
};

export const getHistory = async (limit = 50, skip = 0) => {
  const response = await api.get(`/history?limit=${limit}&skip=${skip}`);
  return response.data;
};

export const deleteHistoryItem = async (id) => {
  const response = await api.delete(`/history/${id}`);
  return response.data;
};

export default api;

