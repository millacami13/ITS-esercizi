import React, { useEffect, useState } from 'react';
import ToDoForm from './ToDoForm';
import ToDoList from './ToDoList';

const API_URL = "http://localhost:4000/tasks";
const ToDoApp = () => {
    
    const [tasks, setTasks] = useState([]);
    const [loading, setLoadig] = useState ("")
    const [error, setError] = useState (null);

    const getTasks = async ()=> {
        try{
            const response = await fetch(API_URL);
            const data = await response.json();
            if (!response.ok) throw Error ("Errore nella fetch");
            setTasks(data);
        }catch(err){
            setError(err)
        }finally{
            setLoadig (false)
        }
    }
    const deleteTask = async (id) => {
        await fetch (API_URL+"/"+id,{method: "DELETE"});
        getTasks();
    }
    useEffect (()=>{
        getTasks()
    },[])

  return(
    
    <div>ToDoApp
        <ToDoForm></ToDoForm>
        <ToDoList tasks = {tasks} onDeleteTask = {deleteTask}></ToDoList>
      
    </div>

  )
}

export default ToDoApp
