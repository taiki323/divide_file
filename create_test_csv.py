import csv

def create_test_csv():
    """
    origin.csvファイルに商品コード（A1からA10000）と入札価格（25）のデータを10000行作成する
    """
    filename = 'origin.csv'
    
    # CSVファイルを書き込みモードで開く
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # ヘッダーを書き込み
        writer.writerow(['商品コード', '入札価格'])
        
        # 10000行のデータを作成
        for i in range(1, 10001):
            product_code = f'A{i}'
            bid_price = 25
            writer.writerow([product_code, bid_price])
    
    print(f'{filename}に10000行のデータを作成しました。')
    print('商品コード: A1 から A10000')
    print('入札価格: 25（固定）')

if __name__ == '__main__':
    create_test_csv()