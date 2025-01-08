### INFO
* Asset/Image buat taro Icon atau gambar yang mau di pakai
* UI/UX Source UI yang belum di merge ke main.py atau belum siap
* file db jgn di pindah 

### Compile
```bash
python -m pip install -U nuitka
```
```bash
pip install PySide6
```
```bash
python -m nuitka --standalone --windows-uac-admin --enable-plugin=tk-inter --enable-plugin=pyside6 --remove-output --windows-console-mode=disable main.py
```