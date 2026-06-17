#!/usr/bin/env python3
from __future__ import annotations
import shutil
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox, simpledialog
from pathlib import Path
from datetime import datetime
import threading
import time
import json

APP_NAME = "Lunaro Touch Launcher"
HOME = Path.home()
AUTOSTART_DIR = HOME / ".config" / "autostart"
DESKTOP_FILE = AUTOSTART_DIR / "lunaro.desktop"
ICON_DIR = HOME / "lunaro_icons"
BACKGROUND = HOME / "lunaro_background.png"

DB_FILE = HOME / "nfc_tags.json"
NFC_DUMPS_DIR = HOME / "NFC" / "dumps"
RF_DIR = HOME / "RF"
RF_HACKRF_DIR = RF_DIR / "hackrf"
RF_RTLSDR_DIR = RF_DIR / "rtlsdr"
RF_CAPTURES_DIR = RF_DIR / "captures"
RF_AUDIO_DIR = RF_DIR / "audio"
RF_NOTES_DIR = RF_DIR / "notes"
RF_SCRIPTS_DIR = RF_DIR / "scripts"
RF_PRESETS_DIR = RF_DIR / "presets"

def load_db():
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


BG = "#081018"
PANEL = "#0d1620"
CARD = "#132131"
CARD_HOVER = "#1f3f5a"
ACCENT = "#38d6ff"
ACCENT2 = "#74ffd4"
TEXT = "#eef7ff"
MUTED = "#9db1c5"
BORDER = "#1d445d"
DANGER = "#ff7373"

PAGES = {
    "Home": [
        {"title": "RF", "subtitle": "SDR and radio workspace", "icon_file": "rf.png", "nav": "RF"},
        {"title": "WiFi", "subtitle": "Packet capture and wireless tools", "icon_file": "wifi.png", "nav": "WiFi"},
        {"title": "NFC", "subtitle": "Tags, readers, and NFC tools", "icon_file": "nfc.png", "nav": "NFC"},
        {"title": "IR", "subtitle": "Infrared workflows and notes", "icon_file": "ir.png", "nav": "IR"},
        {"title": "Files", "subtitle": "Open work folders", "icon_file": "files.png", "nav": "Files"},
        {"title": "Tools", "subtitle": "General tools and utilities", "icon_file": "tools.png", "nav": "Tools"},
    ],
    "RF": [
        {"title": "RF Folder", "subtitle": "Open RF workspace", "icon_file": "rf_folder.png", "cmd": ["pcmanfm", str(HOME / "RF")]},
        {"title": "Terminal", "subtitle": "Open shell for RF work", "icon_file": "terminal.png", "cmd": ["lxterminal"]},
        {"title": "Logs", "subtitle": "Open logs folder", "icon_file": "logs.png", "cmd": ["pcmanfm", str(HOME / "Logs")]},
    ],
    "WiFi": [
        {"title": "Wireshark", "subtitle": "Capture and inspect packets", "icon_file": "wireshark.png", "cmd": ["wireshark"]},
        {"title": "Nmap Scan", "subtitle": "Version scan", "icon_file": "nmap.png", "cmd": ["lxterminal", "-e", "bash -lc 'nmap -sV scanme.nmap.org; echo; read -n 1 -s -r -p \"Press any key to close...\"'"]},
        {"title": "WiFi Folder", "subtitle": "Open WiFi workspace", "icon_file": "wifi_folder.png", "cmd": ["pcmanfm", str(HOME / "WiFi")]},
    ],
    "NFC": [
        {"title": "NFC Tools", "subtitle": "Open NFC helper terminal", "icon_file": "nfc_tools.png", "nav": "NFC_MENU"},
        {"title": "NFC Folder", "subtitle": "Open NFC workspace", "icon_file": "nfc_folder.png", "cmd": ["pcmanfm", str(HOME / "NFC")]},
        {"title": "Terminal", "subtitle": "Open shell for NFC work", "icon_file": "terminal.png", "cmd": ["lxterminal"]},
    ],
    "IR": [
        {"title": "IR Folder", "subtitle": "Open IR workspace", "icon_file": "ir_folder.png", "cmd": ["pcmanfm", str(HOME / "IR")]},
        {"title": "Terminal", "subtitle": "Open shell for IR work", "icon_file": "terminal.png", "cmd": ["lxterminal"]},
        {"title": "Logs", "subtitle": "Open logs folder", "icon_file": "logs.png", "cmd": ["pcmanfm", str(HOME / "Logs")]},
    ],
    "Files": [
        {"title": "RF", "subtitle": "Open RF folder", "icon_file": "rf_folder.png", "cmd": ["pcmanfm", str(HOME / "RF")]},
        {"title": "NFC", "subtitle": "Open NFC folder", "icon_file": "nfc_folder.png", "cmd": ["pcmanfm", str(HOME / "NFC")]},
        {"title": "IR", "subtitle": "Open IR folder", "icon_file": "ir_folder.png", "cmd": ["pcmanfm", str(HOME / "IR")]},
        {"title": "WiFi", "subtitle": "Open WiFi folder", "icon_file": "wifi_folder.png", "cmd": ["pcmanfm", str(HOME / "WiFi")]},
        {"title": "Logs", "subtitle": "Open Logs folder", "icon_file": "logs.png", "cmd": ["pcmanfm", str(HOME / "Logs")]},
    ],
    "Tools": [
        {"title": "System Monitor", "subtitle": "Open htop", "icon_file": "monitor.png", "cmd": ["lxterminal", "-e", "htop"]},
        {"title": "Terminal", "subtitle": "Open shell", "icon_file": "terminal.png", "cmd": ["lxterminal"]},
        {"title": "Reboot", "subtitle": "Restart the Pi", "icon_file": "reboot.png", "action": "reboot", "danger": True},
        {"title": "Settings", "subtitle": "Launcher controls", "icon_file": "fullscreen.png", "nav": "Settings"},
    ],
    "Settings": [
        {"title": "Back", "subtitle": "Return to previous screen", "icon_file": "back.png", "action": "back"},
        {"title": "Fullscreen", "subtitle": "Toggle fullscreen mode", "icon_file": "fullscreen.png", "action": "fullscreen"},
        {"title": "Exit to Desktop", "subtitle": "Close launcher and return to desktop", "icon_file": "desktop.png", "action": "exit_to_desktop"},
        {"title": "Exit Launcher", "subtitle": "Close the launcher", "icon_file": "exit.png", "action": "exit", "danger": True},
    ],

    "RF": [
    {
        "title": "HackRF Info",
        "subtitle": "Detect HackRF and show details",
        "icon_file": "rf.png",
        "action": "hackrf_info"
    },
    {
        "title": "RTL-SDR Info",
        "subtitle": "Detect NESDR / RTL-SDR device",
        "icon_file": "rf.png",
        "action": "rtlsdr_info"
    },
    {
        "title": "RF Folder",
        "subtitle": "Open main RF workspace",
        "icon_file": "rf_folder.png",
        "cmd": ["pcmanfm", str(RF_DIR)]
    },
    {
        "title": "Captures",
        "subtitle": "Open RF captures folder",
        "icon_file": "files.png",
        "cmd": ["pcmanfm", str(RF_CAPTURES_DIR)]
    },
    {
        "title": "Terminal",
        "subtitle": "Open shell for RF work",
        "icon_file": "terminal.png",
        "cmd": ["lxterminal"]
    },
    {
        "title": "More...",
        "subtitle": "Advanced RF options",
        "icon_file": "tools.png",
        "nav": "RF_ADVANCED"
    }
    ],"RF_ADVANCED": [
    {
        "title": "HackRF Folder",
        "subtitle": "Open HackRF workspace",
        "icon_file": "rf_folder.png",
        "cmd": ["pcmanfm", str(RF_HACKRF_DIR)]
    },
    {
        "title": "RTL-SDR Folder",
        "subtitle": "Open RTL-SDR workspace",
        "icon_file": "rf_folder.png",
        "cmd": ["pcmanfm", str(RF_RTLSDR_DIR)]
    },
    {
        "title": "Audio Folder",
        "subtitle": "Open RF audio folder",
        "icon_file": "files.png",
        "cmd": ["pcmanfm", str(RF_AUDIO_DIR)]
    },
    {
        "title": "Notes Folder",
        "subtitle": "Open RF notes folder",
        "icon_file": "files.png",
        "cmd": ["pcmanfm", str(RF_NOTES_DIR)]
    },
    {
        "title": "HackRF Mode Help",
        "subtitle": "Reminder for Pi-side USB use",
        "icon_file": "tools.png",
        "action": "hackrf_mode_help"
    },
    {
        "title": "Back",
        "subtitle": "Return to RF tools",
        "icon_file": "back.png",
        "nav": "RF"
    }
    ],"RF_PRESETS": [
    {
        "title": "HackRF Info",
        "subtitle": "Run hackrf_info in output window",
        "icon_file": "rf.png",
        "action": "hackrf_info"
    },
    {
        "title": "RTL Test",
        "subtitle": "Run rtl_test detection check",
        "icon_file": "rf.png",
        "action": "rtlsdr_info"
    },
    {
        "title": "HackRF Script",
        "subtitle": "Create HackRF capture template",
        "icon_file": "files.png",
        "action": "make_hackrf_template"
    },
    {
        "title": "RTL Script",
        "subtitle": "Create RTL-SDR capture template",
        "icon_file": "files.png",
        "action": "make_rtlsdr_template"
    },
    {
        "title": "Scripts Folder",
        "subtitle": "Open RF scripts folder",
        "icon_file": "files.png",
        "cmd": ["pcmanfm", str(RF_SCRIPTS_DIR)]
    },
    {
        "title": "Capture Presets",
        "subtitle": "RF test and script templates",
        "icon_file": "tools.png",
        "nav": "RF_PRESETS"
    },
    {
        "title": "Back",
        "subtitle": "Return to RF advanced",
        "icon_file": "back.png",
        "nav": "RF_ADVANCED"
    }
    ],
    "NFC_MENU": [
    {
        "title": "Scan Once",
        "subtitle": "Read a tag one time",
        "icon_file": "nfc.png",
        "action": "nfc_scan_once"
    },
    {
        "title": "UID Only",
        "subtitle": "Show only the UID line",
        "icon_file": "nfc.png",
        "action": "nfc_uid_only"
    },
    {
        "title": "Saved Tags",
        "subtitle": "View saved NFC tags",
        "icon_file": "files.png",
        "action": "view_saved_tags"
    },
    {
        "title": "Rename Last Tag",
        "subtitle": "Rename the most recently scanned tag",
        "icon_file": "nfc.png",
        "action": "rename_last_scanned_tag"
    },
    {
        "title": "Backup Tag",
        "subtitle": "Save current tag to dump file",
        "icon_file": "files.png",
        "action": "nfc_backup_tag"
    },
    {
        "title": "More...",
        "subtitle": "Advanced NFC options",
        "icon_file": "nfc_tools.png",
        "nav": "NFC_ADVANCED"
    }
],"NFC_ADVANCED": [
    {
        "title": "Restore Tag",
        "subtitle": "Write a saved dump to a blank tag",
        "icon_file": "nfc.png",
        "action": "nfc_restore_tag"
    },
    {
        "title": "Verify Restore",
        "subtitle": "Compare current tag to latest dump",
        "icon_file": "nfc.png",
        "action": "nfc_verify_restore"
    },
    {
        "title": "Dumps Folder",
        "subtitle": "Open NFC dump files",
        "icon_file": "files.png",
        "cmd": ["pcmanfm", str(NFC_DUMPS_DIR)]
    },
    {
        "title": "Logs",
        "subtitle": "Open scan logs",
        "icon_file": "files.png",
        "cmd": ["pcmanfm", str(HOME / "Logs")]
    },
    {
        "title": "Continuous Scan",
        "subtitle": "Temporarily disabled",
        "icon_file": "nfc.png",
        "action": "nfc_poll_disabled"
    },
    {
        "title": "Back",
        "subtitle": "Return to NFC tools",
        "icon_file": "back.png",
        "nav": "NFC_MENU"
    }
],
}

class LunaroLauncher:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title(APP_NAME)
        self.root.geometry("1024x600")
        self.root.configure(bg=BG)
        self.root.attributes("-fullscreen", True)

        self.status_var = tk.StringVar(value="Ready")
        self.clock_var = tk.StringVar(value="")
        self.current_page = "Home"
        self.page_history = []
        self.icon_cache = {}
        self.bg_img = None
        self.last_scanned_uid = None
        self._ensure_dirs()
        self._build_ui()
        self.render_page("Home", push_history=False)
        self.update_overlay()
        self.animate_ticker()
        self.tick_clock()

    def _ensure_dirs(self):
        for name in ["RF", "NFC", "IR", "WiFi", "Logs"]:
            (HOME / name).mkdir(exist_ok=True)

        NFC_DUMPS_DIR.mkdir(parents=True, exist_ok=True)

        for path in [
            RF_DIR,
            RF_HACKRF_DIR,
            RF_RTLSDR_DIR,
            RF_CAPTURES_DIR,
            RF_AUDIO_DIR,
            RF_NOTES_DIR,
            RF_SCRIPTS_DIR,
            RF_PRESETS_DIR,
        ]:
            path.mkdir(parents=True, exist_ok=True)
        rf_readme = RF_DIR / "README.txt"
        if not rf_readme.exists():
            rf_readme.write_text(
                "Lunaro RF Workspace\n\n"
                "hackrf/   -> HackRF-specific work\n"
                "rtlsdr/   -> RTL-SDR / NESDR work\n"
                "captures/ -> IQ captures and saved files\n"
                "audio/    -> demodulated audio and recordings\n"
                "notes/    -> RF notes, frequencies, presets\n",
                encoding="utf-8"
            )

    def _load_icon(self, filename):
        path = ICON_DIR / filename
        if filename in self.icon_cache:
            return self.icon_cache[filename]
        if not path.exists():
            return None
        try:
            img = tk.PhotoImage(file=str(path))
            self.icon_cache[filename] = img
            return img
        except Exception:
            return None

    def _build_ui(self):
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        header = tk.Frame(self.root, bg=PANEL, height=96, highlightthickness=1, highlightbackground=BORDER)
        header.grid(row=0, column=0, sticky="nsew")
        header.grid_propagate(False)

        left = tk.Frame(header, bg=PANEL)
        left.pack(side="left", padx=18, pady=10)
        tk.Label(left, text="LUNARO", fg=ACCENT, bg=PANEL, font=("DejaVu Sans", 28, "bold")).pack(anchor="w")
        tk.Label(left, text="Touch Console • RF • NFC • IR • WiFi", fg=MUTED, bg=PANEL, font=("DejaVu Sans", 11)).pack(anchor="w")

        right = tk.Frame(header, bg=PANEL)
        right.pack(side="right", padx=18, pady=10)
        tk.Label(right, textvariable=self.clock_var, fg=ACCENT2, bg=PANEL, font=("DejaVu Sans Mono", 12, "bold")).pack(anchor="e")

        ctrls = tk.Frame(right, bg=PANEL)
        ctrls.pack(anchor="e", pady=(8, 0))
        self._small_button(ctrls, "←", self.go_back).pack(side="left", padx=3)
        self._small_button(ctrls, "⛶", self.toggle_fullscreen).pack(side="left", padx=3)
        self._small_button(ctrls, "🏠", self.exit_to_desktop).pack(side="left", padx=3)
        self._small_button(ctrls, "✕", self.quit_confirm, danger=True).pack(side="left", padx=3)

        nav = tk.Frame(header, bg=PANEL)
        nav.pack(fill="x", padx=12, pady=(0, 8))
        for page in ["Home", "RF", "WiFi", "NFC", "IR", "Files", "Tools", "Settings"]:
            tk.Button(nav, text=page, command=lambda p=page: self.render_page(p),
                      font=("DejaVu Sans", 11, "bold"), fg=TEXT, bg=CARD,
                      activebackground=CARD_HOVER, activeforeground=TEXT,
                      bd=0, relief="flat", highlightthickness=1, highlightbackground=BORDER,
                      padx=12, pady=8, cursor="hand2").pack(side="left", padx=4)

        body = tk.Frame(self.root, bg=BG)
        body.grid(row=1, column=0, sticky="nsew", padx=16, pady=16)
        body.grid_rowconfigure(0, weight=1)
        body.grid_columnconfigure(0, weight=1)

        if BACKGROUND.exists():
            try:
                self.bg_img = tk.PhotoImage(file=str(BACKGROUND))
                bg_label = tk.Label(body, image=self.bg_img, bg=BG)
                bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
            except Exception:
                pass

        self.content = tk.Frame(body, bg=BG)
        self.content.grid(row=0, column=0, sticky="nsew")

        self.ticker_canvas = tk.Canvas(
            body,
            bg="#050b10",
            height=34,
            highlightthickness=2,
            highlightbackground="#38d6ff",
            bd=0,
        )
        self.ticker_canvas.place(x=8, y=8, width=990, height=34)

        self.ticker_text = self.ticker_canvas.create_text(
            990,
            17,
            text="Loading...",
            fill="#66ffd9",
            font=("DejaVu Sans Mono", 10, "bold"),
            anchor="w",
        )

        self.ticker_message = "Loading..."
        self.ticker_x = 990
        footer = tk.Frame(self.root, bg=PANEL, height=40, highlightthickness=1, highlightbackground=BORDER)
        footer.grid(row=2, column=0, sticky="nsew")
        footer.grid_propagate(False)
        tk.Label(footer, textvariable=self.status_var, fg=MUTED, bg=PANEL, font=("DejaVu Sans", 10), anchor="w").pack(fill="both", padx=14)

    def _small_button(self, parent, text, command, danger=False):
        bg = DANGER if danger else CARD
        active = "#7a3131" if danger else CARD_HOVER
        return tk.Button(parent, text=text, command=command, font=("DejaVu Sans", 16, "bold"),
                         width=3, fg=TEXT, bg=bg, activeforeground=TEXT,
                         activebackground=active, bd=0, relief="flat",
                         highlightthickness=1, highlightbackground=BORDER,
                         padx=4, pady=4, cursor="hand2")

    def tick_clock(self):
        self.clock_var.set(datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
        self.root.after(1000, self.tick_clock)

    def update_overlay(self):
        try:
            import psutil

            cpu = psutil.cpu_percent()
            ram = psutil.virtual_memory().percent

            temp = "N/A"
            try:
                with open("/sys/class/thermal/thermal_zone0/temp") as f:
                    temp = f"{int(f.read()) / 1000:.1f}"
            except Exception:
                pass

            ip = subprocess.getoutput("hostname -I | awk '{print $1}'").strip() or "N/A"

            wifi_raw = subprocess.getoutput("iwconfig wlan0 2>/dev/null")
            wifi_quality = "N/A"
            wifi_signal = "N/A"
            if "Link Quality" in wifi_raw:
                for line in wifi_raw.splitlines():
                    if "Link Quality" in line:
                        parts = line.strip()
                        if "Link Quality=" in parts:
                            try:
                                wifi_quality = parts.split("Link Quality=")[1].split()[0]
                            except Exception:
                                pass
                        if "Signal level=" in parts:
                            try:
                                wifi_signal = parts.split("Signal level=")[1].split()[0]
                            except Exception:
                                pass

            self.ticker_message = (
                f"LUNARO // CPU:{cpu}%  RAM:{ram}%  TEMP:{temp}°C  "
                f"IP:{ip}  WIFI:{wifi_quality}  SIG:{wifi_signal}  PAGE:{self.current_page}     "
            )

        except Exception as e:
            self.ticker_message = f"LUNARO // OVERLAY ERROR: {e}     "

        self.root.after(2000, self.update_overlay)
    def animate_ticker(self):
        self.ticker_canvas.coords(self.ticker_text, self.ticker_x, 17)
        self.ticker_canvas.itemconfig(self.ticker_text, text=self.ticker_message)

        bbox = self.ticker_canvas.bbox(self.ticker_text)
        if bbox is not None:
            text_width = bbox[2] - bbox[0]
        else:
            text_width = 300

        self.ticker_x -= 2
        if self.ticker_x < -text_width:
            self.ticker_x = 990

        self.root.after(40, self.animate_ticker)

    def render_page(self, page, push_history=True):
        if push_history and self.current_page != page:
            self.page_history.append(self.current_page)
        self.current_page = page

        for w in self.content.winfo_children():
            w.destroy()

        items = PAGES.get(page, [])
        cols = 3
        banner = tk.Frame(self.content, bg=PANEL, highlightthickness=1, highlightbackground=BORDER)
        banner.grid(row=0, column=0, columnspan=cols, sticky="ew", padx=6, pady=(0, 10))
        tk.Label(banner, text=page, fg=ACCENT, bg=PANEL, font=("DejaVu Sans", 18, "bold"), padx=12, pady=8).pack(side="left")

        for c in range(cols):
            self.content.grid_columnconfigure(c, weight=1)

        for i, item in enumerate(items):
            r, c = divmod(i, cols)
            self.make_card(self.content, item).grid(row=r+1, column=c, sticky="nsew", padx=10, pady=10)

        self.status_var.set(f"Viewing {page}")

    def make_card(self, parent, item):
        frame = tk.Frame(parent, bg=CARD, highlightthickness=2, highlightbackground=BORDER)
        icon = self._load_icon(item["icon_file"])

        if icon:
            top = tk.Button(frame, image=icon, command=lambda i=item: self.activate(i),
                            bg=CARD, activebackground=CARD_HOVER, bd=0, relief="flat", cursor="hand2")
            top.image = icon
        else:
            top = tk.Button(frame, text=item.get("title", "?"), command=lambda i=item: self.activate(i),
                            font=("DejaVu Sans", 20, "bold"), fg=ACCENT, bg=CARD,
                            activebackground=CARD_HOVER, activeforeground=ACCENT,
                            bd=0, relief="flat", cursor="hand2")

        top.pack(fill="x", pady=(12, 4))

        title = tk.Button(frame, text=item["title"], command=lambda i=item: self.activate(i),
                          font=("DejaVu Sans", 17, "bold"), fg=TEXT, bg=CARD,
                          activebackground=CARD_HOVER, activeforeground=TEXT,
                          bd=0, relief="flat", wraplength=220, cursor="hand2")
        title.pack(fill="x", padx=8, pady=(0, 2))

        subtitle = tk.Label(frame, text=item["subtitle"],font=("DejaVu Sans", 10), fg=MUTED, bg=CARD, wraplength=205, justify="center")
        subtitle.pack(fill="x", padx=12, pady=(0, 8))

        def enter(_=None):
            frame.configure(bg=CARD_HOVER)
            top.configure(bg=CARD_HOVER)
            title.configure(bg=CARD_HOVER)
            subtitle.configure(bg=CARD_HOVER)

        def leave(_=None):
            frame.configure(bg=CARD)
            top.configure(bg=CARD)
            title.configure(bg=CARD)
            subtitle.configure(bg=CARD)

        for widget in (frame, top, title, subtitle):
            widget.bind("<Enter>", enter)
            widget.bind("<Leave>", leave)

        return frame

    def show_output_window(self, title, initial_text="Working..."):
        win = tk.Toplevel(self.root)
        win.title(title)
        win.geometry("900x500")
        win.configure(bg=BG)

        frame = tk.Frame(win, bg=BG)
        frame.pack(fill="both", expand=True, padx=12, pady=12)

        header = tk.Label(
            frame,
            text=title,
            fg=ACCENT,
            bg=BG,
            font=("DejaVu Sans", 18, "bold")
        )
        header.pack(anchor="w", pady=(0, 8))

        text = tk.Text(
            frame,
            bg="#050b10",
            fg="#66ffd9",
            insertbackground="#66ffd9",
            font=("DejaVu Sans Mono", 10),
            wrap="word",
            relief="flat",
            highlightthickness=1,
            highlightbackground=BORDER
        )
        text.pack(fill="both", expand=True)

        text.insert("1.0", initial_text + "\n")
        text.config(state="disabled")

        btn_frame = tk.Frame(frame, bg=BG)
        btn_frame.pack(fill="x", pady=(10, 0))

        close_btn = tk.Button(
            btn_frame,
            text="Close",
            command=win.destroy,
            fg=TEXT,
            bg=CARD,
            activebackground=CARD_HOVER,
            activeforeground=TEXT,
            bd=0,
            relief="flat",
            padx=16,
            pady=8
        )
        close_btn.pack(side="right")

        return win, text

    def set_output_text(self, text_widget, content):
        text_widget.config(state="normal")
        text_widget.delete("1.0", "end")
        text_widget.insert("1.0", content)
        text_widget.config(state="disabled")
    def extract_nfc_uid(self, output: str) -> str | None:
        for line in output.splitlines():
            if "UID (NFCID1):" in line:
                return " ".join(
                    line.split("UID (NFCID1):", 1)[1].strip().split()
                ).upper()
        return None

    def log_nfc_scan(self, output: str):
        uid = self.extract_nfc_uid(output)
        if not uid:
            return

        self.last_scanned_uid = uid

        log_dir = HOME / "Logs"
        log_dir.mkdir(exist_ok=True)
        log_file = log_dir / "nfc_uids.log"

        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"{datetime.now().isoformat()} | {uid}\n")

        db = load_db()
        if uid not in db:
            db[uid] = {
                "name": "Unknown",
                "first_seen": datetime.now().isoformat()
            }
            save_db(db)

        tag_name = db.get(uid, {}).get("name", "Unknown")
        self.root.after(
            0,
            lambda: self.status_var.set(f"NFC scanned: {tag_name} ({uid})")
        )

    def show_saved_tags_window(self):
        db = load_db()

        win = tk.Toplevel(self.root)
        win.title("Saved NFC Tags")
        win.geometry("760x500")
        win.configure(bg=BG)

        outer = tk.Frame(win, bg=BG)
        outer.pack(fill="both", expand=True, padx=12, pady=12)

        header = tk.Label(
            outer,
            text="Saved NFC Tags",
            fg=ACCENT,
            bg=BG,
            font=("DejaVu Sans", 18, "bold")
        )
        header.pack(anchor="w", pady=(0, 10))

        text = tk.Text(
            outer,
            bg="#050b10",
            fg="#66ffd9",
            insertbackground="#66ffd9",
            font=("DejaVu Sans Mono", 10),
            wrap="word",
            relief="flat",
            highlightthickness=1,
            highlightbackground=BORDER
        )
        text.pack(fill="both", expand=True)

        if not db:
            content = "No saved NFC tags yet."
        else:
            lines = []
            for uid, info in sorted(db.items()):
                name = info.get("name", "Unknown")
                first_seen = info.get("first_seen", "Unknown")
                lines.append(f"Name: {name}")
                lines.append(f"UID : {uid}")
                lines.append(f"First seen: {first_seen}")
                lines.append("-" * 50)
            content = "\n".join(lines)

        text.insert("1.0", content)
        text.config(state="disabled")

        btn_row = tk.Frame(outer, bg=BG)
        btn_row.pack(fill="x", pady=(10, 0))

        rename_btn = tk.Button(
            btn_row,
            text="Rename Last Scanned Tag",
            command=lambda: [win.destroy(), self.rename_last_scanned_tag()],
            fg=TEXT,
            bg=CARD,
            activebackground=CARD_HOVER,
            activeforeground=TEXT,
            bd=0,
            relief="flat",
            padx=16,
            pady=8
        )
        rename_btn.pack(side="left")

        close_btn = tk.Button(
            btn_row,
            text="Close",
            command=win.destroy,
            fg=TEXT,
            bg=CARD,
            activebackground=CARD_HOVER,
            activeforeground=TEXT,
            bd=0,
            relief="flat",
            padx=16,
            pady=8
        )
        close_btn.pack(side="right")

    def rename_last_scanned_tag(self):
        if not self.last_scanned_uid:
            messagebox.showinfo(APP_NAME, "No tag has been scanned yet in this session.")
            return

        db = load_db()
        uid = self.last_scanned_uid

        current_name = db.get(uid, {}).get("name", "Unknown")

        new_name = simpledialog.askstring(
            "Rename NFC Tag",
            f"Enter a name for:\n{uid}",
            initialvalue=current_name,
            parent=self.root
        )

        if not new_name:
            return

        new_name = new_name.strip()
        if not new_name:
            return

        if uid not in db:
            db[uid] = {
                "name": new_name,
                "first_seen": datetime.now().isoformat()
            }
        else:
            db[uid]["name"] = new_name

        save_db(db)
        self.status_var.set(f"Renamed tag {uid} to {new_name}")
        messagebox.showinfo(APP_NAME, f"Saved tag name:\n{new_name}")

    def run_command_in_window(self, title, command):
        win, text = self.show_output_window(title, "Running...")

        def worker():
            try:
                result = subprocess.run(
                    command,
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                output = ""
                if result.stdout:
                    output += result.stdout
                if result.stderr:
                    output += "\n[stderr]\n" + result.stderr
                if not output.strip():
                    output = "(No output)"

                if title in ("NFC Scan Once", "NFC UID Only") and "UID (NFCID1):" in output:
                    self.log_nfc_scan(output)

            except Exception as e:
                output = f"Error:\n{e}"

            self.root.after(0, lambda: self.set_output_text(text, output))

        threading.Thread(target=worker, daemon=True).start()

    def run_nfc_poll_window(self):
        win, text = self.show_output_window(
            "NFC Continuous Scan",
            "Running nfc-poll...\nPresent a tag to the reader.\n"
        )

        def worker():
            try:
                proc = subprocess.Popen(
                    ["nfc-poll"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True
                )

                collected = []
                for line in proc.stdout:
                    collected.append(line)
                    current = "".join(collected)
                    self.root.after(0, lambda c=current: self.set_output_text(text, c))

                proc.wait()
            except Exception as e:
                self.root.after(0, lambda: self.set_output_text(text, f"Error:\n{e}"))

        threading.Thread(target=worker, daemon=True).start()
    def get_latest_nfc_dump(self) -> Path | None:
        dumps = sorted(NFC_DUMPS_DIR.glob("*.mfd"), key=lambda p: p.stat().st_mtime, reverse=True)
        return dumps[0] if dumps else None

    def backup_nfc_tag(self):
        win, text = self.show_output_window("NFC Backup Tag", "Place tag on reader...\n")

        def worker():
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            dump_file = NFC_DUMPS_DIR / f"nfc_backup_{timestamp}.mfd"

            try:
                result = subprocess.run(
                    ["nfc-mfultralight", "r", str(dump_file)],
                    capture_output=True,
                    text=True,
                    timeout=90
                )

                output = ""
                if result.stdout:
                    output += result.stdout
                if result.stderr:
                    output += "\n[stderr]\n" + result.stderr

                if result.returncode == 0 and dump_file.exists():
                    output += f"\n\nBackup saved to:\n{dump_file}\n"
                    self.root.after(0, lambda: self.status_var.set(f"NFC backup saved: {dump_file.name}"))
                else:
                    output += "\n\nBackup may have failed.\n"

            except Exception as e:
                output = f"Error:\n{e}"

            self.root.after(0, lambda: self.set_output_text(text, output))

        threading.Thread(target=worker, daemon=True).start()

    def restore_nfc_tag(self):
        latest = self.get_latest_nfc_dump()
        if not latest:
            messagebox.showinfo(APP_NAME, "No NFC dump files found in ~/NFC/dumps")
            return

        if not messagebox.askyesno(
            APP_NAME,
            f"Restore latest dump to a tag?\n\n{latest.name}\n\nUse only on your own blank/writable tag."
        ):
            return

        win, text = self.show_output_window(
            "NFC Restore Tag",
            f"Restoring from:\n{latest}\n\nWhen prompted in terminal, answer:\n"
            "OTP/Capability Bytes: n\n"
            "Lock Bytes: n\n"
            "Dynamic Lock Bytes: n\n"
            "UID bytes: n\n"
        )

        def worker():
            try:
                result = subprocess.run(
                    ["lxterminal", "-e", f"bash -lc 'cd {HOME} && nfc-mfultralight w \"{latest}\"'"],
                    capture_output=True,
                    text=True,
                    timeout=10
                )

                output = "Restore command launched in terminal.\n\n" \
                         "Answer all prompts with:\n" \
                         "n\nn\nn\nn\n\n" \
                         f"Dump file:\n{latest}\n"

                self.root.after(0, lambda: self.status_var.set(f"NFC restore launched: {latest.name}"))

            except Exception as e:
                output = f"Error:\n{e}"

            self.root.after(0, lambda: self.set_output_text(text, output))

        threading.Thread(target=worker, daemon=True).start()
    def verify_nfc_restore(self):
        latest = self.get_latest_nfc_dump()
        if not latest:
            messagebox.showinfo(APP_NAME, "No NFC dump files found in ~/NFC/dumps")
            return

        win, text = self.show_output_window(
            "NFC Verify Restore",
            f"Comparing current tag against:\n{latest}\n\nPlace the written tag on the reader...\n"
        )

        def worker():
            verify_file = NFC_DUMPS_DIR / "verify_after_write.mfd"

            try:
                read_result = subprocess.run(
                    ["nfc-mfultralight", "r", str(verify_file)],
                    capture_output=True,
                    text=True,
                    timeout=90
                )

                output = ""
                if read_result.stdout:
                    output += read_result.stdout
                if read_result.stderr:
                    output += "\n[stderr]\n" + read_result.stderr

                if read_result.returncode != 0 or not verify_file.exists():
                    output += "\n\nVerification read failed.\n"
                    self.root.after(0, lambda: self.set_output_text(text, output))
                    return

                with open(latest, "rb") as f:
                    src = f.read()
                with open(verify_file, "rb") as f:
                    dst = f.read()

                # Ignore first 16 bytes (manufacturer / UID / protected header area)
                src_user = src[16:]
                dst_user = dst[16:]

                if src_user == dst_user:
                    output += "\n\nVERIFY RESULT: USER MEMORY MATCHES\n"
                    self.root.after(0, lambda: self.status_var.set("NFC verify: user memory matches"))
                else:
                    output += "\n\nVERIFY RESULT: USER MEMORY DOES NOT MATCH\n"

                    max_len = min(len(src_user), len(dst_user))
                    diffs = []
                    for i in range(max_len):
                        if src_user[i] != dst_user[i]:
                            diffs.append(f"Offset {i + 16}: source={src_user[i]:02X} target={dst_user[i]:02X}")
                        if len(diffs) >= 10:
                            break

                    if diffs:
                        output += "\nFirst differences:\n" + "\n".join(diffs) + "\n"

                    self.root.after(0, lambda: self.status_var.set("NFC verify: mismatch found"))

            except Exception as e:
                output = f"Error:\n{e}"

            self.root.after(0, lambda: self.set_output_text(text, output))

        threading.Thread(target=worker, daemon=True).start()
    def create_hackrf_template(self):
        RF_SCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
        script_path = RF_SCRIPTS_DIR / "hackrf_capture_template.sh"

        content = """#!/usr/bin/env bash
set -e

OUTDIR="$HOME/RF/captures"
mkdir -p "$OUTDIR"

FREQ=915000000
RATE=2000000
AMP=0
LNA=16
VGA=20
SAMPLES=10000000
OUTFILE="$OUTDIR/hackrf_capture_$(date +%Y%m%d_%H%M%S).iq"

echo "Starting HackRF capture..."
echo "Frequency: $FREQ"
echo "Sample rate: $RATE"
echo "Output: $OUTFILE"

hackrf_transfer -r "$OUTFILE" -f "$FREQ" -s "$RATE" -a "$AMP" -l "$LNA" -g "$VGA" -n "$SAMPLES"

echo
echo "Done."
echo "Saved to: $OUTFILE"
"""

        script_path.write_text(content, encoding="utf-8")
        script_path.chmod(0o755)
        self.status_var.set(f"Created {script_path.name}")
        messagebox.showinfo(APP_NAME, f"HackRF template created:\n{script_path}")

    def create_rtlsdr_template(self):
        RF_SCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
        script_path = RF_SCRIPTS_DIR / "rtlsdr_capture_template.sh"

        content = """#!/usr/bin/env bash
set -e

OUTDIR="$HOME/RF/captures"
mkdir -p "$OUTDIR"

FREQ=162550000
RATE=2048000
GAIN=20
OUTFILE="$OUTDIR/rtlsdr_capture_$(date +%Y%m%d_%H%M%S).bin"

echo "Starting RTL-SDR capture..."
echo "Frequency: $FREQ"
echo "Sample rate: $RATE"
echo "Gain: $GAIN"
echo "Output: $OUTFILE"

rtl_sdr -f "$FREQ" -s "$RATE" -g "$GAIN" "$OUTFILE"

echo
echo "Done."
echo "Saved to: $OUTFILE"
"""

        script_path.write_text(content, encoding="utf-8")
        script_path.chmod(0o755)
        self.status_var.set(f"Created {script_path.name}")
        messagebox.showinfo(APP_NAME, f"RTL-SDR template created:\n{script_path}")

    def activate(self, item):
        if item.get("nav"):
            self.render_page(item["nav"])
            return

        action = item.get("action")
        if action == "back":
            self.go_back()
            return
        if action == "fullscreen":
            self.toggle_fullscreen()
            return
        if action == "exit":
            self.quit_confirm()
            return
        if action == "exit_to_desktop":
            self.exit_to_desktop()
            return
        if action == "reboot":
            self.reboot_confirm()
            return
        if action == "nfc_scan_once":
            self.run_command_in_window("NFC Scan Once", ["nfc-list"])
            return

        if action == "nfc_uid_only":
            self.run_command_in_window(
                "NFC UID Only",
                ["bash", "-lc", "nfc-list | grep -i 'UID'"]
            )
            return

        if action == "view_saved_tags":
            self.show_saved_tags_window()
            return

        if action == "rename_last_scanned_tag":
            self.rename_last_scanned_tag()
            return

        if action == "nfc_poll_disabled":
            self.status_var.set("Continuous NFC scan temporarily disabled")
            messagebox.showinfo(
                APP_NAME,
                "Continuous NFC scan is temporarily disabled while we stabilize the PN532 integration."
            )
            return
        if action == "nfc_backup_tag":
            self.backup_nfc_tag()
            return

        if action == "nfc_restore_tag":
            self.restore_nfc_tag()
            return

        if action == "nfc_verify_restore":
            self.verify_nfc_restore()
            return
        if action == "hackrf_info":
            self.run_command_in_window("HackRF Info", ["hackrf_info"])
            return

        if action == "rtlsdr_info":
            self.run_command_in_window(
                "RTL-SDR Info",
                ["bash", "-lc", "rtl_test -t 2>&1 | head -20"]
            )
            return

        if action == "hackrf_mode_help":
            messagebox.showinfo(
                APP_NAME,
                "To use HackRF with the Pi:\n\n"
                "1. Connect USB-C to the Pi\n"
                "2. On the PortaPack, enable HackRF Mode\n"
                "3. Then run HackRF tools from Lunaro or terminal"
            )
            return

        if action == "ham_it_up_help":
            messagebox.showinfo(
                APP_NAME,
                "Ham It Up Plus v2:\n\n"
                "- Use with RTL-SDR / NESDR for HF, LF, and MF reception\n"
                "- Typical chain:\n"
                "  Antenna -> Ham It Up -> NESDR Smart -> Pi\n"
                "- Use when exploring lower-frequency bands"
            )
            return

        if action == "lana_help":
            messagebox.showinfo(
                APP_NAME,
                "LaNA / LaNA HF:\n\n"
                "- Use as an LNA when extra gain helps weak signals\n"
                "- Most useful in HF/LF/MF receive chains\n"
                "- Avoid too much gain if signals are already strong"
            )
            return

        if action == "rtl_hf_chain_help":
            messagebox.showinfo(
                APP_NAME,
                "Suggested HF chain:\n\n"
                "Antenna -> LaNA HF (if needed) -> Ham It Up -> NESDR Smart -> Pi\n\n"
                "For direct RTL-SDR use without HF upconversion:\n"
                "Antenna -> NESDR Smart -> Pi"
            )
            return

        if action == "make_hackrf_template":
            self.create_hackrf_template()
            return

        if action == "make_rtlsdr_template":
            self.create_rtlsdr_template()
            return

        cmd = item.get("cmd")
        if not cmd:
            self.status_var.set(f"No action for {item['title']}")
            return

        if shutil.which(cmd[0]) is None:
            messagebox.showerror(APP_NAME, f"'{cmd[0]}' is not installed.")
            self.status_var.set(f"Missing dependency: {cmd[0]}")
            return

        try:
            subprocess.Popen(cmd, start_new_session=True)
            self.status_var.set(f"Launched {item['title']}")
        except Exception as e:
            messagebox.showerror(APP_NAME, str(e))
            self.status_var.set(f"Failed to launch {item['title']}")

    def go_back(self):
        if not self.page_history:
            self.status_var.set("No previous screen")
            return
        prev = self.page_history.pop()
        self.render_page(prev, push_history=False)

    def toggle_fullscreen(self):
        current = bool(self.root.attributes("-fullscreen"))
        self.root.attributes("-fullscreen", not current)
        self.status_var.set("Fullscreen enabled" if not current else "Fullscreen disabled")

    def exit_to_desktop(self):
        if messagebox.askyesno(APP_NAME, "Close Lunaro and return to desktop?"):
            self.root.destroy()

    def quit_confirm(self):
        if messagebox.askyesno(APP_NAME, "Exit Lunaro launcher?"):
            self.root.destroy()

    def reboot_confirm(self):
        if messagebox.askyesno(APP_NAME, "Reboot the Raspberry Pi now?"):
            subprocess.Popen(["lxterminal", "-e", "sudo reboot"], start_new_session=True)

    def nfc_live_scan(self):
        win = tk.Toplevel(self.root)
        win.title("NFC Scanner")
        win.geometry("920x540")
        win.configure(bg=BG)

        outer = tk.Frame(win, bg=BG)
        outer.pack(fill="both", expand=True, padx=18, pady=18)

        header = tk.Label(
            outer,
            text="LUNARO NFC SCANNER",
            fg=ACCENT,
            bg=BG,
            font=("DejaVu Sans", 22, "bold")
        )
        header.pack(anchor="w", pady=(0, 12))

        panel = tk.Frame(
            outer,
            bg="#050b10",
            highlightthickness=2,
            highlightbackground=BORDER
        )
        panel.pack(fill="both", expand=True)

        status = tk.Label(
            panel,
            text="WAITING FOR TAG",
            fg="#ffaa00",
            bg="#050b10",
            font=("DejaVu Sans", 30, "bold")
        )
        status.pack(pady=(40, 16))

        substatus = tk.Label(
            panel,
            text="Hold an NFC tag or card near the reader",
            fg=MUTED,
            bg="#050b10",
            font=("DejaVu Sans", 12)
        )
        substatus.pack()

        uid_title = tk.Label(
            panel,
            text="UID",
            fg=ACCENT2,
            bg="#050b10",
            font=("DejaVu Sans", 14, "bold")
        )
        uid_title.pack(pady=(36, 8))

        uid_frame = tk.Frame(
            panel,
            bg="#081018",
            highlightthickness=1,
            highlightbackground=ACCENT
        )
        uid_frame.pack(padx=30, pady=(0, 20), fill="x")

        uid_label = tk.Label(
            uid_frame,
            text="-- -- -- -- -- -- --",
            fg=TEXT,
            bg="#081018",
            font=("DejaVu Sans Mono", 22, "bold"),
            pady=18
        )
        uid_label.pack()

        info_label = tk.Label(
            panel,
            text="",
            fg=TEXT,
            bg="#050b10",
            font=("DejaVu Sans Mono", 11),
            justify="left"
        )
        info_label.pack(pady=(8, 20))

        btn_row = tk.Frame(panel, bg="#050b10")
        btn_row.pack(side="bottom", pady=20)

        def save_uid():
            uid = uid_label.cget("text").strip()
            if not uid or uid == "-- -- -- -- -- -- --":
                return
            log_dir = HOME / "Logs"
            log_dir.mkdir(exist_ok=True)
            with open(log_dir / "nfc_uids.log", "a", encoding="utf-8") as f:
                f.write(f"{datetime.now().isoformat()} | {uid}\n")
            info_label.config(text=f"Saved UID to {log_dir / 'nfc_uids.log'}", fg=ACCENT2)

        save_btn = tk.Button(
            btn_row,
            text="Save UID",
            command=save_uid,
            bg=CARD,
            fg=TEXT,
            activebackground=CARD_HOVER,
            activeforeground=TEXT,
            bd=0,
            relief="flat",
            padx=18,
            pady=10
        )
        save_btn.pack(side="left", padx=8)

        close_btn = tk.Button(
            btn_row,
            text="Close",
            command=win.destroy,
            bg=CARD,
            fg=TEXT,
            activebackground=CARD_HOVER,
            activeforeground=TEXT,
            bd=0,
            relief="flat",
            padx=18,
            pady=10
        )
        close_btn.pack(side="left", padx=8)

        state = {
            "running": True,
            "pulse": 0,
            "detected": False
        }

        def animate_waiting():
            if not win.winfo_exists() or not state["running"]:
                return

            if not state["detected"]:
                dots = "." * (state["pulse"] % 4)
                status.config(text=f"WAITING FOR TAG{dots}")
                state["pulse"] += 1

            win.after(450, animate_waiting)

        def set_waiting():
            state["detected"] = False
            status.config(text="WAITING FOR TAG", fg="#ffaa00")
            substatus.config(text="Hold an NFC tag or card near the reader", fg=MUTED)
            uid_label.config(text="-- -- -- -- -- -- --")
            info_label.config(text="", fg=TEXT)

        def set_detected(uid_text, raw_output):
            state["detected"] = True
            uid_text = " ".join(uid_text.strip().split()).upper()

            db = load_db()

            if uid_text not in db:
                db[uid_text] = {
                    "name": "Unknown",
                    "first_seen": datetime.now().isoformat()
                }
                save_db(db)

            name = db[uid_text]["name"]

            status.config(text="TAG DETECTED", fg="#00ff9f")
            substatus.config(text=f"Detected: {name}", fg=ACCENT2)
            uid_label.config(text=uid_text)
            info_label.config(text=raw_output.strip(), fg=TEXT)

            def reset_later():
                if win.winfo_exists() and state["running"]:
                    set_waiting()

            win.after(2500, reset_later)

        def worker():
            while state["running"]:
                try:
                    result = subprocess.run(
                        ["nfc-list"],
                        capture_output=True,
                        text=True,
                        timeout=6
                    )

                    output = (result.stdout or "") + ("\n" + result.stderr if result.stderr else "")
                    if "UID (NFCID1):" in output:
                        uid_line = ""
                        for line in output.splitlines():
                            if "UID (NFCID1):" in line:
                                uid_line = line.split("UID (NFCID1):", 1)[1].strip()
                                break

                        trimmed = "\n".join(
                            line for line in output.splitlines()
                            if (
                                "UID (NFCID1):" in line
                                or "ATQA" in line
                                or "SAK" in line
                                or "ISO14443A" in line
                            )
                        )

                        self.root.after(0, lambda u=uid_line, r=trimmed: set_detected(u, r))

                    time.sleep(1.0)

                except Exception as e:
                    self.root.after(0, lambda err=str(e): info_label.config(text=f"Scan error: {err}", fg=DANGER))
                    time.sleep(2.0)

        def on_close():
            state["running"] = False
            win.destroy()

        win.protocol("WM_DELETE_WINDOW", on_close)

        animate_waiting()
        threading.Thread(target=worker, daemon=True).start()

        def worker():
            while True:
                try:
                    result = subprocess.run(
                        ["nfc-list"],
                        capture_output=True,
                        text=True,
                        timeout=5
                    )

                    output = result.stdout

                    if "UID" in output:
                        uid = output.split("UID (NFCID1):")[-1].strip().split("\n")[0]

                        self.root.after(0, lambda: status.config(
                            text="TAG DETECTED",
                            fg="#00ff9f"
                        ))

                        self.root.after(0, lambda: uid_label.config(
                            text=uid
                        ))

                        time.sleep(2)

                        self.root.after(0, lambda: status.config(
                            text="WAITING FOR TAG...",
                            fg="#ffaa00"
                        ))
                        self.root.after(0, lambda: uid_label.config(text=""))

                    time.sleep(1)

                except Exception:
                    pass

        threading.Thread(target=worker, daemon=True).start()

def install_autostart():
    AUTOSTART_DIR.mkdir(parents=True, exist_ok=True)
    DESKTOP_FILE.write_text(f'''[Desktop Entry]
Type=Application
Name=Lunaro
Exec={HOME}/lunaro_start.sh
Terminal=false
X-GNOME-Autostart-enabled=true
''')
    print(f"Autostart installed at {DESKTOP_FILE}")

def remove_autostart():
    if DESKTOP_FILE.exists():
        DESKTOP_FILE.unlink()
        print("Autostart removed")
    else:
        print("No autostart file found")

def main():
    if "--install-autostart" in sys.argv:
        install_autostart()
        return
    if "--remove-autostart" in sys.argv:
        remove_autostart()
        return

    root = tk.Tk()
    LunaroLauncher(root)
    root.mainloop()

if __name__ == "__main__":
    main()
