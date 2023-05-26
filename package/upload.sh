echo "Formatting..."
black . > /dev/null
echo "Building..."
poetry build > /dev/null
echo "Uploading..."
python3 -m twine upload -r pypi dist/*
echo "Done!"