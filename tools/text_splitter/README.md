# 📄 多行文本分割工具 | Multi-line Text Splitter

一个功能强大的Streamlit应用，用于将大段文本按指定规则分割成多个批次，并支持下载各个批次的文件。

A powerful Streamlit application for splitting large text into multiple batches by specified rules, with download support for each batch file.

## 功能特点 | Features

- 📄 **灵活分割** | Flexible splitting - 支持自定义分隔符和批次大小
- 🔧 **实时处理** | Real-time processing - 即时计算和显示分割结果
- 📊 **详细统计** | Detailed statistics - 显示总行数、批次数等信息
- 📥 **批量下载** | Batch download - 支持单个批次或所有批次下载
- 🌐 **双语支持** | Bilingual support - 完整的中英文界面
- 💡 **使用示例** | Usage examples - 内置详细的使用说明

## 使用方法 | How to Use

### 运行应用 | Run the Application

```bash
# 在项目根目录运行
streamlit run tools/text_splitter/app.py
```

### 使用说明 | Usage Instructions

1. **输入文本** | Input text
   - 在大文本框中粘贴需要分割的多行文本
   - 支持各种格式的文本内容

2. **配置分割规则** | Configure split rules
   - **分隔符设置**：默认为换行符 `\n`，可自定义其他分隔符
   - **批次大小**：设置每个批次包含的行数（1-10000行）

3. **执行分割** | Execute split
   - 点击"开始分割"按钮
   - 系统自动计算并显示分割结果

4. **下载文件** | Download files
   - 预览每个批次的内容
   - 单独下载每个批次文件
   - 或下载包含所有批次的合并文件

## 使用场景 | Use Cases

### 🔍 数据处理 | Data Processing
- **日志文件分割**：将大型日志文件分割成小批次便于分析
- **数据批处理**：将大量数据分割成批次进行处理
- **CSV/TSV处理**：分割大型数据文件便于导入处理

### 📧 批量操作 | Batch Operations
- **邮件列表分割**：将大量邮件地址分割成批次发送
- **用户列表处理**：分割用户数据进行批量操作
- **API批处理**：分割请求数据避免API限制

### 📝 文本分析 | Text Analysis
- **文档分割**：将长文档分割成段落进行分析
- **内容分批**：分割文本内容便于处理
- **数据清洗**：分批处理文本数据进行清洗

## 配置选项 | Configuration Options

### 分隔符类型 | Separator Types
- `\n` - 换行符（默认）
- `,` - 逗号分隔
- `;` - 分号分隔
- `|` - 竖线分隔
- `\t` - 制表符分隔
- 自定义字符

### 批次设置 | Batch Settings
- **最小批次**：1行
- **最大批次**：10,000行
- **推荐设置**：100-1000行（根据具体需求）

## 输出格式 | Output Format

### 单个批次文件 | Individual Batch Files
- **文件名**：`batch_1.txt`, `batch_2.txt`, ...
- **内容**：包含指定行数的文本内容
- **格式**：保持原始分隔符格式

### 合并文件 | Combined File
- **文件名**：`all_batches_text.txt`
- **内容**：所有批次内容，用分割线分隔
- **格式**：每个批次标记 `=== 批次 X ===`

## 示例 | Examples

### 邮件列表分割 | Email List Splitting

**输入 | Input:**
```
user1@example.com
user2@example.com
user3@example.com
user4@example.com
user5@example.com
```

**设置 | Settings:**
- 分隔符：`\n`
- 每批行数：2

**输出 | Output:**
- `batch_1.txt`: 包含 user1, user2
- `batch_2.txt`: 包含 user3, user4  
- `batch_3.txt`: 包含 user5

### CSV数据分割 | CSV Data Splitting

**输入 | Input:**
```
ID,Name,Email
1,张三,zhang@example.com
2,李四,li@example.com
3,王五,wang@example.com
```

**设置 | Settings:**
- 分隔符：`\n`
- 每批行数：2（包含标题行）

## 技术实现 | Technical Implementation

- **框架**：Streamlit
- **语言**：Python
- **功能**：文本处理、文件下载、批次管理
- **兼容性**：支持各种文本格式和编码

## 注意事项 | Notes

1. **内存限制**：处理超大文件时注意内存使用
2. **字符编码**：确保文本采用UTF-8编码
3. **分隔符选择**：根据文本格式选择合适的分隔符
4. **批次大小**：根据后续处理需求选择合适的批次大小 