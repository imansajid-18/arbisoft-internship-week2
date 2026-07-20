# prompts.md

## 1. Learning Requirements
When I ask what I need to learn for a task, clearly separate the response into:
- Required concepts
- Nice-to-know concepts
- Optional/Advanced concepts

Only recommend concepts that are necessary for completing the task. Avoid suggesting advanced topics unless they are directly required.

---

## 2. Concept Explanations
Whenever introducing a new concept, explain it in the following order:
1. What it is
2. Why it is useds
3. When it is used
4. A simple example
5. A real-world use case

Use beginner-friendly language and avoid unnecessary jargon.

---

## 3. Debugging
When helping debug code, always explain:
- Why the error occurred
- The root cause
- How to fix it
- How to avoid the issue in the future

Explain the reasoning instead of only providing the corrected code.

---

## 4. YouTube Recommendations
When I ask for YouTube resources:
- Recommend the most beginner-friendly videos or channels.
- Explain why each recommendation is suitable.
- Prefer complete tutorials over short clips.
- Mention whether the content is in English or Hindi/Urdu.

---

## 5. HTTP Fundamentals
When explaining HTTP fundamentals, cover:
- HTTP methods (GET, POST, PUT, PATCH, DELETE)
- HTTP status codes
- HTTP headers
- Request/Response cycle

Explain each topic with practical examples.

---

## 6. REST APIs
When explaining REST APIs, cover:
- What REST is
- Resources
- Endpoints
- HTTP verbs
- CRUD operations
- Idempotency
- Status code conventions
- Best practices

Include simple examples for every concept.

---

## 7. Learning Resources
Suggest the best beginner-friendly YouTube channels for software development topics, especially:
- Python
- Django
- Django REST Framework
- JavaScript
- React
- Git & GitHub
- Unit Testing

Explain why each channel is recommended.

---

## 8. Ruff Linter
Explain:
- What Ruff is
- Why Ruff is used in Python and Django projects
- What problems Ruff detects
- How Ruff differs from other linters

Also provide the exact terminal commands to:
- Install Ruff
- Scan the project
- Check formatting issues
- Check coding style
- Detect unused imports
- Auto-fix issues (if applicable)

Explain what each command does.

---

## 9. Django Serializer Validation
When I ask about Django serializer validation issues, especially custom validation methods such as `validate_title()` or `validate_description()`, help identify common mistakes including:
- Incorrect Python indentation
- Incorrect method naming
- Methods placed outside the serializer class
- Incorrect serializer inheritance
- Missing serializer usage in views
- Validation methods not being called
- Any other common reasons why DRF bypasses validation

Explain how to verify that validation is actually executing.

---

## 10. Django Unit Testing
When discussing unit testing for a small single-model Django CRUD application:
- Recommend the simplest approach first.
- Clearly distinguish between required and advanced testing concepts.
- Explain whether tools like `factory_boy`, `mixer`, raw JSON fixtures, mocks, or other advanced testing libraries are actually necessary.
- Prefer examples using Django's built-in `TestCase`, `setUp()`, Django ORM, and the Django test client unless the task specifically requires more advanced tools.

Always recommend the simplest solution that satisfies the assignment requirements.