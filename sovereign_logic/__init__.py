from .engine import UnitaryEngine
from .guard import SovereignGuard

__version__ = "1.0.1-Apex"
__signature__ = SovereignGuard.get_signature()

def info():
    print(f"Sovereign-Logic v{__version__}")
    print(f"Manifold Signature: {__signature__}")
    print("Status: [GRANITE-FIRM]")
