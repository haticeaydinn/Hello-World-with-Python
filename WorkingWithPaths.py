from pathlib import Path

path = Path("emails")
if path.exists():
    path.rmdir()  # remove directory
else:
    path.mkdir()  # make directory

path1 = Path()  # current directory

# glob metoduyla  belirtilen directory de tüm dosyalar listelenebilir
# glob bir generator fonksiyondur. Iterator gibi davranır ve döngüde kullanılabilir
for file in path1.glob('*.py'):
    print(file)
