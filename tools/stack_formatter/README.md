# 🔧 堆栈字符串格式化工具 | Stack String Formatter

一个简单易用的Streamlit应用，用于格式化以竖线符号（|）分隔的堆栈字符串。

A simple and user-friendly Streamlit application for formatting stack strings separated by pipe symbols (|).

## 功能特点 | Features

- ✨ **简单易用** | Easy to use - 直观的用户界面
- 🔧 **实时格式化** | Real-time formatting - 输入即时格式化
- 📊 **统计信息** | Statistics - 显示堆栈层级数量等信息
- 🌐 **双语支持** | Bilingual support - 中英文界面
- 💡 **示例说明** | Examples included - 内置使用示例

## 使用方法 | How to Use

### 运行应用 | Run the Application

```bash
# 在项目根目录运行
streamlit run tools/stack_formatter/app.py
```

### 使用说明 | Usage Instructions

1. **输入堆栈字符串** | Input stack string
   - 在文本框中粘贴您的堆栈字符串
   - 确保堆栈信息以竖线符号（|）分隔

2. **查看格式化结果** | View formatted result
   - 应用会自动将其转换为多行格式
   - 结果显示在代码块中，便于复制

3. **查看统计信息** | Check statistics
   - 点击统计信息展开面板查看详细信息
   - 包括原始长度、堆栈层级数量等

## 示例 | Example

**输入 | Input:**
```
at com.example.Main.main(Main.java:25)|at com.example.Utils.process(Utils.java:15)|at com.example.Handler.handle(Handler.java:42)
```

**输出 | Output:**
```
at com.example.Main.main(Main.java:25)
at com.example.Utils.process(Utils.java:15)
at com.example.Handler.handle(Handler.java:42)
```

## 适用场景 | Use Cases

- **Java堆栈跟踪** | Java stack traces
- **Python异常信息** | Python exception info  
- **JavaScript错误堆栈** | JavaScript error stacks
- **其他编程语言的调试信息** | Debug info from other programming languages 