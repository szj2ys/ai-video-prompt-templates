"""Validate and render provider-neutral shot plans. Standard library only; no network."""
import argparse
import json
import math
from pathlib import Path
import sys

CAMERAS = {
    'static': 'The camera remains fixed.',
    'slow-push-in': 'The camera slowly moves closer to the subject.',
    'slow-pull-back': 'The camera slowly moves away from the subject.',
    'pan-left': 'The camera slowly pans left from a fixed position.',
    'pan-right': 'The camera slowly pans right from a fixed position.',
    'tilt-up': 'The camera slowly tilts upward from a fixed position.',
    'tilt-down': 'The camera slowly tilts downward from a fixed position.',
    'track-left': 'The camera moves slowly sideways to the left.',
    'track-right': 'The camera moves slowly sideways to the right.',
    'gentle-handheld': 'The camera has small, gentle handheld movement.',
}
TEXT_FIELDS = ('id', 'mode', 'subject', 'action', 'camera', 'framing', 'environment', 'lighting')


def validate_shot(shot):
    if not isinstance(shot, dict):
        raise ValueError('Each shot must be a JSON object.')
    for field in TEXT_FIELDS:
        if not isinstance(shot.get(field), str) or not shot[field].strip():
            raise ValueError(f'{field} must be a nonempty string.')
    if shot['mode'] not in ('text-to-video', 'image-to-video'):
        raise ValueError(f"{shot['id']}: unsupported mode.")
    if shot['camera'] not in CAMERAS:
        raise ValueError(f"{shot['id']}: choose one camera value from {', '.join(CAMERAS)}.")
    duration = shot.get('duration_seconds')
    if isinstance(duration, bool) or not isinstance(duration, (int, float)) or not math.isfinite(duration) or duration <= 0:
        raise ValueError(f"{shot['id']}: duration_seconds must be a positive finite number.")
    for field in ('preserve', 'review'):
        value = shot.get(field)
        if not isinstance(value, list) or any(not isinstance(item, str) or not item.strip() for item in value):
            raise ValueError(f"{shot['id']}: {field} must be a list of nonempty strings.")
    if shot['mode'] == 'image-to-video' and not shot['preserve']:
        raise ValueError(f"{shot['id']}: an image-to-video shot needs at least one preservation note.")
    if not shot['review']:
        raise ValueError(f"{shot['id']}: add at least one observable review check.")


def load_shots(path):
    shots = json.loads(Path(path).read_text(encoding='utf-8-sig'))
    if not isinstance(shots, list) or not shots:
        raise ValueError('Input must be a nonempty JSON list of shots.')
    seen = set()
    for shot in shots:
        validate_shot(shot)
        if shot['id'] in seen:
            raise ValueError(f"Duplicate shot id: {shot['id']}")
        seen.add(shot['id'])
    return shots


def render(shot):
    validate_shot(shot)
    lines = []
    if shot['mode'] == 'image-to-video':
        lines.append('Use the supplied reference image as the visual anchor.')
    lines.extend([
        f"Subject: {shot['subject']}", f"Action: {shot['action']}",
        CAMERAS[shot['camera']], f"Framing: {shot['framing']}",
        f"Environment: {shot['environment']}", f"Lighting: {shot['lighting']}",
    ])
    if shot['preserve']:
        lines.append('Keep stable: ' + '; '.join(shot['preserve']) + '.')
    return '\n'.join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', help='JSON list of shot plans')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--id', help='Render one shot')
    group.add_argument('--list', action='store_true', help='List shot identifiers')
    group.add_argument('--validate', action='store_true', help='Validate every shot')
    args = parser.parse_args(argv)
    try:
        shots = load_shots(args.input)
        if args.list:
            print('\n'.join(shot['id'] for shot in shots))
        elif args.validate:
            print(f'Valid: {len(shots)} shot plans. Model output has not been tested.')
        else:
            shot = next((item for item in shots if item['id'] == args.id), None)
            if shot is None:
                raise ValueError(f'Unknown shot id: {args.id}')
            print(render(shot))
            print(f"\nPlanning duration: {shot['duration_seconds']} seconds; set actual duration in your video tool.")
            print('\nReview after generation:\n' + '\n'.join('- ' + item for item in shot['review']))
        return 0
    except (OSError, ValueError) as error:
        print(f'Error: {error}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
