---
name: write-a-prd
description: >
  Create a PRD through user interview, codebase exploration, and module design, then submit as a GitHub issue after user approval.
  Use when user wants to write a PRD, create a product requirements document, or plan a new feature. Always present the PRD for user approval before submitting.
---

This skill will be invoked when the user wants to create a PRD. You may skip steps if you don't consider them necessary, but you MUST NEVER skip the user approval step before submitting to GitHub.

1. Ask the user for a long, detailed description of the problem they want to solve and any potential ideas for solutions.

2. Explore the repo to verify their assertions and understand the current state of the codebase.

3. Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one by one.

4. Sketch out the major modules you will need to build or modify to complete the implementation. Actively look for opportunities to extract deep modules that can be tested in isolation.

A deep module (as opposed to a shallow module) is one which encapsulates a lot of functionality in a simple, testable interface which rarely changes.

Check with the user that these modules match their expectations. Check with the user which modules they want tests written for.

5. Once you have complete understanding of the problem and solution, use the template below to write the PRD. Present the full PRD to the user and explicitly ask for their approval before proceeding.

6. Only after the user has explicitly approved the PRD, submit it as a GitHub issue. NEVER create the GitHub issue without user approval.

<prd-template>
## Problem Statement

The problem that the user is facing, from the user's perpective. 

## Solution 

The solution to the problem, from user's perspective.

## User Stories
- As a [type of user], I want [some goal] so that [some reason].

## Implementation Decisions

Implementation decisions should not be overly prescriptive, we want those decisions to be durable.

</prd-template>