#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from pathlib import Path
from physics_content.crew import PhysicsContentCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")  # harmless [20]

def ensure_dirs(chapter_number: str):
    for sub in ["research", "index", "content", "examples_bank"]:
        Path(f"artifacts/{sub}/{chapter_number}").mkdir(parents=True, exist_ok=True)  # [20]

def get_inputs():
    if len(sys.argv) >= 3:
        chapter_number = sys.argv[1].strip()
        chapter_name = "_".join(sys.argv[2:]).strip().replace(" ", "_")
    else:
        chapter_number = input("Enter chapter number: ").strip()
        chapter_name = input("Enter chapter name: ").strip().replace(" ", "_")
    return {'chapter_number': chapter_number, 'chapter_name': chapter_name, 'current_year': str(datetime.now().year)}  # [20]

def run():
    inputs = get_inputs()
    ensure_dirs(inputs['chapter_number'])
    try:
        PhysicsContentCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")  # [20]

def train():
    inputs = get_inputs()
    ensure_dirs(inputs['chapter_number'])
    try:
        PhysicsContentCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")  # [20]

def replay():
    try:
        PhysicsContentCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")  # [20]

def test():
    inputs = get_inputs()
    ensure_dirs(inputs['chapter_number'])
    try:
        PhysicsContentCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")  # [20]

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in {"run", "train", "replay", "test"}:
        mode = sys.argv[1]
        sys.argv.pop(1)
        {"run": run, "train": train, "replay": replay, "test": test}[mode]()
    else:
        run()  # [20]
