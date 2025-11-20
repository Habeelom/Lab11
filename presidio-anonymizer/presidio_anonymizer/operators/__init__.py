"""Initializing all the existing anonymizers."""
from .operator import Operator, OperatorType  # ADD THIS LINE FIRST
from .aes_cipher import AESCipher
from .custom import Custom
from .deanonymize_keep import DeanonymizeKeep
from .encrypt import Encrypt
from .decrypt import Decrypt  # isort:skip
from .hash import Hash
from .initial import Initial  # ADD THIS LINE
from .keep import Keep
from .mask import Mask
from .redact import Redact
from .replace import Replace
try:
    from .ahds_surrogate import AHDSSurrogate
    AHDS_AVAILABLE = True
except ImportError:
    AHDSSurrogate = None
    AHDS_AVAILABLE = False
from .operators_factory import OperatorsFactory  # isort:skip
__all__ = [
    "OperatorType",
    "Operator",
    "Hash",
    "Mask",
    "Redact",
    "Keep",
    "DeanonymizeKeep",
    "Replace",
    "Custom",
    "Encrypt",
    "Decrypt",
    "Initial",  # ADD THIS LINE
    "AESCipher",
    "OperatorsFactory",
    "AHDS_AVAILABLE",
]
if AHDS_AVAILABLE:
    __all__.append("AHDSSurrogate")