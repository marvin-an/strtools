import streamlit as st

# 兼容性处理 - 检查Streamlit版本
def rerun_app():
    """兼容不同版本的Streamlit重新运行方法"""
    if hasattr(st, 'rerun'):
        st.rerun()
    elif hasattr(st, 'experimental_rerun'):
        st.experimental_rerun()
    else:
        # 如果都没有，使用query_params来强制刷新
        st.query_params.clear()

# 语言配置
LANGUAGES = {
    "中文": {
        "page_title": "🎈 StrTools - 字符串处理工具集",
        "main_title": "🎈 StrTools",
        "subtitle": "专为程序员设计的字符串处理工具集",
        "language_selector": "选择语言 | Language",
        "menu_title": "🛠️ 工具菜单",
        "tools": {
            "home": "🏠 首页",
            "stack_formatter": "🔧 堆栈字符串格式化",
        },
        "stack_formatter": {
            "title": "🔧 堆栈字符串格式化工具",
            "description": "将以竖线符号（|）分隔的堆栈信息转换为易读的多行格式",
            "input_label": "请粘贴您的堆栈字符串:",
            "input_placeholder": "例如: at main.py:10|at utils.py:25|at handler.py:50|...",
            "result_title": "✨ 格式化结果",
            "success_msg": "✅ 成功格式化！共 {} 行堆栈信息",
            "stats_title": "📊 统计信息",
            "original_length": "原始字符串长度",
            "stack_levels": "堆栈层级数量",
            "formatted_lines": "格式化后行数",
            "no_pipe_warning": "⚠️ 未检测到竖线符号（|）。请确保您的堆栈字符串包含竖线分隔符。",
            "example_title": "💡 示例",
            "input_example": "输入示例:",
            "output_example": "输出示例:",
            "how_to_use": "使用方法：",
            "usage_steps": [
                "在下方输入框中粘贴您的堆栈字符串",
                "堆栈信息应该以竖线符号（|）分隔",
                "工具会自动将其格式化为多行显示",
                "格式化后的结果会在下方显示"
            ]
        },
        "home": {
            "welcome": "欢迎使用StrTools！",
            "description": "这是一个专为程序员设计的字符串处理工具集合。请选择您需要的工具。",
            "features_title": "🛠️ 功能特点",
            "features": [
                "🌐 **多语言支持** - 中英文界面",
                "🔧 **实时处理** - 输入即时格式化", 
                "📊 **详细统计** - 提供处理统计信息",
                "💡 **示例说明** - 内置使用示例",
                "🎯 **专为程序员设计** - 解决实际开发问题"
            ],
            "available_tools": "可用工具：",
            "stack_formatter_desc": "格式化以竖线符号分隔的堆栈字符串，适用于Java、Python、JavaScript等语言的堆栈跟踪信息",
            "more_tools": "更多工具即将到来...",
            "tool_buttons": {
                "stack_formatter": "使用堆栈格式化工具",
                "coming_soon": "敬请期待"
            }
        }
    },
    "English": {
        "page_title": "🎈 StrTools - String Processing Toolkit",
        "main_title": "🎈 StrTools", 
        "subtitle": "String Processing Tools for Developers",
        "language_selector": "Language | 选择语言",
        "menu_title": "🛠️ Tools Menu",
        "tools": {
            "home": "🏠 Home",
            "stack_formatter": "🔧 Stack String Formatter",
        },
        "stack_formatter": {
            "title": "🔧 Stack String Formatter",
            "description": "Convert pipe-separated (|) stack information into readable multi-line format",
            "input_label": "Please paste your stack string:",
            "input_placeholder": "For example: at main.py:10|at utils.py:25|at handler.py:50|...",
            "result_title": "✨ Formatted Result",
            "success_msg": "✅ Successfully formatted! {} stack lines",
            "stats_title": "📊 Statistics",
            "original_length": "Original length",
            "stack_levels": "Stack levels",
            "formatted_lines": "Formatted lines",
            "no_pipe_warning": "⚠️ No pipe symbols (|) detected. Please ensure your stack string contains pipe separators.",
            "example_title": "💡 Example",
            "input_example": "Input Example:",
            "output_example": "Output Example:",
            "how_to_use": "How to use:",
            "usage_steps": [
                "Paste your stack string in the input box below",
                "Stack information should be separated by pipe symbols (|)",
                "The tool will automatically format it into multiple lines",
                "The formatted result will be displayed below"
            ]
        },
        "home": {
            "welcome": "Welcome to StrTools!",
            "description": "This is a collection of string processing tools designed specifically for developers. Please select the tool you need.",
            "features_title": "🛠️ Features",
            "features": [
                "🌐 **Multi-language Support** - Chinese & English interface",
                "🔧 **Real-time Processing** - Instant formatting on input",
                "📊 **Detailed Statistics** - Processing statistics provided",
                "💡 **Examples Included** - Built-in usage examples",
                "🎯 **Developer-focused** - Solving real development problems"
            ],
            "available_tools": "Available Tools:",
            "stack_formatter_desc": "Format pipe-separated stack strings, suitable for Java, Python, JavaScript and other programming languages",
            "more_tools": "More tools coming soon...",
            "tool_buttons": {
                "stack_formatter": "Use Stack Formatter",
                "coming_soon": "Coming Soon"
            }
        }
    }
}

# 页面配置
st.set_page_config(
    page_title="🎈 StrTools - String Processing Toolkit",
    page_icon="🎈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 初始化session state
if 'language' not in st.session_state:
    st.session_state.language = "中文"
if 'selected_tool' not in st.session_state:
    st.session_state.selected_tool = "home"

# 获取当前语言配置
lang = LANGUAGES[st.session_state.language]

# 侧边栏 - 语言选择和工具菜单
with st.sidebar:
    st.title(lang["main_title"])
    
    # 语言选择
    st.markdown(f"### {lang['language_selector']}")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🇨🇳 中文", use_container_width=True, 
                    type="primary" if st.session_state.language == "中文" else "secondary"):
            st.session_state.language = "中文"
    
    with col2:
        if st.button("🇺🇸 English", use_container_width=True,
                    type="primary" if st.session_state.language == "English" else "secondary"):
            st.session_state.language = "English"
    
    st.markdown("---")
    
    # 工具菜单
    st.markdown(f"### {lang['menu_title']}")
    
    # 首页按钮
    if st.button(lang["tools"]["home"], use_container_width=True,
                type="primary" if st.session_state.selected_tool == "home" else "secondary"):
        st.session_state.selected_tool = "home"
    
    # 堆栈格式化工具按钮
    if st.button(lang["tools"]["stack_formatter"], use_container_width=True,
                type="primary" if st.session_state.selected_tool == "stack_formatter" else "secondary"):
        st.session_state.selected_tool = "stack_formatter"
    
    # 预留更多工具按钮
    st.markdown("#### 🚧 " + ("即将推出" if st.session_state.language == "中文" else "Coming Soon"))
    st.button("🔄 JSON Formatter", use_container_width=True, disabled=True)
    st.button("🔗 URL Encoder/Decoder", use_container_width=True, disabled=True)
    st.button("📝 Base64 Encoder", use_container_width=True, disabled=True)
    st.button("🔍 Regex Tester", use_container_width=True, disabled=True)

# 主内容区域
st.title(lang["main_title"])
st.subheader(lang["subtitle"])

# 根据选择的工具显示内容
if st.session_state.selected_tool == "home":
    # 首页
    st.markdown(f"## {lang['home']['welcome']}")
    st.write(lang['home']['description'])
    
    st.markdown(f"### {lang['home']['features_title']}")
    for feature in lang['home']['features']:
        st.markdown(f"- {feature}")
    
    st.markdown("---")
    st.markdown(f"### {lang['home']['available_tools']}")
    
    # 工具卡片展示
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.markdown(f"""
            <div style="padding: 1rem; border: 1px solid #ddd; border-radius: 0.5rem; margin-bottom: 1rem;">
                <h4>🔧 {lang['tools']['stack_formatter'].replace('🔧 ', '')}</h4>
                <p>{lang['home']['stack_formatter_desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(lang['home']['tool_buttons']['stack_formatter'], 
                        key="home_to_stack", use_container_width=True):
                st.session_state.selected_tool = "stack_formatter"
    
    with col2:
        with st.container():
            st.markdown(f"""
            <div style="padding: 1rem; border: 1px solid #ddd; border-radius: 0.5rem; margin-bottom: 1rem; opacity: 0.6;">
                <h4>🚧 {lang['home']['more_tools']}</h4>
                <p>JSON Formatter, URL Encoder/Decoder, Base64 Encoder, Regex Tester</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.button(lang['home']['tool_buttons']['coming_soon'], 
                     key="coming_soon", use_container_width=True, disabled=True)

elif st.session_state.selected_tool == "stack_formatter":
    # 堆栈字符串格式化工具
    st.markdown(f"## {lang['stack_formatter']['title']}")
    st.write(lang['stack_formatter']['description'])
    
    # 使用说明
    with st.expander(lang['stack_formatter']['how_to_use']):
        for i, step in enumerate(lang['stack_formatter']['usage_steps'], 1):
            st.write(f"{i}. {step}")
    
    # 输入区域
    input_text = st.text_area(
        lang['stack_formatter']['input_label'],
        height=150,
        placeholder=lang['stack_formatter']['input_placeholder']
    )
    
    # 格式化处理
    if input_text:
        st.subheader(lang['stack_formatter']['result_title'])
        
        if "|" in input_text:
            # 按|分割并去除空白
            stack_lines = [line.strip() for line in input_text.split("|") if line.strip()]
            
            # 显示格式化后的结果
            formatted_text = "\n".join(stack_lines)
            st.code(formatted_text, language=None)
            
            # 成功提示
            st.success(lang['stack_formatter']['success_msg'].format(len(stack_lines)))
            
            # 统计信息
            with st.expander(lang['stack_formatter']['stats_title']):
                st.write(f"- **{lang['stack_formatter']['original_length']}:** {len(input_text)} {'characters' if st.session_state.language == 'English' else '字符'}")
                st.write(f"- **{lang['stack_formatter']['stack_levels']}:** {len(stack_lines)}")
                st.write(f"- **{lang['stack_formatter']['formatted_lines']}:** {len(stack_lines)}")
        else:
            st.warning(lang['stack_formatter']['no_pipe_warning'])
    
    # 示例
    with st.expander(lang['stack_formatter']['example_title']):
        st.markdown(f"""
        **{lang['stack_formatter']['input_example']}**
        ```
        at com.example.Main.main(Main.java:25)|at com.example.Utils.process(Utils.java:15)|at com.example.Handler.handle(Handler.java:42)|at com.example.Service.execute(Service.java:8)
        ```
        
        **{lang['stack_formatter']['output_example']}**
        ```
        at com.example.Main.main(Main.java:25)
        at com.example.Utils.process(Utils.java:15)
        at com.example.Handler.handle(Handler.java:42)
        at com.example.Service.execute(Service.java:8)
        ```
        """)

# 页脚
st.markdown("---")
if st.session_state.language == "中文":
    st.markdown("🎈 **StrTools** - 让字符串处理更简单")
else:
    st.markdown("🎈 **StrTools** - Making string processing easier for developers")
