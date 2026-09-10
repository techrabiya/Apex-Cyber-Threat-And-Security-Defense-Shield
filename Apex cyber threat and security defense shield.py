print("--- AI Project 9: Security Shield Initialized 🛡️ ---")

def cyber_threat_defender(unauthorized_access, system_breach_level, admin_override):
    if unauthorized_access == True and system_breach_level == "Critical":
        print("[Security Alert: Severe cyber attack in progress! Locking down core.]")
        return "Defense Action: Immediate Network Isolation & Firewall Lockdown 🔒"
    elif unauthorized_access == True and admin_override == True:
        print("[Security Alert: Authorized admin override detected.]")
        return "Defense Action: Grant Superuser Access Under Secure Audit Trail 🔑"
    else:
        print("[Security Alert: All systems secure and operating normally.]")
        return "Defense Action: Maintain Standard Monitoring & Encryption Active ✅"

print("\n[Running Cyber Defense Simulations]")
print(cyber_threat_defender(True, "Critical", False))
print("-" * 80)
print(cyber_threat_defender(True, "Low", True))
print("-" * 80)
print(cyber_threat_defender(False, "None", False))
