platos = ['Rawon :: SURABAYA, INDONESIA', 'Tonkotsu ramen :: FUKUOKA, JAPAN', 'Mercimek çorbası :: TURKIYE', 'Tom kha gai :: NORTHERN THAILAND, THAILAND', 'Sopa de lima :: YUCATÁN, MEXICO', 'Taiwanese Hot Pot :: TAIWAN', 'Ciorba Radauteana :: RĂDĂUȚI, ROMANIA', 'Bori-bori :: PARAGUAY', 'Ramen :: JAPAN', 'Shoyu ramen :: TOKYO, JAPAN', 'Żurek :: POLAND and one more region', 'Salmon Soup (Lohikeitto) :: FINLAND', 'Húsleves :: HUNGARY', 'Northern Vietnamese Beef Pho (Phở bò tái chín) :: NORTHERN VIETNAM, VIETNAM', 'Miso ramen :: SAPPORO, JAPAN', 'Tom yum :: THAILAND', 'Pozole :: MEXICO', 'Gulyás :: HUNGARY', 'Shio ramen :: HAKODATE, JAPAN', 'Rosół :: POLAND', 'Hakata ramen :: FUKUOKA, JAPAN', 'Beef Noodle Soup :: TAIWAN', 'Beef Pho (Phở bò) :: VIETNAM', 'Pasulj :: SERBIA', 'Kapustnica :: SLOVAKIA', 'Česnečka :: CZECH REPUBLIC', 'Encebollado :: ECUADOR', 'Zelňačka :: CZECH REPUBLIC', 'Youvarlakia :: GREECE', 'Cullen Skink :: CULLEN, SCOTLAND', 'Lablabi :: TUNISIA', 'Kalakeitto :: FINLAND', 'Vietnamese Sweet and Sour Soup (Canh chua cá) :: VIETNAM', 'Ciorbă de fasole cu afumătură :: ROMANIA', 'Sopa Tarasca :: MICHOACÁN, MEXICO', 'Chorba beïda :: ALGERIA', 'Pho :: VIETNAM', 'Laksa :: MALAYSIA and 2 more regions', 'Soupe à l’oignon :: FRANCE', 'Šaltibarščiai :: LITHUANIA', 'Tarator :: BULGARIA and one more region', 'Curry Mee :: MALAYSIA and one more region', 'Sopa de tortilla :: MEXICO', 'Sinigang :: PHILIPPINES', 'Bulalô :: CALABARZON, PHILIPPINES', 'Ciorbă de fasole :: ROMANIA', 'Kharcho :: SAMEGRELO-UPPER SVANETI, GEORGIA', 'Kwaśnica :: ŻYWIEC, POLAND', 'Caldo de queso :: SONORA, MEXICO', 'Chupe de camarones :: AREQUIPA, PERU']


pais = input('Ingrese el nombre del pais: ').upper()

counter = 0
for plato in platos:
    if pais in plato:
        counter += 1
    
print(counter)


