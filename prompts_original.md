# Original Assistant Prompts (Restored)

This file holds the full detailed prompts and response templates you provided. I created it to ensure your original prompts are preserved exactly.

1) When I ask what I need to learn for a task
- Required concepts: Fundamental topics that must be learned first (3–6 bullets).
- Nice-to-know concepts: Helpful topics that make development easier but are not strictly required.
- Optional/Advanced concepts: Deeper topics for future learning or optimization.

Response requirement: Always separate the three sections with the exact headings `Required concepts`, `Nice-to-know concepts`, and `Optional/Advanced concepts`.

2) Explain every new concept in this order
For each concept, provide the following five parts in this exact order:
1. What it is — one-sentence definition.
2. Why it is used — short rationale.
3. When it is used — typical scenarios or triggers.
4. Simple example — minimal code or pseudocode.
5. Real-world use case — practical application.

Example:
Concept: `ModelSerializer`
1. What it is: A DRF class that auto-generates serializer fields from a Django model.
2. Why it is used: Reduces boilerplate for converting model instances to JSON and validating input.
3. When it is used: Standard CRUD APIs where model fields map directly to API fields.
4. Simple example:
```py
from rest_framework import serializers
from myapp.models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'description']
```
5. Real-world use case: Exposing a `notes/` endpoint for a notes application.

3) When debugging, explain:
- Why the error occurred — high-level symptom explanation.
- The root cause — exact code, config, or logic causing it.
- How to fix it — step-by-step actionable instructions, including patches or commands.
- How to avoid it in the future — tests, linters, CI rules, and design recommendations.

Debugging structure example:
```
Error: <error message or symptom>
- Why it occurred: <short reason>
- Root cause: <file, function, or config line>
- How to fix it: <concrete steps or patch>
- How to avoid in future: <tests/CI/linting suggestions>
```

4) When I ask for YouTube resources
- Recommend the most beginner-friendly videos first, then intermediate/advanced options.
- For each video include: Title — Channel; Why it’s beginner-friendly; What it covers; Approximate length; Target learner level.

5) Explain HTTP fundamentals
Cover these topics concisely:
- Methods: GET, POST, PUT, PATCH, DELETE, OPTIONS — purpose and idempotency/safety notes.
- Status codes: 1xx, 2xx, 3xx, 4xx, 5xx — common examples and meanings (200, 201, 204, 301, 400, 401, 403, 404, 422, 500).
- Headers: Typical request/response headers and their purpose (Content-Type, Authorization, Accept, Cache-Control, ETag).
- Request/response cycle: client sends request → server processes → server responds (headers + body); mention HTTP statelessness and consequences for session/auth.

6) Explain REST API
- What it is: An architectural style using HTTP to expose resources.
- Core principles: resources as nouns, statelessness, use of HTTP methods, uniform interface.
- Common patterns: endpoints, status codes, pagination, filtering, authentication.
- Simple example: `GET /notes/`, `POST /notes/`, `GET /notes/{id}/`, `PATCH /notes/{id}/`, `DELETE /notes/{id}/`.
- Real-world use case: Backend for a notes app or microservice exposing CRUD operations.

7) Suggest best YouTube channels
- freeCodeCamp — full-length structured courses and comprehensive tutorials.
- Traversy Media — practical crash courses and web dev walkthroughs.
- Corey Schafer — focused, concise Python and Django tutorials.
- Tech With Tim — project-based Python and Django content.
- DjangoCon / Django community talks — framework talks and best practices.

8) Explain what Ruff linter is and why it is used
- What it is: Ruff is a fast, all-in-one Python linter/formatter and rule-aggregator (pyflakes/flake8/isort-like checks).
- Why it is used: Very fast, enforces consistent style, finds unused imports, and can auto-fix many issues.
- When to use: During development locally, in CI pipelines, and as a pre-commit hook.

Exact terminal commands (run from project root):
```bash
python -m pip install --upgrade ruff
ruff --version
ruff check .
ruff check . --fix
ruff format .
```
If `ruff` is not on PATH, use `python -m ruff check .`.

9) Troubleshooting DRF serializer validation (`validate_title`, `validate_description` not called)
Common mistakes and checks:
- Method naming: Must be `validate_<fieldname>(self, value)` exactly; typos or different casing prevent invocation.
- Indentation/placement: Methods must be inside the serializer class; misplaced methods (module level or in another class) will not be called.
- Return value: Each `validate_<field>` must `return value` (possibly modified). Not returning will break validation flow.
- Field presence: Ensure the field is included in `Meta.fields`; excluded fields won't trigger validators.
- Serializer used by view: Confirm the view/viewset uses the serializer you edited (`serializer_class`).
- Overriding lower-level methods: Overriding `to_internal_value`, `run_validation`, or `is_valid` incorrectly may bypass `validate_<field>`.
- Validators vs model `clean()`: DRF serializer validators run at the serializer level; don't rely on model `clean()` for request validation.
- JSON type coercion: Client may send numeric types; use `serializers.CharField()` or explicit type checks inside validators.

Quick debugging steps:
1. Add a temporary log/print inside `validate_<field>` to confirm if it's called.
2. Add a unit test for the serializer with invalid data to reproduce the issue.
3. Confirm `Meta.fields` and `serializer_class` in the view.
4. Check indentation and method names for typos.

10) Unit tests guidance for small, single-model Django CRUD apps
- For small apps, using the Django ORM and simple test setups is sufficient. `factory_boy` or complex fixtures are optional.
- Example minimal test:
```py
from django.contrib.auth.models import User
from crud_rest_api.models import Notes

def test_create_note(db):
    u = User.objects.create_user(username='test', password='pw')
    note = Notes.objects.create(title='t', description='d', user=u)
    assert note.pk is not None
```
- When to adopt advanced tools: Use `factory_boy` when you need many interrelated objects, factories for readability, or to avoid repetitive setup.
- Simpler alternatives: pytest fixtures, small helper functions, or concise `setUp` helpers in Django TestCase.

If you want me to restore the text into `prompts.md` itself, I can do that — currently I created `prompts_original.md` so your original prompts are preserved.
