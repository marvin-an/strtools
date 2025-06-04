import streamlit as st

# 页面配置
st.set_page_config(
    page_title="堆栈字符串格式化工具 | Stack String Formatter",
    page_icon="🔧",
    layout="wide"
)

# 标题
st.title("🔧 堆栈字符串格式化工具")
st.title("🔧 Stack String Formatter")

# 说明介绍
st.markdown("""
## 📖 使用说明 | Instructions

### 中文说明
这个工具可以帮助您格式化堆栈字符串。将以竖线符号（|）分隔的堆栈信息转换为易读的多行格式。

**使用方法：**
1. 在下方输入框中粘贴您的堆栈字符串
2. 堆栈信息应该以竖线符号（|）分隔
3. 工具会自动将其格式化为多行显示
4. 格式化后的结果会在下方显示

### English Description
This tool helps you format stack strings by converting pipe-separated (|) stack information into a readable multi-line format.

**How to use:**
1. Paste your stack string in the input box below
2. Stack information should be separated by pipe symbols (|)
3. The tool will automatically format it into multiple lines
4. The formatted result will be displayed below

---
""")

# 输入区域
st.subheader("📝 输入堆栈字符串 | Input Stack String")
input_text = st.text_area(
    "请粘贴您的堆栈字符串 | Please paste your stack string:",
    height=150,
    placeholder="例如 | For example: at main.py:10|at utils.py:25|at handler.py:50|..."
)

# 格式化按钮和结果显示
if input_text:
    st.subheader("✨ 格式化结果 | Formatted Result")
    
    # 处理输入的堆栈字符串
    if "|" in input_text:
        # 按|分割并去除空白
        stack_lines = [line.strip() for line in input_text.split("|") if line.strip()]
        
        # 显示格式化后的结果
        formatted_text = "\n".join(stack_lines)
        
        # 在代码块中显示结果
        st.code(formatted_text, language=None)
        
        # 提供复制按钮
        st.success(f"✅ 成功格式化！共 {len(stack_lines)} 行堆栈信息 | Successfully formatted! {len(stack_lines)} stack lines")
        
        # 显示统计信息
        with st.expander("📊 统计信息 | Statistics"):
            st.write(f"- **原始字符串长度 | Original length:** {len(input_text)} 字符 | characters")
            st.write(f"- **堆栈层级数量 | Stack levels:** {len(stack_lines)}")
            st.write(f"- **格式化后行数 | Formatted lines:** {len(stack_lines)}")
    else:
        st.warning("⚠️ 未检测到竖线符号（|）。请确保您的堆栈字符串包含竖线分隔符。")
        st.warning("⚠️ No pipe symbols (|) detected. Please ensure your stack string contains pipe separators.")

# 示例
with st.expander("💡 示例 | Example"):
    st.markdown("""
    **输入示例 | Input Example:**
    ```
    at com.example.Main.main(Main.java:25)|at com.example.Utils.process(Utils.java:15)|at com.example.Handler.handle(Handler.java:42)|at com.example.Service.execute(Service.java:8)
    ```
    
    **输出示例 | Output Example:**
    ```
    at com.example.Main.main(Main.java:25)
    at com.example.Utils.process(Utils.java:15)
    at com.example.Handler.handle(Handler.java:42)
    at com.example.Service.execute(Service.java:8)
    ```
    """)

# 页脚
st.markdown("---")
st.markdown("🔧 **堆栈字符串格式化工具** | **Stack String Formatter Tool**") 