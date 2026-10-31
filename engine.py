from dataclasses import dataclass
from typing import List, Set, Dict

@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""

class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[str] = []

    def assert_facts(self, initial: List[str]) -> None:
        """Store initial facts into the working memory."""
        self.facts.update(initial)

    def can_fire(self, rule: Rule) -> bool:
        """Return True if all antecedents are true and consequent not yet known."""
        for antecedent in rule.antecedents:
            if antecedent not in self.facts:
                return False
        if rule.consequent in self.facts:
            return False
        return True

    def run(self) -> None:
        """Implement the forward chaining loop."""
        # while there are rules that can fire:
        #     select one rule (students decide tie-breaking)
        #     add its consequent to facts
        #     record in trace
        while True:
            selected = None
            for rule in self.rules:
                if not self.can_fire(rule):
                    continue
                if selected is None or rule.priority > selected.priority:
                    selected = rule
            if selected is None:
                break
            self.facts.add(selected.consequent)
            preconditions = ", ".join(selected.antecedents)
            self.trace.append(
                f"=> {selected.consequent}\n\t"
                f"explanation:derived from rule \"{selected.name}\"\n\t"
                f"preconditions:{preconditions}"
            )

    def conclusions(self) -> Dict[str, List[str]]:
        """Return separated results (recommendations, specs, other facts)."""
        result = {
            "recommendations": [],
            "specs": [],
            "other_facts": [],
            "trace": self.trace
        }
        for fact in self.facts:
            if fact.startswith("recommend:"):
                recommendation = fact[len("recommend:"):]
                result["recommendations"].append(recommendation)
            elif fact.startswith("spec:"):
                spec = fact[len("spec:"):]
                result["specs"].append(spec)
            else:
                result["other_facts"].append(fact)
        return result
