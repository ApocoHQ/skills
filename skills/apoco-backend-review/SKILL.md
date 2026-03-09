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

Key areas to assess, in order of priority:

**High weight** — These reflect senior-level thinking and are the strongest hiring signals:
- **Code quality & architecture** - TypeScript usage, separation of concerns, abstractions, design patterns
- **REST API design** - Proper methods, URLs, status codes, error handling, consistency
- **Database design** - Schema, migrations, seeds, relationships, query efficiency

**Medium weight** — Important but more learnable:
- **Functional completeness** - Do all required endpoints exist and work?
- **Testing** - Coverage, organization, test types

**Low weight** — Nice to have, not dealbreakers:
- **Docker & DevOps** - Dockerfile, compose, build optimization
- **AI integration** - Implementation quality, graceful degradation
- **Documentation** - README, OpenAPI specs, setup instructions

## Scoring Guide

Apply these criteria **before** generating the assessment:

- **5** - Exceptional: Beyond requirements, senior-level quality
- **4** - Strong: Meets requirements well, good practices
- **3** - Acceptable: Basic requirements met, some rough edges
- **2** - Below Expectations: Missing requirements or significant issues
- **1** - Unacceptable: Major gaps, not production-ready

The **Overall** score is not an average. It reflects holistic judgment weighted by category priority. A weak score on a high-weight category pulls the overall down more than a weak score on a low-weight one.

## Step 3: Generate Initial Assessment

Write the assessment to a file named `review-[candidate-name-or-repo].md` in the current directory. This is a **draft for the reviewer** — they will iterate on it before it goes to decision makers.

Frame the tone accordingly: clear and factual, but leave room for the reviewer to add context, adjust scores, and refine the recommendation.

Use the template at `assets/review-template.md` for the output structure.

Once the file is written, let the reviewer know it's ready and remind them to look it over before forwarding.

## Review Principles

- Be fair and constructive
- Consider time constraints candidates face
- Look for good judgment, not just rule-following
- Note creative solutions positively
- When unclear, ask rather than assume the worst
