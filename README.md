# Python Fullstack loyihalari

Bu yerda kurs uchun tayyorlangan oltita o‘quv loyihasi bor.

| Loyiha | Fayl |
|---|---|
| Bootstrap sahifalari | [bootstrap.zip](bootstrap.zip) |
| Trello bazasi chizmasi | [Chizmani ko‘rish](TRELLO_ERD.md) · [trello.zip](trello.zip) |
| Xabar yuborish formasi | [contact_form.zip](contact_form.zip) |
| Omborxona hisobi | [warehouse.zip](warehouse.zip) |
| Django blog | [blog.zip](blog.zip) |
| Qarzlarni hisoblash | [debt_api.zip](debt_api.zip) |

## Qanday ochiladi?

1. Kerakli ZIP faylini oching.
2. `Download raw file` tugmasi orqali yuklab oling.
3. Arxivni oching.
4. Ichidagi `README.md` yo‘riqnomasiga amal qiling.

Har bir loyihaning ishga tushirish tartibi o‘z README faylida yozilgan.

## Kodlarni ko‘rish

Barcha matnli kodlar [SOURCE_FILES.json](SOURCE_FILES.json) faylida ham bor. Ularni alohida fayllarga ajratish uchun shu fayl va [extract_sources.py](extract_sources.py) ni bitta papkaga yuklab oling. Keyin bajaring:

```sh
python extract_sources.py
```

Kodlar `source` papkasiga chiqadi. Omborxonaning namuna bazasi ZIP ichida bor; koddan boshlansa, `python manage.py seed` bilan yaratiladi.

## Tekshirish natijasi

Contact Form, omborxona va blogda ikkitadan, qarzlar loyihasida uchta test o‘tgan. Bootstrap sahifalari brauzerda tekshirilgan. Qarzlar loyihasining PostgreSQL bilan alohida tekshiruvi bajarilmagan.

Loyihalar AI yordamida tayyorlangan. Ular o‘rganish va kompyuterda sinab ko‘rish uchun mo‘ljallangan.
