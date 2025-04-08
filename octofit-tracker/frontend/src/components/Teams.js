import React, { useEffect, useState } from 'react';
import { Table } from 'react-bootstrap';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('https://improved-space-waddle-6v9g76jg5g62x6rr-8000.app.github.dev/api/teams')
      .then(response => response.json())
      .then(data => setTeams(data));
  }, []);

  return (
    <div>
      <h1 className="text-center my-4">Teams</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
          </tr>
        </thead>
        <tbody>
          {teams.map(team => (
            <tr key={team.id}>
              <td>{team.id}</td>
              <td>{team.name}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
}

export default Teams;