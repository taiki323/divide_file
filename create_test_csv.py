import csv

def create_test_csv():
    filename = 'origin.csv'
    num_records = 600000  # データ行数を変数として定義
    
    # CSVファイルを書き込みモードで開く
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # ヘッダーを書き込み
        writer.writerow(['商品コード', '入札価格'])
        
        # データを作成
        for i in range(1, num_records + 1):
            product_code = f'A{i}'
            bid_price = 25
            writer.writerow([product_code, bid_price])
    
    print(f'{filename}に{num_records}行のデータを作成しました。')
    print(f'商品コード: A1 から A{num_records}')
    print('入札価格: 25（固定）')

if __name__ == '__main__':
    create_test_csv()