## Phase 1 – General Strategy and Planning

### Selected Use Case: Borrow Equipment

We have chosen the “Borrow Equipment” use case because:

- It represents the core functionality of the KitHub system.
- It involves both student and administrator interactions.
- It contains a relatively complex business flow (request → approval → return).
- It is suitable for demonstrating the **Strategy Design Pattern** selected in Assignment 1.

### Applied Design Pattern: Strategy Pattern

**Why Strategy Pattern?**

The borrowing process can require different logic depending on various factors (e.g., user type, purpose of use, borrowing duration). The Strategy Pattern allows us to:

- Create flexible and interchangeable borrowing policies.
- Modify or extend borrowing rules without changing core logic.
- Improve the modularity, reusability, and testability of the implementation.

### Team Members and Planned Responsibilities

| Member               | Responsibility                                                                 |
|----------------------|----------------------------------------------------------------------------------|
| Aylin Barutçu         | Lead author of the Software Design Document, UML diagrams, documentation integration |
| Mehmet Karatekin      | Design pattern implementation, core borrowing logic, component structure         |
| İlbey Efe Taşabatlı   | GitHub structure setup, testing, logging, deployment coordination                 |
| Betül Biçer           | UI wireframes, data model design, markdown documentation and matrices             |

