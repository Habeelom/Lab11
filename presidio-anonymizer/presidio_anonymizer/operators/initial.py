"""Initial operator - converts text to initials."""
from presidio_anonymizer.operators.operator import Operator, OperatorType
from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """Initial operator converts detected PII into initials."""

    def operate(self, text: str = None, params: Dict = None) -> str:
        """Convert text to initials."""
        return ""

    def validate(self, params: Dict = None) -> None:
        """Validate operator parameters."""
        pass

    def operator_name(self) -> str:
        """Return the operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return the operator type."""
        return OperatorType.Anonymize