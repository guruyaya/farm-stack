import './App.css';
import React, {useState, useEffect} from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import config from './config.json';
import TodoView from './components/TodoListView';

function App() {

  const [todoList, setTodoList] = useState([{}]);
  const [title, setTitle] = useState('');
  const [desc, setDesc] = useState('desc');

  useEffect(() => {
    axios.get( config.server_url + '/api/todo/' )
      .then(res => {
        setTodoList(res.data);
      });
  });

  const addTodoHandler = () => {
    axios.post( config.server_url + '/api/todo/', {
      'title': title, 'description': desc
    } ).then(res => console.log(res));
  }

  return (
    <div className="App list-group-items
      justtify-content-center align-items-center
      mx-auto" style={{"width": "400px",
      "backgroundColor": "white", "marginTop": "15px"}}>
        <h1 className="card text-white bg-primary mb-1"
        style={{maxWidth: "20em"}}>Task Manager</h1>
        <h6 className="card text-white bg-primary mb-1">
          FASTAPI - React - MongoDB
        </h6>
        <div className="card-body">
          <h5 className="card text-white bg-dark mb-3">Add your task</h5>
          <span className="card-text">
            <input type="text" className="mb-2 form-control titleIn" placeholder="Title"
              onChange={event => setTitle(event.target.value)} />
            <input type="text" className="mb-2 form-control desIn" placeholder="Description" 
              onChange={event => setDesc(event.target.value)}/>
            <button className="btn btn-outline-primary mx-2 mb-3" 
            style={{'borderRadius': '50px', "fontWeight": "bold"}}
            onClick={addTodoHandler}>Add Task</button>
          </span>

          <h5 className="card text-white bg-dark mb-3">Your tasks</h5>
          <div>
            <TodoView todoList={todoList} />
          </div>
        </div>
    </div>
  );
}

export default App;
