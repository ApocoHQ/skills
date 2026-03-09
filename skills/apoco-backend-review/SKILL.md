---
name: apoco-backend-review
description: Review submissions to the ApocoHQ backend code challenge. Use this skill when reviewing a candidate's Pokemon catalog REST API submission, evaluating backend coding challenges, or assessing Node.js/TypeScript API implementations against the Apoco hiring challenge criteria.
---

# Apoco Backend Code Challenge Review

You are reviewing a candidate's submission to the Apoco Backend Code Challenge.

## Step 1: Fetch Challenge Requirements

First, read the official challenge specification:

```
https://github.com/ApocoHQ/backend-code-challenge
```

Fetch the README to understand current requirements, evaluation criteria, and technical stack expectations. This is the source of truth.

## Step 2: Review the Submission

Systematically evaluate the candidate's code against the challenge requirements. For each area, note specific examples from their code.

Key areas to assess:
- **Functional completeness** - Do all required endpoints exist and work?
- **REST API design** - Proper methods, URLs, status codes, error handling
- **Code quality** - TypeScript usage, architecture, separation of concerns
- **Database design** - Schema, migrations, seeds, relationships
- **Docker & DevOps** - Dockerfile, compose, build optimization
- **Testing** - Coverage, organization, test types
- **AI integration** - Implementation quality, graceful degradation
- **Documentation** - README, OpenAPI specs, setup instructions

## Step 3: Generate Initial Assessment

Write the assessment to a file named `review-[candidate-name-or-repo].md` in the current directory. This is a **draft for the reviewer** — they will iterate on it before it goes to decision makers.

Frame the tone accordingly: clear and factual, but leave room for the reviewer to add context, adjust scores, and refine the recommendation.

```markdown
# Backend Code Challenge — Initial Assessment

> ⚠️ Draft — for reviewer eyes only. Not yet sent to decision makers.

## Candidate: [name if known]
## Repository: [repo link]
## Assessed: [date]

## First Impression
[2-3 sentences on overall impression]

## Scores

| Category | Score (1-5) | Notes |
|----------|-------------|-------|
| Functional Correctness | | |
| REST API Design | | |
| Code Quality | | |
| Database Design | | |
| Docker & DevOps | | |
| Testing | | |
| AI Integration | | |
| Documentation | | |
| **Overall** | | |

## Strengths
- [Specific examples]

## Areas for Improvement
- [Constructive feedback with examples]

## Red Flags (if any)
- [Critical concerns]

## Preliminary Recommendation
[ ] Strong Hire  [ ] Hire  [ ] Lean Hire  [ ] Lean No Hire  [ ] No Hire

[Reasoning — reviewer should validate before sending]

## Suggested Interview Discussion Points
[Topics to explore if candidate advances]

---
*Reviewer notes:* <!-- add any context or adjustments here -->
```

Once the file is written, let the reviewer know it's ready and remind them to look it over before forwarding.

## Scoring Guide

- **5** - Exceptional: Beyond requirements, senior-level quality
- **4** - Strong: Meets requirements well, good practices
- **3** - Acceptable: Basic requirements met, some rough edges
- **2** - Below Expectations: Missing requirements or significant issues
- **1** - Unacceptable: Major gaps, not production-ready

## Review Principles

- Be fair and constructive
- Consider time constraints candidates face
- Look for good judgment, not just rule-following
- Note creative solutions positively
- When unclear, ask rather than assume the worst
