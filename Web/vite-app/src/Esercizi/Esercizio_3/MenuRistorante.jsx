import React from "react"
import piatti from "./piatti"

const MenuRistorante = () => {
    
    return (
        <>
        {piatti.map((piatto) => {

            return (
                <ul>
                    <li key = {piatto.id} > {piatto.nome} - {piatto.prezzo} euro </li>
                </ul>
            )
        }

        )}
        
        </>
    )
}

export default MenuRistorante