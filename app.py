import customtkinter as ctk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the CustomTkinter application
app = ctk.CTk()
app.title("WhatsApp Messaging Application")
app.geometry("600x400")

# Function to open WhatsApp Web
def open_whatsapp():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://web.whatsapp.com")
    status_label.config(text="WhatsApp Web opened in headless mode")

# Create a button to open WhatsApp Web
open_button = ctk.CTkButton(app, text="Open WhatsApp Web", command=open_whatsapp)
open_button.pack(pady=20)

# Create a status label
status_label = ctk.CTkLabel(app, text="Status: Ready")
status_label.pack(pady=10)

# Run the CustomTkinter main loop
app.mainloop()