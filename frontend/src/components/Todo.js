import config from '../config.json';
import axios from 'axios';
import React from 'react';

function TodoItem(props) {
    const deleteTodoHandler = title => {
        axios.delete(
            `${config.server_url}/api/todo/${title}`
        ).then(res => console.log(res.data));
    }

    return (
        <li>
            <span style={{ fontWeight: 'bold, underline' }}>{props.todo.title} : </span> {props.todo.description}
            <button onClick={() => deleteTodoHandler(props.todo.title)}
                className="btn btn-outline-danger my-2 mx-2" style={{borderRadius: '50px'}}
            >X</button>
            <hr />
        </li>
    );
}

export default TodoItem;