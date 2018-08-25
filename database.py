import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='food_bank',
                              use_pure=False)

curA = cnx.cursor(buffered=True)

query = ("SELECT * FROM foods WHERE f_ID=%s AND price=%s")
curA.execute(query,(54, 555))

for i in curA:
    print(i[3])


# for i in curA:
#     print(i)


update_price_query = ("UPDATE foods SET price = %s WHERE foods.f_ID = %s")

curA.execute(update_price_query, (555,54))


# curB.execute(query,(54))

# for (price) in curB:
#     print(price)

cnx.commit()



cnx.close()