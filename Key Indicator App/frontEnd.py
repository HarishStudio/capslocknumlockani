import tkinter as tk
from PIL import Image, ImageTk
import ctypes
import sys
import sys, os

def resource_path(relative_path):
    # For PyInstaller compatibility (single .exe mode)
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def get_screen_size():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)
    return screen_width, screen_height

def show_popup(image_path, message_text="CAPS LOCK ON", is_on=True):
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes('-topmost', True)
    root.attributes('-alpha', 0.0)  # Start fully transparent
    bg_color = "#FFA500" if is_on else "white"  # Orange tint for ON

    root.configure(bg=bg_color)

    # Load and resize image
    img = Image.open(resource_path("caps_lock.png"))
    try:
        resample_filter = Image.Resampling.LANCZOS
    except AttributeError:
        resample_filter = Image.ANTIALIAS

    img = img.resize((90, 90), resample_filter)  # Bigger icon
    icon = ImageTk.PhotoImage(img)

    # Layout
    label_icon = tk.Label(root, image=icon, bg=bg_color)
    label_icon.pack(pady=(15, 5))

    label_text = tk.Label(root, text=message_text, font=("Arial", 18, "bold"), bg=bg_color)
    label_text.pack(pady=(0, 10))

    # Sizing and positioning
    screen_w, screen_h = get_screen_size()
    win_w, win_h = 230, 195  # ~6cm x ~7cm on 1080p
    x = (screen_w - win_w) // 2
    y = screen_h - win_h - 50  # ~50px above taskbar

    root.geometry(f"{win_w}x{win_h}+{x}+{y}")

    # Fade-in animation
    def fade_in(alpha=0.0):
        alpha += 0.05
        if alpha <= 0.95:
            root.attributes("-alpha", alpha)
            root.after(30, fade_in, alpha)
        else:
            root.attributes("-alpha", 0.95)

    fade_in()

    # Auto destroy after 2 seconds
    root.after(2000, root.destroy)

    root.mainloop()

# Example usage
# You can call it with: python frontEnd.py caps_on / num_off etc.

arg = sys.argv[1] if len(sys.argv) > 1 else "caps_on"

if arg == "caps_on":
    show_popup("caps_lock.png", "CAPS LOCK ON", is_on=True)
elif arg == "caps_off":
    show_popup("caps_lock.png", "CAPS LOCK OFF", is_on=False)
elif arg == "num_on":
    show_popup("num_lock.png", "NUM LOCK ON", is_on=True)
elif arg == "num_off":
    show_popup("num_unlock.png", "NUM LOCK OFF", is_on=False)
else:
    show_popup("caps_lock.png", "UNKNOWN STATE", is_on=False)


