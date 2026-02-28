from .engine import UnitaryEngine
from .guard import SovereignGuard
from .bridge import SovereignBridge

__version__ = "1.0.2-Apex"
__signature__ = SovereignGuard.get_signature()

def info():
    print(f"Sovereign-Logic v{__version__}")
    print(f"Manifold Signature: {__signature__}")
    print("Status: [GRANITE-FIRM]")
    print("Bridge Status: OPERATIONAL")
