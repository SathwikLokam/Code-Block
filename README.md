# **CodeBlock Automation Tool**

## **Description**

CodeBlock is an automation tool designed to assist users with coding by listening for specific key sequences and triggering actions in response. It uses keyboard listeners and can automate repetitive tasks, trigger Python scripts, and provide notifications when certain conditions are met.

This tool is primarily built for Python automation but can be extended for various other uses. When a specific sequence of keys (e.g., "buddy") is typed, the program can execute tasks such as running Python scripts, controlling the keyboard/mouse, and displaying alerts or notifications.

---

## **Features**

- **Key Sequence Listener**: Detects and reacts to a predefined sequence of characters typed on the keyboard (e.g., typing "buddy").
- **Automation**: Executes tasks like launching Python scripts, opening files, and controlling the mouse or keyboard based on key presses.
- **Customizable Hotkeys**: Configurable hotkeys (e.g., F12 for running a clip, F4 for triggering exit confirmation).
- **Error Handling**: If the program encounters an error, it handles exceptions gracefully and alerts the user.
- **Sound & Notifications**: Plays a sound and shows a pop-up notification when the tool is launched or terminated.
- **Background Execution**: Utilizes threading to run the keyboard listener in the background without blocking the main program.

---

## **Technologies Used**

- **Python**: Main programming language.
- **pynput**: Used to listen for keyboard and mouse events.
- **pyautogui**: Automates keyboard and mouse control.
- **ctypes**: Windows API used for showing message boxes.
- **tkinter**: For creating GUI message boxes and notifications.
- **playsound**: Plays sound files when certain actions occur.
- **threading**: Ensures background tasks run smoothly without freezing the program.
