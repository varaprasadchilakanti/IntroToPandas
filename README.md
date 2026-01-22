# Introduction to Pandas — Problem Solving Principles & Architecture Guidelines

This document defines the foundational principles, design philosophies, and coding standards for solving Pandas problems and building modular, reproducible data workflows. It is intended to guide developers and LLMs toward producing elegant, efficient, and extensible solutions in the context of data analysis.

---

## 1. SOLID Design Principles

- **Single Responsibility**: Each function or class must encapsulate one well-defined data operation (e.g., cleaning, reshaping).  
- **Open/Closed**: Pipelines should be open for extension (adding new transformations) but closed for modification.  
- **Liskov Substitution**: Subtypes or alternative strategies (e.g., different cleaning methods) must be interchangeable without breaking correctness.  
- **Interface Segregation**: Clients should not depend on unused methods; keep APIs minimal and intention-driven.  
- **Dependency Inversion**: High-level workflows must depend on abstract interfaces (e.g., strategy protocols), not concrete implementations.

---

## 2. Clean Architecture

- Separate **data logic** from orchestration, I/O, and configuration.  
- Use **strategy patterns** to isolate transformation variants (e.g., different fill methods for missing data).  
- Keep interfaces **thin**, implementations **swappable**, and dependencies **minimal**.  
- Favor **composition over inheritance** in pipeline design.  

---

## 3. Efficiency & Elegance

- Prioritize **vectorized operations** over loops.  
- Use **intention-revealing names** for columns, transformations, and helper functions.  
- Prefer **method chaining** for readability and reproducibility.  
- Avoid redundant computation and unnecessary memory allocation.  

---

## 4. Extensibility & Testability

- Design solutions that handle **variants and edge cases** gracefully (e.g., missing values, duplicate rows).  
- Avoid hardcoded values; use **configurable parameters** and **dependency injection**.  
- Structure code to support **unit testing**, **benchmarking**, and **debugging**.  
- Ensure transformations are **modular**, **reusable**, and **traceable**.  

---

## 5. Developer Experience

- Treat each Pandas problem as a **mini-system**, not a one-off script.  
- Use **docstrings**, **type hints**, and **comments** to document intent and behavior.  
- Structure files and folders for **discoverability**, **readability**, and **reuse**.  
- Follow **PEP8**, **DRY**, **KISS**, and **YAGNI** principles.  
- Focus on clarity and correctness first; optimize later.  

---

## 6. Code Structure Template

```python
from typing import Protocol, Any
import pandas as pd

class TransformationStrategy(Protocol):
    def apply(self, df: pd.DataFrame) -> pd.DataFrame: ...

class ConcreteTransformation:
    def apply(self, df: pd.DataFrame) -> pd.DataFrame:
        # Core transformation logic here
        return df

class Solution:
    def __init__(self, strategy: TransformationStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else ConcreteTransformation()

    def entry_point(self, df: pd.DataFrame) -> pd.DataFrame:
        return self.strategy.apply(df)
```

---

## 7. Pseudocode Convention

- Use **clear, step-by-step logic** for transformations.  
- Avoid language-specific syntax when describing workflows.  
- Highlight **conditions**, **edge handling**, and **loop invariants** (if any).  
- Reflect the same modularity and clarity as the final code.  

---

## 8. File Naming & Organization

- Use format: `PD<problem_number>_<problem_slug>.py`  
- Organize by topic: `data_structures/`, `inspection/`, `selection/`, `cleaning/`, `reshaping/`, etc.  
- Include `README.md` in each folder with problem summaries and strategy notes.  

#### Example Project Structure

```bash
IntroToPandas/
├── data_structures/
│   ├── PD001_create_dataframe_from_list.py
│   └── README.md
├── inspection/
│   ├── PD002_get_dataframe_size.py
│   ├── PD003_display_first_three_rows.py
│   └── README.md
├── selection/
│   ├── PD004_select_data.py
│   ├── PD005_create_new_column.py
│   └── README.md
├── cleaning/
│   ├── PD006_drop_duplicates.py
│   ├── PD007_drop_missing_data.py
│   ├── PD008_modify_columns.py
│   ├── PD009_rename_columns.py
│   ├── PD010_change_data_type.py
│   ├── PD011_fill_missing_data.py
│   └── README.md
├── reshaping/
│   ├── PD012_concatenate.py
│   ├── PD013_pivot.py
│   ├── PD014_melt.py
│   └── README.md
├── advanced/
│   ├── PD015_method_chaining.py
│   └── README.md
└── README.md
```

---

## 9. Philosophy

We build Pandas workflows that are:

- **Modular**: Each transformation is replaceable and independently testable.  
- **Resilient**: Handles edge cases and messy data gracefully.  
- **Elegant**: Minimal, expressive, and intention-driven.  
- **Extensible**: Designed to evolve without breaking existing behavior.  

---

This document is the grounding reference for all Pandas problem-solving workflows. Any developer or LLM using this guide is expected to produce solutions that are **production-grade**, **architecturally sound**, and **developer-friendly**.  
