class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        for i in range(0, len(command)):
            if command[i] == "G":
                result += "G"
            elif command[i] == "(" and command[i+1] == ")":
                result += "o"
                i += 2
            elif command[i] == "(" and command[i+1] == "a":
                result += "al"
                i += 4
        return result