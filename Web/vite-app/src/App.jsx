import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import UserAlbumsFullStack from './Esercizi/UserAlbumsFullStack'
import Saluto from './Esercizi/Esercizio_1/Saluto'
import CardUtente from './Esercizi/Esercizio_2/CardUtente'
import MenuRistorante from './Esercizi/Esercizio_3/MenuRistorante'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <MenuRistorante></MenuRistorante>
    </>
  )
}

export default App
