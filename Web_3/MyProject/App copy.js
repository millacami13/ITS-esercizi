import { StatusBar } from 'expo-status-bar';
import { use, useState } from 'react';
import { Button, FlatList, StyleSheet, Text, TextInput, View, Modal} from 'react-native';

export default function App() {
  const [messaggio, setMessaggio] = useState ("Ciao")
  const [visible, setVisible] = useState (false)
  const [nome, setNome] = useState ("")
  const [openModal, setOpenModal] = useState (false)
  const [contatore, setContatore] = useState (0)

  const dati = [
    {id : "1", nome : "Camilla"},
    {id : "2", nome : "Matteo"},
    {id : "3", nome: "Gigi"}
  ]
  return (
    <View style={styles.container}>
      <Text>{nome}</Text>
      {visible && <Text> {messaggio}</Text>}
      <TextInput placeholder = "Inserisci testo" onChangeText = {setNome} style = {styles.inputText}></TextInput>
      <Button 
        title = "Cambia testo"  
        onPress={()=>setMessaggio ("Ho premuto il pulsante")}
      />
      <Button 
        title = {visible ? "Nascondi" : "Visualizza"}  
        onPress={()=>setVisible (!visible)}
      />
      <Text>{contatore}</Text>
      <Button
       title = "Incrementa" 
       onPress={() => setContatore (current => current +1)}>
      </Button>
      <Button
       title = "Decreementa" 
       onPress={() => setContatore(current => current -1)}>
      qw</Button>

      <View style = {styles.containerList}>
        <FlatList
        data = {dati}
        renderItem = {(dato) => <Text> {dato.item.nome}</Text>}
        keyExtractor = {(item) =>item.id}
        />
        </View>
        <View style = {styles.containerList}>
          <Text>Buonasera</Text>
          <Button
           title = "Apri" 
           onPress={() => setOpenModal(true)}></Button>
           <Modal visible = {openModal} animationType = "slide">
            <View style = {styles.container}>
              <Text>Adoro</Text>
              <Button
               title = "CHiudi" 
               onPress = {() => setOpenModal(false)}></Button>
            </View>
           </Modal>
      </View>

    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "skyblue",
    alignItems: "center",
    justifyContent: "center",
    paddingHorizontal : 46,
    padding : 50
  },
  containerList : {
    flex : 3,
    backgroundColor : "skyblue",
    allignItems : "center",
    justifyContent : "center",
  },
  inputText:{
    borderWidth : 1,
    padding :10
  }
});
