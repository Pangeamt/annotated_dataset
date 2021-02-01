from annotated_dataset.annotated_text import AnnotatedText
from dataclasses import dataclass


@dataclass
class AnnotatedTextLocalized(AnnotatedText):
    resource: str
    line: int
