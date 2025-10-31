
# Assignment #8: Contact Management System (Hash Table)

**Course:** Data Structures (Week 9)  
**Languages/Topics:** Python, OOP, Algorithmic Problem Solving

This repository implements a custom **hash table** (no built-in `dict`) to store and retrieve contacts (name → phone number) with **separate chaining** for collision handling.

---

## Files

- `hash_table.py` — Contact, Node, and HashTable classes with:
  - `insert(name, number)` — add/update contact
  - `search(name)` — return `Contact` or `None`
  - `delete(name)` — remove by key
  - `print_table()` — debug view of buckets
  - simple **resize** when load factor > 0.75
  - a `__main__` section showing example usage
- `DESIGN_MEMO.txt` — 200–300 word design memo addressing data structure choice, collisions, and tradeoffs.

---

## Run Locally

```bash
python hash_table.py
```

Expected console output (your bucket indices may differ depending on hash function and table size):

```
Index 0: Empty
Index 1: Empty
...
-- Inserting --
...
-- Search --
Search result: John: 909-876-1234
...
-- Collisions / Updates --
...
-- Update duplicate key (Rebecca) --
...
-- Search missing (Chris) --
None
-- Delete John --
...
All contacts:
 * Rebecca: 999-444-9999
 * Amy: 111-222-3333
 * May: 222-333-1111
```

---

## How It Works

- **Hash function:** djb2-style string hash → `index = hash % size`
- **Buckets:** Array of singly linked lists (`Node`) for **separate chaining**
- **Updates:** Reinserts with same name update that contact’s phone number
- **Delete:** Removes node from chain
- **Resize:** Doubles capacity when `count/size > 0.75` and rehashes

---

## Submit

Push this repo to GitHub and submit the repository link on Canvas:

- Contains `hash_table.py`
- Contains `DESIGN_MEMO.txt` (or memo comment at the bottom of the `.py` file)
