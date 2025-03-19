---

# CodeDupGuard - 兑换码查重工具

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)

专业的兑换码重复检测工具，提供命令行与图形界面双版本，支持高效查重和结果导出。

---

## 📌 功能特性

### 核心功能
- **智能查重**：精准识别兑换码重复项，支持百万级数据检测
- **跨平台支持**：兼容 Windows/macOS/Linux 系统
- **双模式操作**：
  - **GUI 模式**：可视化交互界面（基于 Tkinter）
  - **CLI 模式**：命令行快速操作

### GUI 特色功能
- 📁 文件拖拽检测（支持.txt文件）
- 📊 实时统计面板（总数量/重复数/重复率）
- 📜 滚动式结果展示窗口
- 🚦 智能状态栏反馈
- 📤 一键导出检测报告
- 🧹 快速清空检测结果

### CLI 特色功能
- ⚡️ 极速检测（适合批量处理）
- 📂 支持管道操作
- 🖨️ 简洁结果输出

---

## 🖥️ 界面截图
![GUI 界面示例](https://via.placeholder.com/800x500.png?text=GUI+Preview+Here](https://github.com/SuHu4088/CodeDupGuard/blob/main/Snipaste_2025-03-20_01-55-50.png)  


---

## 🛠️ 安装与使用

### 环境要求
- Python 3.8+
- Tkinter（通常已包含在Python标准库中）

### 快速开始
```bash
# 克隆仓库
git clone https://github.com/yourusername/CodeDupGuard.git

# 进入项目目录
cd CodeDupGuard
```

### GUI 模式
```bash
python gui_code_checker.py
```
**操作流程**：  
1. 点击 "浏览" 按钮选择兑换码文件
2. 点击 "开始检测" 启动查重
3. 查看结果窗口的重复记录
4. 可选导出检测报告或清空结果

### CLI 模式
```bash
python check_codes.py 输入文件路径.txt
```
**输出示例**：
```
发现 3 处重复：
[重复1] V_DataPanBot_XXXXX (行号: 5, 18)
[重复2] V_DataPanBot_YYYYY (行号: 12, 24)
```

---

## 📂 文件结构
```
├── check_codes.py         # 命令行版本核心逻辑
├── gui_code_checker.py    # GUI版本主程序
├── sample_codes.txt       # 示例兑换码数据
├── LICENSE                # MIT许可证文件
└── README.md              # 项目说明文档
```

---

## 🧑💻 开发与贡献

### 代码规范
- PEP8 编码规范
- 类型注解（Type Hints）
- 模块化组件设计

### 扩展建议
- 添加数据库支持
- 实现批量文件处理
- 增加自动排重功能
- 开发Web服务版本

欢迎提交 Issue 或 Pull Request！

---

## 📜 开源协议

本项目采用 **MIT 许可证** - 详情请参阅 [LICENSE](LICENSE) 文件

---


*让重复检查变得简单高效！🚀*  

---

> 提示：实际使用时请替换占位内容（如截图、联系方式等），并添加`requirements.txt`文件（如有额外依赖）
