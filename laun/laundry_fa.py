def total_laundry (nama, kg, item, sm):
  # harga pokok
  hl = 6000
  hdc = 35000
  # Program Hitung Harga
  if kg > 10:
    th = kg*(hl * 95/100) # Diskon 5% laundry
  else:
    th = kg*hl # Menghitung harga laundry
    
  if item > 5:
    tdc = item*(hdc*95/100) # Diskon dry clean
    th = th + tdc
  else:
    th = th + (item*hdc) # Menghitung dry clean

  # Diskon member
  if sm == "gold":
    th = th - (th*5/100)
  elif sm == "silver":
    th = th - (th*4/100)
  elif sm == "bronze":
    th = th - (th*3/100)
  else:
    th = th

  print("Total Biaya Anda: ", round(th))
  return {'Nama':nama, 'Laundry': kg, 'Dry Clean': item, 'Member':sm, 'Total': round(th)}

def penjumlahan (a,b):
  jum = a+b
  return(jum)