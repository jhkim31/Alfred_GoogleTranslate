#!/bin/zsh
# Alfred Script Filter JSON format
#
# This example demonstrates all fields available for populating results.
#
# For an in-depth explanation, use the (?) help button to the bottom left.
#ㅊ
str={query}
q=${str// /%20}
cat {query}
cat $str
cat $q

translateText=$(curl https://translation.googleapis.com/language/translate/v2\?key\={your-api-key}\&q\=$q\&source\=en\&target\=ko\&format\=text | /opt/homebrew/bin/jq '.data.translations[0].translatedText')
t=${translateText//\"/}
cat << EOB
{"items": [

	{
		"valid": true,
		"uid": "desktop",
		"type": "file",
		"title": "$t",
		"subtitle": "cmd : (한글, 영어), ctrl : 웹으로 확인",
		"arg": "$t",
		"mods": {
			"alt": {
				"valid": true,
				"arg": "$t",
				"subtitle": "한글만 저장합니다 ex) hello"
			},
			"cmd": {
				"valid": true,
				"arg": "$str, $t",
				"subtitle": "영어와 한글을 저장합니다 ex) hello, 안녕하세요"
			},
			"ctrl": {
				"valid": true,
				"arg": "$str",
				"subtitle": "웹으로 확인합니다. : $str"
			},

		}
	}
]}
EOB
