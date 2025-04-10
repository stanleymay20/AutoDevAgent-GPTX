# pushbridge_call.sh
curl -X POST https://pushbridge-server-url.com/push \
  -F "repo=AutoDevAgent-GPTX" \
  -F "zip=@project.zip" \
  -F "token=$GITHUB_PAT"
