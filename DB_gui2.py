import sqlite3
import customtkinter as ctk
from tkinter import ttk, messagebox
# Online SQLite Viewer (kui ei taha midagi installida)
# Näiteks:
# https://sqliteonline.com
# https://extendsclass.com/sqlite-browser.html
ctk.set_appearance_mode("System")  # Light, Dark, System
ctk.set_default_color_theme("blue")

DB_NAME = 'movies2.db'

TABLE_SCHEMA = """
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    director TEXT,
    release_year INTEGER,
    genre TEXT,
    duration INTEGER,
    rating REAL,
    language TEXT,
    country_id INTEGER,
    description TEXT,
    FOREIGN KEY(country_id) REFERENCES countries(id)
);
"""

SAMPLE_DATA = """
INSERT OR IGNORE INTO countries (name) VALUES ('USA'), ('UK'), ('France'), ('Germany');

INSERT INTO movies (title, director, release_year, genre, duration, rating, language, country_id, description) VALUES
('The From In With.', 'Francis Ford Coppola', 1994, 'Drama', 142, 9.3, 'English', 1, 'Drama film'),
('The By On To.', 'Christopher Nolan', 2010, 'Sci-Fi', 148, 8.8, 'English', 2, 'Science fiction film'),
('In The With On.', 'Quentin Tarantino', 1972, 'Crime', 175, 9.2, 'English', 1, 'Crime drama'),
('The A To From.', 'Steven Spielberg', 1994, 'Adventure', 154, 8.9, 'English', 3, 'Adventure film');
"""

def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.executescript(TABLE_SCHEMA)
    cursor.execute("SELECT COUNT(*) FROM movies")
    if cursor.fetchone()[0] == 0:
        cursor.executescript(SAMPLE_DATA)
    conn.commit()
    conn.close()

def get_countries():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM countries")
    countries = cursor.fetchall()
    conn.close()
    return countries

def load_data():
    for item in tree.get_children():
        tree.delete(item)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    query = """
        SELECT m.id, m.title, m.director, m.release_year, m.genre, m.duration,
               m.rating, m.language, c.name, m.description
        FROM movies m
        LEFT JOIN countries c ON m.country_id = c.id
    """
    if search_entry.get():
        query += " WHERE m.title LIKE ?"
        cursor.execute(query, (f"%{search_entry.get()}%",))
    else:
        cursor.execute(query)
    for row in cursor.fetchall():
        tree.insert('', 'end', iid=row[0], values=row[1:])
    conn.close()

def load_countries():
    for item in country_tree.get_children():
        country_tree.delete(item)
    for id_, name in get_countries():
        country_tree.insert('', 'end', values=(id_, name))

def open_add_country_window():
    def save_country():
        country_name = country_entry.get().strip()
        if country_name:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO countries (name) VALUES (?)", (country_name,))
                conn.commit()
                load_countries()
                win.destroy()
            except sqlite3.IntegrityError:
                messagebox.showerror("Viga", "See riik on juba olemas.")
            conn.close()

    win = ctk.CTkToplevel(app)
    win.title("Lisa riik")
    win.geometry("300x150")

    ctk.CTkLabel(win, text="Riigi nimi").pack(pady=(10, 5))
    country_entry = ctk.CTkEntry(win)
    country_entry.pack(padx=10, pady=5, fill='x')
    ctk.CTkButton(win, text="Lisa", command=save_country).pack(pady=10)

def open_add_window():
    def save():
        try:
            data = [fields[f].get() for f in field_names[:-2]]
            selected_country = country_menu.get()
            country_id = country_map.get(selected_country)
            data.append(country_id)
            data.append(fields["description"].get())

            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO movies (title, director, release_year, genre, duration, rating, language, country_id, description)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", data)
            conn.commit()
            conn.close()
            load_data()
            win.destroy()
        except Exception as e:
            messagebox.showerror("Viga", str(e))

    win = ctk.CTkToplevel(app)
    win.title("Lisa film")
    win.geometry("400x600")

    fields.clear()
    for label in field_names[:-2]:  # Exclude 'country' and 'description'
        ctk.CTkLabel(win, text=label.capitalize()).pack(pady=(5, 0))
        entry = ctk.CTkEntry(win)
        entry.pack(padx=10, pady=(0, 10), fill='x')
        fields[label] = entry

    ctk.CTkLabel(win, text="Riik").pack(pady=(5, 0))
    country_list = [c[1] for c in get_countries()]
    country_map = {c[1]: c[0] for c in get_countries()}
    country_menu = ctk.CTkOptionMenu(win, values=country_list)
    country_menu.pack(padx=10, pady=(0, 10), fill='x')

    ctk.CTkLabel(win, text="Kirjeldus").pack(pady=(5, 0))
    desc_entry = ctk.CTkEntry(win)
    desc_entry.pack(padx=10, pady=(0, 10), fill='x')
    fields["description"] = desc_entry

    ctk.CTkButton(win, text="Salvesta", command=save).pack(pady=10)

def delete_selected():
    sel = tree.selection()
    if sel:
        record_id = sel[0]
        if messagebox.askyesno("Kustuta", "Kas oled kindel?"):
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM movies WHERE id=?", (record_id,))
            conn.commit()
            conn.close()
            load_data()
    else:
        messagebox.showinfo("Teade", "Vali kirje kustutamiseks.")

# GUI start
app = ctk.CTk()
app.title("Filmide andmebaas")
app.geometry("1000x700")

field_names = ["title", "director", "release_year", "genre", "duration", "rating", "language", "country", "description"]
fields = {}

top_frame = ctk.CTkFrame(app)
top_frame.pack(padx=10, pady=10, fill='x')

search_entry = ctk.CTkEntry(top_frame, placeholder_text="Otsi pealkirja järgi")
search_entry.pack(side='left', padx=10, fill='x', expand=True)

ctk.CTkButton(top_frame, text="Otsi", command=load_data).pack(side='left', padx=5)
ctk.CTkButton(top_frame, text="Lisa film", command=open_add_window).pack(side='left', padx=5)
ctk.CTkButton(top_frame, text="Lisa riik", command=open_add_country_window).pack(side='left', padx=5)
ctk.CTkButton(top_frame, text="Kustuta", command=delete_selected).pack(side='left', padx=5)


tree = ttk.Treeview(app, columns=field_names, show='headings')
for col in field_names:
    tree.heading(col, text=col.capitalize())
    tree.column(col, width=100)
tree.pack(padx=10, pady=10, fill='both', expand=True)

# --- Riikide tabeli kuvamine ---
country_frame = ctk.CTkFrame(app)
country_frame.pack(padx=10, pady=10, fill='x')

ctk.CTkLabel(country_frame, text="Riikide loetelu").pack(anchor='w', padx=10)

country_columns = ("id", "name")
country_tree = ttk.Treeview(country_frame, columns=country_columns, show='headings', height=4)
country_tree.heading("id", text="ID")
country_tree.heading("name", text="Riik")
country_tree.column("id", width=50)
country_tree.column("name", width=150)
country_tree.pack(padx=10, fill='x')

create_database()
load_data()
load_countries()
app.mainloop()