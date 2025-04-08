import React, { useEffect, useState } from 'react';
import { Table } from 'react-bootstrap';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    fetch('https://improved-space-waddle-6v9g76jg5g62x6rr-8000.app.github.dev/api/leaderboard')
      .then(response => response.json())
      .then(data => setLeaderboard(data));
  }, []);

  return (
    <div>
      <h1 className="text-center my-4">Leaderboard</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Score</th>
          </tr>
        </thead>
        <tbody>
          {leaderboard.map(entry => (
            <tr key={entry.id}>
              <td>{entry.id}</td>
              <td>{entry.name}</td>
              <td>{entry.score}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
}

export default Leaderboard;