---
name: "Greet User"
description: "A simple natural language skill to greet a user."
inputs:
  - name: "user_name"
    description: "The name of the user to greet."
handoffs:
  - label: "Next Step"
    agent: "other.skill"
    prompt: "Proceed to the next task..."
---

# Greet User

1. Ask the user for their name if not provided.
2. Say "Hello, [user_name]! Welcome to the agent-agnostic skills framework."
3. Ask if there's anything else you can help with.
