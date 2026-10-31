import engine as e
import kb_loader as kb
from typing import List

def makeEngine() -> e.ForwardChainingEngine:
    rules = kb.load_rules("kb/laptop_rules.json")
    engine = e.ForwardChainingEngine(rules)
    return engine

pass_count = 0
fail_count = 0

def testEngine(facts: List[str], recommendations: List[str], specs: List[str]) -> None:
    global pass_count
    global fail_count
    engine = makeEngine()
    engine.assert_facts(facts)
    engine.run()
    output = engine.conclusions()
    result = (
        set(output["recommendations"]) == set(recommendations) and
        set(output["specs"]) == set(specs) and 
        set(output["other_facts"]) == set(facts)
    )
    fact_str = ",".join(facts)
    recommendation_str = ",".join(recommendations)
    specs_str = ",".join(specs)
    trace_str = "{\n\t" + "\n\t".join(output["trace"]) + "\n\t}"
    print(
        f"test result: {result} for\n"
        f"\tfacts:{fact_str}\n"
        f"\trecommendations:{recommendation_str}\n"
        f"\tspecs:{specs_str}\n"
        f"\ttrace:{trace_str}\n")
    if result:
        pass_count+=1
    else:
        fail_count+=1


testEngine(
    ["budget_high", "portable", "long_battery"],
    ["premium_ultrabook"],
    []
)

testEngine(
    ["budget_low", "office_only", "portable"],
    ["midrange_gaming_laptop"],
    []
)

testEngine(
    ["gaming", "budget_medium"],
    ["midrange_gaming_laptop"],
    []
)

testEngine(
    ["creative_work", "portable"],
    [],
    ["ram_16_plus"]
)

testEngine(
    ["creative_work", "large_screen"],
    [],
    ["display_15_plus_color_accurate"]
)

testEngine(
    ["travel_often", "long_battery"],
    [],
    ["battery_60wh_plus"]
)

testEngine(
    ["pref_os_macos"],
    [],
    ["macos_required"]
)

testEngine(
    ["needs_ai_accel"],
    [],
    ["gpu_with_tensor_cores"]
)

testEngine(
    ["pref_os_linux", "office_only"],
    [],
    ["linux_friendly_hw"]
)

testEngine(
    ["creative_work", "portable", "large_screen"],
    [],
    ["ram_16_plus", "display_15_plus_color_accurate"]
)

testEngine(
    [],
    [],
    []
)

print(f"{pass_count} tests passed and {fail_count} tests failed.")