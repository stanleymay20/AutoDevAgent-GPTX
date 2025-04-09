import React, { useState } from 'react';

function App() {
  const [tasks, setTasks] = useState([]);

  const addTask = task => {
    setTasks([...tasks, { text: task, done: false }]);
  };

  return (
    <div className="container">
      <h1>Task Manager</h1>
      <form onSubmit={e => { e.preventDefault(); addTask(e.target.task.value); }}>
        <input name="task" />
        <button type="submit">Add</button>
      </form>
      <ul>
        {tasks.map((t, i) => (
          <li key={i}>{t.text}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
