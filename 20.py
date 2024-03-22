
bracket_map = {"(": ")", "[": "]", "{": "}"}


class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in bracket_map:
                stack.append(bracket_map.get(i))
                continue
            if len(stack) == 0:
                return False
            bracket = stack.pop()
            if bracket != i:
                return False
        if len(stack) == 0:
            return True
        return False


if __name__ == '__main__':
    str = "([]{}))"
    s = Solution()
    print(s.isValid(str))
