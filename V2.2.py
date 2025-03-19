import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from collections import defaultdict

class CodeCheckerApp:
    def __init__(self, root):
        self.root = root
        root.title("兑换码查重工具 v1.0")
        root.geometry("800x600")
        
        # 设置主题样式
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.create_widgets()
        
    def create_widgets(self):
        # 输入区域
        input_frame = ttk.LabelFrame(self.root, text="输入兑换码（每行一个）")
        input_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        self.input_text = scrolledtext.ScrolledText(
            input_frame,
            wrap=tk.WORD,
            font=('Consolas', 10),
            height=10
        )
        self.input_text.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        # 按钮区域
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(padx=10, pady=5, fill=tk.X)
        
        self.check_btn = ttk.Button(
            btn_frame,
            text="检查重复",
            command=self.check_duplicates
        )
        self.check_btn.pack(side=tk.LEFT, padx=2)
        
        self.clear_btn = ttk.Button(
            btn_frame,
            text="清空",
            command=self.clear_all
        )
        self.clear_btn.pack(side=tk.RIGHT, padx=2)
        
        # 结果展示区域
        result_frame = ttk.LabelFrame(self.root, text="检查结果")
        result_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        self.result_text = scrolledtext.ScrolledText(
            result_frame,
            wrap=tk.WORD,
            font=('Consolas', 10),
            state=tk.DISABLED,
            foreground="#333"
        )
        self.result_text.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        # 状态栏
        self.status_bar = ttk.Label(
            self.root,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def process_codes(self):
        """处理兑换码数据"""
        raw_text = self.input_text.get("1.0", tk.END)
        codes = []
        for line in raw_text.splitlines():
            code = line.strip().lstrip('{').rstrip('}').strip()
            if code:
                codes.append(code)
        return codes
    
    def check_duplicates(self):
        """执行查重操作"""
        codes = self.process_codes()
        
        if not codes:
            messagebox.showwarning("空输入", "请输入要检查的兑换码")
            return
        
        # 统计重复
        count = defaultdict(int)
        for code in codes:
            count[code] += 1
        
        duplicates = {code: cnt for code, cnt in count.items() if cnt > 1}
        
        # 更新结果区域
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        
        if duplicates:
            result = "发现重复兑换码：\n\n"
            for code, cnt in duplicates.items():
                result += f"• {code} \n（出现次数：{cnt}次）\n\n"
            self.result_text.insert(tk.END, result)
            self.status_bar.config(text=f"发现 {len(duplicates)} 个重复项", foreground="red")
        else:
            self.result_text.insert(tk.END, "✅ 没有发现重复的兑换码")
            self.status_bar.config(text="检查完成，无重复项", foreground="green")
        
        self.result_text.config(state=tk.DISABLED)
    
    def clear_all(self):
        """清空所有内容"""
        self.input_text.delete(1.0, tk.END)
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state=tk.DISABLED)
        self.status_bar.config(text="就绪", foreground="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeCheckerApp(root)
    root.mainloop()