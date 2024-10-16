data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}


# TODO здесь писать код
keys = []
values = []

for i_key in data.keys():
    keys.append(i_key)
for i_values in data.values():
    values.append(i_values)

print('Список ключей словаря', keys)
print('Список значений словаря', values)
# В ETH добавить ключ total_diff со значением 100.
print(data['ETH'])
data['ETH']['total_diff'] = 100
print(data['ETH'])
# Внутри fst_token_info значение ключа name поменять с fdf на doge.
print(data['tokens'][0]['fst_token_info']['name'])
data['tokens'][0]['fst_token_info']['name'] = 'doge'
print(data['tokens'][0]['fst_token_info']['name'])
# Удалить total_out из словарей внутри списка tokens и присвоить сумму этих значений в total_out внутри ETH.
print(data['ETH']["total_out"])
print(data['tokens'][0])
print(data['tokens'][1])
data['ETH']["total_out"] = data['tokens'][0].pop('total_out') + data['tokens'][1].pop('total_out')
print(data['ETH']["total_out"])
print(data['tokens'][0])
print(data['tokens'][1])
# Внутри sec_token_info изменить название ключа price на total_price.
print(data['tokens'][1]['sec_token_info'])
data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')
print(data['tokens'][1]['sec_token_info'])
