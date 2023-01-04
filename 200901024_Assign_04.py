import threading

input_str = "" #store the input string


input_lock = threading.Lock()  #Lock to synchronize access to the input string, preventing race conditions

def input_thread():  #Input thread function
  global input_str  
  try:
    input_str = input("Enter a string: ")
  except EOFError:
    #Python stops the thread when there is an EOFError, allowing program to exit when no further input is required
    return
  except Exception as e:
    #Print other exception (if any)
    print(e)


def reverse_thread(): #Thread to reverse the input string
  global input_str  #Globally defined above
  with input_lock:  #Acquire the input lock (used in all thread functions just to be safe)
    input_str = input_str[::-1]  #Reverse string 
    print("The Reversed String becomes:", input_str)

#Thread to capitalize the input string
def capital_thread():
  global input_str
  with input_lock:
    input_str = input_str.upper()  #Capitalizing input string using upper function built in python
    print("The Capitalized String becomes:", input_str)


def shift_thread(): #Thread to shift the characters in the input string
  global input_str
  with input_lock:  #locking input here as well to prevent race condition
    # Shift the characters in the input string
    shifted_str = ""
    for ch in input_str:
      shifted_str += chr(ord(ch) + 2)  #Right shift of 2 characters (for characters x,y,z it may give other non alphabetical strings)
    input_str = shifted_str
    print("The Shifted String becomes:", input_str)

#Create threads
input_t = threading.Thread(target=input_thread)
reverse_t = threading.Thread(target=reverse_thread)
capital_t = threading.Thread(target=capital_thread)
shift_t = threading.Thread(target=shift_thread)

#Start the input thread
input_t.start()

# Wait for the input thread to finish
input_t.join()  

#Start the other threads
reverse_t.start()
capital_t.start()
shift_t.start()

# Wait for the other threads to finish avoiding race condition
reverse_t.join()
capital_t.join()
shift_t.join()