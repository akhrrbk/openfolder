git add .

echo 'commit message: '
read commitMessage

git commit -m "$commitMessage"

git push origin main