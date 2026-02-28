import sovereign_logic as sl
import numpy as np

# Initialize the Infrastructure
bridge = sl.SovereignBridge()
sl.info()

# 1. Signal Recon Application
raw_noise = np.random.normal(0, 5, 1024)
clean_signal = bridge.bridge_signal(raw_noise)
print(f"Signal Recon: {np.mean(clean_signal):.4f} Resonance")

# 2. Market Liquefaction Application
market_volatility = np.random.rand(1024)
market_delta = bridge.bridge_market(market_volatility)
print(f"Fidelity Delta: {market_delta:.16f}")

print("-" * 30)
print("RESULT: Sovereign Bridge Anchored. [GRANITE-FIRM]")
