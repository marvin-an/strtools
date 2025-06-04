# 🛠️ 工具集合 | Tools Collection

这里包含了各种实用的字符串处理和开发工具。

This directory contains various useful string processing and development tools.

## 可用工具 | Available Tools

### 📁 [stack_formatter](./stack_formatter/) - 堆栈字符串格式化工具
- **功能** | **Function**: 格式化以竖线符号（|）分隔的堆栈字符串
- **运行** | **Run**: `streamlit run tools/stack_formatter/app.py`
- **适用** | **Use for**: Java、Python、JavaScript等语言的堆栈跟踪信息

### 📁 [text_splitter](./text_splitter/) - 多行文本分割工具
- **功能** | **Function**: 将大段文本按指定规则分割成多个批次并支持下载
- **运行** | **Run**: `streamlit run tools/text_splitter/app.py`
- **适用** | **Use for**: 日志文件分割、数据批处理、邮件列表分割、文本分析

## 如何添加新工具 | How to Add New Tools

1. 在 `tools/` 目录下创建新的子文件夹
2. 添加 `app.py` 文件（Streamlit应用）
3. 添加 `README.md` 文件说明工具用途
4. 更新此文档的工具列表
5. 在主应用 `streamlit_app.py` 中添加新工具的配置

## 运行要求 | Requirements

所有工具都需要在项目根目录安装依赖：

All tools require dependencies to be installed from the project root:

```bash
pip install -r requirements.txt
```

## 使用方式 | Usage Methods

### 🎯 统一入口（推荐）| Unified Entry (Recommended)
```bash
streamlit run streamlit_app.py
```
通过主应用访问所有工具，支持中英文切换和菜单导航。

Access all tools through the main application with Chinese/English switching and menu navigation.

### 🔧 独立运行 | Independent Run
```bash
# 堆栈格式化工具
streamlit run tools/stack_formatter/app.py

# 文本分割工具
streamlit run tools/text_splitter/app.py
```
直接运行特定工具的独立版本。

Run independent versions of specific tools directly. 