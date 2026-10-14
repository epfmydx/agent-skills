# Apple guidance and platform adaptation

## Choose the target platform first

Identify the target OS, supported versions, framework, input methods, and existing design system before choosing component conventions.

- Apple platforms: use the current HIG and relevant framework documentation; the Apple-specific sections below apply here.
- Android: consult current [Android design guidance](https://developer.android.com/design/ui/mobile) and [Android accessibility guidance](https://developer.android.com/design/ui/mobile/guides/foundations/accessibility), including the relevant Material component guidance when that is the product's system. Check navigation/back behavior, adaptable layouts, font scaling, semantics, and TalkBack. Preserve an established product system rather than imposing a new theme.
- Web: preserve semantic HTML, browser navigation, keyboard behavior, and applicable WCAG criteria. A mobile web surface still needs web semantics.
- Other platforms: consult their official component and accessibility guidance before recommending native interactions.

For Flutter, Ionic, or another cross-platform framework, identify whether each surface uses native controls, framework-rendered widgets, or web content. Verify the framework's accessibility mapping and target-platform behavior. Apple points, Android density-independent units, and CSS pixels are not interchangeable requirements. Carry task logic and identity across platforms; verify controls and assistive-technology behavior on each actual target.

## Current source interpretation

Checked 14 October 2026. Apple's general design-principles page identifies purpose, agency, responsibility, familiarity, flexibility, simplicity, craft, and delight. Treat these as decision lenses: meaningful outcomes, user control, trustworthy behavior, recognizable patterns, varied needs, clarity, detail, and appropriate emotion. They are not a visual recipe. [Apple design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles/)

Apple's Liquid Glass guidance also emphasizes hierarchy, harmony, and consistency. Do not confuse that framing with the complete general-principles page. Standard framework components can adopt the new appearance; adoption does not inherently require redesigning the whole app. [Liquid Glass overview](https://developer.apple.com/documentation/technologyoverviews/liquid-glass)

Apple separates navigation/control materials from the content layer. It advises restrained custom Liquid Glass use, with standard materials for content; its regular and clear variants serve different legibility contexts. [Materials](https://developer.apple.com/design/human-interface-guidelines/materials)

## Operational application: original synthesis

For an Apple-native app, check the current HIG and API behavior for the specific component and supported OS versions rather than copying a promotional screenshot.

- iPhone: prioritize the compact, touch-based task and interruption/resume behavior.
- iPad: consider variable window sizes and both touch and keyboard/pointer work.
- Mac: preserve efficient windowed work, keyboard access, menus, and contextual actions.
- Watch, TV, and spatial platforms: investigate their actual interaction constraints separately. They are not resized phone screens.

These are design prompts, not a replacement for platform-specific HIG requirements. Check behavior on real supported configurations, including large text and assistive technology.

Keep product identity in content, typography choices permitted by the platform, imagery, tone, and task-specific structure. Use native components where they fit. Customize when the task warrants it, with explicit responsibility for accessibility, adaptation, and interaction states.

For a web application, preserve browser expectations, semantic HTML, links, navigation history, keyboard behavior, and responsiveness. Translate useful principles such as clear hierarchy and recovery; do not imitate native chrome or add translucency simply to appear Apple-like. Cross-platform coherence means recognizable identity and task logic, not identical controls everywhere.

## Material decision checklist

1. What relationship does the surface communicate?
2. Is it content, navigation, or a temporary control?
3. Can text remain readable over realistic moving content?
4. What happens in high contrast, reduced transparency, reduced motion, and alternate appearance?
5. Is a system component available for the target version?
6. Does the effect improve orientation enough to justify complexity and rendering cost?

If the answer is uncertain, prototype a simpler surface too and compare in the actual task. Do not claim that an award-winning glass implementation proves glass improves every interface.

## Version discipline

HIG pages evolve and some require JavaScript. Indexed primary-source text helped verify these pages; no hands-on device testing was performed for this guide. Before implementation, refresh the relevant guidance, SDK availability, and accessibility settings. Record the date and target versions. Avoid treating older “clarity, deference, depth” summaries as a complete account of current HIG.
