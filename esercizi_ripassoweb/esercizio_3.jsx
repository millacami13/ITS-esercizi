import React from 'react'
import { useState } from 'react'

const esercizio_3 = () => {
    const [contatore, setContatore] = useState (0);
  return (
    <div>
        <p>{contatore}</p>
        <button onClick={() => setContatore(contatore + 1)}>incrementa</button>
      
    </div>
  )
}

export default esercizio_3
