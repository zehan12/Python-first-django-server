echo " BUILD START"
pip install -r requirements.txt
pip manage.py collectstatic  --noinput --clear
echo " BUILD END"