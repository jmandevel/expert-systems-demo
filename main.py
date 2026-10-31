from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

def collect_initial_facts():
    facts = []
    if input("Is portability important? (y/n): ").lower().startswith("y"):
        facts.append("portable")
    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):
        facts.append("long_battery")
    if input("Is your budget high? (y/n): ").lower().startswith("y"):
        facts.append("budget_high")
    elif input("Is your budget low? (y/n): ").lower().startswith("y"):
        facts.append("budget_low")
    else:
        facts.append("budget_medium")
    if input("Are you a gamer? (y/n): ").lower().startswith("y"):
        facts.append("gaming")
    if input("Do you create things? (y/n): ").lower().startswith("y"):
        facts.append("creative_work")
    if input("Are you an office professional? (y/n): ").lower().startswith("y"):
        facts.append("office_only")
    if input("Do you prefer Linux? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_linux")
    elif input("Do you prefer Windows? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_windows")
    elif input("Do you prefere Macos? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_macos")
    if input("Do you use AI? (y/n): ").lower().startswith("y"):
        facts.append("needs_ai_acel")
    if input("Do you need a large screen? (y/n): ").lower().startswith("y"):
        facts.append("large_screen")
    if input("Do you travel a lot? (y/n): ").lower().startswith("y"):
        facts.append("travel_often")
    return facts

def main():
    rules = load_rules("kb/laptop_rules.json")
    facts = collect_initial_facts()
    engine = ForwardChainingEngine(rules)
    engine.assert_facts(facts)
    engine.run()
    conclusions = engine.conclusions()
    for conclusion in conclusions:
        print(f"{conclusion}: ")
        for fact in conclusions[conclusion]:
            print(fact)

if __name__ == "__main__":
    main()
