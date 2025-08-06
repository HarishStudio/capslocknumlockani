# capslocknumlockani 🔒🔢

**capslocknumlockani** is a lightweight, portable utility that visually notifies you when Caps Lock or Num Lock keys are toggled.  
It combines the power of native C for fast key state detection with a modern Tkinter-based animation frontend.

---

## ✨ Features

- 🧠 Real-time detection of Caps Lock and Num Lock
- 🪄 Smooth animated overlay (like macOS-style notifications)
- 💻 Clean Python GUI with large, centered display
- 🪶 Lightweight & portable — no installation needed
- 👻 Runs silently in the background

---

## 🗂️ Project Structure

```
capslocknumlockani/
├── backEnd.c            # C backend to monitor key state
├── backEnd.exe          # Compiled C executable (runs silently)
├── frontEnd.py          # Tkinter frontend animation script
├── frontEnd.exe         # PyInstaller-built GUI (no console)
├── caps_lock.png        # Caps Lock ON icon
├── num_lock.png         # Num Lock ON icon
├── num_unlock.png       # Num Lock OFF icon
```

---

## 🚀 How to Use

1. Clone or download the repo.
2. Run `backEnd.exe` — this starts the background key listener.
3. Press `Caps Lock` or `Num Lock` to trigger the animation popup.
4. Make sure all `.exe` and `.png` files stay in the **same folder**.

---

## ⚙️ Build Instructions

### 🔧 Backend (C)

Compile `backEnd.c` to a silent `.exe` (no terminal window):
```bash
gcc backEnd.c -o backEnd.exe -mwindows
```

### 🎨 Frontend (Python)

Use PyInstaller to create a GUI-only `.exe`:
```bash
pyinstaller frontEnd.py --onefile --windowed ^
  --add-data "caps_lock.png;." ^
  --add-data "num_lock.png;." ^
  --add-data "num_unlock.png;."
```

> Windows CMD syntax shown. On Linux/Mac use `:` instead of `;`.

---

## 📄 License

MIT License – free to use and modify.

---

## 🧠 Credits

Made with ❤️ by Harish
Optimized for focus-driven users who like clean UI + fast feedback.
