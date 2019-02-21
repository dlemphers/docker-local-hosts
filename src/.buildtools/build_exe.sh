pwd

pip install --upgrade pip && pip install -r requirements.txt

pyinstaller --console --onefile --clean --noupx --distpath=.dist .buildtools/cli.spec
