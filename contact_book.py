import tkinter as tk
from tkinter import messagebox, simpledialog
import tkinter.ttk as ttk

# Contact list to store data
contacts = []

# Function to refresh the contact list in UI
def refresh_contacts():
    contact_list.delete(*contact_list.get_children())
    for i, contact in enumerate(contacts):
        contact_list.insert("", "end", iid=i, values=(contact['name'], contact['phone']))

# Function to add a new contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if not name or not phone:
        messagebox.showwarning("Missing Info", "Name and Phone are required.")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    refresh_contacts()
    clear_fields()
    messagebox.showinfo("Success", "Contact added successfully.")

# Function to search for a contact
def search_contact():
    query = simpledialog.askstring("Search", "Enter Name or Phone Number:")
    if not query:
        return

    found = False
    for i, contact in enumerate(contacts):
        if query.lower() in contact["name"].lower() or query in contact["phone"]:
            contact_list.selection_set(i)
            contact_list.focus(i)
            found = True
            break

    if not found:
        messagebox.showinfo("Not Found", "No matching contact found.")

# Function to update selected contact
def update_contact():
    selected = contact_list.focus()
    if not selected:
        messagebox.showwarning("No Selection", "Please select a contact to update.")
        return

    index = int(selected)
    contacts[index] = {
        "name": entry_name.get(),
        "phone": entry_phone.get(),
        "email": entry_email.get(),
        "address": entry_address.get()
    }
    refresh_contacts()
    clear_fields()
    messagebox.showinfo("Updated", "Contact updated successfully.")

# Function to delete selected contact
def delete_contact():
    selected = contact_list.focus()
    if not selected:
        messagebox.showwarning("No Selection", "Please select a contact to delete.")
        return

    index = int(selected)
    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this contact?")
    if confirm:
        contacts.pop(index)
        refresh_contacts()
        clear_fields()

# Function to show selected contact details in input fields
def show_details(event):
    selected = contact_list.focus()
    if not selected:
        return

    index = int(selected)
    contact = contacts[index]

    entry_name.delete(0, tk.END)
    entry_name.insert(0, contact['name'])

    entry_phone.delete(0, tk.END)
    entry_phone.insert(0, contact['phone'])

    entry_email.delete(0, tk.END)
    entry_email.insert(0, contact['email'])

    entry_address.delete(0, tk.END)
    entry_address.insert(0, contact['address'])

# Clear input fields
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# ================= UI SETUP ===================

root = tk.Tk()
root.title("📒 Contact Book")
root.geometry("600x500")
root.resizable(False, False)

# Top Frame for Input Fields
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

tk.Label(frame_top, text="Name").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame_top, width=25)
entry_name.grid(row=0, column=1)

tk.Label(frame_top, text="Phone").grid(row=1, column=0, padx=5, pady=5)
entry_phone = tk.Entry(frame_top, width=25)
entry_phone.grid(row=1, column=1)

tk.Label(frame_top, text="Email").grid(row=2, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame_top, width=25)
entry_email.grid(row=2, column=1)

tk.Label(frame_top, text="Address").grid(row=3, column=0, padx=5, pady=5)
entry_address = tk.Entry(frame_top, width=25)
entry_address.grid(row=3, column=1)

# Buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Add Contact", command=add_contact, bg="green", fg="white").grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Update", command=update_contact).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Delete", command=delete_contact).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="Search", command=search_contact).grid(row=0, column=3, padx=5)
tk.Button(frame_buttons, text="Clear Fields", command=clear_fields).grid(row=0, column=4, padx=5)

# Treeview for Contact List
columns = ("Name", "Phone")
contact_list = ttk.Treeview(root, columns=columns, show="headings", height=10)
contact_list.heading("Name", text="Name")
contact_list.heading("Phone", text="Phone")
contact_list.bind("<<TreeviewSelect>>", show_details)
contact_list.pack(pady=10, fill='x', padx=20)

# Start app
root.mainloop()
