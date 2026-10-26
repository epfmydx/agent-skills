# Agent Skills

Reusable skills for working with AI agents.

These are workflows I’m putting together for my own projects and sharing with other teams. They cover the work around development too: understanding the requirements, checking the user experience, and keeping the documentation useful.

Use what fits your project. You can start with one skill; you don’t need a full agent team for every task.

## What’s included

| Skill | What it helps with |
| --- | --- |
| [Business Analysis](skills/business-analysis/SKILL.md) | Clarify requirements, business rules, permissions, exceptions, and acceptance criteria. |
| [UI/UX Design Guide](skills/ui-ux-design-guide/SKILL.md) | Review workflows, interaction states, visual hierarchy, and accessibility. |
| [Project Documentation](skills/project-documentation/SKILL.md) | Keep project knowledge accurate. Follow the project’s existing documentation, and use a default structure where one is missing. |
| [Presentation Strategy & Storytelling](skills/presentation-strategy/SKILL.md) | Shape proposals, decision decks, updates, demos, technical talks, and training around the audience, evidence, and delivery setting. |
| [Codex Dev Team](skills/codex-dev-team/SKILL.md) | Coordinate implementation, focused helpers, independent review, and the relevant checks from the other skills. |

Business Analysis, UI/UX, Project Documentation, and Presentation Strategy work independently. Codex Dev Team brings the relevant responsibilities into a development workflow, with Sol for substantive development, Luna for bounded mechanical and coding tasks, Terra for bounded writing, visual interpretation and comparison, and supported app tasks, and Astra for specific problems that need deeper investigation.

Presentation Strategy covers the message, evidence, wording, visual direction, and delivery preparation. For PowerPoint, Google Slides, or other deck files, pair it with an available presentation-authoring skill. It does not supply its own slide renderer or require a particular vendor.

## Using the skills

The four companion skills use general workflow guidance. Codex Dev Team is specific to Codex and its available models and worker tools.

The skills have been reviewed and exercised in Codex. The Claude Code setup below follows its documented skill format; behavior in Claude Code has not yet been tested.

### Codex

Ask Codex to install the skills you want. To install all five in one request:

```text
$skill-installer install these skills from epfmydx/agent-skills:
- skills/business-analysis
- skills/ui-ux-design-guide
- skills/project-documentation
- skills/presentation-strategy
- skills/codex-dev-team
```

Then use a skill by name, for example:

```text
Use $codex-dev-team to implement this feature. Follow the project’s existing conventions and include the relevant documentation updates.
```

See the [official Codex skill instructions](https://learn.chatgpt.com/docs/build-skills) for installation and discovery details.

### Claude Code

Clone this repository, then copy the complete folders for the companion skills you want from `skills/` into either:

- `~/.claude/skills/` for your own use across projects.
- `.claude/skills/` inside a project to share them with that project’s team.

For example, Business Analysis should end up at `~/.claude/skills/business-analysis/SKILL.md`, with its supporting folders alongside it. Use the same approach for UI/UX, Project Documentation, and Presentation Strategy. Codex Dev Team is intended for Codex.

Invoke a skill with `/business-analysis`, `/ui-ux-design-guide`, `/project-documentation`, or `/presentation-strategy`. See the [official Claude Code skill instructions](https://code.claude.com/docs/en/skills) for other installation options.

## A few ways to start

- “Use Business Analysis to review this feature request. Identify the business rules, missing decisions, and acceptance criteria.”
- “Use the UI/UX Design Guide to review this screen. Keep the existing brand and focus on what makes the task difficult.”
- “Use Project Documentation to update the setup guide. Follow the documentation structure we already have.”
- “Use Presentation Strategy to plan a client proposal. Separate the live talk from anything the client needs to read afterwards, and flag claims that need evidence.”

Keep the request specific. A small fix should stay small, and an existing project should keep the conventions that already work for it.

## Maintaining the skills

Each skill lives in its own folder under `skills/`. Keep its instructions and supporting references together. Personal preferences, client details, and local configuration belong outside the shared skill content.

For the UI/UX guide, edit the files under `references/`, then rebuild the combined reading edition from the repository root:

```sh
python3 skills/ui-ux-design-guide/scripts/build_guide.py
python3 skills/ui-ux-design-guide/scripts/build_guide.py --check
```

The generator uses Python 3 and its standard library. The [combined guide](skills/ui-ux-design-guide/UI-UX-DESIGN-GUIDE.md) is also available if you prefer to read everything in one place.

## License

[MIT](LICENSE). You can use and adapt these skills for your own projects and teams, keeping the license notice with copies. Linked third-party sources retain their own terms.
