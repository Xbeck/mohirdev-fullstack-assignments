# Trello ma’lumotlar bazasi

Bu chizma Trello kabi vazifalar boshqariladigan dastur uchun tuzilgan. Unda 12 ta jadval bor.

## Asosiy jadvallar

- `members` — foydalanuvchilar.
- `workspaces` — jamoaning ish joylari.
- `boards` — loyiha doskalari.
- `lists` — doskadagi bo‘limlar, masalan “Bajarish kerak” va “Tayyor”.
- `cards` — vazifalar.
- `templates` — yangi doska uchun tayyor namunalar.
- Qolgan jadvallar a’zolar, izohlar va vazifa ichidagi ro‘yxatlarni saqlaydi.

## Belgilar

- `PK` — yozuvning asosiy raqami.
- `FK` — boshqa jadvaldagi yozuvga bog‘lanish.
- `UK` — takrorlanmaydigan qiymat.
- `bigint` — butun son, `varchar` va `text` — matn.
- `boolean` — ha yoki yo‘q, `numeric` — son.
- `timestamptz` — sana va vaqt, `jsonb` — tuzilgan ma’lumot.

## Chizma

```mermaid
erDiagram
    members ||--o{ workspaces : egasi
    workspaces ||--o{ workspace_members : bor
    members ||--o{ workspace_members : azo
    members ||--o{ templates : yaratadi
    workspaces ||--o{ boards : ichida
    templates |o--o{ boards : namuna
    boards ||--o{ board_members : bor
    members ||--o{ board_members : azo
    boards ||--o{ lists : ichida
    lists ||--o{ cards : ichida
    members ||--o{ cards : yaratadi
    cards ||--o{ card_members : biriktiriladi
    members ||--o{ card_members : bajaradi
    cards ||--o{ comments : bor
    members ||--o{ comments : yozadi
    cards ||--o{ checklists : bor
    checklists ||--o{ checklist_items : ichida
    members {
        bigint id PK
        varchar name
        varchar email UK
        text password_hash
    }
    workspaces {
        bigint id PK
        bigint owner_id FK
        varchar name
        text description
    }
    workspace_members {
        bigint workspace_id PK,FK
        bigint member_id PK,FK
        varchar role
    }
    templates {
        bigint id PK
        bigint creator_id FK
        varchar name
        text description
        jsonb structure
    }
    boards {
        bigint id PK
        bigint workspace_id FK
        bigint template_id FK
        varchar title
        varchar visibility
        boolean archived
    }
    board_members {
        bigint board_id PK,FK
        bigint member_id PK,FK
        varchar role
    }
    lists {
        bigint id PK
        bigint board_id FK
        varchar title
        numeric position
        boolean archived
    }
    cards {
        bigint id PK
        bigint list_id FK
        bigint creator_id FK
        varchar title
        text description
        numeric position
        timestamptz due_at
        boolean archived
    }
    card_members {
        bigint card_id PK,FK
        bigint member_id PK,FK
    }
    comments {
        bigint id PK
        bigint card_id FK
        bigint author_id FK
        text body
        timestamptz created_at
    }
    checklists {
        bigint id PK
        bigint card_id FK
        varchar title
    }
    checklist_items {
        bigint id PK
        bigint checklist_id FK
        varchar text
        boolean completed
        numeric position
    }

```

## Bog‘lanishlar qanday ishlaydi?

Ish joyida bir nechta doska, doskada bir nechta bo‘lim, bo‘limda esa bir nechta vazifa bo‘ladi. Har bir vazifaga a’zolar, izohlar va bajariladigan ishlar ro‘yxati qo‘shiladi.

`workspace_members`, `board_members` va `card_members` jadvallari foydalanuvchini tegishli ish joyi, doska yoki vazifaga bog‘laydi. Ularning ikki ustuni birgalikda asosiy kalit bo‘ladi. Shu sabab bir a’zo ikki marta yozilmaydi.

Doska tayyor namunadan yaratilishi mumkin, lekin bu majburiy emas. Namuna o‘zgarsa, avval yaratilgan doska o‘zgarmaydi. `position` maydoni bo‘lim va vazifalar tartibini saqlaydi.

Doska a’zosi ish joyiga ham kirish huquqiga ega bo‘lishi kerak. Vazifaga faqat shu doska a’zosi biriktiriladi. Bular dasturda yoki baza qoidalari orqali tekshiriladi.

Email kichik harflarda saqlanadi va takrorlanmaydi. Ish joyi egasini o‘chirishdan oldin egalik boshqa a’zoga o‘tkaziladi. Ichki yozuvlar uchun o‘chirish qoidalari belgilanadi; muallif haqidagi ma’lumotni saqlash kerak bo‘lsa, foydalanuvchi faqat faol emas deb belgilanadi.

Tez qidirish uchun bog‘lanish ustunlariga indeks qo‘shiladi. Yaratilgan va o‘zgartirilgan vaqtlarni ham saqlash tavsiya etiladi.

Chizmaning alohida nusxasi `diagram.svg`, Mermaid matni esa `diagram.mmd` faylida.
