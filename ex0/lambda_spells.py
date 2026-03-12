from typing import List


def artifact_sorter(artifacts: List[dict]) -> List[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


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
