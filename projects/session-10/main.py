import pandas as pd
import numpy as np
import datetime

# Baca data
OR_df = pd.read_excel('Online Retail.xlsx', sheet_name='Online Retail')

# Hapus baris dengan CustomerID kosong
OR_df = OR_df[OR_df['CustomerID'].notnull()]

# Hapus transaksi kredit (InvoiceNo yang mengandung huruf 'C')
OR_df = OR_df[~OR_df['InvoiceNo'].astype(str).str.contains('C', na=False)]

# Tambahkan kolom 'TotalPrice'
OR_df['TotalPrice'] = OR_df['Quantity'] * OR_df['UnitPrice']

# Tentukan tanggal referensi = 1 hari setelah transaksi terakhir
reference_date = OR_df['InvoiceDate'].max() + pd.Timedelta(days=1)

# Hitung FRM
frm = OR_df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (reference_date - x.max()).days,  # Recency
    'InvoiceNo': 'nunique',                                    # Frequency
    'TotalPrice': 'sum'                                        # Monetary
}).reset_index()

# Ubah nama kolom
frm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']

# Tampilkan hasil
print(frm.head())

# Ekspor ke CSV
frm.to_csv('frm_results.csv', index=False)
print("FRM results exported to frm_results.csv")
