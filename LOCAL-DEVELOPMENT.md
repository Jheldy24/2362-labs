# Student lab workflow

Use two repositories: your private course repository contains your assessed work, while the public Apex Facilities Platform repository contains the database migrations and synthetic seed data. Never put passwords, database dumps, grades, or another student's work in either repository.

## One-time setup

1. Install Git, Python, VS Code, PostgreSQL 17, and the PostGIS bundle from Stack Builder.
2. Clone the public Apex Facilities Platform and your private course repository into separate folders.
3. In the public platform folder, run:

   `scripts\setup_student.ps1 -CourseName "Geographic Information Systems" -CourseAppPath "C:\path\to\your-private-course-repository"`

4. In the private course repository, create `.venv`, install `requirements.txt`, and run `streamlit run streamlit_app.py`.
5. Confirm **Connection & workspace** passes. The setup builds and loads the local database; students do not download or submit a database dump.

## Every lab

1. Run `python tools/prepare_lab.py --lab N`.
2. Develop the existing `labs/lab_NN.py` page and any supporting notebook/code.
3. Store reproducible workspace changes in `workspace_sql/lab_NN.sql`; shared Apex schemas remain read-only.
4. Complete the evidence templates. Test normal, empty, invalid-input, and clean-run behaviour.
5. Commit and push Part A before starting Part B. Do not rewrite the Part A commit.
6. Extend the work for Part B and update the change record.
7. Commit and push Part B.
8. Run `python tools/build_submission.py --lab N --part A` or `--part B` and upload the resulting clean ZIP to the matching D2L assignment.

Git is the development history. D2L is the official grading, feedback, and submission record.
## VS Code

Use the repository's `.venv` interpreter. The recommended Python and Jupyter extensions support scripts and notebooks; no paid extension is required.

## Approved alternatives

If the instructor explicitly supplies a managed remote database, retain `sslmode = "verify-full"` and hostname verification. Use the assigned hostname, not a raw IP address. Do not weaken TLS or accept an untrusted certificate. DBeaver Community is sufficient; no paid edition is required. A course-approved CSV/Parquet fallback may be used when the learning outcome does not require live database writes; record the source and never imply that a snapshot proves database permissions or persistence.