import json

def detect_interruptions(filename):
    turns = []

    # Load all turns
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            turn = json.loads(line)

            # Defensive loading — some entries may not have these fields
            start = turn.get("startTime")
            end = turn.get("endTime")

            # Skip entries without valid times
            if start is None or end is None:
                continue

            # Convert to float if needed
            try:
                start = float(start)
                end = float(end)
            except ValueError:
                continue

            turns.append({
                "text": turn.get("turnText", ""),
                "start": start,
                "end": end,
                "speaker": turn.get("speaker", "UNKNOWN")
            })

    print(f"Loaded {len(turns)} turns from {filename}")

    # Sort by start time
    turns.sort(key=lambda t: t["start"])

    # 🔍 Debug print: first 10 start times
    print("First 10 start times (sorted):")
    for t in turns[:10]:
        print(f"{t['start']:.2f}")

    interruptions = []

    # Detect overlaps
    for i in range(len(turns) - 1):
        current = turns[i]
        nxt = turns[i + 1]

        if nxt["start"] > 0.1 and nxt["start"] < current["end"]:
            interruptions.append({
                "interrupted_speaker": current["speaker"],
                "interrupter": nxt["speaker"],
                "start_time": nxt["start"],
                "end_time": current["end"],
                "text": nxt["text"],
                "overlap_duration": current["end"] - nxt["start"]
            })

    print(f"Detected {len(interruptions)} interruptions!")
    return interruptions


# Run it
interruptions = detect_interruptions("../data/speakerTurnDataSample.jsonl")

for i in interruptions[:10]:
    print(
        f"{i['interrupter']} interrupted {i['interrupted_speaker']} "
        f"at {i['start_time']:.2f}s "
        f"(overlap {i['overlap_duration']:.2f}s)"
    )