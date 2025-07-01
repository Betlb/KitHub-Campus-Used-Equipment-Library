# SOFTWARE DESIGN DOCUMENT

## System Overview

The **KitHub system** is a web-based application designed to support temporary borrowing of campus equipment such as lab tools, cameras, and sports gear. It aims to enhance sustainability and reduce costs by allowing students to borrow instead of purchase rarely used equipment.

The selected use case for this assignment is **Borrow Equipment**. This is a core operation in the system and involves:

- Students requesting an item
- The system evaluating the request using predefined borrowing strategies
- The administrator approving or rejecting the request

The use case implements the **Strategy Design Pattern** to dynamically switch between borrowing rules based on user type or equipment category.

---

## System Context

The KitHub system operates as a standalone web application designed for use within a university campus. It interacts primarily with two user types: **students** and **administrators**.

This system does not integrate with any external services or university databases in its MVP version, making it lightweight and easy to deploy. The only system boundaries include internal data validation and access restrictions based on roles.

---

## Actors and Interactions

| Actor        | Interaction Type         | Purpose                                      |
|--------------|--------------------------|----------------------------------------------|
| Student      | Web UI / Borrow Module   | Requests to borrow available items           |
| Administrator| Web UI / Admin Panel     | Approves or denies borrow requests           |
| System       | Internal logic (Strategy Pattern) | Selects borrowing strategy based on context (user or item type) |
| Database     | MySQL (internal)         | Stores borrow records, users, items          |

---

## Context Diagram (Simplified)

- Users interact via browser (client-side).
- Frontend connects to backend controller.
- Backend logic invokes appropriate borrowing strategy.
- Database stores/updates state of requests and items.

![](context-diagram.png)

---

## Key Features and Functionality

---

## Assumptions and Dependencies

### Assumptions

- **User Authentication Is Required**  
  It is assumed that users must be authenticated (i.e., logged in) before they can initiate a borrow request.

- **Only Available Items Can Be Borrowed**  
  The borrow operation only applies to items marked as available. Unavailable or already borrowed items are filtered out automatically.

- **Borrow Strategy Is Selected Based on Item Type or Policy**  
  The appropriate borrow rule strategy (e.g., `MaxDurationStrategy`, `RestrictedAccessStrategy`) is selected at runtime based on the item's category or institutional rules.

- **Admin Approval Is Always Required**  
  Every borrow request goes through a manual approval by an administrator. The system does not automatically grant borrow permissions.

- **Single Borrow per User per Item**  
  A user cannot borrow multiple instances of the same item simultaneously.

- **Time Slots and Conflicts Are Pre-validated**  
  Borrow time inputs from users are assumed to be validated against the existing booking records.

---

### Dependencies

- **Authentication Service**  
  Used to verify user identity and role before processing borrow logic.

- **Inventory Management Module**  
  Supplies item availability data and updates item status post-approval or rejection.

- **Notification System**  
  Sends status updates to both students and admins regarding the borrow request.

- **Borrow Strategy Interface and Implementations**  
  A set of strategy classes define the rules for different borrowing policies (e.g., max borrow length, eligibility, item restrictions).


## Architectural Design

* Outline overall architecture (e.g., client-server, MVC).
* Provide diagrams if needed.

---

## Component Design

* Break system into components/modules.
* Describe responsibilities and interactions.

---

## Data Design

* Outline database schema, data models.
* Mention normalization, relationships, key fields.

---

## Design Patterns

* Strategy Pattern (used for borrow rules).
* List any additional patterns and their roles.

---

## Implementation Notes

* Languages used (e.g., JavaScript, Python).
* Frameworks or constraints to consider.

---

## User Interface Design

* Basic UI structure.
* Key screens: Borrow Page, Admin Panel, Login.

---

## External Interfaces

* None for MVP.
* Future: LDAP, university database, email services.

---

## Performance Considerations

* Handle multiple concurrent borrow requests.
* UI responsiveness, database indexing.

---

## Error Handling and Logging

* Logging failed borrow attempts.
* Invalid inputs, unavailable items.

---

## Design for Testability

* Unit tests for borrow strategy.
* Mock database for testing workflows.

---

## Deployment and Installation Design

* Local deployment instructions.
* Suggested hosting platforms (e.g., Heroku, university server).

---

## Change Log

* v1.0 – Initial version with MVP use case.

---

## Future Work / Open Issues

* Add equipment return functionality.
* Notifications for overdue items.
* Mobile support.
