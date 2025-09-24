import React from 'react'
import ToDoItem from './ToDoItem'

const ToDoList = ({tasks = [], onDeleteTask}) => {

  return (
    <ul className = "list-group">
      {tasks.map((t) => {
        return (
          <ToDoItem key = {t.id} task = {t} onDeleteTask={onDeleteTask}></ToDoItem>
        );
      })}
    </ul>
  );
};

export default ToDoList;
