import axios from 'axios';

const API_URL = 'http://localhost:5000';

const logToBackend = async (message) => {
  try {
    await axios.post(`${API_URL}/log`, { message });
  } catch (error) {
    console.error('Erro ao enviar log para o backend:', error);
  }
};

const logToConsoleAndBackend = (message) => {
  const logMessage = `${new Date().toISOString()} - ${message}`;
  console.log(logMessage);
  logToBackend(logMessage);
};

logToConsoleAndBackend('API inicializada com sucesso.');

export const getUsers = async () => {
  const response = await axios.get(`${API_URL}/users`);
  return response.data;
};

export const createUser = async (data) => {
  const response = await axios.post(`${API_URL}/register_user`, data);
  return response.data;
};

export const updateUser = async (id, data) => {
  const response = await axios.put(`${API_URL}/user/${id}`, data);
  return response.data;
};

const api = {
  getUsers,
  createUser,
  updateUser,
};

export default api;
