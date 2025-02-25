class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block_comment = False
        new_source = []
        buffer = ""

        for line in source:
            i = 0
            n = len(line)
            while i < n:
                if not in_block_comment and i + 1 < n and line[i] == '/' and line[i + 1] == '*':
                    in_block_comment = True
                    i += 2
                elif in_block_comment and i + 1 < n and line[i] == '*' and line[i + 1] == '/':
                    in_block_comment = False
                    i += 2
                elif not in_block_comment and i + 1 < n and line[i] == '/' and line[i + 1] == '/':
                    break 
                elif not in_block_comment:
                    buffer += line[i]
                    i += 1
                else:
                    i += 1

            if not in_block_comment and buffer:
                new_source.append(buffer)
                buffer = ""

        return new_source

