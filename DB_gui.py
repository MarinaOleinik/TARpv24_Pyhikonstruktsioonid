import sqlite3
import customtkinter as ctk
from tkinter import ttk, messagebox

ctk.set_appearance_mode("System")  # Light, Dark, System
ctk.set_default_color_theme("blue")

DB_NAME = 'movies.db'
TABLE_SCHEMA = """
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    director TEXT,
    release_year INTEGER,
    genre TEXT,
    duration INTEGER,
    rating REAL,
    language TEXT,
    country TEXT,
    description TEXT
);
"""

SAMPLE_DATA = """
INSERT INTO movies (title, director, release_year, genre, duration, rating, language, country, description) VALUES
('The From In With.', 'Francis Ford Coppola', 1994, 'Drama', 142, 9.3, 'English', 'USA', 'Drama film'),
('The By On To.', 'Christopher Nolan', 2010, 'Sci-Fi', 148, 8.8, 'English', 'UK', 'Science fiction film'),
('In The With On.', 'Quentin Tarantino', 1972, 'Crime', 175, 9.2, 'English', 'USA', 'Crime drama'),
('The A To From.', 'Steven Spielberg', 1994, 'Adventure', 154, 8.9, 'English', 'France', 'Adventure film');
"""

def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(TABLE_SCHEMA)
    cursor.execute("SELECT COUNT(*) FROM movies")
    if cursor.fetchone()[0] == 0:
        cursor.executescript(SAMPLE_DATA)
    conn.commit()
    conn.close()

def load_data():
    for item in tree.get_children():
        tree.delete(item)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    query = "SELECT id, title, director, release_year, genre, duration, rating, language, country, description FROM movies"
    if search_entry.get():
        query += " WHERE title LIKE ?"
        cursor.execute(query, (f"%{search_entry.get()}%",))
    else:
        cursor.execute(query)
    for row in cursor.fetchall():
        tree.insert('', 'end', iid=row[0], values=row[1:])
    conn.close()

def open_add_window():
    def save():
        try:
            data = [fields[f].get() for f in field_names]
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO movies (title, director, release_year, genre, duration, rating, language, country, description)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", data)
            conn.commit()
            conn.close()
            load_data()
            win.destroy()
        except Exception as e:
            messagebox.showerror("Viga", str(e))

    win = ctk.CTkToplevel(app)
    win.title("Lisa film")
    win.geometry("400x700")

    fields.clear()
    for label in field_names:
        ctk.CTkLabel(win, text=label.capitalize()).pack(pady=5)
        entry = ctk.CTkEntry(win)
        entry.pack(padx=5, fill='x')
        fields[label] = entry

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
app.geometry("1000x600")

field_names = ["title", "director", "release_year", "genre", "duration", "rating", "language", "country", "description"]
fields = {}

top_frame = ctk.CTkFrame(app)
top_frame.pack(padx=10, pady=10, fill='x')

search_entry = ctk.CTkEntry(top_frame, placeholder_text="Otsi pealkirja järgi")
search_entry.pack(side='left', padx=10, fill='x', expand=True)

ctk.CTkButton(top_frame, text="Otsi", command=load_data).pack(side='left', padx=5)
ctk.CTkButton(top_frame, text="Lisa film", command=open_add_window).pack(side='left', padx=5)
ctk.CTkButton(top_frame, text="Kustuta", command=delete_selected).pack(side='left', padx=5)


tree = ttk.Treeview(app, columns=field_names, show='headings')
for col in field_names:
    tree.heading(col, text=col.capitalize())
    tree.column(col, width=100)
tree.pack(padx=10, pady=10, fill='both', expand=True)

create_database()
load_data()
app.mainloop()
