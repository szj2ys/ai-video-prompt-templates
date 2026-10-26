# Failure checklist

These are diagnostic hypotheses, not guaranteed fixes. First save the failed clip and its actual settings. Compare one change at a time and inspect the start, middle and end.

| Observed problem | Possible cause to investigate | One change to try | Inspect afterward |
| --- | --- | --- | --- |
| Product outline changes | Too much motion or an unclear reference | Keep the product still and lock the camera | Silhouette, handle, cap and edges |
| Lettering becomes unreadable | The model cannot preserve exact text | Plan a separate text overlay in editing | Required wording and readability |
| Subject drifts out of frame | Framing and movement disagree | Widen the framing while keeping the action | Subject position at all three sample times |
| Movement never happens | Action is vague or too subtle for the shot | Replace mood words with one visible action | Whether that action occurs at all |
| Clip jumps between scenes | Prompt asks for several events or settings | Split the plan into separate shots | Continuity within each shot |
| Background bends | Camera or environmental motion is too ambitious | Use a static camera | Straight edges and stable landmarks |
| Extra hands or objects appear | Contact action is ambiguous | Remove the interaction for a baseline shot | Number and identity of visible objects |
| Motion starts too late | The requested event needs more time | Simplify the event before increasing duration | When the action starts and ends |
| Reference colors shift | Lighting request conflicts with the source | Match the source lighting first | Color consistency, without assuming exact matching |
| Physical behavior looks wrong | The model lacks a stable interpretation | Use a simpler action with a clearer silhouette | Contact, gravity and object boundaries |

Stop iterating when the shot requires exact evidence, identity, factual depiction or precise text that the tool cannot provide. For documentary work, label any generated material appropriately; a plausible image is not a record of an event.

## Minimal comparison

Keep the reference, provider, model/version, output settings and other prompt fields fixed where the tool permits. Change one field, record the result, and note any uncontrolled randomness. A different seed or provider update can change results; a single pair of clips is not proof of general improvement.
