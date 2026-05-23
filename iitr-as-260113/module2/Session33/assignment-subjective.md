# Subjective Assignment — Tool Integration in AI Agents

**Total Questions:** 1 | **Practical Coding Task** | **Difficulty: Medium**

---

## Q1. Build a GadgetMart Product Search Tool

You are on the backend team at **GadgetMart**, an online electronics store. The AI shopping assistant must call a registered `search_product` tool instead of inventing prices from memory. Implement the tool in a single file, `gadgetmart_search_tool.py`, using **Pydantic** and **SQLAlchemy** (`pip install pydantic sqlalchemy` in your virtual environment).

### Your Task

**Task 1 — Catalog setup**  
Define the SQLAlchemy `Base` and `Product` ORM (`products`: `id`, `name`, `category`, `price`, `in_stock`). Connect to `sqlite:///gadgetmart.db`, create tables, and add a `SessionLocal` factory. Implement `insert_data()` to seed the six mobiles below **only when the table is empty** (no duplicate rows on re-run):

| name | category | price | in_stock |
|------|----------|-------|----------|
| iPhone 15 | mobile | 79900 | True |
| Samsung Galaxy S24 | mobile | 74999 | True |
| OnePlus 12R | mobile | 42999 | True |
| Google Pixel 8 | mobile | 54999 | False |
| Redmi Note 13 | mobile | 18999 | True |
| Motorola Edge 40 | mobile | 29999 | True |

**Task 2 — Validated search tool**  
Define `ProductSearchInput` (`category`: required non-empty `str`; `max_price`: required `int` > 0; `in_stock`: optional `bool`, default `True`). Implement `search_product(input_data: dict)` to validate with `try/except ValidationError`, return `{"success": False, "error": "Invalid input provided", "details": err.errors()}` on failure **without** querying the database, and on success run `select(Product).where(...)` on `category`, `price <= max_price`, and `in_stock`, returning `{"success": True, "products": [{"name": p.name, "price": p.price}, ...]}`.

**Task 3 — Simulated agent run**  
Implement `agent_flow()` with one hard-coded call to `search_product` using `category: "mobile"`, `max_price: 50000`, `in_stock: True`. Print each match as `Name — ₹<price>`; on failure print `Search failed:` plus the `error` string. In `if __name__ == "__main__":`, call `insert_data()` then `agent_flow()`.

### Expected Output (fresh empty database)

```
OnePlus 12R — ₹42999
Redmi Note 13 — ₹18999
Motorola Edge 40 — ₹29999
```

Line order may follow database order; each name and price must appear once. Invalid input such as `{"category": 1234, "max_price": 50000}` must yield `success: False` without a database query.

---

### Submission Instructions

- Code all tasks in VS Code in a single file called `gadgetmart_search_tool.py`
- Run the code and verify the output matches the expected result
- Then submit the code in the code editor / answer box in the LMS

---

### Answer Explanation

**Ideal Solution:**

```python
from pydantic import BaseModel, Field, ValidationError
from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, sessionmaker
from typing import Optional

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    category: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
    in_stock: Mapped[bool] = mapped_column()


engine = create_engine("sqlite:///gadgetmart.db", echo=False)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

SAMPLE_PRODUCTS = [
    {"name": "iPhone 15", "category": "mobile", "price": 79900, "in_stock": True},
    {"name": "Samsung Galaxy S24", "category": "mobile", "price": 74999, "in_stock": True},
    {"name": "OnePlus 12R", "category": "mobile", "price": 42999, "in_stock": True},
    {"name": "Google Pixel 8", "category": "mobile", "price": 54999, "in_stock": False},
    {"name": "Redmi Note 13", "category": "mobile", "price": 18999, "in_stock": True},
    {"name": "Motorola Edge 40", "category": "mobile", "price": 29999, "in_stock": True},
]


class ProductSearchInput(BaseModel):
    category: str = Field(..., min_length=1)
    max_price: int = Field(..., gt=0)
    in_stock: Optional[bool] = True


def insert_data() -> None:
    with SessionLocal() as session:
        if session.scalar(select(func.count()).select_from(Product)) > 0:
            return
        session.add_all([Product(**row) for row in SAMPLE_PRODUCTS])
        session.commit()


def search_product(input_data: dict):
    try:
        validated = ProductSearchInput(**input_data)
    except ValidationError as err:
        return {
            "success": False,
            "error": "Invalid input provided",
            "details": err.errors(),
        }

    with SessionLocal() as session:
        query = select(Product).where(
            Product.category == validated.category,
            Product.price <= validated.max_price,
            Product.in_stock == validated.in_stock,
        )
        products = session.scalars(query).all()
        return {
            "success": True,
            "products": [{"name": p.name, "price": p.price} for p in products],
        }


def agent_flow() -> None:
    tool_calls = [
        {
            "tool_name": "search_product_tool",
            "arguments": {
                "category": "mobile",
                "max_price": 50000,
                "in_stock": True,
            },
        }
    ]

    for tool_call in tool_calls:
        result = search_product(tool_call["arguments"])
        if result.get("success"):
            for item in result["products"]:
                print(f"{item['name']} — ₹{item['price']}")
        else:
            print("Search failed:", result.get("error"))


if __name__ == "__main__":
    insert_data()
    agent_flow()
```

**Walkthrough:** Task 1 maps `Product` and seeds only when the table is empty. Task 2 validates before any read and filters in-stock mobiles at or under the price cap (three matches at ₹50,000). Task 3 hard-codes one tool call and prints customer-friendly lines; production code would fill `tool_calls` from LLM routing.

**Alternative approach:** `session.query(Product).filter(...)` is acceptable on older SQLAlchemy styles if validation, filters, and printed output match the specification.
