import React, { useEffect, useState } from "react";


const urlUsers = "https://jsonplaceholder.typicode.com/users";
const urlAlbums = "https://jsonplaceholder.typicode.com/albums";
//const urlPhotos = "https://jsonplaceholder.typicode.com/photos";
const UserAlbumsFullStack = () => {
  const [users, setUsers] = useState([]);
  const [userSelected, setUserSelected] = useState(0);


  const [albums, setAlbums] = useState([]);
  const [albumSelected, setAlbumSelected] = useState(0);


  const getUsers = async () => {
    try {
      const response = await fetch(urlUsers);
      const result = await response.json();
      setUsers(result);
    } catch (err) {
      console.log(err);
    }
  };


  const getAlbums = async () => {
    try {
      const response = await fetch(urlAlbums);
      const result = await response.json();
      setAlbums(result);
    } catch (err) {
      console.log(err);
    }
  };


  useEffect(() => {
    getUsers();
    getAlbums();
  }, []);


  return (
    <div className="container">
      <h1>Gestione albums e photos</h1>
      <div className="row">
        <div className="col-6">
 <select
          className="form-select"
          value={userSelected}
          onChange={(e) => setUserSelected(e.target.value)}
        >
          <option value="">Seleziona Utente</option>


          {users.map((u) => {
            return (
              <option key={u.id} value={u.id}>
              
                {u.name}
              </option>
            );
          })}
        </select>


        </div>
       
        <div className="col-6">
             <select className="form-select">
          <option value="0"> seleziona album</option>
        </select>
        </div>
       
      </div>


      <div className="row">
        <div className="col-12"></div>
      </div>
    </div>
  );
};


export default UserAlbumsFullStack;
