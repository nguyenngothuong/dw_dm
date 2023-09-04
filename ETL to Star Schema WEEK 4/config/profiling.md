khởi tạo thư viện trong jupyter nootbook


# import sys
# !{sys.executable} -m pip install -U ydata-profiling[notebook]
# !jupyter nbextension enable --py widgetsnbextension


```
from ydata_profiling import ProfileReport

excel_file_path = r"G:\My Drive\HỌC TẬP DUE\NNT_năm 4 kì 1\DW & DM\ETL_Sale week 2\ETL SALE PYTHON\SaleDataset.xlsx"
df_ORDER = pd.read_excel(excel_file_path, sheet_name="ORDER")

profile = ProfileReport(df_ORDER, title="Pandas Profiling Report")
profile.to_widgets()
# profile.to_notebook_iframe()

```

