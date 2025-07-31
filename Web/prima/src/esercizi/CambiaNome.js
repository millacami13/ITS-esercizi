import React, { useState } from 'react'

const CambiaNome = () => {
    const [nome, setNome] = useState ("Camilla");
    
    const cambia = () => {
        if (nome === "Camilla"){
            setNome ("Matteo")
        }else {
            setNome ("Camilla")
        }
    }
    return (
        <div>
            {nome}
            <button class = "btn btn-dark" onClick={cambia} >Cambia</button>
            </div>
            
        
  )
}

export default CambiaNome
