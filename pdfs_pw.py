import os
import glob
from PyPDF2 import PdfReader, PdfWriter
# フォルダのパスを取得
folderpath = input("PDFファイルが格納されているフォルダのパスを入力してください: ")
# パスワードを入力
password = input("暗号化に使用するパスワードを入力してください: ")
# ファイルの一覧を取得する
files = glob.glob(os.path.join(folderpath, "*.pdf"))
print(files)
# ファイルごとに処理する
for file in files:
    # PDFを読み込む
    reader = PdfReader(file) 
    # 新しいPDFを作成する
    writer = PdfWriter()
    # 既存ファイルからページを取り込む
    for page in reader.pages:
        writer.add_page(page)
    # パスワードでファイルを暗号化
    writer.encrypt(password)
    # 暗号化したPDFを保存する
    filename = os.path.basename(file)
    filename_without_extension = os.path.splitext(filename)[0]
    outpath = os.path.join(folderpath, f"ecpt_{filename_without_extension}.pdf")
    with open(outpath, "wb") as f:
        writer.write(f)
    print("ファイルを暗号化しました: " + outpath)
print("処理終了")