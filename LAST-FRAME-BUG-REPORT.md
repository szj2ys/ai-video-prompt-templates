# How to make a reproducible bug report when an extracted video frame looks wrong

Prepared by an imgmov-affiliated maintainer with AI assistance; the product link is affiliated. This optional browser workflow is separate from this repository's offline prompt renderer. It is for editors, educators and support teams investigating an unexpected closing image.

“The last frame is wrong” leaves a reviewer several possibilities. The file may be a different revision, the selected image may be earlier than the end, or two players may interpret timing differently. A useful report lets another person distinguish those cases without guessing what you did.

Build a small technical record around the original clip and the actual exported file. Its purpose is reproduction, not proof of when an event happened or a forensic authenticity certificate.

## Preserve the two files before editing

Keep the original clip and the downloaded PNG unchanged. Put any annotated image in a separate file so arrows, circles or redactions do not become confused with the extraction result. Record the clip's filename and byte size, but do not rely on its name alone: two revisions can share the same name.

Only retain or share material you are allowed to handle. If the clip contains private information, first reproduce the issue using a harmless clip you control. A screenshot of a filename or download folder can itself expose client names and project details.

## Record one precise reproduction

For this workflow, open the [imgmov last-frame extractor](https://imgmov.com/extract-last-frame-from-video) and choose the local clip. Record the browser version, operating system, and any error or estimated-frame notice. State whether you selected the final frame or clicked an earlier thumbnail. Download the PNG and open that file outside the web page.

Describe expected and observed behavior separately. For example, an illustrative report could say: “I selected the thumbnail containing the closing title. The downloaded image contains the preceding camera view.” That is more actionable than “bad quality.” This example describes the structure of a report; it is not a failure observed in the campaign test.

If the file did not download, report that instead of attaching an older PNG from the same folder. Check the exact filename and the download time before deciding which artifact belongs to this attempt.

## Qualify the timestamp rather than adding precision

Copy the displayed selection time and note the tool's frame-status wording. Do not turn a rounded decimal into a more precise timestamp by adding zeros. The current filename helper formats seconds to two decimal places; that filename is a locator, not a complete record of decoder timing.

Browser frame metadata can report a media presentation timestamp. It is distinct from a wall-clock capture time. Mozilla describes `mediaTime` as the presented frame's timestamp on the video's media timeline in its [frame-callback documentation](https://developer.mozilla.org/en-US/docs/Web/API/HTMLVideoElement/requestVideoFrameCallback). A displayed time should therefore be reported with its origin: “time shown by the extractor,” not “the recording occurred at this time.”

If the interface says it could not verify every presented frame, include that notice. Do not translate an estimated result into a claim of frame accuracy. An editor's absolute frame number, if available, is a separate observation; specify the application and counting convention rather than assuming the numbers are interchangeable.

## Add content hashes when file identity matters

On Windows, PowerShell can compute SHA-256 hashes without altering the files. Run this from the folder containing your two files, replacing the example filenames with their actual names:

```powershell
Get-FileHash -LiteralPath '.\clip.mp4', '.\closing-frame.png' -Algorithm SHA256 |
    Format-List Algorithm, Hash, Path
```

Copy both results into the report, labeling which is the original and which is the PNG. Microsoft documents `-LiteralPath` and SHA-256 in [Get-FileHash](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash). A hash helps collaborators check that they received the same bytes. It does not establish that a scene is truthful, identify who recorded it, or prove that the chosen frame was correct.

Recompute the hash after transferring the file if transfer integrity is the question. If an image was resized or annotated, expect a different file identity and label it as a derivative. Preserve the original hash rather than replacing it with the edited version's hash.

## Send the minimum useful report

Include these items together:

- One sentence describing the expected image and the observed problem.
- Original and PNG filenames, byte sizes, and hashes when needed.
- The selection action, displayed time, and measured/estimated notice.
- Browser and operating-system versions, plus exact error text.
- An unedited PNG and, only when permitted and necessary, the source clip.
- Any transformation performed before extraction, such as transcoding.

The extractor's selected-file path processes the video locally; the website may still make other network requests. Sending a support attachment is a separate transfer. Agree on an appropriate private delivery route rather than posting a confidential clip publicly.

Preparation checks (31 October 2026): the existing 31 October test verified one sample-to-PNG download. Source inspection confirms two-decimal filename timestamps and the local export path. Hash-command behavior was checked on the existing saved artifact during preparation; no new extraction failure, cross-browser reproduction or forensic validation is claimed.
