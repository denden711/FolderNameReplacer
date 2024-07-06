import os
import tkinter as tk
from tkinter import filedialog, messagebox

class FolderRenamerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("フォルダ名置換プログラム")
        self.create_widgets()

    def create_widgets(self):
        # フォルダ選択ボタン
        self.select_folder_btn = tk.Button(self.root, text="フォルダ選択", command=self.select_folder)
        self.select_folder_btn.pack(pady=10)

        # 選択されたフォルダ表示
        self.selected_folder_label = tk.Label(self.root, text="フォルダが選択されていません")
        self.selected_folder_label.pack(pady=10)

        # 置換前のテキスト入力
        self.old_name_label = tk.Label(self.root, text="置換前の名前:")
        self.old_name_label.pack(pady=5)
        self.old_name_entry = tk.Entry(self.root, width=40)
        self.old_name_entry.pack(pady=5)

        # 置換後のテキスト入力
        self.new_name_label = tk.Label(self.root, text="置換後の名前:")
        self.new_name_label.pack(pady=5)
        self.new_name_entry = tk.Entry(self.root, width=40)
        self.new_name_entry.pack(pady=5)

        # 実行ボタン
        self.rename_btn = tk.Button(self.root, text="置換実行", command=self.rename_folders)
        self.rename_btn.pack(pady=20)

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.selected_folder_label.config(text=folder_path)
            self.selected_folder = folder_path

    def rename_folders(self):
        if not hasattr(self, 'selected_folder'):
            messagebox.showerror("エラー", "フォルダを選択してください")
            return

        old_name = self.old_name_entry.get()
        new_name = self.new_name_entry.get()

        if not old_name or not new_name:
            messagebox.showerror("エラー", "置換前と置換後の名前を入力してください")
            return

        for dirpath, dirnames, _ in os.walk(self.selected_folder):
            for dirname in dirnames:
                if old_name in dirname:
                    old_folder_path = os.path.join(dirpath, dirname)
                    new_folder_name = dirname.replace(old_name, new_name)
                    new_folder_path = os.path.join(dirpath, new_folder_name)
                    try:
                        os.rename(old_folder_path, new_folder_path)
                        print(f"Renamed: {old_folder_path} -> {new_folder_path}")
                    except Exception as e:
                        print(f"Failed to rename: {old_folder_path} -> {new_folder_path}, Error: {e}")

        messagebox.showinfo("成功", "フォルダ名の置換が完了しました")

if __name__ == "__main__":
    root = tk.Tk()
    app = FolderRenamerApp(root)
    root.mainloop()
