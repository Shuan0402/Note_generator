import os

def format_text(file_name, text_width):
    # 獲得 file_name 的檔案路徑
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    file_path = os.path.join(parent_dir, 'txt', file_name)  # 假設txt資料夾的名稱是'txt資料夾'

    if not os.path.isfile(file_path):
        print(file_path)
        print("檔案不存在")
        return None

    # 讀檔，儲存內文
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    lines = []
    line = ''
    for char in content:
        if len(line) < text_width:
            line += char
        elif len(line) >= text_width or char.isspace() or char in ('，', '。', '！', '？', '；', '：', '、'):
            lines.append(line.strip())
            line = char
        else:
            line += char
    if line:
        lines.append(line.strip())

    formatted_text = '\n'.join(lines)

    # print(formatted_text)
    return formatted_text

if __name__ == "__main__":
    text_width = 40
    result = format_text("test3", text_width)
    print(result)
