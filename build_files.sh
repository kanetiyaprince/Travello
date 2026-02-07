# build_files.sh

# Install dependencies with the break-system-packages flag
python3.9 -m pip install -r requirements.txt --break-system-packages

# Collect static files
python3.9 manage.py collectstatic --noinput --clear