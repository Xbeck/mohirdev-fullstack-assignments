# Trello database ER diagram

PostgreSQL types; PK = primary key, FK = foreign key, UK = unique. Composite PKs on membership tables prevent duplicate memberships. IDs use generated identity bigint. JSONB template structure is a reusable snapshot, copied into boards/lists/cards when instantiated; later edits do not mutate existing boards.

```mermaid
erDiagram
    members ||--o{ workspaces : owns
    workspaces ||--o{ workspace_members : has
    members ||--o{ workspace_members : joins
    members ||--o{ templates : creates
    workspaces ||--o{ boards : contains
    templates |o--o{ boards : optional_source
    boards ||--o{ board_members : has
    members ||--o{ board_members : joins
    boards ||--o{ lists : contains
    lists ||--o{ cards : contains
    members ||--o{ cards : creates
    cards ||--o{ card_members : assigns
    members ||--o{ card_members : assigned
    cards ||--o{ comments : has
    members ||--o{ comments : writes
    cards ||--o{ checklists : has
    checklists ||--o{ checklist_items : contains
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

## Relations and integrity
- Workspace owner → members.id. Workspace membership and board membership use join tables with role CHECK (`owner`, `admin`, `member`, `observer` as appropriate).
- Board belongs to one workspace; optional template_id uses ON DELETE SET NULL. Membership in a board must also be permitted by its workspace; enforce this in the service transaction or a database trigger.
- List belongs to board. Card belongs to list, so board/workspace are derived without redundant foreign keys. `position` controls ordering; reorder in a transaction.
- Members may be assigned to many cards. Card assignees must be board members; service/trigger validates this. Comments reference author and card.
- Checklists and checklist items belong to cards through their parents.
- ON DELETE CASCADE for contained lists/cards/comments/checklists/memberships. RESTRICT deletion of workspace owner; transfer ownership first. Soft-delete members when attribution must remain.
- Add created_at/updated_at timestamps to mutable entities. Index all FK columns, cards(due_at), lists(board_id,position), cards(list_id,position), comments(card_id,created_at).
- email is normalized to lowercase before unique validation; role/visibility values are checked. Visibility is private/workspace/public.

Required domains: Workspaces, Boards, Members, Cards, Lists and Templates are all included. diagram.svg is a standalone visual; README Mermaid shows the exact FK relationship graph.
