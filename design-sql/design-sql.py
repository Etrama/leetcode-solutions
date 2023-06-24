class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.tables_dict = {}
        self.tables_dict = {name:{0:"beginning"} for name in names}
        self.last_insert = {name:0 for name in names}
        print(self.tables_dict)
        print(self.last_insert)
    def insertRow(self, name: str, row: List[str]) -> None:
        #250 calls
        self.last_insert[name] = self.last_insert[name] + 1
        self.tables_dict[name][self.last_insert[name]] = row

    def deleteRow(self, name: str, rowId: int) -> None:
        #250 calls
        del self.tables_dict[name][rowId]

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        #10^4 calls
        return self.tables_dict[name][rowId][columnId-1]

# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)