import csv
import json


def convert(csv_file, json_file, model):
    with open(csv_file, encoding='utf-8') as csv_f:
        result = []
        for row in csv.DictReader(csv_f):
            record = {"model": model, "pk":row["id"]}
            del row["id"]

            if "price" in row:
                row["price"] = int(row["price"])

            if "is_published" in row:
                if row["is_published"] == "True":
                    row["is_published"] = True
                else:
                    row["is_published"] = False

            record["fields"] = row
            result.append(record)

    with open(json_file, 'w', encoding='utf-8') as json_f:
        json_f.write(json.dumps(result, ensure_ascii=False))


convert('categories.csv', 'categories.json', 'ads.category')
convert('ads.csv', 'ads.json', 'ads.ad')