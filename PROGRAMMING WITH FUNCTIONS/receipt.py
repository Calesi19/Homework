import csv

def main():
    ITEM_KEY = 0
    ITEM = 1
    ITEM_PRICE = 2

    products = read_products("products.csv", ITEM_KEY)
    print('\nProducts')
    for key in products:
        print(f'{key} {products[key]}')

    print('\nRequested Items')
    process_request('request.csv', products)
    


def read_products(filename, key_column_index):
   
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = [row[1],row[2]]
    return dictionary

def process_request(filename, products):
    
    
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            if row[0] in products:
                print(f'{products[row[0]][0]}: {row[1]} @ {products[row[0]][1]} ')#  @{float(products[row[1]])}')


if __name__ == "__main__":
    main()


