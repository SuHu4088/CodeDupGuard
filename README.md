# 兑换码查重工具 CodeDuplicateChecker

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📖 项目简介

一款用于检测兑换码重复项的桌面应用程序，提供命令行和GUI双版本。支持批量处理、智能过滤和可视化操作，适用于游戏激活码、优惠券码等场景的重复检查。

## ✨ 核心功能

### GUI版本功能
- 🖥️ 可视化操作界面
- 📋 支持大文本直接粘贴（自动处理包含花括号的格式）
- 🔍 智能过滤：
  - 自动忽略空行
  - 去除首尾空格
  - 过滤行首尾的 `{` `}` 符号
- 📊 检查结果高亮显示：
  - 重复项红色警示
  - 显示具体重复次数
- 🚦 状态栏实时反馈
- 🗑️ 一键清空所有内容

### 命令行版本功能
- ⌨️ 快速批量处理
- 📄 支持标准输入输出
- 📈 统计重复次数
- ✅ 轻量级无依赖

## 📸 界面截图
（此处可添加实际截图路径）
![GUI界面截图](screenshot.png)

## ⚙️ 环境要求
- Python 3.7+
- Tkinter（通常随Python自带）

## 📦 安装与使用

### 快速安装
```bash
git clone https://github.com/yourusername/CodeDuplicateChecker.git
cd CodeDuplicateChecker
```

### GUI版本使用
1. 运行程序：
```bash
python code_checker_gui.py
```
2. 在输入框粘贴兑换码（支持含花括号格式）
3. 点击【检查重复】按钮
4. 查看下方结果区域
5. 点击【清空】重置所有内容

### 命令行版本使用
```bash
# 通过管道输入
python check_codes.py < input.txt

# 或直接运行后粘贴内容（Ctrl+D结束输入）
python check_codes.py
```

## 📑 生成可执行文件
使用PyInstaller生成独立exe：
```bash
pip install pyinstaller
pyinstaller --onefile --windowed code_checker_gui.py
```
生成文件位于 `dist/` 目录

## 📜 开发计划
- [ ] 增加文件导入/导出功能
- [ ] 添加自动剪贴板监控
- [ ] 支持CSV/Excel文件处理
- [ ] 国际化支持（多语言界面）

## 🤝 贡献指南
欢迎通过Issue或Pull Request参与改进：
1. Fork项目
2. 创建特性分支 (`git checkout -b feature/your-feature`)
3. 提交修改 (`git commit -am 'Add some feature'`)
4. 推送分支 (`git push origin feature/your-feature`)
5. 创建Pull Request

## 📄 许可证
本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## ☎️ 联系作者
如有任何问题请联系：  
Email: your.email@example.com  
GitHub Issues: [问题反馈](https://github.com/yourusername/CodeDuplicateChecker/issues)
```

---

### 建议的Github仓库结构：
```
CodeDuplicateChecker/
├── docs/                   # 文档目录
│   └── screenshot.png     # 程序截图
├── src/                    # 源代码
│   ├── check_codes.py      # 命令行版本
│   └── code_checker_gui.py # GUI版本
├── LICENSE
├── README.md               # 本说明文件
└── requirements.txt        # 依赖列表（本项目无需额外依赖）
```

可根据实际需要添加：
1. 程序截图文件
2. 示例测试数据文件
3. 打包好的可执行文件（可选）
4. 贡献者指南（CONTRIBUTING.md）
5. 修改日志（CHANGELOG.md）
