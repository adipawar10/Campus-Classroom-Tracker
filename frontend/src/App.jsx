import { useState, useEffect } from 'react'

function App() {
  const [tickets, setTickets] = useState([])

  useEffect(() => {
    fetch('http://127.0.0.1:8000/tickets')
      .then(res => res.json())
      .then(data => setTickets(data))
      .catch(err => console.error("Database connection failed:", err))
  }, [])

  return (
    <div style={{ padding: '40px', fontFamily: 'sans-serif' }}>
      <h1>Campus Tracker 🛠️</h1>
      <h2>Live Tickets from Postgres:</h2>
      {tickets.map(t => (
        <div key={t.ticket_id} style={{ border: '1px solid #ddd', padding: '15px', borderRadius: '8px', margin: '10px 0' }}>
          <h3>{t.title}</h3>
          <p>{t.description}</p>
          <span style={{ background: '#eee', padding: '5px', borderRadius: '4px' }}>Priority: {t.priority}</span>
        </div>
      ))}
    </div>
  )
}

export default App