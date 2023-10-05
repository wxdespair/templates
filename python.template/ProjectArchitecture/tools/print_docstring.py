import os
import ast

""" 打印指定路径中所有py文件中函数的文档 """

def extract_docstrings_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    tree = ast.parse(content)
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            docstring = ast.get_docstring(node)
            if docstring:
                print(f"在文件 {file_path} 中，{node.name} 的docstring是：")
                print(docstring)
                print('-' * 50)

def find_py_files_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                extract_docstrings_from_file(os.path.join(root, file))

if __name__ == "__main__":
    directory = '.'  # 当前目录
    find_py_files_in_directory(directory)
