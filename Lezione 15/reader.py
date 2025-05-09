with open ("example.txt", mode="w", encoding="utf - 8") as file:

    message:str = "Hello world!\n"
    written_char:int = file.write(message)
    print (f"Written characters: {written_char}")


import time

class Stopwatch:

    def __init__(self):
        self.start_time = None
        self.end_time = None

    #memorizza l'ora attuale
    def __enter__(self):               
        self.start_time = time.time()
        return self    
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print (f"Elapsed time: {elapsed_time: 8f} seconds")

        if exc_type is not None:
            print(f"Exception type: {exc_type}")
            print(f"An error occured: {exc_value}")
            print(f"Traceback: {traceback}")

        return False
    pass
    
with Stopwatch():

    print("Hello World!")
    
    #blocca esecuzione per 2 secondi
    time.sleep(2)

with Stopwatch():

    print("Inizio del programma")
    time.sleep(2)
    print("Fine del programma")