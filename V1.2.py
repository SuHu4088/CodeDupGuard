import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from collections import defaultdict

class CodeCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("兑换码查重工具")
        self.root.geometry("800x600")
        
        # 初始化变量
        self.file_path = tk.StringVar()
        self.duplicates = defaultdict(list)
        
        # 创建界面组件
        self.create_widgets()
        
    def create_widgets(self):
        # 文件选择区域
        file_frame = ttk.LabelFrame(self.root, text="文件操作")
        file_frame.pack(pady=10, padx=10, fill="x")
        
        ttk.Label(file_frame, text="选择文件:").grid(row=0, column=0, padx=5)
        ttk.Entry(file_frame, textvariable=self.file_path, width=50).grid(row=0, column=1, padx=5)
        ttk.Button(file_frame, text="浏览", command=self.browse_file).grid(row=0, column=2, padx=5)
        ttk.Button(file_frame, text="开始检测", command=self.check_duplicates).grid(row=0, column=3, padx=5)
        
        # 结果显示区域
        result_frame = ttk.LabelFrame(self.root, text="检测结果")
        result_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        self.result_text = scrolledtext.ScrolledText(
            result_frame,
            wrap=tk.WORD,
            font=('Consolas', 10),
            height=15
        )
        self.result_text.pack(fill="both", expand=True, padx=5, pady=5)
        
        # 底部按钮
        bottom_frame = ttk.Frame(self.root)
        bottom_frame.pack(pady=10, fill="x")
        
        ttk.Button(
            bottom_frame,
            text="导出结果",
            command=self.export_results
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            bottom_frame,
            text="清空结果",
            command=self.clear_results
        ).pack(side=tk.LEFT, padx=5)
        
        # 状态栏
        self.status_bar = ttk.Label(self.root, text="就绪", relief=tk.SUNKEN)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def browse_file(self):
        filetypes = (("文本文件", "*.txt"), ("所有文件", "*.*"))
        filename = filedialog.askopenfilename(title="选择兑换码文件", filetypes=filetypes)
        if filename:
            self.file_path.set(filename)
            self.clear_results()
    
    def check_duplicates(self):
        if not self.file_path.get():
            messagebox.showwarning("警告", "请先选择文件！")
            return
        
        try:
            with open(self.file_path.get(), 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            code_dict = defaultdict(list)
            for idx, line in enumerate(lines, 1):
                stripped = line.strip()
                if stripped:
                    code_dict[stripped].append(idx)
            
            self.duplicates = {k: v for k, v in code_dict.items() if len(v) > 1}
            self.show_results()
            
            if self.duplicates:
                self.status_bar.config(text=f"检测完成，发现 {len(self.duplicates)} 处重复")
            else:
                self.status_bar.config(text="检测完成，未发现重复")
                
        except Exception as e:
            messagebox.showerror("错误", f"文件读取失败: {str(e)}")
            self.status_bar.config(text="文件读取错误")
    
    def show_results(self):
        self.result_text.delete(1.0, tk.END)
        if not self.duplicates:
            self.result_text.insert(tk.END, "未发现重复的兑换码")
            return
            
        for code, lines in self.duplicates.items():
            self.result_text.insert(tk.END, f"重复兑换码：{code}\n")
            self.result_text.insert(tk.END, f"重复行号：{', '.join(map(str, lines))}\n")
            self.result_text.insert(tk.END, "-"*80 + "\n")
    
    def export_results(self):
        if not self.duplicates:
            messagebox.showinfo("提示", "没有需要导出的结果")
            return
            
        filetypes = (("文本文件", "*.txt"), ("所有文件", "*.*"))
        filename = filedialog.asksaveasfilename(
            title="保存检测结果",
            defaultextension=".txt",
            filetypes=filetypes
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"检测文件：{self.file_path.get()}\n")
                    f.write(f"发现重复：{len(self.duplicates)} 处\n\n")
                    for code, lines in self.duplicates.items():
                        f.write(f"重复兑换码：{code}\n")
                        f.write(f"重复行号：{', '.join(map(str, lines))}\n")
                        f.write("-"*80 + "\n")
                messagebox.showinfo("成功", "结果导出成功！")
            except Exception as e:
                messagebox.showerror("错误", f"导出失败: {str(e)}")
    
    def clear_results(self):
        self.duplicates.clear()
        self.result_text.delete(1.0, tk.END)
        self.status_bar.config(text="就绪")

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeCheckerApp(root)
    root.mainloop()