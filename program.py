import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading
import json
import datetime
from tkinter import colorchooser

class EnhancedFlashlightApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Flashlight")
        self.root.geometry("400x600")
        
        self.is_light_on = False
        self.sos_running = False
        self.strobe_running = False
        self.battery_level = 100  # Simulated battery level
        
        # Load settings
        self.settings = self.load_settings()
        
        # Style
        self.root.configure(bg=self.settings.get('theme_color', '#2c3e50'))
        self.create_styles()
        self.create_gui()
        
        # Start battery simulation
        threading.Thread(target=self.simulate_battery_drain, daemon=True).start()
        
        # Emergency contacts
        self.emergency_contacts = self.settings.get('emergency_contacts', [])

    def create_styles(self):
        style = ttk.Style()
        style.configure('Large.TButton', padding=10, font=('Arial', 12))
        style.configure('Emergency.TButton', padding=10, font=('Arial', 12), foreground='red')

    def create_gui(self):
        # Main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Battery indicator
        self.battery_label = tk.Label(
            main_frame,
            text=f"Battery: {self.battery_level}%",
            bg=self.settings.get('theme_color', '#2c3e50'),
            fg='white',
            font=('Arial', 10)
        )
        self.battery_label.pack(pady=5)

        # Light modes frame
        modes_frame = ttk.LabelFrame(main_frame, text="Light Modes")
        modes_frame.pack(fill=tk.X, pady=10)

        # Main light button
        self.light_button = ttk.Button(
            modes_frame,
            text="Turn On",
            command=self.toggle_light,
            style='Large.TButton'
        )
        self.light_button.pack(pady=10, padx=10, fill=tk.X)

        # Brightness control
        self.brightness_scale = ttk.Scale(
            modes_frame,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            command=self.adjust_brightness
        )
        self.brightness_scale.set(self.settings.get('brightness', 100))
        self.brightness_scale.pack(pady=5, padx=10, fill=tk.X)
        
        # Color picker button
        self.color_button = ttk.Button(
            modes_frame,
            text="Choose Color",
            command=self.choose_color
        )
        self.color_button.pack(pady=5, padx=10, fill=tk.X)

        # Strobe light button
        self.strobe_button = ttk.Button(
            modes_frame,
            text="Strobe Light",
            command=self.toggle_strobe
        )
        self.strobe_button.pack(pady=5, padx=10, fill=tk.X)

        # Emergency frame
        emergency_frame = ttk.LabelFrame(main_frame, text="Emergency Features")
        emergency_frame.pack(fill=tk.X, pady=10)

        # SOS button
        self.sos_button = ttk.Button(
            emergency_frame,
            text="SOS Signal",
            command=self.toggle_sos,
            style='Emergency.TButton'
        )
        self.sos_button.pack(pady=5, padx=10, fill=tk.X)

        # Emergency contacts button
        self.contacts_button = ttk.Button(
            emergency_frame,
            text="Manage Emergency Contacts",
            command=self.manage_contacts
        )
        self.contacts_button.pack(pady=5, padx=10, fill=tk.X)

        # Status label
        self.status_label = tk.Label(
            main_frame,
            text="Ready",
            bg=self.settings.get('theme_color', '#2c3e50'),
            fg='white',
            font=('Arial', 12)
        )
        self.status_label.pack(pady=10)

        # Usage statistics
        self.usage_label = tk.Label(
            main_frame,
            text="Usage time: 0 minutes",
            bg=self.settings.get('theme_color', '#2c3e50'),
            fg='white',
            font=('Arial', 10)
        )
        self.usage_label.pack(pady=5)

    def simulate_light_on(self, brightness=100):
        """Simulate turning on the flashlight with given brightness"""
        self.status_label.configure(text=f"Light ON - Brightness: {brightness}%")
        self.root.configure(bg=self.settings.get('light_color', '#FFFFFF'))

    def simulate_light_off(self):
        """Simulate turning off the flashlight"""
        self.status_label.configure(text="Light OFF")
        self.root.configure(bg=self.settings.get('theme_color', '#2c3e50'))

    def sos_signal(self):
        """Generate SOS signal in Morse code (... --- ...)"""
        while self.sos_running:
            # S (...)
            for _ in range(3):
                self.simulate_light_on()
                time.sleep(0.2)
                self.simulate_light_off()
                time.sleep(0.2)
            time.sleep(0.4)
            
            # O (---)
            for _ in range(3):
                self.simulate_light_on()
                time.sleep(0.6)
                self.simulate_light_off()
                time.sleep(0.2)
            time.sleep(0.4)
            
            # S (...)
            for _ in range(3):
                self.simulate_light_on()
                time.sleep(0.2)
                self.simulate_light_off()
                time.sleep(0.2)
            
            time.sleep(1.5)  # Pause before repeating

    def load_settings(self):
        try:
            with open('flashlight_settings.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                'theme_color': '#2c3e50',
                'brightness': 100,
                'emergency_contacts': [],
                'usage_time': 0
            }

    def save_settings(self):
        with open('flashlight_settings.json', 'w') as f:
            json.dump(self.settings, f)

    def toggle_light(self):
        self.is_light_on = not self.is_light_on
        if self.is_light_on:
            self.light_button.configure(text="Turn Off")
            self.simulate_light_on(self.brightness_scale.get())
            self.update_usage_time()
        else:
            self.light_button.configure(text="Turn On")
            self.simulate_light_off()

    def adjust_brightness(self, value):
        brightness = int(float(value))
        self.settings['brightness'] = brightness
        self.save_settings()
        if self.is_light_on:
            self.simulate_light_on(brightness)

    def choose_color(self):
        color = colorchooser.askcolor(title="Choose Light Color")[1]
        if color:
            self.settings['light_color'] = color
            self.save_settings()
            if self.is_light_on:
                self.root.configure(bg=color)

    def toggle_strobe(self):
        self.strobe_running = not self.strobe_running
        if self.strobe_running:
            self.strobe_button.configure(text="Stop Strobe")
            threading.Thread(target=self.strobe_effect, daemon=True).start()
        else:
            self.strobe_button.configure(text="Strobe Light")

    def strobe_effect(self):
        while self.strobe_running:
            self.simulate_light_on(100)
            time.sleep(0.1)
            self.simulate_light_off()
            time.sleep(0.1)

    def toggle_sos(self):
        self.sos_running = not self.sos_running
        if self.sos_running:
            self.sos_button.configure(text="Stop SOS")
            threading.Thread(target=self.sos_signal, daemon=True).start()
            if self.emergency_contacts:
                self.send_emergency_alert()
        else:
            self.sos_button.configure(text="SOS Signal")

    def send_emergency_alert(self):
        # Simulate sending emergency alerts
        message = "EMERGENCY: SOS signal activated at " + \
                 datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        messagebox.showinfo("Emergency Alert", 
                          f"Emergency alert would be sent to {len(self.emergency_contacts)} contacts\n\n{message}")

    def manage_contacts(self):
        contacts_window = tk.Toplevel(self.root)
        contacts_window.title("Emergency Contacts")
        contacts_window.geometry("300x400")

        def add_contact():
            name = name_entry.get()
            phone = phone_entry.get()
            if name and phone:
                self.emergency_contacts.append({"name": name, "phone": phone})
                self.settings['emergency_contacts'] = self.emergency_contacts
                self.save_settings()
                update_contacts_list()
                name_entry.delete(0, tk.END)
                phone_entry.delete(0, tk.END)

        # Contact input fields
        ttk.Label(contacts_window, text="Name:").pack(pady=5)
        name_entry = ttk.Entry(contacts_window)
        name_entry.pack(pady=5)

        ttk.Label(contacts_window, text="Phone:").pack(pady=5)
        phone_entry = ttk.Entry(contacts_window)
        phone_entry.pack(pady=5)

        ttk.Button(contacts_window, text="Add Contact", command=add_contact).pack(pady=10)

        # Contacts list
        contacts_list = tk.Listbox(contacts_window, width=40, height=10)
        contacts_list.pack(pady=10)

        def update_contacts_list():
            contacts_list.delete(0, tk.END)
            for contact in self.emergency_contacts:
                contacts_list.insert(tk.END, f"{contact['name']}: {contact['phone']}")

        update_contacts_list()

    def simulate_battery_drain(self):
        while True:
            if self.is_light_on:
                self.battery_level = max(0, self.battery_level - 1)
                self.battery_label.configure(
                    text=f"Battery: {self.battery_level}%",
                    fg='red' if self.battery_level < 20 else 'white'
                )
                if self.battery_level < 20:
                    self.status_label.configure(text="Low Battery Warning!")
            time.sleep(10)

    def update_usage_time(self):
        if self.is_light_on:
            def update():
                if self.is_light_on:
                    self.settings['usage_time'] = self.settings.get('usage_time', 0) + 1
                    self.usage_label.configure(
                        text=f"Usage time: {self.settings['usage_time']} minutes"
                    )
                    self.save_settings()
                    self.root.after(60000, update)  # Update every minute
            self.root.after(60000, update)

if __name__ == "__main__":
    root = tk.Tk()
    app = EnhancedFlashlightApp(root)
    root.mainloop()
