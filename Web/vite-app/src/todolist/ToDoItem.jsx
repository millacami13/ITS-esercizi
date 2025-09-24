import React from 'react';

const ToDoItem = ({task,onDeleteTask}) => {
  return (
    <li className = "list-group-item d-flex justify-content-between">
      <div>
        <input
          type = "checkbox"
          checked = {task.completed}
          className = "form-check-input me-2"
        ></input>
        <span
          style = {{textDecoration: task.completed ? "line-through" : "nome"}}
        >
          {" "}
          {task.text}
        </span>
      </div>
      <button
        className = "btn btn-danger"
        onClick = {() => {
          onDeleteTask(task.id);
        }}
      >
        Delete
      </button>
    </li>    
  );
};

export default ToDoItem
