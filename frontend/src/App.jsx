import { useState } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';
import axios from "axios";

function App() {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const sendData = async (e) => {
    e.preventDefault();
    setMessage("");

    const data = {
      key: name,
      value: password
    };

    try {
      const response = await axios.post("http://127.0.0.1:5000/api/data", data, {
        headers: {
          'Content-Type': 'application/json',
        }
      });
      
      setMessage(response.data.message || "Відповідь без повідомлення");
    } catch (error) {
      if (error.response) {
        setMessage(error.response.data.message || "Помилка сервера без повідомлення");
      } else {
        setMessage("Помилка при відправці даних");
      }
      console.error("Error sending data:", error);
    }
  };

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <form onSubmit={sendData}>
          <div>
            <label>Ім'я:</label>
            <input type="text" value={name} onChange={(e) => setName(e.target.value)} required />
          </div>
          <div>
            <label>Пароль:</label>
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
          </div>
          <button type="submit">Відправити</button>
        </form>
        {message && <p className="response-message">{message}</p>}
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  );
}

export default App;