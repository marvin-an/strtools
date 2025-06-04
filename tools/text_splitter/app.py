import streamlit as st
import io
import zipfile
from datetime import datetime

# 创建ZIP文件的函数
def create_zip_file(batches_data):
    """创建包含所有批次文件的ZIP"""
    zip_buffer = io.BytesIO()
    
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for i, (batch_content, start_idx, end_idx) in enumerate(batches_data):
            filename = f"batch_{i+1}.txt"
            zip_file.writestr(filename, batch_content)
    
    zip_buffer.seek(0)
    return zip_buffer.getvalue()

# 页面配置
st.set_page_config(
    page_title="📄 多行文本分割工具 | Multi-line Text Splitter",
    page_icon="📄",
    layout="wide"
)

# 标题
st.title("📄 多行文本分割工具")
st.title("📄 Multi-line Text Splitter")

# 说明介绍
st.markdown("""
## 📖 使用说明 | Instructions

### 中文说明
这个工具可以帮助您将大段文本按指定分隔符和行数分割成多个批次，支持复制和下载各个批次的文件。

**使用方法：**
1. 在文本框中粘贴需要分割的多行文本
2. 选择分隔符（默认为换行符\\n）
3. 设置每批包含的行数
4. 点击开始分割按钮
5. 点击代码块右上角复制按钮或下载生成的各个批次文件

### English Description
This tool helps you split large text into multiple batches by specified separator and line count, with copy and download support for each batch file.

**How to use:**
1. Paste multi-line text in the text box
2. Choose separator (default is newline \\n)
3. Set number of lines per batch
4. Click the split button
5. Click copy button at top-right of code block or download the generated batch files

---
""")

# 配置区域
col1, col2 = st.columns([2, 1])

with col1:
    # 分隔符输入
    separator = st.text_input(
        "分隔符 | Separator:",
        value="\\n",
        help="用于分割文本的字符，默认为换行符 | Character used to split text, default is newline"
    )
    # 将\\n转换为实际的换行符
    if separator == "\\n":
        separator = "\n"

with col2:
    # 每批行数
    lines_per_batch = st.number_input(
        "每批行数 | Lines per batch:",
        min_value=1,
        max_value=10000,
        value=100,
        help="每个批次包含的行数 | Number of lines in each batch"
    )

# 文本输入区域
st.subheader("📝 输入文本 | Input Text")
input_text = st.text_area(
    "请输入要分割的文本 | Enter text to split:",
    height=200,
    placeholder="粘贴您的多行文本... | Paste your multi-line text here..."
)

# 分割处理
if input_text:
    if st.button("🚀 开始分割 | Start Splitting", type="primary"):
        # 分割文本
        lines = input_text.split(separator)
        lines = [line for line in lines if line.strip()]  # 去除空行
        
        if lines:
            # 计算批次
            total_lines = len(lines)
            total_batches = (total_lines + lines_per_batch - 1) // lines_per_batch
            
            st.subheader("📊 分割结果 | Split Results")
            
            # 显示统计信息
            col1, col2 = st.columns(2)
            with col1:
                st.metric("总行数 | Total lines", total_lines)
            with col2:
                st.metric("分割批次 | Total batches", total_batches)
            
            # 复制提示
            st.info("💡 点击代码块右上角的复制按钮可一键复制文本 | Click the copy button at the top-right of code block to copy text")
            
            # 生成批次数据
            batches_data = []
            for i in range(total_batches):
                start_idx = i * lines_per_batch
                end_idx = min(start_idx + lines_per_batch, total_lines)
                batch_lines = lines[start_idx:end_idx]
                batch_content = separator.join(batch_lines) if separator != "\n" else "\n".join(batch_lines)
                batches_data.append((batch_content, start_idx, end_idx))
            
            # 下载所有批次的ZIP包
            st.markdown("---")
            if total_batches > 1:
                zip_data = create_zip_file(batches_data)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                st.download_button(
                    label="📦 下载所有批次 (ZIP) | Download All Batches (ZIP)",
                    data=zip_data,
                    file_name=f"text_batches_{timestamp}.zip",
                    mime="application/zip",
                    use_container_width=True
                )
                st.markdown("---")
            
            # 为每个批次创建展示和下载
            for i, (batch_content, start_idx, end_idx) in enumerate(batches_data):
                with st.expander(f"批次 | Batch {i+1} (行 | Lines {start_idx+1}-{end_idx})", expanded=True if total_batches <= 3 else False):
                    
                    # 使用st.code显示内容，自带复制按钮
                    st.markdown("**批次内容 (点击右上角复制按钮) | Batch Content (click copy button at top-right):**")
                    st.code(batch_content, language=None)
                    
                    # 按钮区域
                    col1, col2 = st.columns([1, 1])
                    
                    with col1:
                        # 下载按钮
                        st.download_button(
                            label=f"📥 下载批次 | Download Batch {i+1}",
                            data=batch_content,
                            file_name=f"batch_{i+1}.txt",
                            mime="text/plain",
                            key=f"download_{i}",
                            use_container_width=True
                        )
                    
                    with col2:
                        # 统计信息
                        lines_count = len(batch_content.split(separator if separator != "\n" else "\n"))
                        chars_count = len(batch_content)
                        st.info(f"📊 {lines_count}行/lines / {chars_count}字符/chars")
        else:
            st.warning("⚠️ 请输入要分割的文本内容 | Please enter text content to split")

# 使用示例
with st.expander("💡 使用示例 | Usage Examples"):
    st.markdown("""
    ### 中文示例 | Chinese Examples
    
    **使用场景：**
    1. **分割日志文件：** 将大型日志文件分割成小批次便于处理
    2. **数据批处理：** 将大量数据分割成批次进行处理
    3. **文本分析：** 将长文本分割成段落进行分析
    4. **邮件列表：** 将大量邮件地址分割成批次发送
    
    **输入示例：**
    ```
    用户1@example.com
    用户2@example.com
    用户3@example.com
    ...
    ```
    **设置：** 分隔符=\\n，每批=50行
    **结果：** 
    - ✅ 使用代码块自带的复制按钮一键复制任意批次文本
    - ✅ 下载ZIP包包含所有分开的批次文件
    - ✅ 实时显示每个批次的行数和字符数统计
    
    **复制功能特点：**
    - 🚀 **可靠复制**：使用Streamlit内置的复制按钮，兼容性更好
    - 📝 **一键操作**：点击代码块右上角的复制图标即可复制整个批次
    - 🎯 **精准复制**：确保复制的内容与显示的完全一致
    - 🔧 **无需权限**：不需要额外的浏览器权限或JavaScript支持
    
    ---
    
    ### English Examples
    
    **Usage Scenarios:**
    1. **Split log files:** Divide large log files into small batches for processing
    2. **Data batch processing:** Split large datasets into batches for processing
    3. **Text analysis:** Divide long text into paragraphs for analysis
    4. **Email lists:** Split large email lists into batches for sending
    
    **Input Example:**
    ```
    user1@example.com
    user2@example.com
    user3@example.com
    ...
    ```
    **Settings:** Separator=\\n, Lines per batch=50
    **Result:** 
    - ✅ Use built-in copy button of code block for one-click copying of any batch
    - ✅ Download ZIP package with all separate batch files
    - ✅ Real-time statistics for lines and characters in each batch
    
    **Copy Features:**
    - 🚀 **Reliable Copy**: Uses Streamlit's built-in copy button for better compatibility
    - 📝 **One-click Operation**: Click the copy icon at top-right of code block to copy entire batch
    - 🎯 **Accurate Copy**: Ensures copied content matches exactly what's displayed
    - 🔧 **No Permissions**: No additional browser permissions or JavaScript support needed
    """)

# 页脚
st.markdown("---")
st.markdown("📄 **多行文本分割工具** | **Multi-line Text Splitter Tool**") 