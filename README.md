# Python Fullstack — amaliy loyihalar

Har bir ZIP ichida alohida loyiha, README va kerakli kodlar mavjud. ZIP faylini ochib **Download raw file** orqali yuklab oling, arxivdan chiqaring va ichidagi README bo‘yicha ishga tushiring.

| Topshiriq | Loyiha |
|---|---|
| Bootstrap: Basic, Forms, Tables | [bootstrap.zip](bootstrap.zip) |
| Trello ma’lumotlar bazasi | [ER diagram](TRELLO_ERD.md), [SVG](diagram.svg), [trello.zip](trello.zip) |
| Contact Form va /xabarlar | [contact_form.zip](contact_form.zip) |
| Omborxona FIFO API | [warehouse.zip](warehouse.zip) — namuna SQLite bazasi bilan |
| Django blog | [blog.zip](blog.zip) |
| FastAPI qarz monitoringi | [debt_api.zip](debt_api.zip) |

Kodlar brauzerda tekshirish uchun [SOURCE_FILES.json](SOURCE_FILES.json) ichida ham to‘liq mavjud. `python extract_sources.py` ularni `source/` ichiga alohida fayllar qilib chiqaradi (Python standart kutubxonasi, tashqi bog‘liqliksiz). Warehouse namunaviy bazasi ZIP ichida; manba orqali ishga tushirganda `python manage.py seed` bilan yaratiladi.

## Tekshirish
- Contact Form: 2 Django test — saqlash, redirect, validatsiya, CSRF va HTML escape.
- Omborxona: 2 Django test — umumiy zaxira, yetishmovchilik, DB o‘zgarmasligi, xato so‘rovlar.
- Blog: 2 Django test — moderatsiya, izoh, auth, ko‘rishlar va saralash sahifalari.
- Qarz API: 3 unittest — auth/settings, CRUD/filter/monitoring, foydalanuvchilar izolyatsiyasi/validatsiya. SQLite test muhiti; PostgreSQL integratsiyasi bu kompyuterda ishga tushirilmagan. PostgreSQL sozlamasi va Docker Compose berilgan.

Bu o‘quv loyihalari AI yordamida tayyorlangan. Lokal demo sozlamalari ishlatilgan; haqiqiy shaxsiy ma’lumotlar kiritilmagan. Ishlab chiqarish muhiti uchun har bir README dagi sozlash talablarini bajaring.
