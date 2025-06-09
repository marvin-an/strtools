import streamlit as st
import io
import zipfile
from datetime import datetime
import re
import unicodedata

# 乱码检测函数
def is_garbled_text(text, threshold=0.3):
    """
    检测文本是否为乱码
    Args:
        text: 要检测的文本
        threshold: 乱码字符比例阈值，超过此比例认为是乱码
    Returns:
        bool: True表示是乱码，False表示正常文本
    """
    if not text.strip():
        return True  # 空行认为需要过滤
    
    # 移除空白字符
    text = text.strip()
    if len(text) == 0:
        return True
    
    garbled_count = 0
    total_chars = len(text)
    
    for char in text:
        # 检查是否为控制字符（除了常见的制表符、换行符）
        if unicodedata.category(char).startswith('C') and char not in '\t\n\r':
            garbled_count += 1
            continue
            
        # 检查是否为未定义的Unicode字符
        if unicodedata.category(char) == 'Cn':
            garbled_count += 1
            continue
            
        # 检查是否为替换字符（）
        if char == '\ufffd':
            garbled_count += 1
            continue
            
        # 检查是否为异常的符号密集
        if unicodedata.category(char).startswith('S'):
            # 如果符号字符过多，可能是乱码
            pass
    
    # 检查乱码模式
    # 1. 连续的问号或替换字符
    if re.search(r'\?{3,}|{2,}', text):
        return True
        
    # 2. 大量连续的特殊字符
    if re.search(r'[^\w\s\u4e00-\u9fff]{5,}', text):
        garbled_count += 3
        
    # 3. 检查是否包含明显的编码错误模式
    if re.search(r'\\x[0-9a-fA-F]{2}', text):  # 十六进制转义序列
        return True
        
    # 计算乱码比例
    garbled_ratio = garbled_count / total_chars
    return garbled_ratio > threshold

# 创建ZIP文件的函数
def create_zip_file(batches_data, lang):
    """创建包含所有批次文件的ZIP"""
    zip_buffer = io.BytesIO()
    
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for i, (batch_content, start_idx, end_idx) in enumerate(batches_data):
            filename = f"batch_{i+1}.txt"
            zip_file.writestr(filename, batch_content)
    
    zip_buffer.seek(0)
    return zip_buffer.getvalue()

# 多语言配置
LANGUAGES = {
    "中文": {
        "page_title": "📄 多行文本分割工具",
        "title": "📄 多行文本分割工具",
        "description": "将大段文本按指定分隔符和行数分割成多个批次，支持复制和下载",
        "language_selector": "选择语言 | Language",
        "input_label": "请输入要分割的文本:",
        "input_placeholder": "粘贴您的多行文本...",
        "separator_label": "分隔符:",
        "separator_help": "用于分割文本的字符，默认为换行符",
        "lines_per_batch_label": "每批行数:",
        "lines_per_batch_help": "每个批次包含的行数",
        "filter_garbled_label": "🧹 过滤乱码行",
        "filter_garbled_help": "自动检测并过滤掉乱码、控制字符和异常内容的行",
        "split_button": "开始分割",
        "result_title": "📊 分割结果",
        "total_lines": "总行数",
        "valid_lines": "有效行数",
        "filtered_lines": "过滤行数",
        "total_batches": "分割批次",
        "download_prefix": "批次",
        "download_all_zip": "下载所有批次 (ZIP)",
        "batch_content": "批次内容 (点击右上角复制按钮)",
        "copy_tip": "💡 点击代码块右上角的复制按钮可一键复制文本",
        "filter_info": "🧹 已过滤 {} 行乱码内容",
        "filtered_content_title": "🔍 被过滤的内容",
        "filtered_content_subtitle": "以下内容被识别为乱码已过滤，请检查是否正确：",
        "example_title": "💡 使用示例",
        "how_to_use": "使用方法：",
        "usage_steps": [
            "在文本框中粘贴需要分割的多行文本",
            "选择分隔符（默认为换行符\\n）",
            "设置每批包含的行数",
            "选择是否过滤乱码行",
            "点击开始分割按钮",
            "检查被过滤的内容是否正确",
            "点击代码块右上角复制按钮或下载文件"
        ],
        "no_content_warning": "⚠️ 请输入要分割的文本内容"
    },
    "English": {
        "page_title": "📄 Multi-line Text Splitter",
        "title": "📄 Multi-line Text Splitter",
        "description": "Split large text into multiple batches by specified separator and line count, with copy and download support",
        "language_selector": "Language | 选择语言",
        "input_label": "Enter text to split:",
        "input_placeholder": "Paste your multi-line text here...",
        "separator_label": "Separator:",
        "separator_help": "Character used to split text, default is newline",
        "lines_per_batch_label": "Lines per batch:",
        "lines_per_batch_help": "Number of lines in each batch",
        "filter_garbled_label": "🧹 Filter Garbled Lines",
        "filter_garbled_help": "Automatically detect and filter out garbled, control characters and abnormal content lines",
        "split_button": "Start Splitting",
        "result_title": "📊 Split Results",
        "total_lines": "Total lines",
        "valid_lines": "Valid lines",
        "filtered_lines": "Filtered lines",
        "total_batches": "Total batches",
        "download_prefix": "Batch",
        "download_all_zip": "Download All Batches (ZIP)",
        "batch_content": "Batch Content (click copy button at top-right)",
        "copy_tip": "💡 Click the copy button at the top-right of code block to copy text",
        "filter_info": "🧹 Filtered {} garbled content lines",
        "filtered_content_title": "🔍 Filtered Content",
        "filtered_content_subtitle": "The following content was identified as garbled and filtered, please check if correct:",
        "example_title": "💡 Usage Example",
        "how_to_use": "How to use:",
        "usage_steps": [
            "Paste multi-line text in the text box",
            "Choose separator (default is newline \\n)",
            "Set number of lines per batch",
            "Choose whether to filter garbled lines",
            "Click the split button",
            "Check if filtered content is correct",
            "Click copy button at top-right of code block or download files"
        ],
        "no_content_warning": "⚠️ Please enter text content to split"
    }
}

# 页面配置
st.set_page_config(
    page_title="📄 Multi-line Text Splitter",
    page_icon="📄",
    layout="wide"
)

# 初始化session state
if 'language' not in st.session_state:
    st.session_state.language = "中文"

# 获取当前语言配置
lang = LANGUAGES[st.session_state.language]

# 语言选择器
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
with col3:
    st.markdown(f"**{lang['language_selector']}**")

col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1, 1, 1.5])
with col2:
    if st.button("🇨🇳 中文", use_container_width=True, 
                type="primary" if st.session_state.language == "中文" else "secondary"):
        st.session_state.language = "中文"

with col4:
    if st.button("🇺🇸 English", use_container_width=True,
                type="primary" if st.session_state.language == "English" else "secondary"):
        st.session_state.language = "English"

st.markdown("---")

# 主标题和描述
st.title(lang["title"])
st.write(lang["description"])

# 使用说明
with st.expander(lang['how_to_use']):
    for i, step in enumerate(lang['usage_steps'], 1):
        st.write(f"{i}. {step}")

# 配置区域
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    # 分隔符输入
    separator = st.text_input(
        lang['separator_label'],
        value="\\n",
        help=lang['separator_help']
    )
    # 将\\n转换为实际的换行符
    if separator == "\\n":
        separator = "\n"

with col2:
    # 每批行数
    lines_per_batch = st.number_input(
        lang['lines_per_batch_label'],
        min_value=1,
        max_value=10000,
        value=100,
        help=lang['lines_per_batch_help']
    )

with col3:
    # 过滤乱码选项
    filter_garbled = st.checkbox(
        lang['filter_garbled_label'],
        value=False,
        help=lang['filter_garbled_help']
    )

# 文本输入区域
input_text = st.text_area(
    lang['input_label'],
    height=200,
    placeholder=lang['input_placeholder']
)

# 分割处理
if input_text:
    if st.button(lang['split_button'], type="primary"):
        # 分割文本
        lines = input_text.split(separator)
        original_lines_count = len(lines)
        
        # 过滤乱码行（如果启用）
        filtered_lines = []  # 存储被过滤的行
        if filter_garbled:
            valid_lines = []
            for i, line in enumerate(lines):
                if is_garbled_text(line):
                    filtered_lines.append((i+1, line))  # 存储行号和内容
                else:
                    valid_lines.append(line)
            lines = valid_lines
            filtered_count = len(filtered_lines)
        else:
            lines = [line for line in lines if line.strip()]  # 只去除空行
            filtered_count = 0
        
        if lines:
            # 计算批次
            total_lines = len(lines)
            total_batches = (total_lines + lines_per_batch - 1) // lines_per_batch
            
            st.subheader(lang['result_title'])
            
            # 显示统计信息
            if filter_garbled and filtered_count > 0:
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric(lang['total_lines'], original_lines_count)
                with col2:
                    st.metric(lang['valid_lines'], total_lines)
                with col3:
                    st.metric(lang['filtered_lines'], filtered_count)
                with col4:
                    st.metric(lang['total_batches'], total_batches)
                
                # 过滤信息提示
                st.info(lang['filter_info'].format(filtered_count))
                
                # 显示被过滤的内容
                if filtered_lines:
                    with st.expander(f"🔍 {lang['filtered_content_title']} ({filtered_count} 行)", expanded=False):
                        st.warning(lang['filtered_content_subtitle'])
                        
                        # 创建被过滤内容的展示
                        filtered_text = ""
                        for line_num, content in filtered_lines:
                            # 限制显示长度，避免过长
                            display_content = content[:100] + "..." if len(content) > 100 else content
                            filtered_text += f"行 {line_num}: {display_content}\n"
                        
                        st.code(filtered_text, language=None)
                        
                        # 提供下载被过滤内容的选项
                        filtered_full_text = "\n".join([f"行 {line_num}: {content}" for line_num, content in filtered_lines])
                        st.download_button(
                            label="📥 下载被过滤的内容" if st.session_state.language == "中文" else "📥 Download Filtered Content",
                            data=filtered_full_text,
                            file_name="filtered_content.txt",
                            mime="text/plain",
                            key="download_filtered"
                        )
            else:
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(lang['total_lines'], total_lines)
                with col2:
                    st.metric(lang['total_batches'], total_batches)
            
            # 复制提示
            st.info(lang['copy_tip'])
            
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
                zip_data = create_zip_file(batches_data, lang)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                st.download_button(
                    label=f"📦 {lang['download_all_zip']}",
                    data=zip_data,
                    file_name=f"text_batches_{timestamp}.zip",
                    mime="application/zip",
                    use_container_width=True
                )
                st.markdown("---")
            
            # 为每个批次创建展示和下载
            for i, (batch_content, start_idx, end_idx) in enumerate(batches_data):
                with st.expander(f"{lang['download_prefix']} {i+1} ({'行' if st.session_state.language == '中文' else 'Lines'} {start_idx+1}-{end_idx})", expanded=True if total_batches <= 3 else False):
                    
                    # 使用st.code显示内容，自带复制按钮
                    st.markdown(f"**{lang['batch_content']}:**")
                    st.code(batch_content, language=None)
                    
                    # 按钮区域
                    col1, col2 = st.columns([1, 1])
                    
                    with col1:
                        # 下载按钮
                        st.download_button(
                            label=f"📥 {'下载' if st.session_state.language == '中文' else 'Download'} {lang['download_prefix']} {i+1}",
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
                        st.info(f"📊 {lines_count}{'行' if st.session_state.language == '中文' else 'lines'} / {chars_count}{'字符' if st.session_state.language == '中文' else 'chars'}")
        else:
            st.warning(lang['no_content_warning'])

# 示例和说明
with st.expander(lang['example_title']):
    if st.session_state.language == "中文":
        st.markdown("""
        **使用场景示例：**
        
        1. **分割日志文件：** 将大型日志文件分割成小批次便于处理
        2. **数据批处理：** 将大量数据分割成批次进行处理
        3. **文本分析：** 将长文本分割成段落进行分析
        4. **邮件列表：** 将大量邮件地址分割成批次发送
        
        **新功能 - 乱码过滤：**
        - 🧹 **自动检测**：识别包含控制字符、替换字符（）的行
        - 🔍 **模式识别**：检测连续问号、十六进制转义序列等乱码模式
        - 📊 **统计显示**：显示过滤前后的行数对比
        - ⚡ **智能过滤**：保留正常内容，去除明显的乱码和异常字符
        - 🔍 **过滤预览**：显示被过滤的内容，确认过滤是否正确
        - 📥 **过滤下载**：可下载被过滤的内容进行人工检查
        
        **输入示例：**
        ```
        用户1@example.com
        乱码行
        用户2@example.com
        \\x00\\x01控制字符
        用户3@example.com
        ```
        
        **设置：** 分隔符=\\n，每批=50行，启用乱码过滤
        **结果：** 
        - ✅ 使用代码块自带的复制按钮一键复制
        - ✅ 自动过滤乱码行，只保留有效内容
        - ✅ 显示被过滤的内容供确认
        - ✅ 下载ZIP包包含所有分开的批次文件
        - ✅ 实时显示过滤统计和批次信息
        """)
    else:
        st.markdown("""
        **Usage Examples:**
        
        1. **Split log files:** Divide large log files into small batches for processing
        2. **Data batch processing:** Split large datasets into batches for processing
        3. **Text analysis:** Divide long text into paragraphs for analysis
        4. **Email lists:** Split large email lists into batches for sending
        
        **New Feature - Garbled Text Filtering:**
        - 🧹 **Auto Detection**: Identify lines with control characters, replacement characters ()
        - 🔍 **Pattern Recognition**: Detect consecutive question marks, hex escape sequences and other garbled patterns
        - 📊 **Statistics Display**: Show line count comparison before and after filtering
        - ⚡ **Smart Filtering**: Keep normal content, remove obvious garbled and abnormal characters
        - 🔍 **Filter Preview**: Show filtered content for confirmation
        - 📥 **Filter Download**: Download filtered content for manual review
        
        **Input Example:**
        ```
        user1@example.com
        garbled line
        user2@example.com
        \\x00\\x01control chars
        user3@example.com
        ```
        
        **Settings:** Separator=\\n, Lines per batch=50, Enable garbled filtering
        **Result:** 
        - ✅ Use built-in copy button of code block for one-click copying
        - ✅ Auto filter garbled lines, keep only valid content
        - ✅ Show filtered content for confirmation
        - ✅ Download ZIP package with all separate batch files
        - ✅ Real-time filtering statistics and batch information display
        """)

# 页脚
st.markdown("---")
if st.session_state.language == "中文":
    st.markdown("📄 **多行文本分割工具** - 让大文本处理更简单 | [返回StrTools主页](../../../)")
else:
    st.markdown("📄 **Multi-line Text Splitter** - Making large text processing easier | [Back to StrTools](../../../)") 