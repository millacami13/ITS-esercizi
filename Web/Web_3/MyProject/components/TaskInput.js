import { useState } from 'react';
import { StyleSheet,TextInput, View, Button } from "react-native";

const TaskInput = (props) => {
    const [task, setTask] = useState("");
  function addTask(){
        props.onAddTask(task)
        setTask("")
    }
    return(
    <View style = { styles.inputContainer } >
            <TextInput
              style={styles.textInput}
              placeholder='Inserisci task'
              onChangeText={setTask}
              value={task}
            />
            <Button
              title='Aggiungi'
              onPress={addTask}
              disabled={task === ""}
            ></Button>
          </View >
    );
};

export default TaskInput;

const styles = StyleSheet.create({
 textInput: {
    borderWidth: 1,
    borderColor: '#cccccc',
    width: '70%',
    padding: 8
  },
  inputContainer: {
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 24,
    borderBottomWidth: 1,
    borderColor: '#cccccc'
  }
});