import csv

titles = ['蘋果', '鳯梨', '芭樂']
price = ['15', '90', '12']

with open('data.csv', 'w', newline='', encoding="utf-8") as fa:
    w = csv.writer(fa)
    w.writerow(['水果項目', '價格'])

    for t, p in zip(titles, price):
        w.writerow([t, p])
