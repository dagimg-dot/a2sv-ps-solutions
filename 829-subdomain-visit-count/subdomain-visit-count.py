class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hash_map = defaultdict(int)
        all_splits = []
        
        for domain in cpdomains:
            count, _domain = domain.split(" ")

            splitted = _domain.split(".")

            for i in range(len(splitted)):
                dom = ".".join(splitted[i:])
                hash_map[dom] = hash_map.get(dom, 0) + int(count)
        
        for key, value in hash_map.items():
            all_splits.append(f"{value} {key}")

        return all_splits