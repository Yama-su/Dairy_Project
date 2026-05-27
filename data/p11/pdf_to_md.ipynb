## Read.md ###########
複数のpdfファイルをアップロードしておくと、順々に、markdownにしてくれます。
日本語pdfの場合は、ファイル名に「_jp」という文字列を含ませておいてください。
その文字列がなければ、英語と見なされます。
結果は、zipにまとめて出力されます。mdとjpegとjsonが出力されます。
pdfごとにディレクトリ分けされた状態でzipにされますので、混ざる心配はありません。
以上。
#############################


import os
import subprocess
from google.colab import files

# 1. Markerパッケージの最新版をインストール
!pip install marker-pdf

# 2. 複数PDFファイルの一括アップロード
print("PDFファイルをすべて選択してアップロードしてください:")
uploaded = files.upload()
pdf_files = list(uploaded.keys())

output_root = "./combined_outputs"
os.makedirs(output_root, exist_ok=True)

print(f"\n--- 合計 {len(pdf_files)} 個のファイルを順番に処理します ---")

# 3. ファイル名に応じた言語切り替えループ（環境変数版）
for idx, pdf_filename in enumerate(pdf_files, 1):
    folder_name = os.path.splitext(pdf_filename)[0]
    each_output_dir = os.path.join(output_root, folder_name)
    
    # 現在の環境変数をコピー
    current_env = os.environ.copy()
    
    # ファイル名（小文字化）に "ja" が含まれているかチェック
    if "_ja" in pdf_filename.lower():
        # 最新版では環境変数 MARKER_LANGS で言語を指定します
        current_env["MARKER_LANGS"] = "ja"
        mode_text = "【日本語モード】"
    else:
        current_env["MARKER_LANGS"] = "en"
        mode_text = "【英語モード】"
        
    print(f"\n[{idx}/{len(pdf_files)}] {mode_text} 処理中: {pdf_filename} ...")
        
    try:
        # エラーを正しく検知するため、! ではなく subprocess を使用して実行します
        # 最新の引数は [入力ファイル] --output_dir [出力先] のみです
        result = subprocess.run(
            ["marker_single", pdf_filename, "--output_dir", each_output_dir],
            env=current_env,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print(f"-> 成功: {pdf_filename} の変換が完了しました。")
        else:
            print(f"-> エラー: {pdf_filename} の処理中にMarkerがエラーを返しました。")
            print(result.stderr)
            
    except Exception as e:
        print(f"-> エラー: {pdf_filename} の実行中に予期せぬ問題が発生しました: {e}")
        continue

# 4. まとめてZIPダウンロード
print("\n--- すべての処理が終了しました。ダウンロードを準備します ---")
if os.path.exists(output_root) and len(os.listdir(output_root)) > 0:
    if os.path.exists("batch_output.zip"):
        os.remove("batch_output.zip")
    !zip -r batch_output.zip {output_root}
    files.download("batch_output.zip")
    print("batch_output.zip のダウンロードを開始しました。")
else:
    print("変換に成功したファイルがありませんでした。出力フォルダが空です。")
