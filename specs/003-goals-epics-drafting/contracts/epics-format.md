# Epic Schema Contract

To be compatible with the automation loop, all entries in `EPICS.md` MUST follow this exact Markdown structure.

## Structure Example

```markdown
## [Feature Title]
Description: This is a clear description of the feature.
Priority: 1
- [ ] Status: Pending
```

## Rules for Agents

1. **Headers**: Use H2 (`##`) for the title.
2. **Brackets**: The title MUST be enclosed in `[...]`.
3. **Fields**: `Description`, `Priority`, and `Status` must be on separate lines.
4. **Ordering**: Epics should be listed in increasing order of priority.
