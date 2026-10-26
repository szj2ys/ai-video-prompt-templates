# AI video prompt templates

A small, offline kit for planning a single AI video shot. It includes editable JSON examples, a Python prompt renderer, camera vocabulary and a failure checklist. Use it with the video tool you already have; it has no account requirement, network calls or model dependency.

The examples are **illustrative starting points, not tested model outputs**. A well-specified shot can still fail. Duration, aspect ratio, reference-image support and negative-prompt syntax depend on the tool you choose.

## Start in two minutes

Python 3.10 or later is enough; there are no packages to install.

```sh
python promptkit.py examples.json --list
python promptkit.py examples.json --id ceramic-cup-steam
python promptkit.py examples.json --validate
python -m unittest discover -s tests
```

Copy `examples.json` to a new JSON file and keep just one shot object inside the outer `[ ]` list. Keep those square brackets; a bare object is not valid input. Change the subject and one intended motion, then render it. The program prints text; it does not generate a video or upload a reference image.

## A shot is a small decision sheet

| Field | Decide before generating |
| --- | --- |
| `mode` | Are you inventing a scene (`text-to-video`) or animating a reference (`image-to-video`)? |
| `subject` | What must the viewer recognize? Use a concrete object or person description. |
| `action` | What one visible action happens? Use `remains still` when only the camera moves. |
| `camera` | Choose one movement. Framing is a separate field. |
| `framing` | How much of the subject and setting should be visible? |
| `environment` | Where is the shot? Name a useful spatial or material detail. |
| `lighting` | Name a light source or direction rather than a quality adjective. |
| `duration_seconds` | A planning estimate, not a command that overrides a tool's duration controls. |
| `preserve` | Which visible properties should remain stable? Required for image-to-video. |
| `review` | What observable defect would make you reject the result? |

The schema prevents missing fields and unsupported camera labels. It does **not** understand your scene or prove that an action is physically achievable.

## Worked adaptation

For `ceramic-cup-steam`, the reference supplies the cup, composition and table. The proposed action is steam rising; the camera stays still. The preservation notes keep the handle and rim stable. The review checklist asks you to inspect those features frame by frame.

To adapt it to a candle, change the subject and motion to a small flame flickering. Replace the preservation notes with the candle's shape and wick position. Do not merely replace the noun while leaving cup-specific constraints behind.

For a more dynamic composition, make a second version using `slow-push-in` and compare it with the static version. Change one decision at a time. Save the chosen tool, settings, reference and observed failure in [the review worksheet](REVIEW-WORKSHEET.md). This kit supplies no performance benchmark.

## Choose the right amount of freedom

- For image-to-video, begin with a reference you have permission to use. Describe intended motion and a few visual anchors. A prompt cannot guarantee identity, shape or label preservation.
- For text-to-video, describe the subject and environment explicitly. Avoid relying on invented lettering for exact names or claims; add important text during editing.
- Split actions that need different framing into separate shots. A product reveal and a reaction shot usually need two decision sheets.
- Prefer explicit constraints such as “the camera stays fixed” over a long list of adjectives. If your provider uses a separate negative-prompt field, adapt constraints to its documented interface.

## Contents

- [Ten editable examples](examples.json): product, portrait, fabric, food, architectural, teaching and abstract shots.
- [Camera vocabulary](SHOT-VOCABULARY.md): movement versus framing, with common contradictions.
- [Failure checklist](FAILURE-CHECKLIST.md): symptoms, possible causes and single-change experiments.
- [Review worksheet](REVIEW-WORKSHEET.md): record what actually happened rather than claiming a prompt worked.
- [Offline renderer](promptkit.py) and its validation tests.

## Further reading and affiliation

This kit accompanies Imgmov's [guide to writing AI video prompts](https://imgmov.com/blog/2026-07-27-ai-video-prompt-writing-guide), which explains the subject/action/camera approach in prose. It is published by an Imgmov-affiliated maintainer. The examples and code here are a separate educational resource.

At the 2026-10-27 publication check, Imgmov's creation, sign-in and credit-purchase services were offline. The written guide remained readable. The kit does not depend on those services and does not endorse a specific video model.

## Contributing

Useful contributions include a clearer example, an additional validation edge case, or a documented observation with the tool/version, settings and permission to share its reference. Keep examples provider-neutral. Label untested examples as illustrative, avoid performance promises, and do not add unrelated promotional links. Report problems through this repository's issue tracker where available.

## License

The original code, documentation and illustrative examples in this repository are provided under the [MIT license](LICENSE).
