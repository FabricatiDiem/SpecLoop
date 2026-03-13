# Epic Schema Requirements

All entries in `EPICS.md` MUST follow this structure to be parseable by the automation loop.

## Structure

```markdown
## [Title of the Epic]
Description: <Single or multiline description of the feature>
Priority: <Integer starting from 1>
- [ ] Status: <Pending | In Progress | Completed | Failed>
```

## Parsing Rules

1. **Title**: Extracted from the H2 header. Brackets `[...]` are optional but recommended for visual clarity.
2. **Description**: Begins with the prefix `Description:` and continues until the next field or empty line.
3. **Priority**: Must be a positive integer. Lower numbers are processed first.
4. **Status Checkbox**:
   - `[ ]`: Pending
   - `[~]`: In Progress
   - `[x]`: Completed
   - `[!]`: Failed
