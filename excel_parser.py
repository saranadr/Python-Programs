import xlwt
import xlrd

def writeExcel():
  # Initialize a workbook 
  book = xlwt.Workbook(encoding="utf-8")
  
  # Add a sheet to the workbook 
  sheet1 = book.add_sheet("PythonSheet1") 
  
  # Write to the sheet of the workbook 
  sheet1.write(0, 0, "This is the First Cell of the First Sheet")
  sheet1.write(0, 1, "This is the Second Cell of the First Sheet")
  for i in range(1, 11):
    sheet1.write(i, 0, "This is row-%d"%(i))
    sheet1.write(i, 1, "This is row-%d1"%(i))
  
  # Save the workbook 
  book.save("Excel_Data.xls")
  print("File created successfully...")


def readExcel():
  # Open a workbook 
  workbook = xlrd.open_workbook('Excel_Data.xls')
  
  # Load a specific sheet by name
  #sheet = workbook.sheet_by_name('PythonSheet1')
  
  # Load a specific sheet by index 
  sheet = workbook.sheet_by_index(0)
  
  # Retrieve the value from cell at indices (0,0) 
  print( "ROWS: ",sheet.nrows)
  print ("COLS: ",sheet.ncols)
  print ("VALUE: ", sheet.cell(0, 0).value)
  for i in range(sheet.nrows):
    for j in range(sheet.ncols):
      print (i,j,  sheet.cell(i, j).value)

#writeExcel()
readExcel()
