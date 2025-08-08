import csv
import os

def divide_csv_file(input_file='origin.csv', records_per_file=1000):
    """
    CSVファイルを指定された件数ずつ分割して複数のファイルに出力する
    
    Args:
        input_file (str): 分割元のCSVファイル名
        records_per_file (int): 1ファイルあたりのレコード数
    """
    if not os.path.exists(input_file):
        print(f"エラー: {input_file} が見つかりません。")
        return
    
    file_count = 1
    record_count = 0
    output_file = None
    writer = None
    
    try:
        with open(input_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)  # ヘッダー行を読み取り
            
            print(f"ヘッダー: {header}")
            print(f"{input_file}を{records_per_file}件ずつ分割しています...")
            
            for row in reader:
                # 新しいファイルを開始する必要がある場合
                if record_count == 0:
                    if output_file:
                        output_file.close()
                    
                    output_filename = f"{file_count}.csv"
                    output_file = open(output_filename, 'w', newline='', encoding='utf-8')
                    writer = csv.writer(output_file)
                    writer.writerow(header)  # ヘッダーを書き込み
                    print(f"  {output_filename} を作成中...")
                
                # データ行を書き込み
                writer.writerow(row)
                record_count += 1
                
                # 指定件数に達した場合、次のファイルへ
                if record_count >= records_per_file:
                    output_file.close()
                    print(f"  {file_count}.csv 完了 ({records_per_file}件)")
                    file_count += 1
                    record_count = 0
                    output_file = None
        
        # 最後のファイルがまだ開いている場合は閉じる
        if output_file:
            output_file.close()
            print(f"  {file_count}.csv 完了 ({record_count}件)")
        
        print(f"\n分割完了: {file_count}個のファイルを作成しました")
        
    except FileNotFoundError:
        print(f"エラー: {input_file} が見つかりません。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        if output_file:
            output_file.close()

if __name__ == '__main__':
    divide_csv_file()