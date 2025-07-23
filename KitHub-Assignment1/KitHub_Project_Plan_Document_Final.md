# Project Plan Document

Project Title: KitHub – Campus Used Equipment Library

## 1. Project Scope

Included in the project:
- A web-based platform for borrowing campus equipment.
- User roles: student (borrower) and administrator.
- Borrowing workflow (request → approval → return).
- Inventory display with categories and availability status.
- Notification system for due dates and approvals.

Excluded from the project:
- Physical item tracking (e.g., RFID, QR code).
- Integration with university systems.
- Payment or fine features.

## 2. Project Organization – Roles and Responsibilities

| Team Member         | Role                             | Responsibilities                                                             |
|:--------------------|:---------------------------------|:-----------------------------------------------------------------------------|
| Aylin Barutçu       | Project Coordinator              | Project definition, documentation integration, UI design, team communication |
| Betül Biçer         | Requirements Analyst & Developer | SRS writing, borrow logic implementation, design patterns                    |
| Mehmet Karatekin    | System Architect                 | Architecture diagram, backend design, admin features development             |
| İlbey Efe Taşabatlı |  DevOps & Planner                      | Timeline planning, GitHub management, testing coordination, version control  |

## 3. Project Goals (Implementation and Management)

- Deliver a working MVP before the deadline.
- Ensure that each phase (requirements, design, implementation) is completed on time.
- Maintain version control and task traceability via GitHub.
- Clearly document the process for evaluation and review.

## 4. Key Stages and Timeline

| Stage            | Description                                     | Date(s)              | Deliverables                        |
|:-----------------|:------------------------------------------------|:---------------------|:------------------------------------|
| Initial Delivery | Project documentation and setup                 | June 15 – 25th       | Project Definition & Plan Documents |
| Design           | UI sketches and architecture decisions          | June 25th– July 5th  | Architecture Diagram                |
| Implementation   | Core development of system features             | July 5th– August 5th | MVP version on GitHub               |
| Testing & Final  | User tests, bug fixes, documentation completion | August 5 – 15th      | SRS, Pattern Mapping, Final Upload  |

## 5. Resource Planning

- Development Tools: Visual Studio Code, Git, GitHub
- Languages and Frameworks: HTML/CSS, JavaScript, Python (Backend)
- Database: MySQL

## 6. Risk Management

- Delays due to exams or schedule:
  If time conflicts occur, tasks will be redistributed among available members or the timeline will be slightly adjusted with team consensus.

- Scope creep (uncontrolled expansion of features):
  Team will regularly review the project scope and only include new features after evaluating their necessity and feasibility.

## 7. Communication Plan

- Weekly progress meetings via Zoom
- Daily updates via WhatsApp/Slack group
- GitHub Issues and commit messages for tracking code tasks
- Shared Google Drive for document collaboration

## 8. Change Management Plan

- All major scope or requirement changes will:
  1. Be discussed and agreed upon during team meetings
  2. Be updated in the GitHub README

## 9. Acceptance Tests and Criteria

| Test Scenario                     | Success Criteria                                                        |
|:----------------------------------|:------------------------------------------------------------------------|
| User registration and login       | Users can securely create accounts and log in without errors            |
| Equipment borrow & return process | Borrow requests can be sent, approved, and marked returned correctly    |
| Notifications                     | Users receive timely reminders for return dates and admin approvals     |
| Admin equipment management        | Admin can add, update, or remove inventory items without system crashes |
| Page loading/performance          | All pages load within 2 seconds under standard conditions               |

## 10. Task Matrix for This Document

| Task                          | Description                                                     | Responsible Member   |
|:------------------------------|:----------------------------------------------------------------|:---------------------|
| Draft Structure               | Defined the document outline and core sections                  | İlbey Efe Taşabatlı  |
| Content Writing               | Completed the full text and examples for use cases and planning | Aylin Barutçu        |
| Architecture & Pattern Review | Reviewed architecture alignment and design pattern mapping      | Mehmet Karatekin     |
| Final Review & Submission     | Final proofreading, table formatting, version check | Betül Biçer          |

