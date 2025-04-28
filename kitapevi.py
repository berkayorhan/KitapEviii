import tkinter as tk
from tkinter import messagebox

class Kitap:
    def __init__(self, ad, yazar, yayinevi):
        self.ad = ad
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.yorumlar = []

    def kitap_bilgisi(self):
        return f"{self.ad} - {self.yazar} - {self.yayinevi}"

    def yorum_ekle(self, yorum):
        self.yorumlar.append(yorum)

class Kullanici:
    def __init__(self, kullanici_adi, sifre):
        self.kullanici_adi = kullanici_adi
        self.sifre = sifre
        self.okunan_kitaplar = []

    def kitap_oku(self, kitap):
        self.okunan_kitaplar.append(kitap)

kitaplar = []
kullanicilar = []
current_user = None

root = tk.Tk()
root.title("Kitap Okuma ve Paylaşım Platformu")
root.geometry("600x400")

def hesap_olustur():
    def create_account():
        username = username_entry.get()
        password = password_entry.get()
        if username and password:
            yeni_kullanici = Kullanici(username, password)
            kullanicilar.append(yeni_kullanici)
            messagebox.showinfo("Başarılı", "Hesabınız oluşturuldu!")
            window.destroy()
        else:
            messagebox.showerror("Hata", "Lütfen tüm alanları doldurun.")
    
    window = tk.Toplevel(root)
    window.title("Hesap Oluştur")
    
    tk.Label(window, text="Kullanıcı Adı:").pack()
    username_entry = tk.Entry(window)
    username_entry.pack()
    
    tk.Label(window, text="Şifre:").pack()
    password_entry = tk.Entry(window, show="*")
    password_entry.pack()
    
    tk.Button(window, text="Hesap Oluştur", command=create_account).pack()

def giris_yap():
    def login():
        username = username_entry.get()
        password = password_entry.get()
        global current_user
        for kullanici in kullanicilar:
            if kullanici.kullanici_adi == username and kullanici.sifre == password:
                current_user = kullanici
                messagebox.showinfo("Başarılı", "Giriş başarılı!")
                window.destroy()
                main_menu()
                return
        messagebox.showerror("Hata", "Kullanıcı adı veya şifre hatalı.")

    window = tk.Toplevel(root)
    window.title("Giriş Yap")
    
    tk.Label(window, text="Kullanıcı Adı:").pack()
    username_entry = tk.Entry(window)
    username_entry.pack()
    
    tk.Label(window, text="Şifre:").pack()
    password_entry = tk.Entry(window, show="*")
    password_entry.pack()
    
    tk.Button(window, text="Giriş Yap", command=login).pack()

def kitap_ekle():
    def add_book():
        title = title_entry.get()
        author = author_entry.get()
        publisher = publisher_entry.get()
        if title and author and publisher:
            new_book = Kitap(title, author, publisher)
            kitaplar.append(new_book)
            messagebox.showinfo("Başarılı", "Kitap eklendi!")
            window.destroy()
        else:
            messagebox.showerror("Hata", "Lütfen tüm alanları doldurun.")
    
    window = tk.Toplevel(root)
    window.title("Kitap Ekle")
    
    tk.Label(window, text="Kitap Adı:").pack()
    title_entry = tk.Entry(window)
    title_entry.pack()
    
    tk.Label(window, text="Yazar:").pack()
    author_entry = tk.Entry(window)
    author_entry.pack()
    
    tk.Label(window, text="Yayınevi:").pack()
    publisher_entry = tk.Entry(window)
    publisher_entry.pack()
    
    tk.Button(window, text="Kitap Ekle", command=add_book).pack()

def kitaplari_goster():
    display_window = tk.Toplevel(root)
    display_window.title("Kitaplar")
    
    if not kitaplar:
        tk.Label(display_window, text="Henüz kitap yok. Kitap ekleyin.").pack()
    else:
        for kitap in kitaplar:
            tk.Label(display_window, text=kitap.kitap_bilgisi()).pack()
            if kitap.yorumlar:
                for yorum in kitap.yorumlar:
                    tk.Label(display_window, text=f"Yorum: {yorum}").pack()

def yorum_ekle():
    def add_review():
        book_title = book_title_entry.get()
        review = review_entry.get()
        if book_title and review:
            for kitap in kitaplar:
                if kitap.ad == book_title:
                    kitap.yorum_ekle(f"{current_user.kullanici_adi}: {review}")
                    messagebox.showinfo("Başarılı", "Yorum eklendi!")
                    window.destroy()
                    return
            messagebox.showerror("Hata", "Kitap bulunamadı.")
        else:
            messagebox.showerror("Hata", "Lütfen kitap adı ve yorumu girin.")
    
    window = tk.Toplevel(root)
    window.title("Yorum Ekle")
    
    tk.Label(window, text="Kitap Adı:").pack()
    book_title_entry = tk.Entry(window)
    book_title_entry.pack()
    
    tk.Label(window, text="Yorum:").pack()
    review_entry = tk.Entry(window)
    review_entry.pack()
    
    tk.Button(window, text="Yorum Ekle", command=add_review).pack()

def main_menu():
    def logout():
        global current_user
        current_user = None
        messagebox.showinfo("Çıkış", "Çıkış yaptınız.")
    
    menu_window = tk.Toplevel(root)
    menu_window.title("Ana Menü")
    
    tk.Button(menu_window, text="Kitap Ekle", command=kitap_ekle).pack()
    tk.Button(menu_window, text="Kitapları Göster", command=kitaplari_goster).pack()
    tk.Button(menu_window, text="Yorum Ekle", command=yorum_ekle).pack()
    tk.Button(menu_window, text="Çıkış", command=logout).pack()

def main_window():
    root.geometry("600x400")
    
    tk.Label(root, text="Hoşgeldiniz!").pack(pady=20)
    
    tk.Button(root, text="Hesap Oluştur", command=hesap_olustur).pack(pady=10)
    tk.Button(root, text="Giriş Yap", command=giris_yap).pack(pady=10)
    
    root.mainloop()

main_window()