echo "Fixing poetry..."
pip install --upgrade poetry > /dev/null
echo "Updating/Installing dependencies..."
poetry update > /dev/null
echo "Logging completion..."
touch /tmp/updated.txt
echo "Done!"