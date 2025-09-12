import React, { useState } from 'react';
import api from '../services/api';
import './Login.css';

const logToBackend = async (message) => {
  try {
    await api.post('/log', { message });
  } catch (error) {
    console.error('Erro ao enviar log para o backend:', error);
  }
};

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await api.post('/login', { username, password });
      alert('Login bem-sucedido!');
      console.log(response.data);
      logToBackend(`Login bem-sucedido para o usuário: ${username}`);
    } catch (error) {
      logToBackend(`Erro no login para o usuário: ${username} - ${error.message}`);
      alert('Erro no login!');
      console.error(error);
    }
  };

  return (
    <div className="login-container">
      <div className="login-box">
        <h1 className="login-title">Bem-vindo</h1>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Usuário"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="login-input"
          />
          <input
            type="password"
            placeholder="Senha"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="login-input"
          />
          <button type="submit" className="login-button">Entrar</button>
        </form>
      </div>
    </div>
  );
};

export default Login;
