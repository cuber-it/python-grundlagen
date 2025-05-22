#!/usr/bin/env python3
import sys
import yaml
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Dict, Any

def load_yaml(file: Path) -> Dict[str, Any]:
    with file.open(encoding='utf-8') as f:
        return yaml.safe_load(f)

def questions_to_xml(name: str, questions: List[Dict[str, Any]],
                     capability: str = "C001", language: str = "DE") -> str:
    quiz = ET.Element("quiz")
    ET.SubElement(quiz, "name").text = name
    ET.SubElement(quiz, "capability").text = capability
    ET.SubElement(quiz, "language").text = language
    questions_el = ET.SubElement(quiz, "questions")

    for q in questions:
        q_el = ET.SubElement(questions_el, "question")
        ET.SubElement(q_el, "questionType").text = q.get("type", "multiple_choice")
        ET.SubElement(q_el, "question").text = q["question"].strip()
        ET.SubElement(q_el, "duration").text = str(q.get("duration", 10))
        ET.SubElement(q_el, "correct").text = str(q["correct"])
        answers_el = ET.SubElement(q_el, "answers")
        for ans in q["answers"]:
            ET.SubElement(answers_el, "answer").text = str(ans).strip()
    return ET.tostring(quiz, encoding="unicode")

def convert_file(yaml_path: Path):
    data = load_yaml(yaml_path)
    name = data.get("name", yaml_path.stem)
    questions = data.get("questions", [])
    if not questions:
        print(f"⚠️  Keine Fragen in {yaml_path.name}", file=sys.stderr)
        return
    xml_str = questions_to_xml(name, questions)
    out_path = yaml_path.with_suffix(".xml")
    out_path.write_text(xml_str, encoding="utf-8")
    print(f"✅ {out_path.name} erzeugt")

def main():
    if len(sys.argv) < 2:
        print("Verwendung: create_quaz.py file1.yaml file2.yaml ...", file=sys.stderr)
        sys.exit(1)
    for f in sys.argv[1:]:
        path = Path(f)
        if not path.exists():
            print(f"❌ Datei nicht gefunden: {f}", file=sys.stderr)
            continue
        convert_file(path)

if __name__ == "__main__":
    main()
