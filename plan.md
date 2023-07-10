# Project Plan: `dev` an LM-powered util for automating software development

### inbox

- prompts p1, p2
  - p1 uses p2 as a tool

### developer actions

- run tests
- commit

### learned

-   gpt4 does not understand "inline" immediately, need to design a prompt for that
-   extract function is not easy to do in one fell swoop
    -   design a prompt chain / loop that:
        1. adds a todo in the code
        2. create a new empty unused function focusing on signature
        3. fill the impl
        4. replace the call site
        5. validate each step

### 0k

-   patch.py

    -   separate out the main function so it can be used as a module in addition to a cli

-   English First
    -   puts comments in the code for later steps to convert into code
    -   can be based on the same overall structure of patch.py

### Objective

A utility that leverages Large Language Models (LLMs) for automating series of coding tasks using prompt chains and loops. Each task will be made simpler, done in English first, coded, and validates making sure the execution is error-free.

### Concepts

-   **TODO**: use a todo list
-   **Simplifier**: Breaks down large tasks into smaller ones and rates their complexity
-   **Contextual Inputs**: Include inputs like code summary, todo, dev workflow, command history, commit history, test results, previous steps results and more.
-   **Persistent State**: Maintains the state of context, goals and tasks; state is persisted in files under `dev/`
-   micro commits
-   loops should have breaking criteria
-   prompts to have clear output format; can be encapsulated in a util, a wrapper
-   English first; English only, before code
    -   the English could be committed too
        -   in a file under `dev/`
        -   inlined in the code as a comment
-   Mikado - modify, test, revert, learn
    -   git branch - a sandbox for experimentation, with a meaningful name
    -   learnings are accumulated under `dev/`
    -   finally can be squashed into `main`

### Meta-development guidelines

-   approval tests
-   executable command for prompts design
-   built as a cli; a collection of cli utils

### Task Breakdown/Components

4. **Code Reader**: A specialized tool for specific purposes.
5. **Chain of Steps**: A series of steps for problem-solving that includes task simplification, validation, coming up with solutions, shrinking tasks and etc.
6. **Validation**: A standard format for validation results.
7. **Key Ranking**: Ranking of specific keywords based on use and importance.
8. **Source Code Summarizer**: An LLM-based tool that summarizes the source code.
9. **Improvement System**: An LLM-driven system to continually improve the prompt chains.
10. **Diff Coder**: A tool that utilizes "fuzzy match" in diffs.

### Expected Outcome

The end product will be a comprehensive software utility that simplifies and automates parts of the coding/development workflow. It will not only perform standalone tasks but will also streamline the coding process by effectively using a large language model.

The utility explores the possibility of using LLM to improve the chain of prompts for continual enhancement of the software's capabilities. This utility represents an ambitious effort to leverage machine learning to streamline and enhance development workflows by prioritizing certain tasks, keeping context and scoring the difficulty.

### potential extensions

-   LM searches the code
