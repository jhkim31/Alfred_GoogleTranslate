#!/bin/zsh
str=$@

q=${str//\"/\`}
q=$(echo "$q" | tr '\n' ' ')


url=https://translation.googleapis.com/language/translate/v2
translateText=$(curl --data-urlencode "key={your-api-key}" --data-urlencode "q=$q" --data-urlencode "source=ko" --data-urlencode "target=en" --data-urlencode "format=text" $url | /opt/homebrew/bin/jq '.data.translations[0].translatedText')
t=${translateText//\"/}

cat << EOB
{"items": [
	{
		"title": "${t}",
		"arg": "${t}",
		"mods": {
			"cmd": {
				"valid": true,
				"arg": "$q, \"$t\"",
				"subtitle": "사전에 저장합니다. ($q, \"$t\")"
			}
		}
	}
]}
EOB