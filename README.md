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
# 🚀 Auto-Launch on Windows Startup

To automatically launch `backEnd.exe` on system startup (so Caps Lock / Num Lock animations work from boot):

---

## ✅ Method 1: Add a Shortcut to Startup Folder (Recommended)

1. Press `Win + R`, type:
   ```
   shell:startup
   ```
   and hit **Enter** — this opens the Windows startup folder.

2. Right-click inside the folder → `New > Shortcut`.

3. In the location box, type the **full path** to `backEnd.exe`, for example:
   ```
   "D:\Key Indicator Project\Key Indicator App\backEnd.exe"
   ```

4. Click **Next**, name it:
   ```
   CapsNum Indicator
   ```
   and click **Finish**.

> ✅ Now `backEnd.exe` will silently run in background on every Windows startup.

---

## 💡 Tip

- Make sure all files (including icons and `frontEnd.exe`) stay in the **same folder**.
- You can place this folder anywhere, but **don't delete or move it** after setting up the shortcut.

---

## ❌ Don't Use Task Scheduler (unless advanced)

For most users, the startup folder method is:
- Easier to manage
- Launches quicker
- Doesn't trigger UAC or admin prompts

---


## 📄 License

MIT License – free to use and modify.

---

## 🧠 Credits

Made with ❤️ by Harish
Optimized for focus-driven users who like clean UI + fast feedback.
