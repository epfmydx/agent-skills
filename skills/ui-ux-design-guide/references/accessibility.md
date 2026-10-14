# Accessibility as a design constraint

Accessibility should shape information structure, controls, and recovery from the beginning. Automated testing is useful, but passing a scanner is not proof that a workflow is usable or conforms to all applicable requirements. Use the relevant standard and platform guidance, plus manual and user testing.

## Selected web baseline checks

WCAG 2.2 is the reference standard used here. For a Level AA target, evaluate all applicable A and AA criteria across the relevant scope; this short checklist is not a conformance audit or legal determination. Check keyboard access, semantic relationships, labels, error identification, alternatives, resizing/reflow, focus visibility, and assistive-technology compatibility. [WCAG 2.2](https://www.w3.org/TR/WCAG22/)

- Text contrast: normally at least 4.5:1; large text can use 3:1. Large means at least 18 pt regular or 14 pt bold (approximately 24 CSS px or 18.67 CSS px). Exceptions exist for incidental text and logos; required labels are not decorative. Do not round a failing ratio upward. [Contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- Pointer targets: WCAG 2.2 AA generally requires 24 × 24 CSS pixels or a permitted exception, such as sufficient spacing. The exceptions need actual evaluation. This is a minimum criterion, not an ideal target for every context. [Target size minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- Focus: at AA, an item receiving keyboard focus must not be entirely hidden by author-created content. A stronger design goal is to keep the entire focused control visible. Test sticky headers, banners, popovers, and dialogs. [Focus not obscured](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html)

Native platform points and web CSS pixels are different units. Apple button guidance gives a general 44 × 44 pt hit-region rule, with 60 × 60 pt for visionOS; consult specific current platform/component guidance. Do not describe 44 px as a universal WCAG AA requirement. [Apple buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)

## Manual workflow checks: original testing protocol

Run the primary task without a mouse. Confirm a logical focus order, a visible focus indicator, operable controls, an escape route from overlays, and appropriate focus restoration. Verify that a visual change is also conveyed through the interface's accessible structure when necessary.

Use an appropriate screen reader to inspect headings, landmarks, names, roles, states, field instructions, validation, and asynchronous results. Test the complete task, not just a list of individually labeled buttons. Avoid over-announcing frequent updates that make the experience noisy.

Increase text size, zoom, and spacing; examine content at narrow widths. Essential information must remain available rather than being clipped behind fixed-height containers. Test long translations and right-to-left layouts if they are supported.

Check reduced-motion, contrast, and transparency preferences where applicable. Test status comprehension without color. Review images, charts, and media for equivalent information, including captions or transcripts when needed. In data visualizations, provide usable labels and an alternative means of accessing important values.

For authentication and forms, inspect avoidable memory demands, repeated entry, input assistance, and recovery. Offer inclusive input methods; do not assume everyone can drag precisely, hear audio, or interpret an unfamiliar symbol.

## Report honestly

Record platform, browser/OS, assistive technology and version, exact task, tested states, results, and unresolved barriers. Report “keyboard task passed in this environment” rather than “fully accessible.” Include users with relevant access needs in research when feasible; simulations and expert inspection do not reproduce their experience.
