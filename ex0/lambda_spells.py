from typing import List


def artifact_sorter(artifacts: List[dict]) -> List[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: List[dict], min_power: int) -> List[dict]:
    filtered = list(filter(lambda x: True if x['power'] >= min_power
                           else False, mages))
    return filtered


def spell_transformer(spells: List[str]) -> List[str]:
    transformed = list(map(lambda s: '* ' + s + ' *', spells))
    return transformed


def mage_stats(mages: list[dict]) -> dict:
    _max = max(mages, key=lambda x: x['power'])
    _min = min(mages, key=lambda x: x['power'])
    _sum = sum(mages, key=lambda x: x['power'])
    avg = round(_sum / len(mages), 2)
    return {"max_power": _max, "min_power": _min, "avg_power": avg}


if __name__ == "__main__":
    artifacts = [{'name': 'Fire Staff', 'power': 86, 'type': 'accessory'},
                 {'name': 'Crystal Orb', 'power': 84, 'type': 'weapon'},
                 {'name': 'Wind Cloak', 'power': 105, 'type': 'accessory'},
                 {'name': 'Wind Cloak', 'power': 77, 'type': 'weapon'}]
    mages = [{'name': 'River', 'power': 90, 'element': 'light'},
             {'name': 'Zara', 'power': 100, 'element': 'fire'},
             {'name': 'Rowan', 'power': 70, 'element': 'light'},
             {'name': 'Riley', 'power': 82, 'element': 'shadow'},
             {'name': 'Ember', 'power': 58, 'element': 'shadow'}]
    spells = ['heal', 'shield', 'earthquake', 'meteor']
    new_artifacts = artifact_sorter(artifacts)
    lst = [x['power'] for x in new_artifacts]
    print(lst)
