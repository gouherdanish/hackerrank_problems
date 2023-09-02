
class Pattern:
    def solid_rectangle(rows,cols):
        """Prints following pattern based on rows and cols
        
        ******
        ******
        ******

        Args:
            rows (int): number of rows
            columns (int): number of columns
        """        
        rows = int(input())
        columns = int(input())

        for i in range(rows):
            print(f"*"*columns)

if __name__=='__main__':
    