import React, { useState, useEffect } from 'react';
import { getUsers, createUser, updateUser } from '../services/api';
import './Home.css';

const Home = () => {
  const [users, setUsers] = useState([]);
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    email: '',
    username: '',
    password: '',
  });
  const [editingUserId, setEditingUserId] = useState(null);

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    const data = await getUsers();
    setUsers(data);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (editingUserId) {
      await updateUser(editingUserId, formData);
    } else {
      await createUser(formData);
    }
    setFormData({ first_name: '', last_name: '', email: '', username: '', password: '' });
    setEditingUserId(null);
    fetchUsers();
  };

  const handleEdit = (user) => {
    setFormData({
      first_name: user.first_name,
      last_name: user.last_name,
      email: user.email,
      username: user.username,
      password: '',
    });
    setEditingUserId(user.id);
  };

  return (
    <div className="home">
      <h1>Gerenciar Usuários</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="first_name"
          placeholder="Primeiro Nome"
          value={formData.first_name}
          onChange={handleInputChange}
          required
        />
        <input
          type="text"
          name="last_name"
          placeholder="Último Nome"
          value={formData.last_name}
          onChange={handleInputChange}
          required
        />
        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleInputChange}
          required
        />
        <input
          type="text"
          name="username"
          placeholder="Username"
          value={formData.username}
          onChange={handleInputChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Senha"
          value={formData.password}
          onChange={handleInputChange}
          required
        />
        <button type="submit">{editingUserId ? 'Atualizar' : 'Criar'} Usuário</button>
      </form>

      <h2>Lista de Usuários</h2>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            {user.first_name} {user.last_name} ({user.email})
            <button onClick={() => handleEdit(user)}>Editar</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Home;
