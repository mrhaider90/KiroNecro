# main.py - Main Entry Point for KiroNecro Orchestrator
from config import LEGACY_DATABASE, SYSTEM_VERSION
from agents import NecromancerAgent, SpookyStoryAgent

def run_kiro_orchestrator():
    print("====================================================")
    print(f"🧟‍♂️ KIRONECRO MULTI-AGENT SWARM ORCHESTRATION v{SYSTEM_VERSION} 🧟‍♂️")
    print("====================================================\n")
    
    # Initialize components from modular files
    byte_necromancer = NecromancerAgent(name="ByteNecromancer", role="Legacy System Resurrection")
    crypt_keeper = SpookyStoryAgent(name="CryptKeeper", role="Spooky UI Narrative Generator")
    
    print(f"\n🚨 [System Alert] Outdated Server Status: {LEGACY_DATABASE['server_status']}")
    
    # Trigger Swarm Pipeline
    print("\n🔗 Triggering Agent Hook: OnLegacySystemFailure...")
    patch_result = byte_necromancer.execute_task(LEGACY_DATABASE)
    print(f"✅ Success: {patch_result['action_taken']}")
    
    print("\n🔗 Triggering Agent Hook: OnSystemRemediationComplete...")
    spooky_alert = crypt_keeper.execute_task(patch_result)
    
    print("\n====================================================")
    print("🎃 SPOOKY MONITORING DASHBOARD OUTPUT:")
    print(spooky_alert)
    print("====================================================")

if __name__ == "__main__":
    run_kiro_orchestrator()
